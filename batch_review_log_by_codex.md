# Batch review log (by Codex)

This file records batch-by-batch manual review outcomes for `data/benchmark/v1_items.jsonl`.

Rules followed:
- Manual, per-item decisions (no template/bulk expansions).
- Only add acceptable alternative tools if they clearly match the same user intent **and** are present in the local usegalaxy.org tool snapshot.
- Keep `data/benchmark/v1_items_readable.md` in sync via `scripts/export_readable.py`.

Notes:
- Historical batch notes (earlier work) are in `batch_review_log_by_github_copilot.md`.

---

## Batch 0044 (4301–4400)
- Status: **expanded** (version-drift fixes)
- Date: 2026-01-26
- Summary:
  - Fixed “version drift” where `metadata.tool_focus` pointed to a non-snapshot version while `tools[]` contained the snapshot-installed one:
    - `metabolomics-mfassignr-q025`, `metabolomics-mfassignr-q026`: `mfassignr_mfassignCHO` `+galaxy0` → `+galaxy1`
    - `metabolomics-mfassignr-q039`–`q042`: `mfassignr_mfassign` `+galaxy0` → `+galaxy1`
  - Preserved the existing QCxMS “Advanced Cut” drift handling (`metabolomics-qcxms-predictions-q011`–`q014`) and kept both installed versions listed.
  - Re-exported `data/benchmark/v1_items_readable.md`.

## Batch 0045 (4401–4500)
- Status: **expanded** (version-drift fixes + small same-intent alternatives)
- Date: 2026-01-26
- Summary:
  - Fixed “version drift” by adding snapshot-installed alternate versions to `tools[]` (and recording a manual note) for:
    - Open Babel compound conversion (`metabolomics-qcxms-predictions-q023`–`q026`)
    - FastQC (`microbiome-beer-data-analysis-q011`–`q014`)
    - Porechop (`microbiome-beer-data-analysis-q015`–`q018`)
    - fastp (`microbiome-beer-data-analysis-q019`–`q022`)
    - Kraken2 (`microbiome-beer-data-analysis-q023`–`q026`)
    - KrakenTools kreport-to-Krona (`microbiome-beer-data-analysis-q031`–`q034`)
    - msconvert (`microbiome-clinical-mp-2-discovery-q015`–`q018`)
  - Added a same-intent functional alternative for dataset concatenation:
    - `tp_cat` ↔ `cat1` (`metabolomics-qcxms-predictions-q027`–`q030`)
  - Normalized `metadata.tool_focus` to the snapshot-installed version when the previous focus version was not present:
    - QCxMS run tools (`metabolomics-qcxms-predictions-q039`–`q050`)
    - UniProt XML downloader (`microbiome-clinical-mp-1-database-generation-q011`–`q014`)
- Flags:
  - `xtb_molecular_optimization` tool IDs referenced in `metabolomics-qcxms-predictions-q035`–`q038` are not present in the local usegalaxy.org snapshot; no snapshot-verified alternative was added.
