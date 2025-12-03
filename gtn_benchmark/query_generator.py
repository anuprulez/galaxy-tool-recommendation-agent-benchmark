from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from .io_utils import safe_filename, write_json
from .llm_client import JetstreamClient
from .models import BenchmarkItem, TutorialInfo
from gtn_benchmark import VERSION

LOGGER = logging.getLogger(__name__)


def build_system_prompt() -> str:
    return (
        "You are an expert Galaxy instructor. "
        "Given a GTN tutorial description, you will craft realistic questions that a user might ask "
        "when trying to run that analysis inside Galaxy. "
        "Return JSON strictly following the requested schema."
    )


def build_user_prompt(tutorial: TutorialInfo, requested_queries: int, include_body: bool) -> str:
    tools_text = ", ".join(tutorial.tools) if tutorial.tools else "No explicit tools listed"
    workflows_text = ", ".join(tutorial.workflows) if tutorial.workflows else "No workflows listed"
    headings_text = "\n".join(tutorial.headings) if tutorial.headings else "No headings parsed"
    body_text = tutorial.body if include_body else "Body omitted (brief mode enabled)"
    dataset_paths = tutorial.dataset_paths or tutorial.datasets
    datasets_text = ", ".join(dataset_paths) if dataset_paths else "No dataset links"
    dataset_count = tutorial.dataset_count or len(dataset_paths)
    return f"""Tutorial title: {tutorial.title}
GTN path: {tutorial.tutorial_id}
Topic: {tutorial.topic}
Summary: {tutorial.summary}
Tools used: {tools_text}
Workflows referenced: {workflows_text}
Datasets ({dataset_count}): {datasets_text}
Headings:
{headings_text}

Body:
{body_text}

Write {requested_queries} diverse, natural-language questions aimed at getting Galaxy tool recommendations for this exact tutorial.
Requirements for each question:
- Explicitly ask which Galaxy tool(s) or workflow step(s) to use; intent must be tool recommendation (not metrics interpretation or results explanation).
- Assume the user does NOT know tool names; phrase questions as “which Galaxy tool should I use to …?” or “how do I do X in Galaxy?” (avoid naming a specific tool unless it’s unavoidable).
- Target analytical steps that require choosing an analysis tool or workflow step (preprocessing, training, evaluation). Do NOT ask about data management/tagging/exporting or report interpretation-only questions.
- Ground the question in the provided datasets (names/paths above) and the analysis goal; avoid generic questions with no data context.
- Keep questions natural; you may name specific tools only when appropriate, otherwise ask for recommendations.
- Avoid referencing GTN explicitly.

Return JSON in this shape:
{{
  "tutorial_id": "{tutorial.tutorial_id}",
  "queries": [
    {{
      "id_suffix": "q01",
      "query": "How do I ...?",
      "difficulty": "easy|medium|hard",
      "rationale": "Optional short note explaining what part of the tutorial this covers."
    }}
  ],
  "analysis_focus": "One short sentence describing what this analysis aims to accomplish"
}}

Ensure id_suffix values are sequential (q01, q02, ...).
"""


def generate_queries_for_tutorial(
    tutorial: TutorialInfo,
    client: JetstreamClient,
    raw_dir: Path,
    version: str = VERSION,
    include_body: bool = False,
) -> list[BenchmarkItem]:
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"{safe_filename(tutorial.tutorial_id)}_raw.json"
    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(tutorial, tutorial.min_queries, include_body)
    LOGGER.info("Generating queries for %s", tutorial.tutorial_id)
    response = client.generate_json(system_prompt, user_prompt)
    write_json(response, raw_path)
    payload = response.get("queries") or response.get("items")
    if not isinstance(payload, list):
        LOGGER.warning("Jetstream response missing 'queries' list for %s", tutorial.tutorial_id)
        return []
    benchmark_items: list[BenchmarkItem] = []
    for idx, query_block in enumerate(payload, start=1):
        query_text = str(query_block.get("query", "")).strip()
        if not query_text:
            continue
        suffix = query_block.get("id_suffix") or f"q{idx:02d}"
        rationale = query_block.get("rationale")
        difficulty = str(query_block.get("difficulty", "medium")).lower()
        if difficulty not in {"easy", "medium", "hard"}:
            difficulty = "medium"
        analysis_focus = response.get("analysis_focus") or tutorial.context_summary
        benchmark_items.append(
            BenchmarkItem(
                id=f"{tutorial.short_name}-{suffix}",
                tutorial_id=tutorial.tutorial_id,
                query=query_text,
                tools=tutorial.tools,
                workflows=tutorial.workflows,
                metadata={
                    "topic": tutorial.topic,
                    "tutorial_title": tutorial.title,
                    "datasets": tutorial.datasets,
                    **({"dataset_paths": tutorial.dataset_paths} if tutorial.dataset_paths else {}),
                    "dataset_count": tutorial.dataset_count,
                    "difficulty": difficulty,
                    "context_summary": analysis_focus or tutorial.context_summary,
                    "priority": idx,  # 1 = first generated
                    "version": version,
                    **({"workflow_steps": tutorial.workflow_steps} if tutorial.workflow_steps else {}),
                    **({"rationale": rationale} if rationale else {}),
                },
            )
        )
    if len(benchmark_items) < tutorial.min_queries:
        LOGGER.warning(
            "Tutorial %s returned %s queries (expected %s)",
            tutorial.tutorial_id,
            len(benchmark_items),
            tutorial.min_queries,
        )
    return benchmark_items
