from __future__ import annotations

import json
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

import yaml

from .models import BenchmarkItem, TutorialRequest
from gtn_benchmark import VERSION


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def safe_filename(value: str) -> str:
    """Return a filesystem-friendly string."""
    cleaned = "".join(ch if ch.isalnum() else "_" for ch in value)
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_") or "tutorial"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def write_yaml(data: dict, path: Path) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False)


def write_json(data: dict, path: Path) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)


def load_tutorial_list(list_path: Path) -> list[TutorialRequest]:
    payload = load_yaml(list_path)
    tutorials = payload.get("tutorials", [])
    requests: list[TutorialRequest] = []
    for entry in tutorials:
        if isinstance(entry, str):
            requests.append(TutorialRequest(tutorial_id=entry))
            continue
        if isinstance(entry, dict) and "id" in entry:
            requests.append(
                TutorialRequest(
                    tutorial_id=entry["id"],
                    min_queries=int(entry.get("min_queries") or entry.get("queries", 10)),
                )
            )
    return requests


def write_jsonl(items: Sequence[BenchmarkItem], path: Path) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            handle.write(json.dumps(asdict(item), ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def write_summary(
    items: Sequence[BenchmarkItem],
    path: Path,
    *,
    model: str,
    version: str = VERSION,
    generated_at: datetime | None = None,
) -> None:
    generated_at = generated_at or datetime.now(timezone.utc)
    tutorial_counts = Counter(item.tutorial_id for item in items)
    summary = {
        "version": version,
        "model": model,
        "generated_at": generated_at.isoformat(),
        "total_queries": len(items),
        "tutorials": len(tutorial_counts),
        "counts_per_tutorial": dict(tutorial_counts),
    }
    write_yaml(summary, path)


def iter_chunks(iterable: Iterable, size: int):
    """Yield fixed-size chunks from an iterable."""
    batch: list = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
