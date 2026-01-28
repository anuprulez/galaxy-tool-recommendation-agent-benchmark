from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from scripts.eval.evaluate_recommendations import (
    compute_metrics,
    normalize_tool_id,
    unique_in_order,
)
from scripts.benchmark.generate_llm_predictions import extract_predictions, load_jsonl
from scripts.llm.llm_providers import (
    call_anthropic,
    call_gemini,
    call_ollama,
    call_openai_compatible,
)

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOGGER = logging.getLogger(__name__)


def _slug(text: str) -> str:
    text = (text or "").strip()
    text = re.sub(r"[^a-zA-Z0-9._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "unknown"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a tool-recommendation agent on benchmark v1 and evaluate it "
            "with Hit@k / MRR@k / nDCG@k."
        )
    )
    parser.add_argument(
        "--gold",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark JSONL file with {'id','query','tools',...} (default: v1).",
    )
    parser.add_argument(
        "--filter-topic",
        action="append",
        default=None,
        help=(
            "Only evaluate items whose metadata.topic matches one of these values "
            "(repeatable)."
        ),
    )
    parser.add_argument(
        "--filter-tutorial-regex",
        type=str,
        default=None,
        help="Only evaluate items whose tutorial_id matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--filter-tool-regex",
        type=str,
        default=None,
        help="Only evaluate items whose gold tools contain a tool_id matching this regex (case-insensitive).",
    )
    parser.add_argument(
        "--filter-tool-section",
        action="append",
        default=None,
        help=(
            "Only evaluate items whose gold tools fall under one of these Galaxy tool panel sections "
            "according to --tool-sections-file (repeatable)."
        ),
    )
    parser.add_argument(
        "--tool-sections-file",
        type=Path,
        default=Path("data/tool_catalog/usegalaxy_org_by_section.json"),
        help="JSON file with a 'by_section' mapping used by --filter-tool-section.",
    )
    parser.add_argument(
        "--filter-query-regex",
        type=str,
        default=None,
        help="Only evaluate items whose query text matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--filter-id-regex",
        type=str,
        default=None,
        help="Only evaluate items whose id matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--output-predictions",
        type=Path,
        default=None,
        help="Destination JSONL for {'id','predictions'} entries.",
    )
    parser.add_argument(
        "--output-metrics",
        type=Path,
        default=None,
        help="Destination JSON for aggregated metrics.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path("runs/eval"),
        help="Root folder for auto-named results (default: runs/eval).",
    )
    parser.add_argument(
        "--run-name",
        type=str,
        default=None,
        help=(
            "Optional extra subfolder under provider/model, e.g. "
            "'candidates50_temp0'. If omitted, writes directly under provider/model."
        ),
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip query IDs already present in the predictions file for this run.",
    )
    parser.add_argument(
        "--agent",
        type=str,
        default="llm",
        choices=("llm", "oracle", "first_tutorial_tool"),
        help=(
            "Agent strategy: "
            "'llm' calls an OpenAI-compatible chat completions endpoint; "
            "'oracle' returns gold tools (sanity check only); "
            "'first_tutorial_tool' returns the top retrieved tool-catalog candidates."
        ),
    )
    parser.add_argument(
        "--tool-catalog",
        type=Path,
        default=Path("data/tool_catalog/usegalaxy_org_tools.jsonl"),
        help=(
            "Tool catalog JSONL used to build candidate tools for the LLM. "
            "Expected fields per line: tool_id, name, description (at minimum)."
        ),
    )
    parser.add_argument(
        "--candidate-k",
        type=int,
        default=50,
        help="How many candidate tools to include in the LLM prompt.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Request up to this many predictions per query.",
    )
    parser.add_argument(
        "--k",
        type=str,
        default="1,3,5,10",
        help="Comma-separated evaluation cutoffs (default: 1,3,5,10).",
    )
    parser.add_argument(
        "--normalize-tools",
        action="store_true",
        help="Normalize toolshed IDs by removing the version (last path segment).",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="LLM model name to request from the API (agent=llm).",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="openai_compatible",
        choices=("openai_compatible", "anthropic", "gemini", "ollama"),
        help=(
            "LLM provider protocol. 'openai_compatible' works with OpenAI-style "
            "/v1/chat/completions endpoints (many providers support this)."
        ),
    )
    parser.add_argument(
        "--api-url",
        type=str,
        default="https://api.openai.com/v1/chat/completions",
        help=(
            "Provider endpoint. "
            "openai_compatible: full /v1/chat/completions URL; "
            "anthropic: https://api.anthropic.com/v1/messages; "
            "gemini: https://generativelanguage.googleapis.com/v1beta; "
            "ollama: http://localhost:11434/api/chat."
        ),
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="Optional API key (fallback depends on --provider).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature for the LLM (agent=llm).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls (agent=llm).",
    )
    parser.add_argument(
        "--max-queries",
        type=int,
        default=None,
        help="Stop after scoring this many queries (default: all).",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help=(
            "Deprecated alias for --resume. Prefer --resume. "
            "If either is set, existing IDs are skipped."
        ),
    )
    return parser.parse_args()


