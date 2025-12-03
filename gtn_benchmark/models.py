from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class TutorialRequest:
    """Entry describing which tutorial we plan to process."""

    tutorial_id: str
    min_queries: int = 10


@dataclass(slots=True)
class TutorialInfo:
    """Parsed GTN tutorial metadata plus derived attributes."""

    tutorial_id: str
    title: str
    topic: str
    summary: str
    tools: list[str]
    workflows: list[str]
    body: str
    tutorial_path: Path
    datasets: list[str] = field(default_factory=list)
    dataset_paths: list[str] = field(default_factory=list)
    dataset_count: int = 0
    context_summary: str = ""
    headings: list[str] = field(default_factory=list)
    workflow_steps: dict[str, list[str]] = field(default_factory=dict)
    min_queries: int = 10
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def short_name(self) -> str:
        """Short identifier derived from the tutorial_id."""
        return self.tutorial_id.rstrip("/").split("/")[-1]


@dataclass(slots=True)
class BenchmarkItem:
    """Final benchmark entry describing one NL query."""

    id: str
    tutorial_id: str
    query: str
    tools: list[str]
    workflows: list[str]
    metadata: dict[str, Any] = field(default_factory=dict)
