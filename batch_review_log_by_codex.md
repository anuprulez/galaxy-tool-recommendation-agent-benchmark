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

## Batch 0046 (4501–4600)
- Status: **expanded** (version-drift fixes)
- Date: 2026-01-26
- Summary:
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common microbiome/proteomics steps, including:
    - `query_tabular` (`microbiome-clinical-mp-3-verification-q027`–`q030`)
    - `maxquant` (`microbiome-clinical-mp-4-quantitation-q011`–`q014`)
    - `unipept` (`microbiome-clinical-mp-5-data-interpretation-q011`–`q014`)
    - DADA2 steps (`microbiome-dada-16S-*`: PlotQualityProfile, FilterAndTrim, dada, MergePairs, MakeSequenceTable)
    - Mothur preprocessing steps (`microbiome-general-tutorial-*`: MergeFiles, MakeGroup, UniqueSeqs, AlignSeqs, ScreenSeqs)
    - KrakenTools alpha/beta diversity (`microbiome-diversity-*`)
  - Normalized `metadata.tool_focus` for PepQuery2 verification steps where the previous focus version was not present in the snapshot:
    - `microbiome-clinical-mp-3-verification-q019`–`q022`
- Flags:
  - `lotus2` tool IDs referenced in `microbiome-lotus2-identifying-fungi-q011`–`q012` are not present in the local usegalaxy.org snapshot; no snapshot-verified alternative was added.

## Batch 0047 (4601–4700)
- Status: **expanded** (version-drift fixes + snapshot tool normalization)
- Date: 2026-01-26
- Summary:
  - Replaced non-snapshot tool IDs with snapshot-installed, same-intent equivalents:
    - Cutadapt: `devteam/cutadapt` → `lparsons/cutadapt` (metatranscriptomics and metatranscriptomics-short trimming steps)
    - SortMeRNA: `iuc/sortmerna` → `rnateam/sortmerna/bg_sortmerna` (rRNA filtering steps)
    - FASTQ interlacing: `fastq_interlacer` → `fastq_paired_end_interlacer` (paired-end interlacing steps)
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common metagenomics steps:
    - `quast`, `bowtie2`, `samtools_sort`, `binette`, `minimap2`, `multiqc`
- Flags:
  - `lotus2` tool IDs referenced in `microbiome-lotus2-identifying-fungi-q013`–`q014` are not present in the local usegalaxy.org snapshot; no snapshot-verified alternative was added.

## Batch 0048 (4701–4800)
- Status: **expanded** (version-drift fixes + snapshot tool normalization)
- Date: 2026-01-26
- Summary:
  - Normalized a non-snapshot FASTQ interlacing tool ID to the snapshot-installed equivalent:
    - `fastq_interlacer` → `fastq_paired_end_interlacer` (`microbiome-metatranscriptomics-short-q029`–`q030`)
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common microbiome steps, including:
    - `fastq_dl`, `fastp`
    - Mothur MiSeq SOP steps (merge, unique, screen, etc.)
    - FastQC / NanoPlot QC steps (nanopore tutorials)

## Batch 0049 (4801–4900)
- Status: **expanded** (version-drift fixes; OSW tools flagged)
- Date: 2026-01-26
- Summary:
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common microbiome steps, including:
    - `kraken2`, `nanoplot`, `minimap2`, `multiqc`
    - KrakenTools helpers (kreport → Krona, etc.)
    - `msconvert`
- Flags:
  - Several proteomics DIA/OSW-related tool IDs referenced in this batch are not present in the local usegalaxy.org snapshot, so no snapshot-verified alternatives were added for them:
    - `OpenSwathWorkflow` (`proteomics-DIA_Analysis_OSW-q015`–`q018`)
    - `diapysef` (`proteomics-DIA_lib_OSW-q015`–`q018`)
    - `OpenSwathAssayGenerator` / `OpenSwathDecoyGenerator` (`proteomics-DIA_lib_OSW-q019`–`q025`)

## Batch 0050 (4901–5000)
- Status: **expanded** (version-drift fixes + one runnable alternative)
- Date: 2026-01-26
- Summary:
  - Fixed “version drift” for snapshot-present tools by adding alternate installed versions to `tools[]` (with manual notes), including:
    - Advanced Cut (`tp_cut_tool`) (`proteomics-biomarker_selection-q023`–`q026`)
    - `msconvert` (`proteomics-clinical-mp-2-discovery-q031`–`q034`)
  - Normalized `metadata.tool_focus` to the snapshot-installed UniProt XML downloader version:
    - `proteomics-clinical-mp-1-database-generation-q011`–`q014`
    - `proteomics-clinical-mp-2-discovery-q011`–`q014`
  - Added a runnable Galaxy alternative for Venn diagram generation:
    - `Jvenn` ↔ `venn_list` (`proteomics-biomarker_selection-q019`–`q022`)
- Flags:
  - Several tutorial tool IDs in this batch are not present in the local usegalaxy.org snapshot (kept as-is; no snapshot-verified alternatives added), including:
    - `bioconductor_scp` (`proteomics-bioconductor-scp-q023`–`q026`)
    - multiple `proteore_*` tools used in `proteomics-biomarker_selection-*`

## Batch 0051 (5001–5100)
- Status: **expanded** (version-drift fixes + built-in ID normalization)
- Date: 2026-01-26
- Summary:
  - Normalized a built-in tool ID mismatch to the snapshot-installed spelling:

---