def _compile_optional_regex(pattern: Optional[str]) -> Optional[re.Pattern[str]]:
    if not pattern:
        return None
    return re.compile(pattern, re.IGNORECASE)


def filter_gold_items(args: argparse.Namespace, gold_items: List[dict]) -> List[dict]:
    topics = set(t.strip() for t in (args.filter_topic or []) if isinstance(t, str) and t.strip())
    tutorial_re = _compile_optional_regex(args.filter_tutorial_regex)
    tool_re = _compile_optional_regex(args.filter_tool_regex)
    query_re = _compile_optional_regex(args.filter_query_regex)
    id_re = _compile_optional_regex(args.filter_id_regex)
    sections = set(
        s.strip()
        for s in (args.filter_tool_section or [])
        if isinstance(s, str) and s.strip()
    )
    section_tool_bases: Optional[set[str]] = None
    if sections:
        if not args.tool_sections_file.exists():
            raise FileNotFoundError(
                f"--filter-tool-section requires --tool-sections-file, but it does not exist: {args.tool_sections_file}"
            )
        payload = json.loads(args.tool_sections_file.read_text(encoding="utf-8"))
        by_section = payload.get("by_section") if isinstance(payload, dict) else None
        if not isinstance(by_section, dict):
            raise ValueError(
                f"Expected a JSON object with 'by_section' in {args.tool_sections_file}"
            )
        bases: set[str] = set()
        for sec in sections:
            tools = by_section.get(sec)
            if not isinstance(tools, list):
                continue
            for t in tools:
                if isinstance(t, str) and t:
                    bases.add(normalize_tool_id(t))
        section_tool_bases = bases

    if not (topics or tutorial_re or tool_re or query_re or id_re or sections):
        return gold_items

    filtered: List[dict] = []
    for item in gold_items:
        qid = item.get("id")
        if id_re and (not isinstance(qid, str) or not id_re.search(qid)):
            continue

        if topics:
            topic = ((item.get("metadata") or {}).get("topic")) or ""
            if topic not in topics:
                continue

        if tutorial_re:
            tutorial_id = item.get("tutorial_id") or ""
            if not isinstance(tutorial_id, str) or not tutorial_re.search(tutorial_id):
                continue

        if query_re:
            query = item.get("query") or ""
            if not isinstance(query, str) or not query_re.search(query):
                continue

        if tool_re:
            tools = item.get("tools") or []
            if not isinstance(tools, list) or not any(isinstance(t, str) and tool_re.search(t) for t in tools):
                continue
        if section_tool_bases is not None:
            tools = item.get("tools") or []
            if not isinstance(tools, list):
                continue
            tool_bases = [normalize_tool_id(t) for t in tools if isinstance(t, str)]
            if not any(tb in section_tool_bases for tb in tool_bases):
                continue

        filtered.append(item)
    return filtered


def resolve_output_paths(args: argparse.Namespace) -> Tuple[Path, Path]:
    """
    If the user provided explicit paths, use them.
    Otherwise, use: <results-dir>/<provider>/<model>/<run-name?>/{predictions.jsonl,metrics.json}
    """
    if args.output_predictions is not None and args.output_metrics is not None:
        return args.output_predictions, args.output_metrics

    provider = _slug(getattr(args, "provider", "unknown"))
    model = _slug(getattr(args, "model", "unknown"))
    base = args.results_dir / provider / model
    if args.run_name:
        base = base / _slug(args.run_name)
    predictions = args.output_predictions or (base / "predictions.jsonl")
    metrics = args.output_metrics or (base / "metrics.json")
    return predictions, metrics


def _normalize_list(values: Iterable[str], do_normalize: bool) -> List[str]:
    if not do_normalize:
        return unique_in_order(values)
    return unique_in_order(normalize_tool_id(v) for v in values)


