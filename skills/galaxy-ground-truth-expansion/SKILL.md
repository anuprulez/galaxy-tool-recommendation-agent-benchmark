# Galaxy Ground-Truth Expansion (Manual, per item)

Purpose: expand each benchmark item’s **acceptable ground-truth tools** (multiple correct answers) by **manually** reviewing the query and the underlying tutorial context.  
This skill exists because automated, “template-like” expansions can easily introduce incorrect alternatives.

This skill is for maintaining `data/benchmark/v1_items.jsonl` and keeping `data/benchmark/v1_items_readable.md` in sync.

## Non-negotiable rules

- Expansion is **manual**: review **one query + one tool** at a time.
- Do **not** use “pattern rules”, “keyword triggers”, or “template expansions” to add tools in bulk.
- Only add an alternative tool if it is **clearly acceptable** for the same user intent **in Galaxy**.
- Only add tool IDs that exist on the target server (usegalaxy.org) tool universe.
- Prefer a small, high-precision set of alternatives over a large noisy set.

## What “acceptable alternative” means

An alternative tool is acceptable if, given the query as written:

- A typical Galaxy user could reasonably choose either tool to accomplish the task, and
- The tool is not a different *analysis step* (e.g., a preprocessing step vs a downstream step), and
- The tool is not an unrelated visualization/reporting helper, and
- The alternative does not change the task semantics (e.g., long-read vs short-read aligner).

## Inputs / outputs

- Input benchmark: `data/benchmark/v1_items.jsonl`
- Output benchmark (in-place updates): `data/benchmark/v1_items.jsonl`
- Readable export: `data/benchmark/v1_items_readable.md`
- Tool catalogs (usegalaxy.org): `data/tool_catalog/`

## Step 0 — Make sure you have the tool universe

Build or refresh the catalog from usegalaxy.org (recommended: panel tools):

`python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --in-panel --include-io-details`

If you need the full installed universe:

`python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --no-in-panel --include-io-details`

Use these as references:

- `data/tool_catalog/usegalaxy_org_tools.jsonl` / `data/tool_catalog/usegalaxy_org_index.json`
- `data/tool_catalog/usegalaxy_org_all_tools.jsonl` / `data/tool_catalog/usegalaxy_org_all_index.json`

## Step 1 — Pick an item to expand

Work item-by-item. For a given `id` in `data/benchmark/v1_items.jsonl`:

1. Read the `query` (and ensure it does not mention datasets or the tool name).
2. Note the current single ground-truth tool in `tools[0]` and `metadata.tool_focus`.
3. Identify the tutorial (`tutorial_id`) and, if needed, open the tutorial markdown in `training-material/`.

## Step 2 — Propose alternatives (manual)

For each proposed alternative tool:

1. Confirm it exists on usegalaxy.org (tool ID must be present in the catalog index).
2. Confirm it matches the query intent (not just “related”).
3. Prefer tools that appear in the same tutorial **for the same step** (strong evidence).
4. If the alternative is not in the tutorial, require stronger justification (e.g., a well-known equivalent Galaxy tool).

## Step 3 — Apply the change (edit JSONL)

Update only the target item:

- Append additional tool IDs to the item’s `tools` list (keep the original tool first).
- Add `metadata.ground_truth_alternatives = true`
- Add `metadata.ground_truth_alternatives_note` with a short human note, e.g.:
  - “Manual: Tabular Learner also fits this tabular ML training intent.”
  - “Manual: HISAT2 and RNA STAR are both spliced aligners for RNA-seq mapping.”

Do **not** add “bulk source” tags or apply the same change across many items without reviewing each one.

## Step 4 — Re-export the readable view

`python3 -m scripts.benchmark.export_readable --input data/benchmark/v1_items.jsonl --output data/benchmark/v1_items_readable.md`

## Step 5 — Spot-check

Open the relevant section in `data/benchmark/v1_items_readable.md` and verify:

- The query still makes sense and does not mention datasets/tools.
- The listed tools are plausible alternatives (no obvious false positives).

## Notes

- Do not commit secrets (API keys). usegalaxy.org `/api/tools` does **not** require an API key.
- If you previously applied any automated expansions, remove them before proceeding with manual expansion.