## Batch A0001 (1–150)
- Status: **rewritten + expanded** (manual)
- Date: 2026-02-04
- Scope: first 150 items (assembly tutorials near file start)
- Summary:
  - Rewrote tool-leaking and overly templated queries into Galaxy-user phrasing (no tool IDs/names/backticks, no dataset IDs).
  - Increased science-first style coverage within this batch (updated `metadata.query_type`; rewrote a subset of key items to be principle/goal driven).
  - Normalized De Bruijn Graph Assembly tool IDs to stable ToolShed GUIDs (Velvet Optimiser, velveth/velvetg, Bandage visualization).
  - Added a small number of manual, same-intent ground-truth alternatives (with `metadata.ground_truth_alternatives_note`), including:
    - translated nucleotide→protein search alternatives (DIAMOND vs blastx-style search)
    - short-read host-mapping alternatives (Bowtie2 vs BWA-MEM)
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (Cut/Filter/Grep/cat/etc.).

## Batch A0002 (151–300)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 151–300 (assembly tutorials: E. coli comparison, intro assembly, PacBio HiFi assembly, hybrid assembly, large genome assembly, metagenomics assembly, mitochondrial assembly, MRSA Illumina/nanopore)
- Summary:
  - Rewrote tool-leaking and templated queries into Galaxy-user phrasing (removed backticks/tool names/IDs and made intent explicit with realistic context).
  - Fixed one non-stable tool ID in this range by normalizing it to the ToolShed GUID (`circos_aln_to_links`) and updated the query accordingly.
  - Preserved (and did not reduce) science-first query coverage in this batch (kept existing `metadata.query_type` distribution).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 151 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs and other known stable core tools.
    - `Remove_beginning1` → `Remove beginning1` (clinical MP discovery/verification rows in this batch)
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common steps, including:
    - `filter_tabular`, `query_tabular`, `msconvert`, `maxquant`, `unipept`

## Batch A0003 (301–450)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 301–450 (assembly: MRSA nanopore, Unicycler, VGP genome assembly + workflow training; climate: Argo/Pangeo, Climate-101, FATES, Earth system, ocean QCV, ocean variables)
- Summary:
  - Rewrote tool-leaking and templated queries into realistic Galaxy-user questions (removed backticks/tool names/IDs, no tutorial references, no dataset URLs/IDs in the query text).
  - Increased science-first coverage in this batch by relabeling a subset of items where the question is principle/goal driven (final split: 110 science-first / 40 tool-first).
  - Kept the existing ground-truth tool selections intact for this batch (no new gold expansions added).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 301 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (Cut/Grep/cat/sort/etc.).

## Batch A0004 (451–600)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 451–600 (climate: Sentinel-5P visualization; computational chemistry: MD trajectory analysis + cheminformatics/docking)
- Summary:
  - Rewrote all queries to remove tool leakage and GTN guide phrasing (no backticks, no tool names/IDs, no tutorial references, no dataset URLs/IDs in query text).
  - Increased science-first coverage in this batch (final split: 109 science-first / 41 tool-first) while keeping a mix of user styles.
  - Kept ground-truth tool selections intact for this batch (no new gold expansions added).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 451 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (Grep/cat).

## Batch A0005 (601–750)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 601–750 (computational chemistry: cheminformatics utilities; COVID-19 docking workflow; high-throughput MD setup + analysis)
- Summary:
  - Rewrote all queries to remove tool leakage and guide phrasing (no backticks, no tool names/IDs, no tutorial references, no dataset URLs/IDs in query text).
  - Increased science-first coverage in this batch (final split: 110 science-first / 40 tool-first) while preserving a mix of user styles.
  - Kept ground-truth tool selections intact for this batch (no new gold expansions added).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 601 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for known core/placeholder-like tool IDs (e.g., `Grep1`, `xchem_pose_scoring`).

## Batch A0006 (751–900)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 751–900 (computational chemistry: HTMD analysis continuation; MD simulation setup/workflows; medicinal-chemistry data; conformers/alignment)
- Summary:
  - Rewrote all queries to remove tool leakage and guide phrasing (no backticks, no tool names/IDs, no tutorial references, no dataset URLs/IDs in query text).
  - Increased science-first coverage in this batch (final split: 111 science-first / 39 tool-first) while keeping some tool-directed questions.
  - Kept ground-truth tool selections intact for this batch (no new gold expansions added).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 751 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for known core/placeholder-like tool IDs (e.g., `Grep1`, and the NAMD-wrapper placeholders `setup/minimizer/namd_*`).

## Batch A0007 (901–1050)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 901–1050 (computational chemistry: molecule alignment + table utilities; contributing: tutorial authoring examples; data science: tabular/text manipulation tasks)
- Summary:
  - Rewrote all queries to remove tool leakage and guide phrasing (no backticks, no tool names/IDs, no tutorial references, no dataset URLs/IDs in query text).
  - Balanced query styles to match your new target: **75 science-first / 75 tool-first** in this batch, and ensured the wording matches the labeled style.
  - Normalized legacy core tool IDs to match usegalaxy.org API spellings:
    - `Remove_beginning1` → `Remove beginning1`
    - `Show_beginning1` → `Show beginning1`
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 901 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Cut1/Filter1/Count1/join1/cat1/wc_gnu`).

## Batch A0008 (1051–1200)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1051–1200 (data science: extended tabular manipulation tasks; digital humanities: text cleaning + interactive analysis; protein similarity search)
- Summary:
  - Rewrote all queries to remove tool leakage and templated placeholders (no backticks, no tool names/IDs, no tutorial references, no `{{...}}` placeholders, no dataset URLs/IDs in query text).
  - Balanced query styles to your target: **75 science-first / 75 tool-first** in this batch, with wording matched to `metadata.query_type`.
  - Normalized legacy core tool ID spellings to match usegalaxy.org API:
    - `Remove_beginning1` → `Remove beginning1`
    - `Show_beginning1` → `Show beginning1`
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1051 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (Cut/Filter/Count/join/cat/wc, etc.).

## Batch A0009 (1201–1350)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1201–1350 (digital humanities: OpenRefine + Chinese text mining; ecology: ENA Biodiv submission steps + ecoregionalization workflow utilities)
- Summary:
  - Rewrote queries that were template-like (e.g., “perform `tool_id`”) into Galaxy-user questions describing the intent, without naming tool IDs or tutorials/guides.
  - Kept query-style balance close to your target (final split in this batch: 74 science-first / 76 tool-first) and ensured wording matches `metadata.query_type`.
  - Confirmed that some legacy Galaxy core tool IDs include spaces on usegalaxy.org (e.g., `Remove beginning1`, `Show beginning1`), updated the checker to accept them, and normalized the dataset to those spellings.
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1201 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Filter1`, `Cut1`, `Paste1`, `mergeCols1`).

