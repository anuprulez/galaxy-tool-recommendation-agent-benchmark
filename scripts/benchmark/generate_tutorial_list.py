from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan GTN repo and build tutorial_list.yaml")
    parser.add_argument(
        "--gtn-root",
        type=Path,
        default=Path("training-material"),
        help="Path to GTN training-material checkout",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/tutorial_list.yaml"),
        help="Where to write the tutorial list YAML",
    )
    parser.add_argument(
        "--min-queries",
        type=int,
        default=10,
        help="Default min_queries to assign to each tutorial",
    )
    parser.add_argument(
        "--filter",
        dest="filter_str",
        help="Only include tutorials whose path contains this substring",
    )
    parser.add_argument(
        "--exclude-topic",
        action="append",
        dest="exclude_topics",
        default=["admin", "galaxy-interface", "teaching"],
        help="Exclude tutorials under these topics (repeatable). Default: admin, galaxy-interface, teaching",
    )
    return parser.parse_args()


def find_tutorial_ids(gtn_root: Path, filter_str: str | None, exclude_topics: List[str]) -> List[str]:
    tutorial_ids: List[str] = []
    exclude = set(exclude_topics or [])
    for tutorial_md in gtn_root.glob("topics/*/tutorials/*/tutorial.md"):
        tutorial_id = tutorial_md.parent.relative_to(gtn_root).as_posix()
        parts = tutorial_id.split("/")
        topic = parts[1] if len(parts) > 1 else ""
        if topic in exclude:
            continue
        if filter_str and filter_str not in tutorial_id:
            continue
        tutorial_ids.append(tutorial_id)
    tutorial_ids.sort()
    return tutorial_ids


def build_yaml_payload(tutorial_ids: List[str], min_queries: int) -> dict:
    return {"tutorials": [{"id": tid, "min_queries": min_queries} for tid in tutorial_ids]}


def write_yaml(payload: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, sort_keys=False)


def main() -> None:
    args = parse_args()
    tutorial_ids = find_tutorial_ids(args.gtn_root, args.filter_str, args.exclude_topics)
    if not tutorial_ids:
        raise SystemExit(f"No tutorials found under {args.gtn_root}")
    payload = build_yaml_payload(tutorial_ids, args.min_queries)
    write_yaml(payload, args.output)
    print(f"Wrote {len(tutorial_ids)} tutorials to {args.output}")


if __name__ == "__main__":
    main()
