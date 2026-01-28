from __future__ import annotations

import argparse
import json
import logging
import ssl
import subprocess
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOGGER = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch a Galaxy server tool list and write an agent-friendly JSONL snapshot "
            "(plus optional indices)."
        )
    )
    parser.add_argument(
        "--server",
        type=str,
        default="https://usegalaxy.org",
        help="Galaxy server base URL (default: https://usegalaxy.org).",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--in-panel",
        action="store_true",
        help="Fetch only tools shown in the tool panel (smaller candidate set).",
    )
    group.add_argument(
        "--no-in-panel",
        action="store_true",
        help="Fetch all installed tools including non-panel/hidden tools (larger universe).",
    )
    parser.add_argument(
        "--out-jsonl",
        type=Path,
        default=None,
        help="Output JSONL path (one tool per line).",
    )
    parser.add_argument(
        "--out-index",
        type=Path,
        default=None,
        help="Output index JSON path: base_id -> [tool_id,...].",
    )
    parser.add_argument(
        "--out-by-section",
        type=Path,
        default=None,
        help="Output JSON path with 'by_section' mapping: section_name -> [tool_id,...].",
    )
    parser.add_argument(
        "--include-io-details",
        action="store_true",
        help=(
            "Also fetch per-tool input/output metadata via /api/tools/<tool_id> "
            "(slower; many HTTP requests)."
        ),
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="HTTP timeout seconds (default: 120).",
    )
    return parser.parse_args()


