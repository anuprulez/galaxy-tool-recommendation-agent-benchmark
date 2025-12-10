from __future__ import annotations

import logging
from pathlib import Path
import json
from typing import Any
from urllib.parse import urlparse

# Simple extensions to map datasets to tools
FASTQ_EXTS = (".fastq", ".fastq.gz", ".fq", ".fq.gz", ".fastqsanger")
BAM_EXTS = (".bam",)
BED_EXTS = (".bed",)
GFF_EXTS = (".gff", ".gff3", ".gtf")

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
    workflows_text = ", ".join(tutorial.workflows) if tutorial.workflows else "No workflows listed"
    headings_text = "\n".join(tutorial.headings) if tutorial.headings else "No headings parsed"
    body_text = tutorial.body if include_body else "Body omitted (brief mode enabled)"
    dataset_values = tutorial.dataset_paths or tutorial.datasets
    dataset_pairs = []
    for value in dataset_values:
        parsed = urlparse(value)
        candidate = parsed.path if parsed.scheme else value
        name = Path(candidate).name or candidate
        dataset_pairs.append((name, value))
    datasets_text = "\n".join(f"- {name}: {path}" for name, path in dataset_pairs) if dataset_pairs else "No dataset links"
    dataset_count = tutorial.dataset_count or len(dataset_pairs)

    tools_to_show = tutorial.tools  # Use all tools so each receives 4 queries

    # If no tools, generate general queries about the tutorial topic
    if not tools_to_show:
        tools_text = "No specific tools required for this tutorial"
        num_queries = requested_queries or 4  # Generate 4 general queries
        query_instructions = f"""Generate {num_queries} general queries about this tutorial:
- 2 queries asking what tools would be needed for specific tasks mentioned in the tutorial
- 2 queries asking how to achieve goals described in the tutorial

For each query, use "general" as the query_type and leave tool_focus empty."""
    else:
        tools_text = "\n".join([f"- {tool}" for tool in tools_to_show])
        num_queries = requested_queries or (len(tools_to_show) * 4)
        dataset_labels = ", ".join(name for name, _ in dataset_pairs) if dataset_pairs else "no datasets listed"
        query_instructions = f"""Generate {num_queries} queries (4 per tool, in the order listed):
- 2 science-first queries per tool (describe a biological/scientific goal; DO NOT mention any tool name or ID)
- 2 tool-first queries per tool (ask which Galaxy tool to use or how to proceed; DO NOT mention any tool name or ID)
- ALWAYS attach dataset names/paths from the dataset list (prefer the file names: {dataset_labels}) in the datasets field for each query
- Do not introduce any datasets beyond the list provided
- IMPORTANT: Use the exact Galaxy tool IDs from the Tools list (no abbreviations, no substitutions, no new tools). Keep the full toolshed path and version.
Return the queries ordered as:
- Tool1: science-first #1, science-first #2, tool-first #1, tool-first #2
- Tool2: science-first #1, science-first #2, tool-first #1, tool-first #2
...and so on.
For each tool, create:"""

    return f"""Tutorial: {tutorial.title}
Topic: {tutorial.topic}
Summary: {tutorial.summary}
Workflows: {workflows_text}
Headings: {headings_text}
Tutorial content:
{body_text}
Datasets ({dataset_count}): 
{datasets_text}
Tools ({len(tools_to_show)} of {len(tutorial.tools)}):
{tools_text}

{query_instructions}
Science-first examples (no tool names):
- "I have paired-end FASTQ reads from a ChIP-seq experiment ([dataset_name]), want to assess library quality before alignment. What should I do?"
- "My single-cell FASTQ files ([dataset_name]) show variable read quality; how can I clean them for downstream analysis?"
- "We sequenced tumor samples ([dataset_name]); how do I check for adapter contamination and trim low-quality bases?"

Tool-first examples (still no tool names):
- "Which Galaxy tool should I use to assess read quality for [dataset_name]?"
- "How can I trim adapters and low-quality bases on [dataset_name] in Galaxy?"

Use the actual dataset names from the datasets list. Make queries specific and realistic.
IMPORTANT: Use the full tool_id as shown in the tools list (including toolshed path and version).

Return JSON:
{{
  "queries": [
    {{
      "id_suffix": "q01",
      "query": "Question text",
      "query_type": "science_first",
      "tool_focus": "full_tool_id",
      "difficulty": "easy|medium|hard",
      "tools": ["full_tool_id"],
      "datasets": ["exact_dataset_name_from_list"]
    }}
  ]
}}
"""


