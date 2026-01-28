from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from gtn_benchmark.gtn_loader import load_tutorials
from gtn_benchmark.io_utils import load_tutorial_list


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate template queries for all tutorials.")
    parser.add_argument(
        "--tutorial-list",
        type=Path,
        default=Path("data/tutorial_list_all_tools.yaml"),
        help="Tutorial list YAML",
    )
    parser.add_argument(
        "--gtn-root",
        type=Path,
        default=Path("training-material"),
        help="GTN root",
    )
    parser.add_argument(
        "--out-jsonl",
        type=Path,
        default=Path("tmp_stats/manual_queries_all.jsonl"),
        help="Output JSONL path",
    )
    return parser.parse_args()


KEYWORD_ACTIONS = [
    (re.compile(r"svm", re.IGNORECASE), "train a support vector machine classifier"),
    (re.compile(r"ensemble", re.IGNORECASE), "train an ensemble model"),
    (re.compile(r"searchcv|grid|random", re.IGNORECASE), "tune hyperparameters with cross-validation"),
    (re.compile(r"build_pipeline|pipeline", re.IGNORECASE), "build a machine-learning pipeline"),
    (re.compile(r"plotly|ggplot", re.IGNORECASE), "visualize model performance"),
    (re.compile(r"keras|deep", re.IGNORECASE), "configure or train a deep learning model"),
    (re.compile(r"numeric_clustering|cluster", re.IGNORECASE), "cluster numeric samples"),
    (re.compile(r"csv_to_tabular", re.IGNORECASE), "convert CSV data to tabular format"),
    (re.compile(r"pdaug_sequence_property_based_descriptors", re.IGNORECASE), "compute peptide descriptors"),
    (re.compile(r"pdaug_addclasslabel", re.IGNORECASE), "add class labels to a feature table"),
    (re.compile(r"pdaug_merge_dataframes", re.IGNORECASE), "merge feature tables"),
    (re.compile(r"pdaug_ml_models", re.IGNORECASE), "train machine-learning models"),
    (re.compile(r"pdaug_basic_plots", re.IGNORECASE), "plot model evaluation summaries"),
]


def action_for_tool(tool_id: str) -> str:
    for pattern, action in KEYWORD_ACTIONS:
        if pattern.search(tool_id):
            return action
    return "run an analysis step from the tutorial"


def tool_base(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def version_key(version: str) -> tuple[Any, ...]:
    parts = re.split(r"[._+-]", version)
    key: list[Any] = []
    for part in parts:
        if part.isdigit():
            key.append((0, int(part)))
        else:
            key.append((1, part))
    return tuple(key)


def select_latest_versions(tool_ids: list[str]) -> list[str]:
    latest: dict[str, str] = {}
    for tool_id in tool_ids:
        if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
            base = tool_base(tool_id)
            version = tool_id.split("/")[-1]
            if base not in latest:
                latest[base] = tool_id
                continue
            current_version = latest[base].split("/")[-1]
            if version_key(version) > version_key(current_version):
                latest[base] = tool_id
        else:
            latest[tool_id] = tool_id
    return list(latest.values())


def build_queries(title: str, tool_id: str) -> list[dict[str, str]]:
    action = action_for_tool(tool_id)
    return [
        {
            "query": f"In the context of {title}, I need to {action}. How should I proceed?",
            "query_type": "science_first",
        },
        {
            "query": f"My goal is to complete the {title} workflow; I need to {action}. What should I do?",
            "query_type": "science_first",
        },
        {
            "query": f"Which Galaxy tool should I use to {action} in {title}?",
            "query_type": "tool_first",
        },
        {
            "query": f"How can I {action} for {title} in Galaxy?",
            "query_type": "tool_first",
        },
    ]


def main() -> None:
    args = parse_args()
    tutorial_requests = load_tutorial_list(args.tutorial_list)
    tutorials = load_tutorials(tutorial_requests, args.gtn_root)

    out_items: list[dict[str, Any]] = []
    for tutorial in tutorials:
        tool_ids = select_latest_versions(tutorial.tools)
        if not tool_ids:
            continue
        datasets = tutorial.dataset_paths or tutorial.datasets or []
        short_name = tutorial.short_name
        for tool_index, tool_id in enumerate(tool_ids, start=1):
            queries = build_queries(tutorial.title, tool_id)
            for i, q in enumerate(queries, start=1):
                suffix = f"q{tool_index:02d}{i}"
                out_items.append(
                    {
                        "id": f"{short_name}-{suffix}",
                        "tutorial_id": tutorial.tutorial_id,
                        "query": q["query"],
                        "tools": [tool_id],
                        "workflows": tutorial.workflows,
                        "metadata": {
                            "topic": tutorial.topic,
                            "tutorial_title": tutorial.title,
                            "datasets": datasets,
                            "dataset_paths": datasets,
                            "dataset_count": len(datasets),
                            "query_type": q["query_type"],
                            "tool_focus": tool_id,
                            "version": "manual_template",
                        },
                    }
                )

    args.out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with args.out_jsonl.open("w", encoding="utf-8") as handle:
        for item in out_items:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
