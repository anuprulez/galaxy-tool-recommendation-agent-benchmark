# Galaxy Tool-Recommendation Agent Benchmark

This repository contains a benchmark dataset and utilities for evaluating **Galaxy tool-recommendation agents**.
The benchmark pairs **natural-language user queries** with **ground-truth Galaxy tool IDs**.

A key goal of this project is to build a large set of realistic queries **generated with Codex (Codex CLI)** by reading GTN (Galaxy Training Network) tutorials and writing tool-recommendation questions (not tool-configuration questions).

## Quick start

1. Create a Python 3.11+ virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```
2. (Optional) Copy `.env.example` to `.env` and set `OPENAI_API_KEY` if you plan to run `scripts/generate_llm_predictions.py`.

## Current status

- **Benchmark items (v1)**: `data/benchmark/v1_items.jsonl` (source of truth) and `data/benchmark/v1_items_readable.md` (human-readable export).
- **Tool universe (usegalaxy.org)**: `data/tool_catalog/` contains snapshots of installed tools and indices for building candidate tool sets.
- **Ground truth expansion**: we are actively expanding each item’s acceptable answers (multiple tools can be correct) using conservative, rule-driven alternatives.
- **LLM-generation scripts**: earlier LLM-API-based query generation scripts are no longer part of the workflow and are being cleaned up.

## Workflow (high level)

1. **Generate queries with Codex** (human-in-the-loop): read each GTN tutorial and write English tool-recommendation questions.
2. **Consolidate into v1**: merge batch outputs into `data/benchmark/v1_items.jsonl`.
3. **Build tool catalog from usegalaxy.org**: use the server’s API to obtain the candidate tool universe.
4. **Normalize + expand ground truth**:
   - Normalize tool IDs against usegalaxy.org installed tools (versions/availability).
   - Add conservative alternative tools for the same user intent (rule-driven).
5. **Export + evaluate**: export readable views and run evaluation scripts as needed.

## Rules and guidelines

The workflow rules and review checks are documented as Codex skills:

- Repo-local: `skills/galaxy-query-guidelines/SKILL.md`
- Installed into Codex (if you ran the installer): `~/.codex/skills/galaxy-query-guidelines/SKILL.md`
- Ground-truth expansion (repo-local): `skills/galaxy-ground-truth-expansion/SKILL.md`

## Tool catalog

Build/update the catalog from usegalaxy.org:

- Tool panel only (recommended candidate set):
  - `python3 scripts/build_usegalaxy_tool_catalog.py --server https://usegalaxy.org --in-panel --include-io-details`
  - Outputs:
    - `data/tool_catalog/usegalaxy_org_tools.jsonl`
    - `data/tool_catalog/usegalaxy_org_index.json`
    - `data/tool_catalog/usegalaxy_org_by_section.json`

- All installed tools (larger universe; includes non-panel/hidden tools):
  - `python3 scripts/build_usegalaxy_tool_catalog.py --server https://usegalaxy.org --no-in-panel`
  - Outputs:
    - `data/tool_catalog/usegalaxy_org_all_tools.jsonl`
    - `data/tool_catalog/usegalaxy_org_all_index.json`
    - `data/tool_catalog/usegalaxy_org_all_by_section.json`

## Expanding ground truth (multiple acceptable tools)

Rule files live in `data/tool_catalog/alternative_rules_*.json`.
Apply scripts mutate `data/benchmark/v1_items.jsonl` in-place and annotate `metadata.ground_truth_alternatives_source`.

Examples:

- Machine Learning: `python3 scripts/expand_ground_truth_alternatives_ml.py`
- Trimming/adapters: `python3 scripts/expand_ground_truth_alternatives_qc.py`
- Short-read mapping: `python3 scripts/expand_ground_truth_alternatives_mapping.py`
- RNA-seq spliced alignment: `python3 scripts/expand_ground_truth_alternatives_rnaseq_alignment.py`
- Gene-level counting: `python3 scripts/expand_ground_truth_alternatives_counting.py`

After any update, regenerate the readable export:

`python3 scripts/export_readable.py --input data/benchmark/v1_items.jsonl --output data/benchmark/v1_items_readable.md`

## LLM predictions (optional)

`scripts/generate_llm_predictions.py` can generate ranked tool predictions for each query.
It uses `data/tool_catalog/*index.json` to expand candidate tools and requires `OPENAI_API_KEY`.

## Repo layout

- `data/benchmark/`: benchmark JSONL + readable export
- `data/tool_catalog/`: usegalaxy.org tool snapshots and indices
- `scripts/`: utilities for catalog building, ground-truth expansion, exporting, and evaluation
- `skills/`: Codex skills documenting query-generation rules and checks