def _pick_datasets_for_tool(
    requested_names: list[str],
    tutorial: TutorialInfo,
    tool_id: str | None,
) -> list[str]:
    """Choose dataset paths relevant to a tool, preferring LLM-specified names."""
    # Map basename to path for quick lookup
    name_to_path: dict[str, str] = {}
    for path in tutorial.dataset_paths or []:
        name_to_path[Path(path).name] = path

    # If LLM provided names, try to map them to local paths and then filter
    matched: list[str] = []
    for name in requested_names:
        base = Path(name).name
        matched.append(name_to_path.get(base, name))
    if matched:
        candidates = matched
    else:
        candidates = tutorial.dataset_paths or tutorial.datasets or []

    if not tool_id or not candidates:
        return candidates

    def _filter_by_ext(exts: tuple[str, ...]) -> list[str]:
        return [p for p in candidates if any(p.lower().endswith(ext) for ext in exts)]

    tool_lower = tool_id.lower()
    if "fastqc" in tool_lower or "cutadapt" in tool_lower or "fastq_quality_filter" in tool_lower:
        filtered = _filter_by_ext(FASTQ_EXTS)
    elif "multiqc" in tool_lower:
        filtered = _filter_by_ext(FASTQ_EXTS + BAM_EXTS)
    else:
        filtered = candidates

    # Limit to a small relevant subset
    if len(filtered) > 4:
        filtered = filtered[:4]
    return filtered


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
    # Calculate expected queries: 4 per tool (2 science-first + 2 tool-first)
    # Or 4 general queries if no tools
    tools_to_process = len(tutorial.tools)
    expected_queries = tools_to_process * 4 if tools_to_process > 0 else 4
    user_prompt = build_user_prompt(tutorial, expected_queries, include_body)
    LOGGER.info("Generating queries for %s (expecting %s queries for %s tools)",
                tutorial.tutorial_id, expected_queries, len(tutorial.tools))

    response: dict[str, Any] | None = None
    decode_attempts = 2
    for attempt in range(1, decode_attempts + 1):
        try:
            response = client.generate_json(system_prompt, user_prompt)
            break
        except json.JSONDecodeError as exc:
            LOGGER.warning(
                "JSON decode failed for %s (attempt %s/%s): %s",
                tutorial.tutorial_id,
                attempt,
                decode_attempts,
                exc,
            )
            if attempt == decode_attempts:
                return []
    if response is None:
        return []
    write_json(response, raw_path)
    payload = response.get("queries") or response.get("items")
    if not isinstance(payload, list):
        LOGGER.warning("Jetstream response missing 'queries' list for %s", tutorial.tutorial_id)
        return []

    benchmark_items: list[BenchmarkItem] = []
    tool_query_count = {}  # Track queries per tool

    for idx, query_block in enumerate(payload, start=1):
        query_text = str(query_block.get("query", "")).strip()
        if not query_text:
            continue

        suffix = query_block.get("id_suffix") or f"q{idx:02d}"
        rationale = query_block.get("rationale")
        # We no longer surface difficulty; retain only if needed internally
        difficulty = None

        # Extract new fields
        analysis_focus = response.get("analysis_focus") or tutorial.context_summary

        # Enforce exact tutorial tool IDs: 4 queries per tool, in order
        rec_tools: list[str] = []
        if tutorial.tools:
            target_idx = (idx - 1) // 4 % len(tutorial.tools)
            target_tool = tutorial.tools[target_idx]
            rec_tools = [target_tool]
            tool_focus = target_tool
            # Alternate query type: first 2 science, next 2 tool
            offset = (idx - 1) % 4
            query_type = "science_first" if offset < 2 else "tool_first"
        else:
            tool_focus = query_block.get("tool_focus")
            query_type = query_block.get("query_type", "unknown")
            tools_field = query_block.get("tools")
            if isinstance(tools_field, list):
                rec_tools = [str(t).strip() for t in tools_field if str(t).strip()]

        # Track query count per tool (only if tools exist)
        if rec_tools:
            for tool in rec_tools:
                tool_query_count[tool] = tool_query_count.get(tool, 0) + 1

        # Handle datasets: prefer tool-specific subset
        q_datasets: list[str] = []
        q_ds_field = query_block.get("datasets")
        if isinstance(q_ds_field, list):
            q_datasets = [str(d).strip() for d in q_ds_field if str(d).strip()]
        tool_for_dataset = rec_tools[0] if rec_tools else None
        q_datasets = _pick_datasets_for_tool(q_datasets, tutorial, tool_for_dataset)

        answer = query_block.get("answer")

        # Build metadata with new fields
        metadata = {
            "topic": tutorial.topic,
            "tutorial_title": tutorial.title,
            "datasets": q_datasets or tutorial.datasets,
            "dataset_paths": q_datasets or tutorial.dataset_paths or tutorial.datasets,
            "dataset_count": len(q_datasets) if q_datasets else tutorial.dataset_count,
            "context_summary": analysis_focus or tutorial.context_summary,
            "priority": idx,  # 1 = first generated
            "version": version,
            **({"workflow_steps": tutorial.workflow_steps} if tutorial.workflow_steps else {}),
            **({"rationale": rationale} if rationale else {}),
            **({"answer": answer} if answer else {}),
            "query_type": query_type,
            **({"tool_focus": tool_focus} if tool_focus else {}),
        }

        benchmark_items.append(
            BenchmarkItem(
                id=f"{tutorial.short_name}-{suffix}",
                tutorial_id=tutorial.tutorial_id,
                query=query_text,
                tools=rec_tools,
                workflows=tutorial.workflows,
                metadata=metadata,
            )
        )

    # Log statistics
    if tutorial.tools:
        for tool in tutorial.tools:
            count = tool_query_count.get(tool, 0)
            if count == 0:
                LOGGER.warning("No queries generated for tool: %s", tool)
            elif count < 4:
                LOGGER.warning("Only %s query(ies) generated for tool: %s (expected 4)", count, tool)

    if len(benchmark_items) < expected_queries:
        if tutorial.tools:
            LOGGER.warning(
                "Tutorial %s returned %s queries (expected %s, 4 per tool)",
                tutorial.tutorial_id,
                len(benchmark_items),
                expected_queries,
            )
        else:
            LOGGER.warning(
                "Tutorial %s returned %s queries (expected %s general queries)",
                tutorial.tutorial_id,
                len(benchmark_items),
                expected_queries,
            )
    else:
        if tutorial.tools:
            LOGGER.info(
                "Successfully generated %s queries for %s (average %.1f per tool)",
                len(benchmark_items),
                tutorial.tutorial_id,
                len(benchmark_items) / len(tutorial.tools) if tutorial.tools else 0,
            )
        else:
            LOGGER.info(
                "Successfully generated %s general queries for %s",
                len(benchmark_items),
                tutorial.tutorial_id,
            )

    return benchmark_items
