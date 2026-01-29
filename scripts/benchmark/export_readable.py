from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render JSONL benchmark items into a human-readable Markdown file.")
    parser.add_argument("--input", type=Path, required=True, help="Path to v0_items.jsonl")
    parser.add_argument("--output", type=Path, required=True, help="Path to write Markdown report")
    return parser.parse_args()


def load_items(path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def group_by_tutorial(items: List[Dict[str, Any]]) -> dict[str, list[Dict[str, Any]]]:
    grouped: dict[str, list[Dict[str, Any]]] = defaultdict(list)
    for item in items:
        grouped[item.get("tutorial_id", "unknown")].append(item)
    return grouped


def format_list(values: list[str]) -> str:
    return ", ".join(values) if values else "N/A"


def short_tool_name(tool: str) -> str:
    # Show the tool name/version (last 2 path segments) to keep lines short.
    parts = tool.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else tool


def short_path(path: str) -> str:
    # Use basename for readability.
    return path.split("/")[-1] if "/" in path else path


def format_tools_short(tools: list[str]) -> str:
    return ", ".join(short_tool_name(t) for t in tools) if tools else "N/A"


def format_paths_short(paths: list[str]) -> str:
    return ", ".join(short_path(p) for p in paths) if paths else "N/A"


def collect_all_datasets(items: list[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    for item in items:
        meta = item.get("metadata", {})
        for path in meta.get("dataset_paths") or meta.get("datasets") or []:
            seen.add(path)
    return sorted(seen)


def write_markdown(items: List[Dict[str, Any]], output: Path) -> None:
    grouped = group_by_tutorial(items)
    lines: list[str] = ["# GTN Benchmark Items (Readable)", ""]
    for tutorial_id, t_items in sorted(grouped.items(), key=lambda kv: kv[0]):
        first = t_items[0]
        meta = first.get("metadata", {})
        title = meta.get("tutorial_title") or tutorial_id
        topic = meta.get("topic", "N/A")
        tools = format_list(first.get("tools", []))  # show full tool ids

        # Use all datasets referenced across items to avoid missing entries.
        dataset_paths = collect_all_datasets(t_items)
        dataset_count = len(dataset_paths)
        lines.extend(
            [
                f"## {title} ({tutorial_id})",
                f"- Topic: {topic}",
                f"- Tools: {tools}",
                f"- Datasets ({dataset_count}): {format_paths_short(dataset_paths)}",
                "",
                "Questions:",
            ]
        )
        for idx, item in enumerate(t_items, start=1):
            meta = item.get("metadata", {})
            q_tools = format_list(item.get("tools", []))  # full ids per question
            q_datasets = format_paths_short(meta.get("dataset_paths") or meta.get("datasets") or [])
            lines.append(f"- **{item.get('id')}** — {item.get('query')}")
            lines.append(f"  - Tools: {q_tools}")
            lines.append(f"  - Datasets: {q_datasets}")
        lines.append("")  # blank line between tutorials
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    items = load_items(args.input)
    write_markdown(items, args.output)


if __name__ == "__main__":
    main()
