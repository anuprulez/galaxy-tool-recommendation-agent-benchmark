# Tool Catalog (usegalaxy.org)

This folder contains an **agent-friendly** snapshot of the tools installed on `https://usegalaxy.org`.

## Files

- `data/tool_catalog/usegalaxy_org_tools.jsonl`
  - One tool per line.
  - Fields include: `tool_id`, `name`, `version`, `description`, `base_id`.
  - When built with `--include-io-details`, also includes `inputs_raw`, `outputs_raw`, and a flattened `input_params_flat` summary.

- `data/tool_catalog/usegalaxy_org_index.json`
  - Fast lookup index: `base_id -> [tool_id, ...]` (sorted roughly newest-first for toolshed tools).
  - `base_id` is the toolshed tool identifier without the final version segment (for non-toolshed tools it is identical to `tool_id`).

- `data/tool_catalog/usegalaxy_org_by_section.json`
  - Coarse grouping by Galaxy tool panel section name (e.g. `Machine Learning`).

## Build / refresh

Run:

`python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --in-panel --include-io-details`

To fetch **all installed tools** (not just those shown in the tool panel), use:

`python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --no-in-panel --include-io-details`
