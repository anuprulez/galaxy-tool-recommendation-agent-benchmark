from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a topic-organized catalog of GTN tools referenced in the benchmark."
    )
    parser.add_argument(
        "--benchmark",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark JSONL file used to derive query tools.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tmp_stats/tool_catalog.md"),
        help="Markdown destination for the catalog.",
    )
    return parser.parse_args()


def load_items(path: Path) -> list[dict]:
    if not path.exists():
        raise ValueError(f"Benchmark file {path} does not exist.")
    items = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def main() -> None:
    args = parse_args()
    entries = load_items(args.benchmark)
    topic_tools: dict[str, set[str]] = defaultdict(set)
    tool_counts: dict[str, int] = defaultdict(int)

    for entry in entries:
        topic = entry.get("metadata", {}).get("topic") or "uncategorized"
        tools = entry.get("tools") or []
        for tool in tools:
            if not tool:
                continue
            topic_tools[topic].add(tool.strip())
            tool_counts[tool.strip()] += 1

    lines = ["# Tool catalog by topic", ""]
    for topic in sorted(topic_tools):
        lines.append(f"## {topic}")
        lines.append("")
        tools = sorted(topic_tools[topic])
        for tool in tools:
            lines.append(f"- `{tool}`")
        lines.append("")

    lines.append("## Tool frequencies")
    lines.append("")
    for tool, count in sorted(tool_counts.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{tool}` — referenced in {count} queries")
    lines.append("")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