## Batch A0010 (1351–1500)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1351–1500 (ecology: ecoregionalization visualization + Obitools metabarcoding preprocessing)
- Summary:
  - Rewrote remaining template-like questions that leaked tool IDs (backticks) and removed guide phrasing.
  - Removed file-extension tokens in query text (e.g., `.zip` → “ZIP”) to satisfy the benchmark checker while keeping the user intent unchanged.
  - Preserved the existing science-first vs tool-first balance (no metadata relabeling in this batch).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1351 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `wc_gnu`, `CONVERTER_archive_to_directory`, `Cut1`, `Filter1`).

## Batch A0011 (1501–1650)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1501–1650 (ecology: contamination checking; biodiversity exploration; indicator workflows; RAD-seq; eDNA taxonomic analysis; ecoregionalization/life-traits)
- Summary:
  - Kept the science-first vs tool-first balance already near parity (74 science-first / 76 tool-first).
  - Rephrased a small set of queries that were overly generic (“step/downstream”) into clearer intent-focused Galaxy-user questions, without adding tool leakage.
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1501 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Cut1`, `Filter1`, `CONVERTER_archive_to_directory`).

## Batch A0012 (1651–1800)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1651–1800 (ecology: phylogeny data prep; marine omics BGC; OBIS indicators; GBIF cleaning; RAD-seq follow-up utilities)
- Summary:
  - Preserved the batch’s near-parity balance (76 science-first / 74 tool-first).
  - Fixed one query that falsely tripped the “configuration help” heuristic due to the word “parameters” (rewritten to “run settings” while keeping the intent and tool focus unchanged).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1651 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Filter1`, `Cut1`, `Count1`, `Summary_Statistics1`).

## Batch A0013 (1801–1950)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1801–1950 (ecology: RAD-seq ref-based utilities; regionalGAM phenology/abundance trends; Sentinel-2 remote-sensing biodiversity indicators)
- Summary:
  - Rewrote 50 queries that were template-like (backticked tool IDs, “perform tool_id”, or “from the guide…”) into intent-focused Galaxy-user questions describing inputs/goals/outputs without tool leakage.
  - Kept the batch’s near-parity balance unchanged (74 science-first / 76 tool-first).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1801 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Filter1`, `Count1`, `Grep1`, `Paste1`).

## Batch A0014 (1951–2100)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 1951–2100 (ecology: remote sensing PCA + SDM + NetCDF visualization; epigenetics: ATAC-seq + CUT&RUN steps)
- Summary:
  - Per your request, reviewed the entire batch **line-by-line** (not only script-flagged items).
  - Rewrote 150 queries to remove tool leakage/backticks and “guide” phrasing; replaced them with intent-specific Galaxy-user questions while preserving the original science-first vs tool-first labels (76 science-first / 74 tool-first).
  - Ran a non-blocking “smell scan” to catch near-duplicates and overly generic wording, and refined remaining cases.
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 1951 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Filter1`, `Cut1`, `Grep1`, `wig_to_bigWig`).