def _ensure_llm_key(args: argparse.Namespace) -> str:
    try:
        from dotenv import load_dotenv  # type: ignore
    except ModuleNotFoundError:
        load_dotenv = None
    if load_dotenv is not None:
        load_dotenv(dotenv_path=Path(".env"))
    if args.provider == "anthropic":
        api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    elif args.provider == "gemini":
        api_key = args.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    elif args.provider == "ollama":
        api_key = ""
    else:
        api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        if args.provider == "anthropic":
            LOGGER.error("No API key provided. Set ANTHROPIC_API_KEY or pass --api-key.")
        elif args.provider == "gemini":
            LOGGER.error("No API key provided. Set GEMINI_API_KEY/GOOGLE_API_KEY or pass --api-key.")
        else:
            LOGGER.error("No API key provided. Set OPENAI_API_KEY or pass --api-key.")
        sys.exit(1)
    return api_key


def _load_existing_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {item["id"] for item in load_jsonl(path) if isinstance(item.get("id"), str)}


def _write_prediction(path: Path, qid: str, predictions: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as out_handle:
        out_handle.write(
            json.dumps({"id": qid, "predictions": predictions}, ensure_ascii=False)
            + "\n"
        )


_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "before",
    "by",
    "can",
    "data",
    "dataset",
    "do",
    "for",
    "from",
    "have",
    "how",
    "i",
    "in",
    "into",
    "is",
    "it",
    "need",
    "of",
    "on",
    "or",
    "run",
    "should",
    "that",
    "the",
    "this",
    "to",
    "tool",
    "use",
    "using",
    "what",
    "which",
    "with",
}


def _tokenize(text: str) -> List[str]:
    text = text.lower()
    parts = re.split(r"[^a-z0-9]+", text)
    tokens: List[str] = []
    for part in parts:
        if len(part) < 2:
            continue
        if part in _STOPWORDS:
            continue
        tokens.append(part)
    return tokens


def _tool_text(tool: dict) -> str:
    tool_id = str(tool.get("tool_id") or "")
    name = str(tool.get("name") or "")
    desc = str(tool.get("description") or "")
    return " ".join([tool_id, name, desc]).strip()


