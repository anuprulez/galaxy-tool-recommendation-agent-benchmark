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


def write_markdown(items: List[Dict[str, Any]], output: Path) -> None:
    grouped = group_by_tutorial(items)
    lines: list[str] = ["# GTN Benchmark Items (Readable)", ""]
    for tutorial_id, t_items in sorted(grouped.items(), key=lambda kv: kv[0]):
        first = t_items[0]
        meta = first.get("metadata", {})
        title = meta.get("tutorial_title") or tutorial_id
        topic = meta.get("topic", "N/A")
        tools = format_list(first.get("tools", []))
        workflows = format_list(first.get("workflows", []))
        dataset_paths = meta.get("dataset_paths") or meta.get("datasets") or []
        dataset_count = meta.get("dataset_count") or len(dataset_paths)
        lines.extend(
            [
                f"## {title} ({tutorial_id})",
                f"- Topic: {topic}",
                f"- Tools: {tools}",
                f"- Workflows: {workflows}",
                f"- Datasets ({dataset_count}): {format_list(dataset_paths)}",
                "",
                "Questions:",
            ]
        )
        for idx, item in enumerate(t_items, start=1):
            meta = item.get("metadata", {})
            difficulty = meta.get("difficulty", "medium")
            lines.append(f"{idx}. [{difficulty}] {item.get('id')}: {item.get('query')}")
        lines.append("")  # blank line between tutorials
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    items = load_items(args.input)
    write_markdown(items, args.output)


if __name__ == "__main__":
    main()
