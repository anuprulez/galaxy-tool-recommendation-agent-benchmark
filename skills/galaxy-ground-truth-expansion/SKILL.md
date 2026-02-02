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

## Why IO details + help text matter (discovery + validation)

`io_details` (IO fields in the catalog) are useful for **two** reasons:

1. **Discovery (finding plausible alternatives):** tools that can plausibly substitute each other often share
   IO structure (e.g., both take tabular `data` + require a `data_column` target, both output a trained model, etc.).
2. **Validation (preventing false positives):** even if names/help text look similar, IO mismatch usually means
   the tools are not interchangeable for the same step.

`tool_help_text` adds the missing semantic layer: it can confirm whether a tool genuinely supports the specific
algorithm/operation implied by the query (e.g., “SVM”, “one-hot encoding”, “hyperparameter search”), and whether
that support can be constrained to match the intent (e.g., “SVM-only”).

## Step 0 — Make sure you have the tool universe

Build or refresh the catalog from usegalaxy.org (recommended: panel tools):

`python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --in-panel --include-io-details`

If you need the full installed universe:

`python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --no-in-panel --include-io-details`

**Non-negotiable for expansion:** the tool catalog must include **input/output details**.

- This skill assumes each tool entry in the catalog JSONL includes IO-related fields such as:
  - `input_params_flat` (preferred summary)
  - `inputs_raw` / `outputs_raw` (raw Galaxy tool parameter schema)
- If your catalog JSONL does not contain IO fields, rebuild it with `--include-io-details` before expanding ground truth.

Use these as references:

- `data/tool_catalog/usegalaxy_org_tools.jsonl` / `data/tool_catalog/usegalaxy_org_index.json`
- `data/tool_catalog/usegalaxy_org_all_tools.jsonl` / `data/tool_catalog/usegalaxy_org_all_index.json`

Notes on the tool catalog builder:

- The catalog is built by `python3 -m scripts.catalog.build_usegalaxy_tool_catalog`.
- `--include-io-details` enriches each JSONL entry with IO-related fields used by this expansion workflow.

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
5. **IO compatibility check (required):**
   - Compare the candidate tool’s expected **inputs** and **outputs** against the original tool using the catalog IO fields.
   - Only add an alternative if a typical user could swap it in without changing the overall step semantics.
   - If IO details are missing/unclear for either tool, do **not** expand for that item yet (rebuild the catalog with IO details).
6. **Help text check (recommended):**
   - Use `tool_help_text` (if available) to confirm task semantics and important constraints.
   - If `tool_help_text` is missing for a critical decision, consider regenerating the helptext-enriched catalog first.

## Step 3 — Apply the change (edit JSONL)

Update only the target item:

- Append additional tool IDs to the item’s `tools` list (keep the original tool first).
- Add `metadata.ground_truth_alternatives = true`
- Add `metadata.ground_truth_alternatives_note` with a short human note, e.g.:
  - “Manual: Tabular Learner also fits this tabular ML training intent.”
  - “Manual: HISAT2 and RNA STAR are both spliced aligners for RNA-seq mapping.”
  - “Manual: SVM classifier can also be trained with Tabular Learner when configured to compare only SVM models.”

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

## Worked example — SVM → Tabular Learner (when justified)

**Scenario:** the gold tool is the dedicated SVM classifier tool:

- `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/<version>`

You may add the AutoML-style tool:

- `toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/<version>`

**Only if all of the following are true:**

- The query intent is “train an SVM classifier on tabular data” (not “compare many algorithms”).
- `tabular_learner` supports **classification** for the dataset type, and its inputs match the intent (tabular dataset + target column).
- In `tabular_learner` parameters (from `inputs_raw` / `input_params_flat` and/or `tool_help_text`), you can restrict the compared model set to **SVM only** (e.g., select `SVM - Linear Kernel` / `SVM - Radial Kernel`).
- You record in `metadata.ground_truth_alternatives_note` that the equivalence depends on configuring Tabular Learner to SVM-only (so the task semantics remain “SVM training”).

**How IO details help you discover this alternative:**

- The SVM-specific tool and `tabular_learner` both operate on **tabular inputs**.
- `tabular_learner` has a **target column** parameter (e.g., `data_column`) which matches the “supervised classification” shape.
- `tool_help_text` / parameters reveal it includes explicit SVM model choices and allows constraining to SVM-only.

**Why this is acceptable:** with SVM-only configuration, both tools implement the same analysis step (SVM training on tabular inputs), even though Tabular Learner can do broader model comparison when not constrained.

**Example queries that justify this expansion (SVM-only intent):**

- “I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to train an SVM classifier and evaluate accuracy with a proper train/test split. Which tool in Galaxy can do this?”
- “I have a machine learning dataset where you want to train and evaluate a predictive model. I need a support vector machine classifier for my feature matrix and evaluation outputs. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?”

**Counterexamples (do NOT expand to Tabular Learner unless the query explicitly allows AutoML / model comparison):**

- Queries whose primary intent is “compare many algorithms and pick the best model”, “AutoML”, or “try multiple models automatically”.
- Queries that mix incompatible intents (e.g., “unsupervised clustering” *and* “fit an SVM classifier”) without clarifying the requested step.
