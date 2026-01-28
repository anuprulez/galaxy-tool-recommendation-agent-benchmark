from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import textwrap
import time
from pathlib import Path
from typing import Any, Iterable, List, Optional

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOGGER = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate ranked tool predictions for Galaxy benchmark queries using an LLM."
    )
    parser.add_argument(
        "--queries",
        type=Path,
        default=Path("tmp_stats/codex_quiers_all.jsonl"),
        help="JSONL file containing queries to score.",
    )
    parser.add_argument(
        "--gold",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Gold benchmark file used to gather tutorial-to-tool mappings.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tmp_stats/codex_predictions.jsonl"),
        help="Destination JSONL for {'id','predictions'} entries.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Request up to this many predictions per query.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="LLM model name to request from the API.",
    )
    parser.add_argument(
        "--api-url",
        type=str,
        default="https://api.openai.com/v1/chat/completions",
        help="Chat completions endpoint.",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="Optional OpenAI API key (fallbacks to OPENAI_API_KEY).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature for the LLM.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls.",
    )
    parser.add_argument(
        "--max-queries",
        type=int,
        default=None,
        help="Stop after scoring this many queries (default: all).",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Do not re-request predictions that already exist in the output file.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> List[dict]:
    items: List[dict] = []
    if not path.exists():
        return items
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def build_tool_map(gold_items: Iterable[dict]) -> dict[str, List[str]]:
    tool_map: dict[str, List[str]] = {}
    for item in gold_items:
        tid = item.get("tutorial_id")
        if not tid:
            continue
        tools = item.get("tools") or []
        existing = tool_map.setdefault(tid, [])
        for tool in tools:
            if tool and tool not in existing:
                existing.append(tool)
    return tool_map


def build_prompt(
    entry: dict,
    candidate_tools: List[str],
    top_k: int,
) -> list[dict[str, str]]:
    tutorial = entry.get("tutorial_id", "unknown tutorial")
    topic = entry.get("metadata", {}).get("topic") or "unknown topic"
    datasets = entry.get("metadata", {}).get("datasets") or []
    dataset_info = ", ".join(datasets) or "N/A"
    tools_text = (
        ", ".join(candidate_tools) if candidate_tools else "No tutorial tools available"
    )

    system_content = (
        "You are an expert Galaxy Training Network assistant. "
        "Given a user's question, select the most appropriate Galaxy tool IDs."
    )
    user_content = textwrap.dedent(
        f"""
        Tutorial: {tutorial}
        Topic: {topic}
        Datasets: {dataset_info}
        Candidate tools: {tools_text}

        User query: {entry.get('query')}

        Instructions:
        - Pick up to {top_k} Galaxy tool IDs that best solve the query.
        - Prefer tools listed in the candidate tools when possible.
        - Output a single JSON object and nothing else, e.g.
          {{"predictions": ["toolshed.g2.bx.psu.edu/repos/..."]}}.
        - Ensure the `predictions` list is ordered from most to least relevant.
        - If you cannot map the query confidently, return an empty list.
        """
    ).strip()
    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


def extract_predictions(content: str, top_k: int) -> list[str]:
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, re.S)
        if not match:
            raise
        payload = json.loads(match.group(0))

    preds = payload.get("predictions") or payload.get("tools") or []
    if not isinstance(preds, list):
        raise ValueError("`predictions` value must be a list.")
    output: list[str] = []
    seen: set[str] = set()
    for tool in preds:
        if not isinstance(tool, str):
            continue
        if tool in seen:
            continue
        seen.add(tool)
        output.append(tool)
        if len(output) >= top_k:
            break
    return output


def call_llm(
    api_url: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    temperature: float,
    max_retries: int = 3,
) -> str:
    try:
        import requests  # type: ignore
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Missing dependency 'requests'. Install project dependencies to use --agent llm."
        ) from exc

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    for attempt in range(1, max_retries + 1):
        response = requests.post(api_url, headers=headers, json=payload, timeout=60)
        if response.status_code == 429:
            backoff = attempt * 2.0
            LOGGER.warning("Rate limited, sleeping %.1fs before retry...", backoff)
            time.sleep(backoff)
            continue
        response.raise_for_status()
        data = response.json()
        choices = data.get("choices") or []
        if not choices:
            raise RuntimeError("No choices returned from LLM.")
        return choices[0]["message"]["content"]
    raise RuntimeError("Exceeded retry budget for LLM call.")


def main() -> None:
    args = parse_args()
    try:
        from dotenv import load_dotenv  # type: ignore
    except ModuleNotFoundError:
        load_dotenv = None
    if load_dotenv is not None:
        load_dotenv(dotenv_path=Path(".env"))
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        LOGGER.error(
            "No OpenAI API key provided. Set OPENAI_API_KEY or use --api-key."
        )
        sys.exit(1)

    queries = load_jsonl(args.queries)
    if not queries:
        LOGGER.error("No queries found in %s", args.queries)
        sys.exit(1)

    gold_items = load_jsonl(args.gold)
    tool_map = build_tool_map(gold_items)

    existing_ids = set()
    if args.skip_existing and args.output.exists():
        existing_ids = {item["id"] for item in load_jsonl(args.output) if "id" in item}

    processed = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8") as out_handle:
        for entry in queries:
            qid = entry.get("id")
            if not qid:
                continue
            if args.skip_existing and qid in existing_ids:
                continue
            if args.max_queries and processed >= args.max_queries:
                break

            messages = build_prompt(
                entry,
                tool_map.get(entry.get("tutorial_id", ""), []),
                args.top_k,
            )
            try:
                content = call_llm(
                    args.api_url,
                    api_key,
                    args.model,
                    messages,
                    args.temperature,
                )
                predictions = extract_predictions(content, args.top_k)
            except Exception as exc:
                LOGGER.error("Failed to score %s: %s", qid, exc)
                continue

            output_item = {"id": qid, "predictions": predictions}
            out_handle.write(json.dumps(output_item, ensure_ascii=False) + "\n")
            out_handle.flush()
            processed += 1
            existing_ids.add(qid)
            LOGGER.info("Wrote predictions for %s (%d/%s)", qid, processed, len(queries))
            time.sleep(max(0.0, args.delay))


if __name__ == "__main__":
    main()
