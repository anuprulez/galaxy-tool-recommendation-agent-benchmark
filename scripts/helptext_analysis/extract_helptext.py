#!/usr/bin/env python3
"""
Fetch Galaxy tool panel from https://usegalaxy.org/api/tools, extract all entries with
Fetch Galaxy tool panel from https://usegalaxy.org/api/tools, extract all entries with
{"model_class": "Tool"}, write:
  1) JSON file of only tools
  2) Tabular file (TSV or CSV) with columns:
     tool_id, name, description, panel_section_id, panel_section_name

"""

from __future__ import annotations

import argparse
import json
from math import dist
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pandas as pd
import numpy as np
import re
import requests

from markdown import markdown
from bs4 import BeautifulSoup

import extract_embeddings

DEFAULT_URL = "https://usegalaxy.org/api/tools"
n_tools = 3500
K = 5
similarity_threshold = 0.5


def fetch_json(url: str, timeout: int = 120) -> Any:
    r = requests.get(url, timeout=timeout, headers={"Accept": "application/json"})
    r.raise_for_status()
    return r.json()


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_tool_objects(
    node: Any,
    inherited_section_id: Optional[str] = None,
    inherited_section_name: Optional[str] = None,
) -> Iterable[Tuple[Dict[str, Any], str, str]]:
    """
    Walk the /api/tools payload, yielding (tool_obj, panel_section_id, panel_section_name)
    for each tool_obj where model_class == "Tool".

    The Galaxy tool panel is typically nested: ToolSection -> elems -> (Tool|ToolSection|...)
    """
    if isinstance(node, dict):
        mc = node.get("model_class")

        # If this is a section, update inherited info and traverse elems (if present)
        if mc == "ToolSection":
            sec_id = node.get("id") or inherited_section_id or ""
            sec_name = node.get("name") or inherited_section_name or ""
            elems = node.get("elems")
            if isinstance(elems, list):
                for child in elems:
                    yield from iter_tool_objects(child, sec_id, sec_name)
            return

        # If this is a Tool, yield it
        if mc == "Tool":
            sec_id = node.get("panel_section_id") or inherited_section_id or ""
            sec_name = node.get("panel_section_name") or inherited_section_name or ""
            yield node, str(sec_id or ""), str(sec_name or "")
            return

        # Other dict types: traverse common container fields
        for k in ("elems", "items", "children", "tools"):
            v = node.get(k)
            if isinstance(v, list):
                for child in v:
                    yield from iter_tool_objects(
                        child, inherited_section_id, inherited_section_name
                    )
                return  # avoid traversing multiple container keys redundantly

        # Generic dict traversal (safe fallback)
        for v in node.values():
            yield from iter_tool_objects(
                v, inherited_section_id, inherited_section_name
            )

    elif isinstance(node, list):
        for item in node:
            yield from iter_tool_objects(
                item, inherited_section_id, inherited_section_name
            )


def tools_to_dataframe(payload: Any) -> Tuple[pd.DataFrame, List[Dict[str, Any]]]:
    """
    Returns:
      - df with columns [tool_id, name, description, panel_section_id, panel_section_name]
      - tools_only: list of raw tool dicts (deduplicated by tool id)
    """
    records: List[Dict[str, str]] = []
    tools_only: List[Dict[str, Any]] = []
    seen_ids = set()
    n_tl = 0

    for tool_obj, sec_id, sec_name in iter_tool_objects(payload):
        tid = str(tool_obj.get("id", "")).strip()
        if not tid or tid in seen_ids:
            continue
        seen_ids.add(tid)

        tools_only.append(tool_obj)
        records.append(
            {
                "tool_id": tid,
                "name": str(tool_obj.get("name", "") or ""),
                "description": str(tool_obj.get("description", "") or ""),
                "panel_section_id": str(sec_id or ""),
                "panel_section_name": str(sec_name or ""),
            }
        )
        n_tl += 1
        if n_tl == n_tools:
            print(f"  Processed {n_tl} tools...")
            break

    df = pd.DataFrame.from_records(
        records,
        columns=[
            "tool_id",
            "name",
            "description",
            "panel_section_id",
            "panel_section_name",
        ],
    )

    # Stable ordering (useful for diffs)
    if not df.empty:
        df = df.sort_values(
            by=["panel_section_name", "name", "tool_id"],
            kind="mergesort",  # stable sort
            ignore_index=True,
        )

    return df, tools_only


def write_tools_json(tools_only: List[Dict[str, Any]], out_json: Path) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_json.open("w", encoding="utf-8") as f:
        json.dump(tools_only, f, ensure_ascii=False, indent=2)


def write_table(df: pd.DataFrame, out_path: Path, fmt: str = "tsv") -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if fmt.lower() == "csv":
        df.to_csv(out_path, index=False)
    else:
        df.to_csv(out_path, sep="\t", index=False)


def clean_text(text: str) -> str:
    # Replace multiple whitespace with single space, strip leading/trailing whitespace
    text = re.sub(r"\s+", " ", text).strip()
    html = markdown(text)
    help_text = BeautifulSoup(html, "html.parser").get_text("\n")
    return help_text.strip()


