# Tool Catalog (usegalaxy.org)

This folder contains an **agent-friendly** snapshot of the tools installed on `https://usegalaxy.org`, intended to be used as the **candidate tool universe** for tool recommendation.

## Files

- `data/tool_catalog/usegalaxy_org_tools.jsonl`
  - One tool per line.
  - Fields include: `tool_id`, `name`, `version`, `description`, `panel_path`, `base_id`.
  - When built with `--include-io-details`, also includes `inputs_raw`, `outputs_raw`, and a flattened `input_params_flat` summary.

- `data/tool_catalog/usegalaxy_org_index.json`
  - Fast lookup index: `base_id -> [tool_id, ...]` (sorted roughly newest-first for toolshed tools).
  - `base_id` is the toolshed tool identifier without the final version segment (for non-toolshed tools it is identical to `tool_id`).

- `data/tool_catalog/usegalaxy_org_by_section.json`
  - Coarse grouping by Galaxy panel section name (e.g. `Machine Learning`), falling back to the first `panel_path` segment.

## Build / refresh

Run:

`python3 scripts/build_usegalaxy_tool_catalog.py --server https://usegalaxy.org --include-io-details`

To fetch **all installed tools** (not just those shown in the tool panel), use:

`python3 scripts/build_usegalaxy_tool_catalog.py --server https://usegalaxy.org --no-in-panel --include-io-details --out-jsonl data/tool_catalog/usegalaxy_org_all_tools.jsonl --out-index data/tool_catalog/usegalaxy_org_all_index.json --out-by-section data/tool_catalog/usegalaxy_org_all_by_section.json`

## Ground-truth alternatives (Machine Learning)

This repo supports **multiple acceptable tools** for a single query (e.g., a specific classifier tool vs. a multi-model tabular learner).

- Rules: `data/tool_catalog/alternative_rules_ml.json`
- Apply: `python3 scripts/expand_ground_truth_alternatives_ml.py`