def normalize_base_id(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def _http_get_json(url: str, timeout: int) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "galaxy-tool-recommendation-agent-benchmark/0.1",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8")
        return json.loads(data)
    except (ssl.SSLError, urllib.error.URLError):
        # Some older Python/OpenSSL builds can fail TLS negotiation with modern servers.
        # Fall back to curl (commonly available) to keep the script usable.
        return _curl_get_json(url, timeout=timeout)


def _curl_get_json(url: str, timeout: int) -> Any:
    cmd = [
        "curl",
        "-fsSL",
        "--max-time",
        str(timeout),
        "-H",
        "Accept: application/json",
        "-A",
        "galaxy-tool-recommendation-agent-benchmark/0.1",
        url,
    ]
    out = subprocess.check_output(cmd)
    return json.loads(out.decode("utf-8"))


def fetch_tools(server: str, in_panel: bool, timeout: int) -> List[dict]:
    server = server.rstrip("/")
    query = urllib.parse.urlencode({"in_panel": "true" if in_panel else "false"})
    url = f"{server}/api/tools?{query}"
    payload = _http_get_json(url, timeout=timeout)
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected /api/tools response type: {type(payload)}")
    tools: List[dict] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        tool_id = item.get("id") or item.get("tool_id")
        if not isinstance(tool_id, str) or not tool_id:
            continue
        tools.append(
            {
                "tool_id": tool_id,
                "name": item.get("name") or "",
                "version": item.get("version") or "",
                "description": item.get("description") or "",
                "base_id": normalize_base_id(tool_id),
            }
        )
    return tools


def fetch_by_section(server: str, timeout: int) -> dict:
    server = server.rstrip("/")
    url = f"{server}/api/tool_panels/default"
    payload = _http_get_json(url, timeout=timeout)
    if not isinstance(payload, dict):
        raise ValueError(f"Unexpected /api/tool_panels/default response type: {type(payload)}")

    by_section: Dict[str, List[str]] = {}
    for _section_id, section in payload.items():
        if not isinstance(section, dict):
            continue
        name = section.get("name")
        tools = section.get("tools")
        if not isinstance(name, str) or not name:
            continue
        if not isinstance(tools, list):
            continue
        tool_ids: List[str] = [t for t in tools if isinstance(t, str) and t]
        if tool_ids:
            by_section[name] = tool_ids

    return {
        "server": server,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "by_section": by_section,
    }


def _flatten_inputs(inputs: Any) -> List[dict]:
    """
    Best-effort flattening of Galaxy tool input specs.
    This is intentionally conservative: it stores a compact, schema-agnostic summary.
    """
    out: List[dict] = []
    if not isinstance(inputs, list):
        return out
    for inp in inputs:
        if not isinstance(inp, dict):
            continue
        summary: dict = {}
        for key in ("name", "label", "type", "optional", "help"):
            if key in inp:
                summary[key] = inp.get(key)
        if summary:
            out.append(summary)
    return out


def fetch_tool_io_details(server: str, tool_id: str, timeout: int) -> dict:
    server = server.rstrip("/")
    url = f"{server}/api/tools/{urllib.parse.quote(tool_id, safe='')}"
    # Some Galaxy servers accept io_details=true; harmless if ignored.
    url = f"{url}?{urllib.parse.urlencode({'io_details': 'true'})}"
    payload = _http_get_json(url, timeout=timeout)
    if not isinstance(payload, dict):
        return {}
    inputs = payload.get("inputs")
    outputs = payload.get("outputs")
    return {
        "inputs_raw": inputs,
        "outputs_raw": outputs,
        "input_params_flat": _flatten_inputs(inputs),
    }


def write_jsonl(path: Path, tools: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for tool in tools:
            handle.write(json.dumps(tool, ensure_ascii=False) + "\n")


def build_index(tools: Iterable[dict]) -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = defaultdict(list)
    for tool in tools:
        tool_id = tool.get("tool_id")
        base_id = tool.get("base_id")
        if not isinstance(tool_id, str) or not tool_id:
            continue
        if not isinstance(base_id, str) or not base_id:
            base_id = normalize_base_id(tool_id)
        out[base_id].append(tool_id)
    # deterministic ordering
    return {k: sorted(v) for k, v in sorted(out.items(), key=lambda kv: kv[0])}


def main() -> None:
    args = parse_args()
    in_panel = True if args.in_panel or not args.no_in_panel else False
    out_jsonl = args.out_jsonl
    out_index = args.out_index
    out_by_section = args.out_by_section
    if out_jsonl is None:
        out_jsonl = (
            Path("data/tool_catalog/usegalaxy_org_tools.jsonl")
            if in_panel
            else Path("data/tool_catalog/usegalaxy_org_all_tools.jsonl")
        )
    if out_index is None:
        out_index = (
            Path("data/tool_catalog/usegalaxy_org_index.json")
            if in_panel
            else Path("data/tool_catalog/usegalaxy_org_all_index.json")
        )
    if out_by_section is None:
        out_by_section = (
            Path("data/tool_catalog/usegalaxy_org_by_section.json")
            if in_panel
            else Path("data/tool_catalog/usegalaxy_org_all_by_section.json")
        )
    tools = fetch_tools(args.server, in_panel=in_panel, timeout=args.timeout)
    if args.include_io_details:
        LOGGER.info("Fetching per-tool io details for %d tools...", len(tools))
        for idx, tool in enumerate(tools, start=1):
            tool_id = tool.get("tool_id")
            if not isinstance(tool_id, str) or not tool_id:
                continue
            try:
                tool.update(fetch_tool_io_details(args.server, tool_id, timeout=args.timeout))
            except Exception as exc:
                # Keep the catalog build resilient; IO details are optional.
                tool["io_details_error"] = str(exc)
            if idx % 250 == 0:
                LOGGER.info("...%d/%d", idx, len(tools))
    write_jsonl(out_jsonl, tools)
    index = build_index(tools)
    out_index.parent.mkdir(parents=True, exist_ok=True)
    out_index.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    try:
        by_section_payload = fetch_by_section(args.server, timeout=args.timeout)
        out_by_section.parent.mkdir(parents=True, exist_ok=True)
        out_by_section.write_text(
            json.dumps(by_section_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except Exception as exc:
        LOGGER.warning("Failed to build by-section mapping: %s", exc)


if __name__ == "__main__":
    main()
