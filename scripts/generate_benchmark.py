from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

from gtn_benchmark.downloader import download_datasets_for_tutorials, ensure_gtn_repo
from gtn_benchmark.gtn_loader import load_tutorials
from gtn_benchmark.io_utils import load_tutorial_list, read_jsonl, write_jsonl, write_summary
from gtn_benchmark.llm_client import JetstreamClient
from gtn_benchmark.models import BenchmarkItem
from gtn_benchmark.query_generator import generate_queries_for_tutorial
from gtn_benchmark import VERSION

LOGGER = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate GTN benchmark dataset (v0).")
    parser.add_argument(
        "--gtn-root",
        type=Path,
        required=True,
        help="Path to training-material checkout (will be cloned if missing with --auto-fetch-gtn)",
    )
    parser.add_argument(
        "--gtn-repo",
        default="https://github.com/galaxyproject/training-material.git",
        help="Git repo URL for GTN tutorials (used when --auto-fetch-gtn is set)",
    )
    parser.add_argument(
        "--auto-fetch-gtn",
        action="store_true",
        help="Clone the GTN repository if --gtn-root is missing",
    )
    parser.add_argument(
        "--tutorial-list",
        type=Path,
        default=Path("data/tutorial_list.yaml"),
        help="YAML file describing which tutorials to process",
    )
    parser.add_argument("--out-dir", type=Path, default=Path("data/benchmark"), help="Directory for dataset outputs")
    parser.add_argument("--raw-dir", type=Path, default=Path("data/raw_llm"), help="Directory for raw LLM responses")
    parser.add_argument(
        "--datasets-dir",
        type=Path,
        default=Path("data/datasets"),
        help="Directory to store datasets referenced by tutorials",
    )
    parser.add_argument("--max-tutorials", type=int, default=None, help="Optional cap for number of tutorials")
    parser.add_argument(
        "--download-datasets",
        action="store_true",
        help="Download tutorial datasets (based on GTN metadata) into --datasets-dir",
    )
    parser.add_argument(
        "--full-context",
        action="store_true",
        help="Send full tutorial body and headings to LLM (default sends metadata + summary only)",
    )
    parser.add_argument(
        "--exclude-topic",
        action="append",
        dest="exclude_topics",
        default=["admin", "galaxy-interface", "teaching"],
        help="Exclude tutorials under these topics (repeatable). Default: admin, galaxy-interface, teaching",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from existing JSONL; skip tutorials already present unless --refresh-tutorial is used",
    )
    parser.add_argument(
        "--tutorial-id",
        action="append",
        dest="tutorial_ids",
        help="Only process these tutorial IDs (comma-separated or repeat flag)",
    )
    parser.add_argument(
        "--refresh-tutorial",
        action="append",
        dest="refresh_ids",
        help="Regenerate these tutorial IDs even if present in existing JSONL (use with --resume)",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing dataset outputs")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    out_dir: Path = args.out_dir
    raw_dir: Path = args.raw_dir
    items_path = out_dir / f"{VERSION}_items.jsonl"
    summary_path = out_dir / f"{VERSION}_summary.yaml"
    if not args.overwrite and not args.resume and (items_path.exists() or summary_path.exists()):
        LOGGER.error("Output files already exist. Use --overwrite to replace them.")
        sys.exit(1)

    tutorial_filters: set[str] = set()
    if args.tutorial_ids:
        for entry in args.tutorial_ids:
            tutorial_filters.update(id_.strip() for id_ in entry.split(",") if id_.strip())
    refresh_filters: set[str] = set()
    if args.refresh_ids:
        for entry in args.refresh_ids:
            refresh_filters.update(id_.strip() for id_ in entry.split(",") if id_.strip())

    try:
        ensure_gtn_repo(args.gtn_root, args.gtn_repo, args.auto_fetch_gtn)
    except FileNotFoundError as exc:
        LOGGER.error("%s", exc)
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001
        LOGGER.error("Failed to ensure GTN repo: %s", exc)
        sys.exit(1)

    requests = load_tutorial_list(args.tutorial_list)
    if not requests:
        LOGGER.error("No tutorials found in %s", args.tutorial_list)
        sys.exit(1)

    tutorials = load_tutorials(requests, args.gtn_root)
    if args.exclude_topics:
        before = len(tutorials)
        tutorials = [t for t in tutorials if t.topic not in set(args.exclude_topics)]
        excluded_count = before - len(tutorials)
        if excluded_count:
            LOGGER.info("Excluded %s tutorial(s) by topic: %s", excluded_count, ", ".join(args.exclude_topics))
    if tutorial_filters:
        tutorials = [t for t in tutorials if t.tutorial_id in tutorial_filters]
        missing = tutorial_filters - {t.tutorial_id for t in tutorials}
        if missing:
            LOGGER.warning("Tutorial IDs not found in list: %s", ", ".join(sorted(missing)))
    if args.max_tutorials:
        tutorials = tutorials[: args.max_tutorials]
    if not tutorials:
        LOGGER.error("No tutorials could be loaded. Check GTN root path.")
        sys.exit(1)

    if args.download_datasets:
        dataset_results, skipped_for_size = download_datasets_for_tutorials(tutorials, args.datasets_dir)
        for tutorial in tutorials:
            paths = dataset_results.get(tutorial.tutorial_id) or []
            # store relative paths for readability if under repo
            rel_paths = []
            for p in paths:
                try:
                    rel_paths.append(str(p.relative_to(Path.cwd())))
                except ValueError:
                    rel_paths.append(str(p))
            tutorial.dataset_paths = rel_paths
            tutorial.dataset_count = len(paths)
            if tutorial.dataset_count and tutorial.context_summary:
                tutorial.context_summary = f"{tutorial.context_summary}\n\nDataset files ({tutorial.dataset_count}): {', '.join(rel_paths)}"
        if skipped_for_size:
            original = len(tutorials)
            tutorials = [t for t in tutorials if t.tutorial_id not in skipped_for_size]
            LOGGER.info(
                "Skipped %s tutorial(s) due to MAX_DATASET_BYTES: %s",
                len(skipped_for_size),
                ", ".join(sorted(skipped_for_size)),
            )
            if not tutorials:
                LOGGER.error("All tutorials skipped due to dataset size limit.")
                sys.exit(1)
        LOGGER.info(
            "Datasets downloaded for %s tutorials into %s",
            len(dataset_results),
            args.datasets_dir,
        )

    client = JetstreamClient.from_env()
    LOGGER.info("Loaded %s tutorials. Model=%s", len(tutorials), client.config.model)

    existing_items: list[BenchmarkItem] = []
    completed_tutorials: set[str] = set()
    if args.resume and items_path.exists():
        for record in read_jsonl(items_path):
            try:
                existing_items.append(BenchmarkItem(**record))
            except TypeError:
                LOGGER.warning("Skipping malformed record in %s: %s", items_path, record)
                continue
        completed_tutorials = {item.tutorial_id for item in existing_items} - refresh_filters
        if refresh_filters:
            existing_items = [item for item in existing_items if item.tutorial_id not in refresh_filters]
            LOGGER.info("Refreshing tutorials: %s", ", ".join(sorted(refresh_filters)))
        if completed_tutorials:
            LOGGER.info("Skipping already completed tutorials: %s", ", ".join(sorted(completed_tutorials)))

    all_items: list[BenchmarkItem] = existing_items.copy()
    for tutorial in tutorials:
        if args.resume and tutorial.tutorial_id in completed_tutorials:
            continue
        try:
            tutorial_items = generate_queries_for_tutorial(
                tutorial,
                client,
                raw_dir,
                include_body=args.full_context,
            )
        except Exception as exc:  # noqa: BLE001
            LOGGER.error("Failed to generate tutorial %s: %s", tutorial.tutorial_id, exc)
            continue
        all_items.extend(tutorial_items)

    if not all_items:
        LOGGER.error("LLM did not return any benchmark items.")
        sys.exit(1)

    write_jsonl(all_items, items_path)
    write_summary(
        all_items,
        summary_path,
        model=client.config.model,
        version=VERSION,
        generated_at=datetime.now(timezone.utc),
    )
    LOGGER.info("Wrote %s items to %s", len(all_items), items_path)


if __name__ == "__main__":
    main()
