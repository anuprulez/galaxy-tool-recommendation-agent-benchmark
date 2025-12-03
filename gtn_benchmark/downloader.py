from __future__ import annotations

import logging
import os
import subprocess
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .io_utils import ensure_parent, safe_filename
from .models import TutorialInfo

LOGGER = logging.getLogger(__name__)


class DatasetTooLargeError(Exception):
    """Raised when a dataset exceeds MAX_DATASET_BYTES."""


def ensure_gtn_repo(gtn_root: Path, repo_url: str, auto_fetch: bool) -> None:
    """Clone GTN repo if missing (no update if already present)."""
    if gtn_root.exists():
        return
    if not auto_fetch:
        raise FileNotFoundError(
            f"GTN root {gtn_root} not found. Re-run with --auto-fetch-gtn to clone {repo_url}."
        )
    LOGGER.info("GTN root missing. Cloning %s into %s", repo_url, gtn_root)
    gtn_root.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "clone", "--depth", "1", repo_url, str(gtn_root)],
        check=True,
    )


def download_datasets_for_tutorials(
    tutorials: list[TutorialInfo],
    base_dir: Path,
) -> tuple[dict[str, list[Path]], set[str]]:
    """Download datasets referenced in tutorials into per-tutorial folders.

    Returns (downloaded_files_by_tutorial, skipped_tutorial_ids).
    Tutorials can be skipped if datasets exceed MAX_DATASET_BYTES.
    """
    results: dict[str, list[Path]] = {}
    skipped: set[str] = set()
    max_bytes: int | None = None
    env_limit = os.environ.get("MAX_DATASET_BYTES")
    if env_limit:
        try:
            max_bytes = int(env_limit)
        except ValueError:
            LOGGER.warning("Invalid MAX_DATASET_BYTES=%s, ignoring", env_limit)
    base_dir.mkdir(parents=True, exist_ok=True)
    for tutorial in tutorials:
        if not tutorial.datasets:
            continue
        if max_bytes is not None:
            # If any dataset already downloaded and exceeds limit, skip this tutorial
            target_dir = base_dir / tutorial.topic / tutorial.short_name
            existing = list(target_dir.glob("*"))
            if any(p.is_file() and p.stat().st_size > max_bytes for p in existing):
                LOGGER.info("Skipping %s: existing dataset exceeds MAX_DATASET_BYTES", tutorial.tutorial_id)
                skipped.add(tutorial.tutorial_id)
                continue
        target_dir = base_dir / tutorial.topic / tutorial.short_name
        downloaded: list[Path] = []
        skip_tutorial = False
        for url in tutorial.datasets:
            try:
                assets = _download_assets(url, target_dir, max_bytes=max_bytes)
                downloaded.extend(assets)
                if assets:
                    LOGGER.info(
                        "Downloaded %s asset(s) for %s from %s",
                        len(assets),
                        tutorial.tutorial_id,
                        url,
                    )
            except DatasetTooLargeError:
                LOGGER.info("Skipping %s: dataset exceeds MAX_DATASET_BYTES", tutorial.tutorial_id)
                skip_tutorial = True
                break
            except Exception as exc:  # noqa: BLE001
                LOGGER.warning("Failed to download %s for %s: %s", url, tutorial.tutorial_id, exc)
        if skip_tutorial:
            skipped.add(tutorial.tutorial_id)
            continue
        if downloaded:
            results[tutorial.tutorial_id] = _dedupe_paths(downloaded)
    return results, skipped


def _target_path(target_dir: Path, url: str) -> Path:
    parsed = urlparse(url)
    filename = Path(parsed.path).name
    if not filename:
        filename = safe_filename(url)
    return target_dir / filename


def _is_html_file(path: Path) -> bool:
    try:
        snippet = path.read_bytes()[:2048].lower()
        return b"<html" in snippet or b"<!doctype" in snippet
    except Exception:
        return False


def _download_assets(url: str, target_dir: Path, max_bytes: int | None = None) -> list[Path]:
    """Download a URL; if it's an HTML landing page, download all linked files."""
    links = _resolve_download_links(url)
    downloaded: list[Path] = []
    for link in links:
        dest = _target_path(target_dir, link)
        if dest.exists() and not _is_html_file(dest):
            downloaded.append(dest)
            continue
        ensure_parent(dest)
        with requests.get(link, stream=True, timeout=60) as response:
            response.raise_for_status()
            total_downloaded = 0
            with dest.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        total_downloaded += len(chunk)
                        if max_bytes and total_downloaded > max_bytes:
                            LOGGER.info("Aborting download %s (exceeds MAX_DATASET_BYTES)", link)
                            handle.close()
                            dest.unlink(missing_ok=True)
                            raise DatasetTooLargeError("download exceeds limit")
                        handle.write(chunk)
        downloaded.append(dest)
    return downloaded


def _resolve_download_links(url: str) -> list[str]:
    """Return one or many downloadable URLs. If HTML page, extract file links."""
    with requests.get(url, timeout=60) as response:
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "").lower()
        if "text/html" not in content_type:
            return [response.url]
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        links: list[str] = []
        for a in soup.select('a[href*="download=1"], a[href*="/files/"]'):
            href = a.get("href")
            if not href:
                continue
            links.append(requests.compat.urljoin(response.url, href))
        if not links:
            return [response.url]
        return _dedupe_preserve_order(links)


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique


def _dedupe_paths(paths: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in paths:
        if p in seen:
            continue
        seen.add(p)
        unique.append(p)
    return unique