def load_tool_catalog(path: Path) -> List[dict]:
    if not path.exists():
        raise FileNotFoundError(
            f"Tool catalog not found: {path}. "
            "Build a usegalaxy.org tool snapshot and point --tool-catalog to it."
        )
    tools: List[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            if not isinstance(item, dict):
                continue
            if not item.get("tool_id"):
                continue
            tools.append(item)
    return tools


def build_inverted_index(tools: List[dict]) -> tuple[Dict[str, List[int]], Dict[str, float]]:
    """
    Build a simple token->tool_index inverted index with IDF weights.
    """
    postings: Dict[str, List[int]] = {}
    df: Dict[str, int] = {}
    for idx, tool in enumerate(tools):
        seen_tokens = set(_tokenize(_tool_text(tool)))
        for tok in seen_tokens:
            postings.setdefault(tok, []).append(idx)
            df[tok] = df.get(tok, 0) + 1

    n = max(1, len(tools))
    idf: Dict[str, float] = {}
    for tok, freq in df.items():
        # Smooth IDF; simple and dependency-free
        idf[tok] = 1.0 + (0.0 if freq <= 0 else (math_log((n + 1) / (freq + 1))))
    return postings, idf


def math_log(x: float) -> float:
    # local helper to avoid importing math at top for a single call-site
    import math

    return math.log(x)


def select_candidates(
    query: str,
    tools: List[dict],
    postings: Dict[str, List[int]],
    idf: Dict[str, float],
    candidate_k: int,
) -> List[dict]:
    tokens = _tokenize(query)
    scores: Dict[int, float] = {}
    for tok in tokens:
        tool_idxs = postings.get(tok)
        if not tool_idxs:
            continue
        weight = idf.get(tok, 1.0)
        for idx in tool_idxs:
            scores[idx] = scores.get(idx, 0.0) + weight

    if not scores:
        # Deterministic fallback: first N tools from the snapshot.
        return tools[:candidate_k]

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    out: List[dict] = []
    for idx, _score in ranked[:candidate_k]:
        out.append(tools[idx])
    return out


def build_llm_messages(query: str, candidates: List[dict], top_k: int) -> List[dict[str, str]]:
    system_content = (
        "You are a Galaxy tool recommendation agent. "
        "Given a user query and a list of candidate Galaxy tools, return the best-matching tool IDs."
    )

    lines: List[str] = []
    for tool in candidates:
        tool_id = str(tool.get("tool_id") or "").strip()
        name = str(tool.get("name") or "").strip()
        desc = str(tool.get("description") or "").strip()
        if not tool_id:
            continue
        snippet = f"{tool_id} | {name}"
        if desc:
            snippet = f"{snippet} | {desc}"
        lines.append(snippet)

    user_content = (
        "User query:\n"
        f"{query}\n\n"
        "Candidate tools (tool_id | name | description):\n"
        + ("\n".join(lines) if lines else "N/A")
        + "\n\n"
        "Instructions:\n"
        f"- Pick up to {top_k} tool_id values from the candidate tools that best solve the query.\n"
        "- Output a single JSON object and nothing else: {\"predictions\": [\"tool_id\", ...]}.\n"
        "- Order predictions from most to least relevant.\n"
        "- If none match, return an empty list.\n"
    )

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


def generate_predictions(args: argparse.Namespace) -> None:
    output_predictions, _output_metrics = resolve_output_paths(args)
    gold_items = filter_gold_items(args, load_jsonl(args.gold))
    if not gold_items:
        raise ValueError(f"No items found in {args.gold}")

    tools: List[dict] = []
    postings: Dict[str, List[int]] = {}
    idf: Dict[str, float] = {}
    if args.agent != "oracle":
        tools = load_tool_catalog(args.tool_catalog)
        postings, idf = build_inverted_index(tools)
    do_resume = bool(args.resume or args.skip_existing)
    existing_ids = _load_existing_ids(output_predictions) if do_resume else set()

    api_key: Optional[str] = None
    if args.agent == "llm":
        api_key = _ensure_llm_key(args)

    processed = 0
    for entry in gold_items:
        qid = entry.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        if do_resume and qid in existing_ids:
            continue
        if args.max_queries and processed >= args.max_queries:
            break

        query = str(entry.get("query") or "").strip()
        if args.agent == "oracle":
            predictions = [t for t in entry.get("tools") or [] if isinstance(t, str)]
        elif args.agent == "first_tutorial_tool":
            candidates = select_candidates(
                query=query,
                tools=tools,
                postings=postings,
                idf=idf,
                candidate_k=max(0, args.candidate_k),
            )
            predictions = [str(t.get("tool_id")) for t in candidates if t.get("tool_id")][: args.top_k]
        else:
            candidates = select_candidates(
                query=query,
                tools=tools,
                postings=postings,
                idf=idf,
                candidate_k=max(0, args.candidate_k),
            )
            messages = build_llm_messages(query=query, candidates=candidates, top_k=args.top_k)
            if args.provider == "anthropic":
                content = call_anthropic(
                    api_url=args.api_url,
                    api_key=api_key or "",
                    model=args.model,
                    messages=messages,
                    temperature=args.temperature,
                ).content
            elif args.provider == "gemini":
                content = call_gemini(
                    api_base=args.api_url,
                    api_key=api_key or "",
                    model=args.model,
                    messages=messages,
                    temperature=args.temperature,
                ).content
            elif args.provider == "ollama":
                content = call_ollama(
                    api_url=args.api_url,
                    model=args.model,
                    messages=messages,
                    temperature=args.temperature,
                ).content
            else:
                content = call_openai_compatible(
                    api_url=args.api_url,
                    api_key=api_key or "",
                    model=args.model,
                    messages=messages,
                    temperature=args.temperature,
                ).content
            predictions = extract_predictions(content, args.top_k)

        predictions = unique_in_order(predictions)[: args.top_k]
        _write_prediction(output_predictions, qid, predictions)
        existing_ids.add(qid)
        processed += 1
        LOGGER.info("Wrote predictions for %s (%d)", qid, processed)
        time.sleep(max(0.0, args.delay if args.agent == "llm" else 0.0))


def evaluate(args: argparse.Namespace) -> Dict[str, Any]:
    output_predictions, _output_metrics = resolve_output_paths(args)
    ks = [int(k.strip()) for k in args.k.split(",") if k.strip()]

    gold_items_raw = filter_gold_items(args, load_jsonl(args.gold))
    pred_items_raw = load_jsonl(output_predictions)

    gold_items: Dict[str, List[str]] = {}
    for item in gold_items_raw:
        qid = item.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        tools = [t for t in (item.get("tools") or []) if isinstance(t, str)]
        gold_items[qid] = _normalize_list(tools, args.normalize_tools)

    pred_items: Dict[str, List[str]] = {}
    for item in pred_items_raw:
        qid = item.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        preds = [p for p in (item.get("predictions") or []) if isinstance(p, str)]
        pred_items[qid] = _normalize_list(preds, args.normalize_tools)

    return compute_metrics(gold_items, pred_items, ks)


def main() -> None:
    args = parse_args()
    output_predictions, output_metrics = resolve_output_paths(args)
    args.output_predictions = output_predictions
    args.output_metrics = output_metrics
    generate_predictions(args)
    results = evaluate(args)

    output_metrics.parent.mkdir(parents=True, exist_ok=True)
    output_metrics.write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
