from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate tool recommendations with Hit@k, MRR@k, and nDCG@k."
    )
    parser.add_argument(
        "--gold",
        type=Path,
        required=True,
        help="Gold JSONL file (e.g., data/benchmark/v1_items.jsonl)",
    )
    parser.add_argument(
        "--predictions",
        type=Path,
        required=True,
        help=(
            "Predictions JSONL with {'id': str, 'predictions': [tool_id, ...]}"
        ),
    )
    parser.add_argument(
        "--k",
        type=str,
        default="1,3,5,10",
        help="Comma-separated cutoffs (default: 1,3,5,10)",
    )
    parser.add_argument(
        "--normalize-tools",
        action="store_true",
        help=(
            "Normalize toolshed IDs by removing the version (last path segment)."
        ),
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def normalize_tool_id(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def unique_in_order(values: Iterable[str]) -> List[str]:
    seen = set()
    output: List[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output


def hit_at_k(preds: List[str], gold: set[str], k: int) -> float:
    if not gold:
        return 0.0
    return 1.0 if any(p in gold for p in preds[:k]) else 0.0


def mrr_at_k(preds: List[str], gold: set[str], k: int) -> float:
    if not gold:
        return 0.0
    for idx, pred in enumerate(preds[:k], start=1):
        if pred in gold:
            return 1.0 / idx
    return 0.0


def ndcg_at_k(preds: List[str], gold: set[str], k: int) -> float:
    if not gold:
        return 0.0

    def dcg(relevances: List[int]) -> float:
        score = 0.0
        for i, rel in enumerate(relevances, start=1):
            if rel:
                score += 1.0 / math.log2(i + 1)
        return score

    relevances = [1 if p in gold else 0 for p in preds[:k]]
    ideal = [1] * min(len(gold), k)
    dcg_val = dcg(relevances)
    idcg_val = dcg(ideal)
    return dcg_val / idcg_val if idcg_val > 0 else 0.0


def compute_metrics(
    gold_items: Dict[str, List[str]],
    pred_items: Dict[str, List[str]],
    ks: List[int],
) -> Dict[str, Dict[str, float]]:
    totals = {k: {"hit": 0.0, "mrr": 0.0, "ndcg": 0.0} for k in ks}
    count = 0

    for qid, gold_tools in gold_items.items():
        preds = pred_items.get(qid)
        if preds is None:
            continue
        gold_set = set(gold_tools)
        count += 1
        for k in ks:
            totals[k]["hit"] += hit_at_k(preds, gold_set, k)
            totals[k]["mrr"] += mrr_at_k(preds, gold_set, k)
            totals[k]["ndcg"] += ndcg_at_k(preds, gold_set, k)

    if count == 0:
        return {str(k): {"hit": 0.0, "mrr": 0.0, "ndcg": 0.0} for k in ks}

    results: Dict[str, Dict[str, float]] = {}
    for k in ks:
        results[str(k)] = {
            "hit": totals[k]["hit"] / count,
            "mrr": totals[k]["mrr"] / count,
            "ndcg": totals[k]["ndcg"] / count,
        }
    results["count"] = {"queries": count}
    return results


def main() -> None:
    args = parse_args()
    ks = [int(k.strip()) for k in args.k.split(",") if k.strip()]

    gold_items_raw = load_jsonl(args.gold)
    pred_items_raw = load_jsonl(args.predictions)

    gold_items: Dict[str, List[str]] = {}
    for item in gold_items_raw:
        qid = item.get("id")
        tools = item.get("tools") or []
        if qid is None:
            continue
        if args.normalize_tools:
            tools = [normalize_tool_id(t) for t in tools]
        gold_items[qid] = unique_in_order(tools)

    pred_items: Dict[str, List[str]] = {}
    for item in pred_items_raw:
        qid = item.get("id")
        preds = item.get("predictions") or []
        if qid is None:
            continue
        if args.normalize_tools:
            preds = [normalize_tool_id(p) for p in preds]
        pred_items[qid] = unique_in_order(preds)

    results = compute_metrics(gold_items, pred_items, ks)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
