# Galaxy Tool Recommendation Benchmark - Copilot Instructions

This repository contains a benchmark for evaluating Galaxy tool recommendation systems.

## Skills

### Galaxy Ground-Truth Expansion

Purpose: expand each benchmark item's **acceptable ground-truth tools** (multiple correct answers) by **manually** reviewing the query and the underlying tutorial context.

#### Non-negotiable rules

- Expansion is **manual**: review **one query + one tool** at a time.
- Do **not** use "pattern rules", "keyword triggers", or "template expansions" to add tools in bulk.
- Only add an alternative tool if it is **clearly acceptable** for the same user intent **in Galaxy**.
- Only add tool IDs that exist on the target server (usegalaxy.org) tool universe.
- Prefer a small, high-precision set of alternatives over a large noisy set.

#### What "acceptable alternative" means

An alternative tool is acceptable if, given the query as written:

- A typical Galaxy user could reasonably choose either tool to accomplish the task, and
- The tool is not a different *analysis step* (e.g., a preprocessing step vs a downstream step), and
- The tool is not an unrelated visualization/reporting helper, and
- The alternative does not change the task semantics (e.g., long-read vs short-read aligner).

#### Key files

- Input benchmark: `data/benchmark/v1_items.jsonl`
- Readable export: `data/benchmark/v1_items_readable.md`
- Tool catalogs: `data/tool_catalog/`

### Galaxy Query Guidelines

#### Rules (must-follow)

1. **English only** in the query line.
2. The query must ask for a **tool recommendation** (e.g., "Which Galaxy tool should I use…?"), not tool-configuration help.
3. Do **not** mention **tutorial/GTN** in the query line.
4. Do **not** mention concrete **datasets / filenames / accessions** in the query line (e.g., `SRR...`, `E-MTAB-...`, `.fastq.gz`, `.bam`, URLs). Use generic descriptions (e.g., "paired-end FASTQ", "genome assembly FASTA", "count matrix").
5. Every query bullet must be followed by **at least one** `- tool: ...` line (no orphan queries).
6. `- tool:` must be a **stable identifier**:
   - Prefer Toolshed GUIDs like `toolshed.g2.bx.psu.edu/repos/<owner>/<repo>/<tool_id>/<version>`.
   - Allowed special IDs: `upload1`, `__MERGE_COLLECTION__` (and other `__...__` Galaxy internal tools), `interactive_tool_*`.
   - Avoid plain display names or workflow-step labels when a Toolshed GUID exists.
7. The query text must be **consistent** with the chosen `- tool:`.

## Common Commands

```bash
# Build tool catalog from usegalaxy.org
python3 scripts/build_usegalaxy_tool_catalog.py --server https://usegalaxy.org --in-panel --include-io-details

# Export readable benchmark
python3 scripts/export_readable.py --input data/benchmark/v1_items.jsonl --output data/benchmark/v1_items_readable.md

# Check query format
ruby -EUTF-8 skills/galaxy-query-guidelines/scripts/check_queries.rb tmp_stats/codex_quiers_batch*.md
```
