from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

import yaml

from .models import TutorialInfo, TutorialRequest

LOGGER = logging.getLogger(__name__)
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)", re.MULTILINE)


def parse_front_matter(markdown_text: str) -> tuple[dict[str, Any], str]:
    """Split Markdown text into YAML front matter + body."""
    match = FRONT_MATTER_RE.match(markdown_text)
    if not match:
        return {}, markdown_text
    metadata_block, body = match.groups()
    metadata = yaml.safe_load(metadata_block) or {}
    return metadata, body


def extract_tool_ids(metadata: dict[str, Any]) -> list[str]:
    tools = metadata.get("tools") or metadata.get("tool_link") or []
    return _normalize_id_list(tools, prefer_key="tool_id")


def extract_workflow_ids(metadata: dict[str, Any]) -> list[str]:
    workflows = metadata.get("workflows") or metadata.get("workflow") or []
    return _normalize_id_list(workflows, prefer_key="id")


def extract_dataset_links(metadata: dict[str, Any]) -> list[str]:
    """Extract dataset/Zenodo URLs from tutorial metadata."""
    candidate_keys = [
        "zenodo_link",
        "zenodo_links",
        "zenodo_dataset",
        "zenodo_datasets",
        "datasets",
        "data_url",
        "data_urls",
    ]
    urls: list[str] = []
    for key in candidate_keys:
        value = metadata.get(key)
        urls.extend(_normalize_url_list(value))
    # Preserve order, drop duplicates
    seen: set[str] = set()
    unique: list[str] = []
    for url in urls:
        cleaned = url.strip()
        if cleaned and cleaned.startswith("http") and cleaned not in seen:
            seen.add(cleaned)
            unique.append(cleaned)
    return unique


def _normalize_id_list(entries: Any, *, prefer_key: str) -> list[str]:
    ids: list[str] = []
    if isinstance(entries, str):
        ids.append(entries)
    elif isinstance(entries, dict):
        value = entries.get(prefer_key) or entries.get("url") or entries.get("path")
        if value:
            ids.append(str(value))
    elif isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, str):
                ids.append(entry)
            elif isinstance(entry, dict):
                value = (
                    entry.get(prefer_key)
                    or entry.get("url")
                    or entry.get("path")
                    or entry.get("name")
                )
                if value:
                    ids.append(str(value))
    # Remove duplicates but keep order
    seen: set[str] = set()
    unique: list[str] = []
    for tool_id in ids:
        normalized = tool_id.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        unique.append(normalized)
    return unique


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        val = item.strip()
        if not val or val in seen:
            continue
        seen.add(val)
        unique.append(val)
    return unique


def _normalize_url_list(entries: Any) -> list[str]:
    urls: list[str] = []
    if isinstance(entries, str):
        urls.append(entries)
    elif isinstance(entries, dict):
        for key in ("url", "link", "href", "path"):
            value = entries.get(key)
            if value:
                urls.append(str(value))
    elif isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, str):
                urls.append(entry)
            elif isinstance(entry, dict):
                for key in ("url", "link", "href", "path"):
                    value = entry.get(key)
                    if value:
                        urls.append(str(value))
    return urls


def derive_topic_from_id(tutorial_id: str) -> str:
    parts = tutorial_id.strip("/").split("/")
    if len(parts) >= 2 and parts[0] == "topics":
        return parts[1]
    return parts[0] if parts else "unknown"


def derive_summary(metadata: dict[str, Any], body: str) -> str:
    candidate_keys = [
        "summary",
        "short_description",
        "description",
        "abstract",
        "synopsis",
    ]
    for key in candidate_keys:
        value = metadata.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    body_text = body.strip().split("\n\n")[0]
    return body_text[:300].strip()


def derive_context_summary(body: str, max_chars: int = 800) -> str:
    """Concise context line describing what the analysis is about."""
    body = body.strip()
    if not body:
        return ""
    first_line = body.split("\n", 1)[0].strip()
    return first_line[:max_chars]