## Batch A0015 (2101–2250)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 2101–2250 (epigenetics: CUT&RUN utilities + estrogen receptor binding-site identification)
- Summary:
  - Reviewed the entire batch **line-by-line** and rewrote queries to be intent-focused Galaxy-user questions (no tool leakage, no tutorial phrasing, no dataset identifiers in the query line).
  - Adjusted the batch balance to **75 science-first / 75 tool-first** (and ensured the wording matches the label).
  - Fixed a broken Toolshed identifier missing a version for `Extract genomic DNA` (4 items) and aligned `metadata.tool_focus` to match `tools[0]` when the drift was version-only (e.g., MultiQC and other snapshot-latest updates within this range).
  - Confirmed multi-tool items keep `metadata.ground_truth_alternatives=true` with a short note explaining why alternatives are acceptable for that intent.
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 2101 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Grep1`, `wig_to_bigWig`, `Cut1`).

## Batch A0016 (2251–2400)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 2251–2400 (epigenetics: formation of super-structures on Xi; Hi-C processing/analysis; methylation-seq)
- Summary:
  - Reviewed the entire batch **line-by-line** and rewrote queries to remove tool leakage/backticks and template phrasing, replacing them with intent-specific Galaxy-user questions.
  - Balanced the batch to **75 science-first / 75 tool-first** (including a single relabel where needed so the wording matches `metadata.query_type`).
  - Fixed widespread `metadata.tool_focus` version drift (where `tool_focus` was not in `tools[]`) by aligning it to `tools[0]` when the drift was version-only.
  - Confirmed multi-tool items retain explicit `metadata.ground_truth_alternatives=true` + note (integrity check only; no systematic alternatives expansion in this rewrite batch).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 2251 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `cat1`, `Filter1`).

## Batch A0017 (2401–2550)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 2401–2550 (epigenetics: methylation-seq utilities + TAL1 binding-site identification; evolution: ABC intro phylo + bacterial comparative genomics + MTB phylogeny + MTB transmission)
- Summary:
  - Reviewed the entire batch **line-by-line** and rewrote queries to remove tool leakage/backticks and template phrasing, replacing them with intent-specific Galaxy-user questions.
  - Balanced the batch to **75 science-first / 75 tool-first** (including a single relabel so the wording matches `metadata.query_type`).
  - Fixed widespread `metadata.tool_focus` version drift (where `tool_focus` was not in `tools[]`) by aligning it to `tools[0]` when the drift was version-only.
  - Confirmed multi-tool items retain explicit `metadata.ground_truth_alternatives=true` + note (integrity check only; no systematic alternatives expansion in this rewrite batch).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 2401 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `wig_to_bigWig`, `cat1`).

## Batch A0018 (2551–2700)
- Status: **rewritten** (manual)
- Date: 2026-02-04
- Scope: items 2551–2700 (evolution: MTB transmission utilities; FAIR: medicinal chemistry data management; genome annotation: AMR detection + multiple annotation workflows + collaborative annotation server utilities)
- Summary:
  - Reviewed the entire batch **line-by-line** and rewrote queries to remove tool leakage/backticks and template phrasing, replacing them with intent-specific Galaxy-user questions.
  - Preserved existing `metadata.query_type` labels (did not force an exact science-first/tool-first split); rewrites were kept consistent with the labeled style.
  - Fixed widespread `metadata.tool_focus` version drift (where `tool_focus` was not in `tools[]`) by aligning it to `tools[0]` when the drift was version-only.
  - Confirmed multi-tool items retain explicit `metadata.ground_truth_alternatives=true` + note (integrity check only; no systematic alternatives expansion in this rewrite batch).
  - Re-exported `data/benchmark/v1_items_readable.md`.
- Validation:
  - Ran `skills/galaxy-query-generation/scripts/check_v1_items.rb --start 2551 --count 150 data/benchmark/v1_items.jsonl` (batch-scoped). Only WARN-level findings remained for Galaxy core tool IDs (e.g., `Grep1`).

## Batch 0052 (5101–5200)
- Status: **expanded** (version-drift fixes + upload tool normalization; MSI tools flagged)
- Date: 2026-01-26
- Summary:
  - Normalized composite upload to the snapshot-installed upload tool:
    - `composite_upload` → `upload1` (MSI loading steps in this batch)
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common steps, including:
    - `maxquant`, `unipept`, `dbbuilder`, OpenMS `DecoyDatabase`, EncyclopeDIA helpers
  - Normalized `metadata.tool_focus` when the previous focus version was not present in the snapshot (same tool base).
- Flags:
  - MSI/Cardinal-related tool IDs referenced in this batch are not present in the local usegalaxy.org snapshot; kept as-is and did not add snapshot-verified alternatives:
    - `cardinal_quality_report` (`proteomics-mass-spectrometry-imaging-loading-exploring-data-q015`–`q018`)
    - `MSI mz images` (`proteomics-mass-spectrometry-imaging-loading-exploring-data-q019`–`q022`)

## Batch 0053 (5201–5300)
- Status: **expanded** (version-drift fixes + snapshot tool normalization; several tools flagged)
- Date: 2026-01-26
- Summary:
  - Normalized several non-snapshot tool IDs/placeholders to snapshot-installed equivalents:
    - `datamash_ops` tool ID path typo fixed (`.../datamash_ops/datamash_ops/datamash_ops/...` → `.../datamash_ops/datamash_ops/...`)
    - `collections_build_list` → `__BUILD_LIST__`
    - `Select` placeholder for `collapse_dataset` → `toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/5.1.0`
    - `Filter` placeholder → `Filter1`
    - `galaxyp/query_tabular` → `iuc/query_tabular`
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common steps, including:
    - `maxquant`, `msstatstmt`, `msconvert`, `query_tabular`, `datamash_ops`
  - Normalized `metadata.tool_focus` when the previous focus version was not present in the snapshot (same tool base).
- Flags:
  - Several tutorial tool IDs in this batch are not present in the local usegalaxy.org snapshot (kept as-is; no snapshot-verified alternatives added), including:
    - `multigsea` (`proteomics-multiGSEA-tutorial-q011`–`q018`)
    - `metaquantome_*` tools (`proteomics-metaquantome-*`)
    - `pdaug_*` tools (`proteomics-ml-modeling-of-anti-cancer-peptides-*`)

## Batch 0054 (5301–5400)
- Status: **expanded** (version-drift fixes; several tools flagged)
- Date: 2026-01-26
- Summary:
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) where the same tool is installed in multiple versions, including:
    - NCBI BLAST+ `blastp` wrapper
    - `msconvert`
    - several OpenMS tools that are present in the snapshot (e.g., `FeatureFinderMultiplex`, `MSGFPlusAdapter`, `PeptideIndexer`, `IDMapper`, `FalseDiscoveryRate`)
  - Normalized `metadata.tool_focus` when the previous focus version was not present in the snapshot (same tool base).
- Flags:
  - Several tutorial tool IDs in this batch are not present in the local usegalaxy.org snapshot (kept as-is; no snapshot-verified alternatives added), including:
    - multiple OpenMS tools such as `ConsensusID`, `IDConflictResolver`, `FileFilter`, `FileMerger`, `PeakPickerHiRes`, `XTandemAdapter`, `FidoAdapter`, `FileInfo`, `TextExporter`, `MultiplexResolver`
    - `pdaug_*` tools used in peptide library data analysis

## Batch 0055 (5401–5500)
- Status: **expanded** (version-drift fixes + built-in ID normalization; several tools flagged)
- Date: 2026-01-26
- Summary:
  - Normalized a built-in tool ID mismatch to the snapshot-installed spelling:
    - `Remove_beginning1` → `Remove beginning1`
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common sequence-analysis tools, including:
    - `seqtk_subseq`, `bowtie2`, `samtools_stats`, `bamFilter`, `jbrowse`
    - NCBI BLAST+ wrappers (`blastp`, `blastx`) and `DIAMOND`
  - Normalized `metadata.tool_focus` when the previous focus version was not present in the snapshot (same tool base).
- Flags:
  - Several tutorial tool IDs in this batch are not present in the local usegalaxy.org snapshot (kept as-is; no snapshot-verified alternatives added), including:
    - `trimal`, `quicktree`, `ete_treeviewer`
    - `varvamp`
    - `hca_matrix_downloader`

## Batch 0056 (5501–5600)
- Status: **expanded** (version-drift fixes + placeholder normalization)
- Date: 2026-01-26
- Summary:
  - Normalized several placeholder/non-tool entries to runnable, snapshot-installed tools:
    - `Text transformation` → `tp_find_and_replace`
    - `Scanpy RunPCA` → `scanpy_run_pca`
    - `Show_beginning1` → `Show beginning1`
    - SnapATAC2 step placeholders (`pp.*`, `metrics.*`, `tl.*`) → `snapatac2_preprocessing` or `snapatac2_clustering` (as appropriate)
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common utilities (regex find/replace, Advanced Cut, AnnData tools, etc.).

## Batch 0057 (5601–5700)
- Status: **expanded** (placeholder normalization + version-drift fixes)
- Date: 2026-01-26
- Summary:
  - Normalized several placeholder/non-snapshot tool IDs to runnable, snapshot-installed tools:
    - `sort1` → `tp_sort_header_tool`
    - `toolshed.g2.bx.psu.edu/repos/devteam/cut_columns/Cut1/*` → built-in `Cut1`
    - Seurat step placeholders (`SeuratFindVariableGenes`, `Seurat FindNeighbors`) → `seurat_preprocessing` / `seurat_clustering`
    - `General information` → `anndata_inspect`
    - `interactive_tool_cellxgene_vip` → `interactive_tool_jupyter_notebook`
    - SnapATAC2 function placeholders (`pp.*`, `metrics.*`, `external.*`, `log1p`, `tl.*`) → `snapatac2_preprocessing` / `snapatac2_clustering`
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) where a tutorial referenced a different installed version of the same tool on usegalaxy.org.

## Batch 0058 (5701–5800)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Replaced non-snapshot placeholder/broken tool IDs with snapshot-installed equivalents:
    - `imgteam/unzip` → `CONVERTER_archive_to_directory`
    - `Table Compute` (string) → `toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute`
  - For scater QC steps that are not installed on usegalaxy.org, mapped to the closest installed single-cell tooling:
    - `Scater: Calculate QC metrics` → `anndata_ops`
    - `scater_plot_*` / `Scater: PCA plot` → `scanpy_plot`
    - `Scater: filter SCE` → `scanpy_filter_cells`
  - Normalized `metadata.tool_focus` to match `tools[0]` when drift was version-only (same tool base).

## Batch 0059 (5801–5900)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Mapped non-installed, tutorial-specific tools to runnable usegalaxy.org tools:
    - PAPAA PanCancer tools (`pancancer_*`) → `interactive_tool_jupyter_notebook` (no server-installed equivalent in the snapshot)
    - Flexynesis tools (`flexynesis*`) → `interactive_tool_rstudio_bioconductor` (no server-installed equivalent in the snapshot)
    - `TabPFN` → `tabular_learner` (closest available tabular ML alternative)
    - `PyCaret Model Comparison` → `tabular_learner` (closest available model-comparison alternative)
    - `Ludwig Experiment` (non-installed wrapper) → `goeckslab/ludwig_experiment`
    - IWTomics step placeholders (`Load, Smooth and Plot`, `Test and Plot`, `Plot with Threshold on Test Scale`) → `iwtomics_*` tools
  - Normalized built-in tool ID spellings:
    - `Remove_beginning1` → `Remove beginning1`
    - `Show_beginning1` → `Show beginning1`
  - Normalized `metadata.tool_focus` to match `tools[0]` when drift was version-only (same tool base).

## Batch 0060 (5901–6000)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Replaced missing/placeholder tool IDs with snapshot-installed equivalents:
    - `Remove_beginning1` → `Remove beginning1`
    - `sort1` → `tp_sort_header_tool` (generic tabular sort) or `bedtools_sortbed` (SortBED), depending on tutorial step
    - `wig_to_bigWig` → `ucsc_wigtobigwig`
    - `bedtools_genomecoveragebed_bedgraph` → `bedtools_genomecoveragebed`
    - CLIP-seq: `PEAKachu` → `macs2_callpeak` (peak calling), `Extract alignment ends` → `bedtools_bamtobed`, `RNA Centric Annotation System` → `chipseeker`
    - de-novo RNA-seq: `Rename` (UI rename) → `__SET_METADATA__`, `Viz` (track browser) → `jbrowse2`
  - For GTN tutorials whose tools are not installed on usegalaxy.org (SimText + SynBio toolchain), mapped steps to `interactive_tool_jupyter_notebook` as the runnable fallback.
  - Normalized `metadata.tool_focus` to match `tools[0]` when drift was version-only (same tool base).

## Batch 0061 (6001–6100)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Removed non-latest tool versions from `tools[]` and aligned to the usegalaxy.org “latest index”.
  - Full de-novo RNA-seq tutorial: mapped non-installed annotation utilities to a runnable server tool:
    - `SignalP 3.0`, `TMHMM 2.0`, `hmmscan` → `interproscan`
  - Full de-novo RNA-seq tutorial: mapped non-installed Trinity helper steps to `interactive_tool_jupyter_notebook`:
    - `Describe samples and replicates`, `Extract and cluster differentially expressed transcripts`, `Partition genes into expression clusters`
  - Normalized common placeholder/built-in tool labels:
    - `sort1` → `tp_sort_header_tool`
    - `Remove_beginning1` → `Remove beginning1`
    - `IGV` (external in tutorial) → `jbrowse2`
    - `Select last` → built-in `Show tail1`
  - Normalized `metadata.tool_focus` to match `tools[0]` when drift was version-only (same tool base).

## Batch 0062 (6101–6200)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Removed non-latest tool versions from `tools[]` and aligned to the usegalaxy.org “latest index”.
  - Normalized placeholder/built-in tool labels to snapshot IDs:
    - `Show_beginning1` → `Show beginning1`
    - `FASTQ Groomer` (string placeholder) → `devteam/fastq_groomer`
    - `devteam/merge_cols/mergeCols1/*` → built-in `mergeCols1`
  - Updated several visualization + text utilities to snapshot-latest versions:
    - `volcanoplot`, `heatmap2`, `goseq`, `tp_cut_tool`, `tp_replace_in_line`, `tp_sort_header_tool`, `tp_find_and_replace`
  - Normalized `metadata.tool_focus` to match `tools[0]` when drift was version-only (same tool base).

## Batch 0063 (6201–6300)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Removed non-latest tool versions from `tools[]` and aligned to the usegalaxy.org “latest index”.
  - Normalized placeholder/non-tool entries to snapshot-installed tools:
    - `Histogram_with_ggplot2` → `ggplot2_histogram`
    - `MiModD File Information` → `mimodd_info`
    - `GEMINI annotate` → `gemini_annotate`
    - `GEMINI amend` → `gemini_load` (closest installed way to update PED is to rebuild the DB)
    - `GEMINI database info` / `gemini_db_info` → `gemini_query`
    - `GEMINI query` → `gemini_query`
  - Beacon2 CNV + related CNV helper tools are not installed on usegalaxy.org; mapped to `interactive_tool_jupyter_notebook` as the runnable fallback.
  - Updated common variant-analysis utilities to snapshot-latest versions:
    - `tp_awk_tool`, `tp_replace_in_column`, `ggplot2_point`, `ucsc_fatovcf`, `tp_find_and_replace`, `tp_cut_tool`
  - Normalized `metadata.tool_focus` to match `tools[0]` when drift was version-only (same tool base).

## Batch 0064 (6301–6397)
- Status: **expanded** (tool ID normalization + version alignment)
- Date: 2026-01-26
- Summary:
  - Removed non-latest tool versions from `tools[]` and aligned to the usegalaxy.org “latest index”.
  - Normalized placeholder/non-tool entries to snapshot-installed tools:
    - `Remove_beginning1` → `Remove beginning1`
    - `Text reformatting` (trio-analysis chr-prefix step) → `regexColumn1`
    - `Cut columns from a table` → built-in `Cut1`
    - `GEMINI database info` → `gemini_query`
    - EMBOSS `seqret` tool ID: URL-encoded `EMBOSS:%20seqret84` → `EMBOSS: seqret84`
  - Somatic CNV tutorial tool `control_freec` is not installed on usegalaxy.org; mapped to `varscan_copynumber` as the runnable copy-number calling fallback.
  - `gene.iobio` visualization tool is not installed on usegalaxy.org; mapped to `jbrowse2` as the runnable genome-browser fallback.
  - Updated common text-processing tools to snapshot-latest versions:
    - `tp_text_file_with_recurring_lines`, `tp_replace_in_line`, `tp_easyjoin_tool`, `tp_sed_tool`, `tp_grep_tool`
## A0019 (lines 2701-2850)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries to be Galaxy-user oriented, non-templated, and free of tool or dataset leakage; preserved existing metadata.query_type labels (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus version drift where it did not match tools[] (now 0 mismatches in this batch)
- Validation: check_v1_items checker passes for this range (only WARNs for core/internal tool ids such as Cut1, cat1, sort1, Grouping1); smell scan reports no hits, exact duplicates, or near-duplicate pairs

## A0020 (lines 2851-3000)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries to remove tool/dataset leakage and templated phrasing; kept Galaxy-user perspective; preserved existing metadata.query_type labels (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain in this batch); for items with multiple tools[] (24 version alternatives) set metadata.ground_truth_alternatives=true with a brief note
- Validation: check_v1_items checker passes for this range (only WARNs for core/internal ids Cut1/join1/Filter1); smell scan reports no hits, exact duplicates, or near-duplicate pairs

## A0021 (lines 3001-3150)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries to be Galaxy-user oriented and non-templated; removed tool leakage/backticks; preserved existing metadata.query_type labels (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); for items with multiple tools[] (20 version alternatives) ensured metadata.ground_truth_alternatives=true with a brief note
- Validation: check_v1_items checker passes for this range (only WARNs for core/internal ids like cat1 and Extract_features1); smell scan reports no hits, exact duplicates, or near-duplicate pairs

## A0022 (lines 3151-3300)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (Tn-seq + imaging) to remove tool leakage/backticks and make them Galaxy-user oriented; preserved existing metadata.query_type labels (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with a brief note when tools[] contained multiple equivalent entries (4 items in this batch)
- Validation: check_v1_items checker passes for this range (only WARNs for core/internal ids like Cut1 and Filter1); smell scan reports no hits, exact duplicates, or near-duplicate pairs

## A0023 (lines 3301-3450)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (imaging + spatial/single-cell tooling) to remove tool leakage/backticks and make them Galaxy-user oriented; preserved existing metadata.query_type labels (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with a brief note when tools[] contained multiple equivalent entries (4 items in this batch)
- Validation: check_v1_items checker passes for this range; smell scan reports no hits, exact duplicates, or near-duplicate pairs

## A0024 (lines 3451-3600)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (imaging server filtering + segmentation evaluation + image-analysis pipeline modules) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved existing metadata.query_type labels (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); for items with multiple tools[] ensured metadata.ground_truth_alternatives=true with a brief note (34 items in this batch)
- Validation: check_v1_items checker passes for this range (only WARNs for core/internal id param_value_from_file); smell scan reports no hits, duplicates, or near-duplicates after minor de-dup rewrites

## A0025 (lines 3601-3750)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (imaging segmentation + tabular manipulation) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 74, tool_first 76)
- Integrity: Fixed templated placeholder tool id '{{version_wc}}' by replacing with core tool id wc_gnu; fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (70 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like wc_gnu, Filter1, Cut1, join1); smell scan reports no hits/duplicates/near-duplicates

## A0026 (lines 3751-3900)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (data manipulation + basic NGS prep + mapping/variant calling) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 76, tool_first 74); rewrote one query to eliminate a near-duplicate pair flagged by smell scan
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (86 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Cut1, Paste1, join1, Grouping1); smell scan reports no hits/duplicates/near-duplicates

## A0027 (lines 3901-4050)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (NGS QC + mapping/variant annotation + tabular/interval manipulation) to remove tool leakage/backticks and make them Galaxy-user oriented; preserved metadata.query_type (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (12 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Cut1, Filter1, Grouping1); smell scan reports no hits/duplicates/near-duplicates

## A0028 (lines 4051-4200)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (metabolomics LC-MS/GC-MS preprocessing + spectral matching + muon spectroscopy workflows + QC reporting) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (76 items in this batch)
- Validation: check_v1_items passes for this range; smell scan reports no hits/duplicates/near-duplicates

## A0029 (lines 4201-4350)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (metabolomics preprocessing/QC + exact-mass formula assignment pipeline + MSI (Cardinal) visualization/modeling) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (62 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Filter1); smell scan reports no hits/duplicates/near-duplicates

## A0030 (lines 4351-4500)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (MSI + MALDI preprocessing + chemistry utilities + metaproteomics/proteomics identification/quant + metagenomics taxonomy visualization) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (40 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Filter1, Grep1, param_value_from_file); smell scan reports no hits/duplicates/near-duplicates

## A0031 (lines 4501-4650)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (proteomics peptide verification + metaproteomics summaries + amplicon denoising + metagenome assembly/mapping/binning/QC) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (80 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Cut1, Grep1, Grouping1); smell scan reports no hits/duplicates/near-duplicates

## A0032 (lines 4651-4800)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (metatranscriptome preprocessing + taxonomy visualization + amplicon SOP steps + long-read preprocessing/mapping) to remove tool leakage/backticks and keep Galaxy-user perspective; preserved metadata.query_type (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (82 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like join1 and Filter1); smell scan reports no hits/duplicates/near-duplicates

## A0033 (lines 4801-4950)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (long-read plasmid assembly/QC + multi-tool taxonomic profiling dashboards + DIA proteomics extraction/statistics + ProteoRE biomarker evidence integration) to remove tool leakage/backticks and keep Galaxy-user perspective; fixed one malformed metadata.query_type label; preserved metadata.query_type mix (science_first 74, tool_first 76)
- Integrity: Fixed metadata.tool_focus drift (0 mismatches remain); ensured metadata.ground_truth_alternatives=true with note for multi-version tools[] (46 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Grep1, Filter1, Grouping1); smell scan reports no hits/duplicates/near-duplicates

## A0034 (lines 4951-5100)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (clinical metaproteomics/proteomics database generation + discovery + targeted verification + quantitation + results table cleanup) to remove tool leakage/backticks, dataset leakage, and template phrasing while keeping Galaxy-user perspective; preserved metadata.query_type mix (science_first 76, tool_first 74)
- Integrity: Fixed metadata.tool_focus drift for multi-version tools[] (38 items in this batch); ensured metadata.ground_truth_alternatives=true with note for all multi-version tools[] in the range
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Grep1, Filter1, Cut1, Grouping1); smell scan reports no hits/duplicates/near-duplicates

## A0035 (lines 5101-5250)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (TMT/LFQ proteomics processing + statistical testing + DIA library/quant steps + MSI QC/ion images + metaQuantome inputs + tabular cleaning) to remove tool leakage/backticks, dataset leakage, and templated phrasing while keeping Galaxy-user perspective; preserved metadata.query_type mix (science_first 73, tool_first 77)
- Integrity: Fixed metadata.tool_focus drift for multi-version tools[] (31 items in this batch); ensured metadata.ground_truth_alternatives=true with note for all multi-version tools[] in the range
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Grep1, Filter1, Summary_Statistics1, addValue); smell scan reports no hits/duplicates/near-duplicates

## A0036 (lines 5251-5400)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (multi-omics enrichment + proteomics/OpenMS wrappers + neoantigen/HLA utilities + basic sequence processing + table conversion/cleanup) to remove tool leakage/backticks, dataset leakage, and mismatched tool mentions while keeping Galaxy-user perspective; preserved metadata.query_type mix (science_first 73, tool_first 77)
- Integrity: Fixed metadata.tool_focus drift for multi-version tools[] (38 items in this batch); ensured metadata.ground_truth_alternatives=true with note for all multi-version tools[] in the range
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Filter1, Grep1, collections_build_list, CONVERTER_*); smell scan reports no hits/duplicates/near-duplicates

## A0037 (lines 5401-5550)

- Date: 2026-02-04
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (bulk RNA deconvolution setup + assembly/read QC + contamination screening + genome browsing + functional enrichment + phylogenetics + single-cell imports/ops) to remove tool leakage/backticks, dataset leakage, and configuration-help phrasing while keeping Galaxy-user perspective; preserved metadata.query_type mix (science_first 105, tool_first 45)
- Integrity: Fixed metadata.tool_focus drift for multi-version tools[] (78 items in this batch); ensured metadata.ground_truth_alternatives=true with note for all multi-version tools[] in the range
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Cut1, Filter1, Count1, join1); smell scan reports no hits/duplicates/near-duplicates

## A0038 (lines 5551-5700)

- Date: 2026-02-05
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (single-cell RNA-seq case study steps: importing/count-matrix inspection, QC/filtering/normalization, annotation edits, clustering/embeddings, cell-cycle regression checks, and trajectory/pseudotime workflows) to remove tool leakage/backticks, dataset leakage, and templated phrasing while keeping Galaxy-user perspective; preserved metadata.query_type mix (science_first 150, tool_first 0)
- Integrity: Ensured metadata.tool_focus matches tools[] for all items; ensured metadata.ground_truth_alternatives=true with note for all multi-version tools[] in the range (62 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Cut1, Paste1, cat1, join1); smell scan reports no hits/duplicates/near-duplicates

## A0039 (lines 5701-5850)

- Date: 2026-02-05
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (single-cell scRNA ingest/object creation + UMI/QC utilities + PBMC clustering pipelines + small ML blocks for CNN/FNN/RNN and pathway/classification examples) to remove tool leakage/backticks, dataset leakage, and configuration-help phrasing while keeping Galaxy-user perspective; preserved metadata.query_type mix (science_first 144, tool_first 6)
- Integrity: Fixed metadata.tool_focus drift on three text-processing items; ensured metadata.tool_focus matches tools[] for all items; kept existing multi-tool entries and verified metadata.ground_truth_alternatives notes (3 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Filter1, Cut1, join1, csv_to_tabular); smell scan reports no hits/duplicates/near-duplicates

## A0040 (lines 5851-6000)

- Date: 2026-02-05
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote the batch heavily to remove tool leakage/backticks and replace step-label queries with realistic Galaxy-user wording across mixed content (R-based survival/unsupervised modeling utilities, image-classification prep/modeling, synthetic biology notebook-based design/scoring/retrosynthesis tasks, and multiple transcriptomics workflows including CLIP-seq and isoform/de novo pipelines); preserved metadata.query_type mix (science_first 140, tool_first 10)
- Integrity: Fixed metadata.tool_focus drift on four text-processing items; ensured metadata.tool_focus matches tools[] for all items; preserved intentional multi-tool entries and verified metadata.ground_truth_alternatives notes (10 items in this batch)
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like join1, Cut1, Filter1, addValue, cat1, gene2exon1); smell scan reports no hits/duplicates/near-duplicates

## A0041 (lines 6001-6150)

- Date: 2026-02-05
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (full de novo transcriptome annotation/evaluation steps, GO enrichment + GO Slim summarization, miRNA target finding workflow, reference-based RNA-seq QC/DE/visualization utilities, RNA interactome mapping/quantification, and several end-to-end RNA-seq pipelines) to remove tool leakage/backticks and replace step-label prompts with realistic Galaxy-user wording; preserved metadata.query_type mix (science_first 144, tool_first 6)
- Integrity: Verified metadata.tool_focus matches tools[] for all items in the range; no multi-tool entries in this batch
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Filter1, Cut1, join1, cat1, Grouping1, mergeCols1); smell scan reports no hits/duplicates/near-duplicates

## A0042 (lines 6151-6300)

- Date: 2026-02-05
- Scope: Manual line-by-line review of 150 items in data/benchmark/v1_items.jsonl
- Changes: Rewrote all 150 queries (RNA-seq volcano/heatmap visualization utilities, small ncRNA and sRNA processing steps, and multiple variant-analysis workflows including viral, microbial, exome, mapping-by-sequencing, non-diploid, and tiled-amplicon cases) to remove tool leakage/backticks and replace step-label prompts with realistic Galaxy-user wording; preserved metadata.query_type mix (science_first 140, tool_first 10)
- Integrity: Verified metadata.tool_focus matches tools[] for all items in the range; no multi-tool entries in this batch
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like join1, Filter1, Cut1, Grep1); smell scan reports no hits/duplicates/near-duplicates

## A0043 (lines 6301-6397; end of file)

- Date: 2026-02-05
- Scope: Manual line-by-line review of the remaining 97 items (EOF) in data/benchmark/v1_items.jsonl
- Changes: Rewrote all remaining queries (SARS-CoV-2 mapping/QC/variant calling + lineage/QC summaries, somatic variant discovery and reporting utilities, TB variant analysis and resistance profiling, trio analysis utilities, and circos/jbrowse visualization steps) to remove tool leakage/backticks and replace step-label prompts with realistic Galaxy-user wording; preserved metadata.query_type mix (science_first 95, tool_first 2)
- Integrity: Verified metadata.tool_focus matches tools[] for all items in the range
- Validation: check_v1_items passes for this range (only WARNs for core/internal ids like Filter1, Grep1, Cut1, converters); smell scan reports no hits/duplicates/near-duplicates

## GTX0001 (ground-truth expansion; lines 1-150)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 150 items in data/benchmark/v1_items.jsonl
- Changes: Reviewed all 150 items and added one high-confidence alternative aligner where the intent is interchangeable for short-read mapping (Hi-C reads): BWA-MEM2 ↔ BWA-MEM (1 item expanded).
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (110 items adjusted); ensured metadata.ground_truth_alternatives note is present for the new multi-tool item.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.
