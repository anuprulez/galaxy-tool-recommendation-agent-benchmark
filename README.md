# Galaxy Tool-Recommendation Agent Benchmark

This repository contains a benchmark dataset and utilities for evaluating **Galaxy tool-recommendation agents**.
The benchmark pairs **natural-language user queries** with **ground-truth Galaxy tool IDs**.

A key goal of this project is to build a large set of realistic queries **generated with Codex (Codex CLI)** by reading GTN (Galaxy Training Network) tutorials and writing tool-recommendation questions (not tool-configuration questions).

## Quick start

No API keys are required for the core workflow.

If you want to run the helper scripts in `scripts/`, use a Python 3.11+ virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Evaluate benchmark v1 (agent runner)

This repo includes a one-command runner that generates predictions and scores them:

```bash
# Build / refresh the candidate tool catalog (recommended: panel tools only)
python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --in-panel --include-io-details

OPENAI_API_KEY=... \
python3 -m scripts.eval.run_v1_agent_eval \
  --agent llm \
  --model gpt-4o-mini \
  --provider openai_compatible \
  --tool-catalog data/tool_catalog/usegalaxy_org_tools.jsonl \
  --candidate-k 50 \
  --top-k 10 \
  --k 1,3,5,10 \
  --normalize-tools
```

It writes:
- `runs/eval/<provider>/<model>/predictions.jsonl` (predictions)
- `runs/eval/<provider>/<model>/metrics.json` (metrics)

Note: the LLM prompt contains only the user query plus tool-catalog candidates (no `tutorial_id`, `topic`, or dataset metadata).

To use a non-OpenAI provider:

- Anthropic:
  - `ANTHROPIC_API_KEY=... python3 -m scripts.eval.run_v1_agent_eval --agent llm --provider anthropic --api-url https://api.anthropic.com/v1/messages --model claude-3-5-sonnet-latest`
- Gemini:
  - `GEMINI_API_KEY=... python3 -m scripts.eval.run_v1_agent_eval --agent llm --provider gemini --api-url https://generativelanguage.googleapis.com/v1beta --model gemini-1.5-pro`
- Ollama (local):
  - `python3 -m scripts.eval.run_v1_agent_eval --agent llm --provider ollama --api-url http://localhost:11434/api/chat --model llama3.1`

## Setup (optional)

### Update GTN tutorials

This repo includes a `training-material/` checkout. To update it:

`git -C training-material pull --ff-only`

### Install Codex skills

For Codex CLI, install (or symlink) the repo-local skills into `~/.codex/skills/` and restart Codex:

```bash
ln -sf "$(pwd)/skills/galaxy-query-guidelines" ~/.codex/skills/galaxy-query-guidelines
ln -sf "$(pwd)/skills/galaxy-ground-truth-expansion" ~/.codex/skills/galaxy-ground-truth-expansion
```

## Current status

- **Benchmark items (v1)**: `data/benchmark/v1_items.jsonl` (source of truth) and `data/benchmark/v1_items_readable.md` (human-readable export).
- **Tool universe (usegalaxy.org)**: `data/tool_catalog/` contains snapshots of installed tools and indices for building candidate tool sets.
- **Ground truth expansion**: we are actively expanding each item’s acceptable answers (multiple tools can be correct) using conservative, rule-driven alternatives.
- **Query generation**: LLM-API-based query generation is not part of the workflow; queries are maintained manually/human-in-the-loop.

## Key challenge: datasets vs tools in tutorials

GTN tutorials often include:

- **Concrete dataset links / filenames / accessions** used for teaching, which we intentionally avoid mentioning in query text to keep queries generalizable.
- **Tool mentions that are not stable identifiers**, e.g. step labels in workflows, UI display names, or version-pinned tool IDs that do not match what is installed on a target server.

This project addresses the challenge by:

- Writing queries that describe the **user intent** (tool-recommendation) without naming datasets or the target tool.
- Normalizing and expanding ground truth tools against the **usegalaxy.org installed tool universe** (`data/tool_catalog/`), so answers are runnable and auditable.

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
  - `python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --in-panel --include-io-details`
  - Outputs:
    - `data/tool_catalog/usegalaxy_org_tools.jsonl`
    - `data/tool_catalog/usegalaxy_org_index.json`

- All installed tools (larger universe; includes non-panel/hidden tools):
  - `python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --no-in-panel --include-io-details`
  - Outputs:
    - `data/tool_catalog/usegalaxy_org_all_tools.jsonl`
    - `data/tool_catalog/usegalaxy_org_all_index.json`

## Expanding ground truth (multiple acceptable tools)

Rule files live in `data/tool_catalog/alternative_rules_*.json`.
The expansion scripts mutate `data/benchmark/v1_items.jsonl` in-place and annotate `metadata.ground_truth_alternatives_source`.

After any update, regenerate the readable export:

`python3 -m scripts.benchmark.export_readable --input data/benchmark/v1_items.jsonl --output data/benchmark/v1_items_readable.md`

## Repo layout

- `data/benchmark/`: benchmark JSONL + readable export
- `data/tool_catalog/`: usegalaxy.org tool snapshots and indices
- `scripts/`: utilities for catalog building, exporting, evaluation (organized into subpackages under `scripts/benchmark/`, `scripts/catalog/`, `scripts/eval/`, `scripts/llm/`; run via `python3 -m scripts.<subpkg>.<module>`)
- `skills/`: Codex skills documenting query-generation rules and checks
