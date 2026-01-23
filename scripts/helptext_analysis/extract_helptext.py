#!/usr/bin/env python3
"""
Fetch Galaxy tool panel from https://usegalaxy.eu/api/tools, extract all entries with
{"model_class": "Tool"}, write:
  1) JSON file of only tools
  2) Tabular file (TSV or CSV) with columns:
     tool_id, name, description, panel_section_id, panel_section_name

Works both:
  - online via requests (default), and
  - offline via an existing downloaded JSON (e.g. /mnt/data/tools.json)
  - https://usegalaxy.eu/api/tools/toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0/raw_tool_source
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pandas as pd
import requests

DEFAULT_URL = "https://usegalaxy.eu/api/tools"
n_tools = 100


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
                    yield from iter_tool_objects(child, inherited_section_id, inherited_section_name)
                return  # avoid traversing multiple container keys redundantly

        # Generic dict traversal (safe fallback)
        for v in node.values():
            yield from iter_tool_objects(v, inherited_section_id, inherited_section_name)

    elif isinstance(node, list):
        for item in node:
            yield from iter_tool_objects(item, inherited_section_id, inherited_section_name)


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
        columns=["tool_id", "name", "description", "panel_section_id", "panel_section_name"],
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
    return df


import re
import xml.etree.ElementTree as ET
from markdown import markdown
from bs4 import BeautifulSoup

def _extract_help_from_xml(xml_text: str) -> str | None:
    # 1) Try XML parsing first (robust to nested tags inside <help>)
    try:
        root = ET.fromstring(xml_text)
        help_el = root.find(".//help")
        if help_el is not None:
            # Collect all text within <help>, including nested tags
            txt = "".join(help_el.itertext()).strip()
            return txt if txt else None
    except Exception:
        pass

    # 2) Fallback: regex extraction (handles malformed XML in rare cases)
    m = re.search(r"<help\b[^>]*>(.*?)</help>", xml_text, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return None
    inner = m.group(1)
    # Remove any tags inside help and unescape basic entities
    inner = re.sub(r"<[^>]+>", "", inner)
    inner = inner.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    inner = inner.strip()
    return inner if inner else None

def _clean_text(text: str) -> str:
    # Replace multiple whitespace with single space, strip leading/trailing whitespace
    text = re.sub(r"\s+", " ", text).strip()
    html = markdown(text)
    help_text = BeautifulSoup(html, "html.parser").get_text("\n")
    return help_text.strip()


def fetch_tool_help_texts(df, tool_id_col: str = "tool_id", base_url: str = "https://usegalaxy.eu", timeout: int = 30):
    """
    For each Galaxy tool_id in `df[tool_id_col]`, fetch the raw tool XML via:
        {base_url}/api/tools/{tool_id}/raw_tool_source
    and extract the text inside <help>...</help>.

    Returns
    -------
    list[str | None]
        A list aligned to df rows. Each element is the extracted help text (str),
        or None if missing/unavailable/unparseable.
    """
    import re
    import requests
    import xml.etree.ElementTree as ET

    tool_ids = df[tool_id_col].astype(str).tolist()
    out = []

    with requests.Session() as s:
        s.headers.update({"User-Agent": "tool-help-scraper/1.0"})
        for tidx, tid in enumerate(tool_ids):
            url = f"{base_url.rstrip('/')}/api/tools/{tid}/raw_tool_source"
            try:
                r = s.get(url, timeout=timeout)
                if not r.ok or not r.text:
                    out.append(None)
                    continue
                help_text = _extract_help_from_xml(r.text)
                help_text = _clean_text(help_text)
                print(f"Tool id: {tid}, tool help text: {help_text}")
                print()
                print()
                out.append(help_text)
            except Exception:
                out.append(None)
            if tidx == n_tools:
                print(f"  Fetched help text for {tidx + 1}/{len(tool_ids)} tools...")
                break

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=DEFAULT_URL, help="Galaxy /api/tools URL")
    ap.add_argument("--input_json", default=None, help="Optional: path to a previously downloaded /api/tools JSON (skips HTTP).")
    ap.add_argument("--out-json", default="data/tools_only.json", help="Output JSON (tools only)")
    ap.add_argument("--out-table", default="data/tools_metadata.tsv", help="Output table (TSV/CSV)")
    ap.add_argument("--table-format", choices=["tsv", "csv"], default="tsv", help="Table format")
    ap.add_argument("--timeout", type=int, default=120, help="HTTP timeout seconds")
    args = ap.parse_args()
    if args.input_json:
        payload = load_json_file(Path(args.input_json))
    else:
        payload = fetch_json(args.url, timeout=args.timeout)
    df, tools_only = tools_to_dataframe(payload)

    write_tools_json(tools_only, Path(args.out_json))
    df_tools = write_table(df, Path(args.out_table), fmt=args.table_format)

    lst_help = fetch_tool_help_texts(df_tools)
    print(lst_help)
    df_tools["help_text"] = lst_help
    write_table(df_tools, Path(args.out_table), fmt=args.table_format)

    print(f"Wrote {len(tools_only)} Tool objects -> {args.out_json}")
    print(f"Wrote {len(df)} rows -> {args.out_table} ({args.table_format.upper()})")
    return 0


if __name__ == "__main__":
    main()
