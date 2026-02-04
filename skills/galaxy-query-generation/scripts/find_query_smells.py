#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Item:
    line_no: int
    item_id: str
    query_type: str
    tool0: str
    query: str


def iter_items(path: str, start: int, end: int) -> Iterable[Item]:
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if line_no < start:
                continue
            if line_no > end:
                break
            if not line.strip():
                continue
            obj = json.loads(line)
            metadata = obj.get("metadata") if isinstance(obj.get("metadata"), dict) else {}
            tools = obj.get("tools") if isinstance(obj.get("tools"), list) else []
            tool0 = tools[0] if tools and isinstance(tools[0], str) else ""
            yield Item(
                line_no=line_no,
                item_id=str(obj.get("id", "")),
                query_type=str(metadata.get("query_type", "")),
                tool0=tool0,
                query=str(obj.get("query", "")),
            )


_WS_RE = re.compile(r"\s+")
_NUM_RE = re.compile(r"\b\d+(\.\d+)?\b")
_PUNCT_RE = re.compile(r"[^a-z0-9<> ]+")


def normalize_query(q: str) -> str:
    q = q.strip().lower()
    q = _NUM_RE.sub("<n>", q)
    q = q.replace("galaxy", "galaxy")  # keep as-is, but explicit for clarity
    q = _PUNCT_RE.sub(" ", q)
    q = _WS_RE.sub(" ", q).strip()
    return q


def compile_smell_patterns() -> list[tuple[str, re.Pattern[str]]]:
    return [
        ("tool_leak_toolshed", re.compile(r"toolshed\.g2\.bx\.psu\.edu", re.I)),
        ("tool_leak_backticks", re.compile(r"`")),
        ("tutorial_or_gtn", re.compile(r"\b(tutorial|gtn)\b", re.I)),
        ("guide_phrase", re.compile(r"\bguide\b|from the guide", re.I)),
        ("template_perform", re.compile(r"\bwould you recommend to perform\b", re.I)),
        ("template_analysis_step", re.compile(r"\brun (an )?analysis step\b", re.I)),
        ("too_generic_step", re.compile(r"\b(previous|downstream|intermediate) (step|dataset|output)\b", re.I)),
        ("too_generic_custom_code", re.compile(r"\brun custom (code|scripts?)\b", re.I)),
        ("file_extension_like", re.compile(r"\.(fastq|fq|fasta|fa|bam|sam|vcf|bed|gtf|gff|tsv|csv|txt|json|yaml|yml|h5ad|loom|mzml|mgf|zip|tar|gz)\b", re.I)),
        ("url", re.compile(r"https?://", re.I)),
        ("accession_like", re.compile(r"\b(SRR|ERR|DRR)\d+\b|\bE-MTAB-\d+\b|\bGSE\d+\b|\bGSM\d+\b", re.I)),
    ]


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Heuristic 'smell' scan for queries that might deserve rewrite (non-blocking)."
    )
    ap.add_argument("--input", required=True, help="Path to v1_items.jsonl")
    ap.add_argument("--start", type=int, required=True, help="Start line (1-based, inclusive)")
    ap.add_argument("--count", type=int, required=True, help="Number of lines/items to scan")
    ap.add_argument("--near-dup-threshold", type=float, default=0.92, help="SequenceMatcher ratio threshold")
    ap.add_argument("--min-query-len", type=int, default=50, help="Flag queries shorter than this")
    args = ap.parse_args()

    start = args.start
    end = start + args.count - 1

    items = list(iter_items(args.input, start=start, end=end))
    if not items:
        print("No items found in requested range.", file=sys.stderr)
        return 2

    smell_patterns = compile_smell_patterns()

    # 1) Pattern hits + "tool id appears in query" (common leakage)
    hits: list[tuple[int, str, str, str]] = []
    for it in items:
        q = it.query
        for name, pat in smell_patterns:
            if pat.search(q):
                hits.append((it.line_no, it.item_id, name, q))
        if it.tool0 and it.tool0.lower() in q.lower():
            hits.append((it.line_no, it.item_id, "tool_leak_tool_id_literal", q))
        if len(q.strip()) < args.min_query_len:
            hits.append((it.line_no, it.item_id, f"very_short(<{args.min_query_len})", q))

    # 2) Exact duplicates after normalization
    norm_map: dict[str, list[Item]] = defaultdict(list)
    for it in items:
        norm_map[normalize_query(it.query)].append(it)
    exact_dups = {k: v for k, v in norm_map.items() if len(v) > 1}

    # 3) Near-duplicate pairs (within batch only; O(n^2) but n=150)
    near_dups: list[tuple[float, Item, Item]] = []
    norms = [(it, normalize_query(it.query)) for it in items]
    for i in range(len(norms)):
        it_a, na = norms[i]
        for j in range(i + 1, len(norms)):
            it_b, nb = norms[j]
            if not na or not nb:
                continue
            ratio = difflib.SequenceMatcher(a=na, b=nb).ratio()
            if ratio >= args.near_dup_threshold:
                near_dups.append((ratio, it_a, it_b))
    near_dups.sort(key=lambda t: (-t[0], t[1].line_no, t[2].line_no))

    # Output
    print(f"Range: {start}-{end} (items: {len(items)})")
    print()

    if hits:
        print("Smell hits (non-blocking):")
        for line_no, item_id, name, q in sorted(hits, key=lambda x: (x[0], x[2])):
            q1 = q.strip().replace("\n", " ")
            if len(q1) > 160:
                q1 = q1[:160] + "…"
            print(f"- L{line_no} {item_id} [{name}] {q1}")
        print()
    else:
        print("Smell hits: none")
        print()

    if exact_dups:
        print("Exact duplicates (normalized):")
        for _, ditems in sorted(exact_dups.items(), key=lambda kv: (-len(kv[1]), kv[1][0].line_no)):
            print(f"- {len(ditems)}x: " + ", ".join(f"L{it.line_no}:{it.item_id}" for it in ditems))
        print()
    else:
        print("Exact duplicates: none")
        print()

    if near_dups:
        print(f"Near-duplicate pairs (ratio >= {args.near_dup_threshold}):")
        for ratio, a, b in near_dups[:80]:
            print(f"- {ratio:.3f}: L{a.line_no}:{a.item_id}  <->  L{b.line_no}:{b.item_id}")
        if len(near_dups) > 80:
            print(f"... ({len(near_dups) - 80} more)")
        print()
    else:
        print(f"Near-duplicate pairs (>= {args.near_dup_threshold}): none")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
