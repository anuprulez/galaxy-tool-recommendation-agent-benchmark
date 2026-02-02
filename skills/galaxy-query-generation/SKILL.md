# Galaxy Query Generation (Repo Copy)

This is a repo-local copy of the Codex skill located at:

`~/.codex/skills/galaxy-query-generation/SKILL.md`

Use it to keep the query-writing standards versioned with the project.

## Rules (must-follow)

1. **English only** in the query line.
2. The query must ask for a **tool recommendation** (e.g., “Which Galaxy tool should I use…?”), not tool-configuration help.
3. Do **not** mention **tutorial/GTN** in the query line.
4. Do **not** mention concrete **datasets / filenames / accessions** in the query line (e.g., `SRR...`, `E-MTAB-...`, `.fastq.gz`, `.bam`, URLs). Use generic descriptions (e.g., “paired-end FASTQ”, “genome assembly FASTA”, “count matrix”).
5. Do **not** mention the tool name, tool ID, or backticked function-like names in the query (no “perform `tool_x`”).
6. Queries must be **realistic** (close to how real users ask), not “benchmarky”:
   - Use a brief, concrete context: the data type, the goal, and the desired output.
   - Prefer natural phrasing (“I have…”, “I’m trying to…”) over rigid patterns.
   - Avoid stilted wording like “perform X”, “execute Y”, or “for this task” without details.
7. Queries must be **non-templated** and **non-repetitive**:
   - Avoid copy/paste patterns like “Which Galaxy tool would you recommend to perform …?”
   - For the **same tool**, avoid having multiple benchmark items with the **same or near-duplicate** query text.
8. Every query bullet must be followed by **at least one** `- tool: ...` line (no orphan queries).
9. `- tool:` must be a **stable identifier**:
   - Prefer Toolshed GUIDs like `toolshed.g2.bx.psu.edu/repos/<owner>/<repo>/<tool_id>/<version>`.
   - Allowed special IDs: `upload1`, `__MERGE_COLLECTION__` (and other `__...__` Galaxy internal tools), `interactive_tool_*`.
   - Avoid plain display names or workflow-step labels (e.g., `Diamond`, `PeptideShaker`, “Extract and cluster …”) when a Toolshed GUID exists.
10. The query text must be **consistent** with the chosen `- tool:` (no “Select” in the query while `- tool:` is `Grep1`, etc.).

## Generation workflow (manual, not templated)

These benchmark queries must be **handwritten after reading the tutorial**, not produced by filling a fixed template.

1. Open the tutorial: `training-material/<tutorial_id>/tutorial.md`
2. Read around each tool mention to understand the *user goal*:
   - GTN tool tags like `{% tool [Name](tool_id) %}` (usually provides a tool ID)
   - Bold tool mentions like `**ToolName** {% icon tool %}` (often only a display name)
3. Infer the real task for that step (the “why”), not just the step title.
4. Write a natural English query describing the task **with enough intent detail** (inputs/outputs/goal), but **without**:
   - mentioning the tutorial/GTN
   - mentioning datasets / filenames / accessions
   - asking how to configure parameters
   - leaking the tool name / tool id
5. Attach exactly one `- tool:` line with a stable identifier.
   - Prefer resolving via the tutorial workflow `.ga` under `training-material/<tutorial_id>/workflows/`.
   - Use Toolshed API lookups only when needed.

## Where to write the results

Write final queries directly into `data/benchmark/v1_items.jsonl` (do not rely on `tmp_stats/*` as the deliverable).

### Anti-patterns (avoid)

- Generic boilerplate with no task detail (e.g., “Which Galaxy tool would you recommend for this task?” everywhere).
- Copying workflow-step labels as the query intent.
- Parameter-centric questions (“Which inputs should I select and how do I configure …”).
- Multiple benchmark items for the same tool that differ only by a swapped adjective or punctuation.

## Checker

From repo root:

`ruby -EUTF-8 skills/galaxy-query-generation/scripts/check_v1_items.rb data/benchmark/v1_items.jsonl`

This project’s final target is `data/benchmark/v1_items.jsonl` (not `tmp_stats/*`).