def request_galaxy_tool_help(
    raw_tool_source_url: str, timeout: int = 60, tid: str = ""
) -> str:
    """
    Download a Galaxy tool wrapper (raw_tool_source) and return the contents of <help>...</help>.
    Works even if the XML is slightly malformed elsewhere.
    """
    HELP_BLOCK_RE = re.compile(
        r"<help\b[^>]*>\s*(?P<body>.*?)\s*</help>",
        flags=re.DOTALL | re.IGNORECASE,
    )

    r = requests.get(raw_tool_source_url, timeout=timeout)
    r.raise_for_status()
    xml_text = r.text

    m = HELP_BLOCK_RE.search(xml_text)
    if not m:
        print(
            f"{m} is also None. No <help> text found after text search for tool id: {tid}"
        )
    return m.group("body").strip()


def fetch_tool_help_texts(
    df,
    tool_id_col: str = "tool_id",
    base_url: str = "https://usegalaxy.org",
    timeout: int = 30,
):

    tool_ids = df[tool_id_col].astype(str).tolist()
    out = []

    with requests.Session() as s:
        s.headers.update({"User-Agent": "tool-help-scraper/1.0"})
        for tidx, tid in enumerate(tool_ids):
            url = f"{base_url.rstrip('/')}/api/tools/{tid}/raw_tool_source"
            try:
                help_text = request_galaxy_tool_help(url, timeout=timeout, tid=tid)
                help_text = clean_text(help_text)
                out.append(help_text)
            except Exception as e:
                print(f"Error fetching/parsing help text for tool id: {tid}: {e}")
                out.append("")
                continue
            if tidx % 100 == 0 and tidx > 0:
                print(f" Processed help text for {tidx}/{len(tool_ids)} tools...")
    return out


def compute_text_similarity(df_tools) -> float:

    tool_ids = df_tools["tool_id"].astype(str).to_list()
    # extract embeddings for help texts
    embeddings = extract_embeddings.get_sentence_embeddings(
        df_tools["help_text"].fillna("").tolist()
    )

    df_tools["embeddings"] = embeddings

    print("Computing similarity...")
    # Parse embeddings: string -> list -> numpy array
    X = df_tools["embeddings"].to_list()

    # Normalize rows (cosine sim = dot of normalized vectors)
    X /= np.linalg.norm(X, axis=1, keepdims=True) + 1e-12

    # All-vs-all cosine similarity (N, N)
    S = X @ X.T

    # Top-K neighbors per row (exclude self)
    top_ids = []
    top_sims = []

    n = S.shape[0]
    k = min(K, n - 1)

    for i in range(n):
        sims = S[i].copy()
        sims[i] = -np.inf  # exclude self

        # fast top-k selection (unsorted), then sort those k
        idx = np.argpartition(sims, -k)[-k:]
        idx = idx[np.argsort(sims[idx])[::-1]]

        top_ids.append([tool_ids[j] for j in idx])
        top_sims.append([float(sims[j]) for j in idx])

    df_tools["topk_neighbor_tool_ids"] = [json.dumps(x) for x in top_ids]
    df_tools["topk_cosine_sims"] = [json.dumps(x) for x in top_sims]
    return df_tools


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=DEFAULT_URL, help="Galaxy /api/tools URL")
    ap.add_argument(
        "--input_json",
        default=None,
        help="Optional: path to a previously downloaded /api/tools JSON (skips HTTP).",
    )
    ap.add_argument(
        "--out-json", default="data/tools_only.json", help="Output JSON (tools only)"
    )
    ap.add_argument(
        "--out-table", default="data/tools_metadata.tsv", help="Output table (TSV/CSV)"
    )
    ap.add_argument(
        "--out-table-helptext", default="data/tools_helptext.tsv", help="Output table (TSV/CSV)"
    )
    ap.add_argument(
        "--table-format", choices=["tsv", "csv"], default="tsv", help="Table format"
    )
    ap.add_argument("--timeout", type=int, default=120, help="HTTP timeout seconds")

    args = ap.parse_args()
    if args.input_json:
        payload = load_json_file(Path(args.input_json))
    else:
        payload = fetch_json(args.url, timeout=args.timeout)
    print("Extracted tool metadata for", len(df_tools), "tools")
    df_tools, tools_only = tools_to_dataframe(payload)
    
    df_tools["help_text"] = fetch_tool_help_texts(df_tools)
    print("Extracted tool helptext for", len(df_tools), "tools")
    df_outcome = df_tools[["tool_id", "help_text"]]

    write_tools_json(tools_only, Path(args.out_json))
    print(f"Wrote {len(tools_only)} Tool objects -> {args.out_json}")
    write_table(df_tools, Path(args.out_table), fmt=args.table_format)
    print(f"Wrote {len(df_tools)} rows -> {args.out_table} ({args.table_format})")
    write_table(df_outcome, Path(args.out_table_helptext), fmt=args.table_format)
    print(f"Wrote {len(df_outcome)} rows -> {args.out_table_helptext} ({args.table_format})")


if __name__ == "__main__":
    main()