def extract_headings(body: str, max_headings: int = 30) -> list[str]:
    headings: list[str] = []
    for match in HEADING_RE.finditer(body):
        level = len(match.group(1))
        title = match.group(2).strip()
        if title:
            headings.append(f"H{level}: {title}")
        if len(headings) >= max_headings:
            break
    return headings


def _safe_load_workflow(path: Path) -> dict[str, Any] | None:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:  # noqa: BLE001
        LOGGER.warning("Failed to parse workflow %s: %s", path, exc)
        return None


def extract_workflow_tools(tutorial_dir: Path) -> list[str]:
    """Gather tool IDs from workflow files bundled with the tutorial."""
    workflow_dir = tutorial_dir / "workflows"
    if not workflow_dir.exists():
        return []
    tool_ids: list[str] = []
    for wf_file in workflow_dir.glob("*"):
        if wf_file.suffix not in {".ga", ".json"}:
            continue
        data = _safe_load_workflow(wf_file)
        if not data:
            continue
        steps = data.get("steps")
        if not isinstance(steps, dict):
            continue
        for step in steps.values():
            tool_id = step.get("tool_id")
            if not tool_id or str(tool_id).startswith("__"):
                continue
            tool_ids.append(str(tool_id))
    return _dedupe_preserve_order(tool_ids)


def parse_workflow_files(tutorial_dir: Path) -> tuple[list[str], dict[str, list[str]]]:
    """Return workflow identifiers and ordered tool_ids per workflow."""
    workflow_dir = tutorial_dir / "workflows"
    if not workflow_dir.exists():
        return [], {}
    workflow_ids: list[str] = []
    workflow_steps: dict[str, list[str]] = {}
    for wf_file in workflow_dir.glob("*"):
        if wf_file.suffix not in {".ga", ".json"}:
            continue
        data = _safe_load_workflow(wf_file)
        if not data:
            continue
        wf_name = wf_file.stem
        workflow_ids.append(wf_name)
        steps = data.get("steps")
        if not isinstance(steps, dict):
            continue
        ordered: list[str] = []
        for key, step in sorted(steps.items(), key=lambda kv: int(kv[0]) if str(kv[0]).isdigit() else str(kv[0])):
            tool_id = step.get("tool_id")
            if not tool_id or str(tool_id).startswith("__"):
                continue
            ordered.append(str(tool_id))
        if ordered:
            workflow_steps[wf_name] = ordered
    return _dedupe_preserve_order(workflow_ids), workflow_steps


def load_tutorials(
    tutorial_requests: list[TutorialRequest],
    gtn_root: Path,
) -> list[TutorialInfo]:
    tutorials: list[TutorialInfo] = []
    for request in tutorial_requests:
        tutorial_path = gtn_root / f"{request.tutorial_id}/tutorial.md"
        if not tutorial_path.exists():
            LOGGER.warning("Tutorial markdown missing: %s", tutorial_path)
            continue
        markdown = tutorial_path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(markdown)
        title = metadata.get("title") or request.tutorial_id.split("/")[-1]
        summary = derive_summary(metadata, body)
        context_summary = derive_context_summary(body)
        topic = derive_topic_from_id(request.tutorial_id)
        tools = extract_tool_ids(metadata)
        workflow_ids, workflow_steps = parse_workflow_files(tutorial_path.parent)
        workflow_tools = extract_workflow_tools(tutorial_path.parent)
        tools = _dedupe_preserve_order(tools + workflow_tools)
        workflows = _dedupe_preserve_order(extract_workflow_ids(metadata) + workflow_ids)
        datasets = extract_dataset_links(metadata)
        headings = extract_headings(body)
        tutorials.append(
            TutorialInfo(
                tutorial_id=request.tutorial_id,
                title=str(title),
                topic=topic,
                summary=summary,
                body=body,
                tools=tools,
                workflows=workflows,
                datasets=datasets,
                context_summary=context_summary,
                headings=headings,
                workflow_steps=workflow_steps,
                tutorial_path=tutorial_path,
                min_queries=request.min_queries,
                metadata=metadata,
            )
        )
    return tutorials
