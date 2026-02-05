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

## GTX0002 (ground-truth expansion; lines 151-350)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Changes: Reviewed all 200 items and kept expansions conservative (no new alternatives added in this batch). Made two small query rewrites to eliminate a smell-scan “too generic step” flag and a near-duplicate BUSCO query pair while keeping intent unchanged.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (123 items adjusted).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0003 (ground-truth expansion; lines 351-550)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Changes: Reviewed all 200 items and added one high-confidence alternative short-read aligner where the intent is interchangeable: BWA-MEM2 ↔ BWA-MEM (1 item expanded). Also made one small query rewrite to remove a smell-scan “guide phrase” while keeping intent unchanged (q050).
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (84 items adjusted).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0004 (ground-truth expansion; lines 551-750)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Changes: Reviewed all 200 items and expanded 4 Open Babel compound-format conversion items to include `ctb_compound_convert` as an acceptable alternative to `openbabel_compound_convert` (q059–q062). Also made two small query rewrites to remove a smell-scan “guide phrase” while keeping intent unchanged (q077, q060).
  - Evidence (tool_catalog w/ helptext + IO): `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` shows both tools’ helptext describe an Open Babel “compound converter” that *interconverts various chemistry / molecular modeling file formats* and lets the user choose an output format; both expose a `infile` data input and emit a converted structure output (`outfile` / `file_outputs`), making them interchangeable for these “convert ligand library between formats” intents.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (124 items adjusted).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0005 (ground-truth expansion; lines 751-950)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (132 items adjusted).
- Query hygiene: Rewrote 1 query to avoid accidentally leaking a tool-id literal (“setup”) while keeping intent unchanged (q012).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0006 (ground-truth expansion; lines 951-1150)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (111 items adjusted).
- Query hygiene: Rewrote 7 queries to eliminate exact-duplicate pairs flagged by smell scan while keeping intent unchanged (q121, q157, q090, q104, q125, q129, q130).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no smell hits and no exact duplicates in this range.

## GTX0007 (ground-truth expansion; lines 1151-1350)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (40 items adjusted).
- Query hygiene: Rewrote 4 queries to clear smell-scan “too generic step” flags and an exact-duplicate pair while keeping intent unchanged (q029, q044, q017, q048).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0008 (ground-truth expansion; lines 1351-1550)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (8 items adjusted).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0009 (ground-truth expansion; lines 1551-1750)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 7 queries to clear smell-scan “too generic (custom code)” and exact-duplicate flags while keeping intent unchanged (q022, q025, q026, q015, q016, q018, q013).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates (one remaining near-duplicate pair acceptable).

## GTX0010 (ground-truth expansion; lines 1751-1950)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (8 items adjusted).
- Query hygiene: Rewrote 9 queries to clear smell-scan “too generic (custom code)” and an exact-duplicate pair while keeping intent unchanged (q026, q038, q050, q058, q062, q014, q058, q061, q027).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates (one remaining near-duplicate pair acceptable).

## GTX0011 (ground-truth expansion; lines 1951-2150)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Integrity: Fixed metadata.tool_focus drift so tool_focus is always one of tools[] in this range (98 items adjusted).
- Query hygiene: Rewrote 5 queries to remove exact-duplicate pairs between ATAC-seq and CUT&RUN variants while keeping intent unchanged (q038, q045, q049, q061, q081).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates (remaining near-duplicate pairs acceptable).

## GTX0012 (ground-truth expansion; lines 2151-2350)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0013 (ground-truth expansion; lines 2351-2550)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0014 (ground-truth expansion; lines 2551-2750)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0015 (ground-truth expansion; lines 2751-2950)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0016 (ground-truth expansion; lines 2951-3150)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0017 (ground-truth expansion; lines 3151-3350)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool existence/semantics (helptext) and IO shape for any potential alternative additions, even when ultimately deciding not to expand. Noted that some tools referenced in v1 may be missing from this catalog snapshot (e.g., `toolshed.g2.bx.psu.edu/repos/imgteam/unzip/unzip/6.0+galaxy0` not found; only `__UNZIP_COLLECTION__` present), so I avoided adding any new alternatives that I could not corroborate via the catalog.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 4 queries to remove exact duplicates across imaging tutorials while keeping intent unchanged (`imaging-imaging-introduction-q021`, `imaging-imaging-introduction-q022`, `imaging-imaging-introduction-q033`, `imaging-imaging-introduction-q042`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates (remaining near-duplicate pairs acceptable).

## GTX0018 (ground-truth expansion; lines 3351-3550)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review for tool existence/semantics (helptext) and IO shape. Many imaging-related Toolshed tools in this range (including the CellProfiler tool IDs in `imaging-tutorial-CP`) were not present in this catalog snapshot, so I did not add any new alternatives that could not be corroborated via catalog helptext/IO.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 2 queries to remove exact duplicates across imaging tutorials while keeping intent unchanged (`imaging-tutorial-CP-q019`, `imaging-tutorial-CP-q020`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates (remaining near-duplicate pairs acceptable).

## GTX0019 (ground-truth expansion; lines 3551-3750)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review for tool existence/semantics (helptext) and IO shape (e.g., checked the tabular “Sort (keep header)” tool family via `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/...`).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added and no query rewrites were needed in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0020 (ground-truth expansion; lines 3751-3950)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate tool semantics via helptext/IO (notably, confirmed that `lofreq_viterbi` is a read realignment step rather than a variant caller).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 1 query to match the real intent of the gold tool while keeping the item’s step meaning consistent (`introduction-galaxy-intro-ngs-data-managment-q033`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0021 (ground-truth expansion; lines 3951-4150)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review for tool existence/semantics and IO shape (e.g., intersect/overlap operations and fastq QC/preprocessing tools such as `toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/...`).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added and no query rewrites were needed in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0022 (ground-truth expansion; lines 4151-4350)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate tool semantics/IO where possible (e.g., confirmed metabolomics chromatogram plotting via `toolshed.g2.bx.psu.edu/repos/lecorguille/xcms_plot_chromatogram/xcms_plot_chromatogram/...`). Several other metabolomics tools referenced in this range were not present in this catalog snapshot, so I did not add any new alternatives without catalog corroboration.
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 4 queries to remove exact duplicates across metabolomics tutorials while keeping intent unchanged (`metabolomics-lcms-preprocessing-q022`, `metabolomics-lcms-dataprocessing-q011`, `metabolomics-lcms-dataprocessing-q021`, `metabolomics-lcms-dataprocessing-q022`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates (remaining near-duplicate pairs acceptable).

## GTX0023 (ground-truth expansion; lines 4351-4550)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate tool semantics/IO for candidate edits (e.g., proteomics steps around `toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/...` and FASTA merge/deduplication tools).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 8 queries to remove exact duplicates across metabolomics vs microbiome tutorials while keeping intent unchanged (`microbiome-clinical-mp-3-verification-q017`, `microbiome-clinical-mp-3-verification-q018`, `microbiome-clinical-mp-4-quantitation-q011`, `microbiome-clinical-mp-4-quantitation-q012`, `microbiome-clinical-mp-4-quantitation-q013`, `microbiome-clinical-mp-4-quantitation-q014`, `microbiome-clinical-mp-4-quantitation-q017`, `microbiome-clinical-mp-4-quantitation-q018`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates (remaining near-duplicate pairs acceptable).

## GTX0024 (ground-truth expansion; lines 4551-4750)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate tool semantics/IO for the mothur MiSeq SOP tool chain (merge files, unique sequences, alignment, screening).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 15 queries to remove exact duplicates between the generic microbiome tutorial and the mothur MiSeq SOP tutorial while keeping intent unchanged (updated `microbiome-mothur-miseq-sop-q011`..`q022` and `microbiome-mothur-miseq-sop-q024`..`q026`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no exact duplicates (one remaining near-duplicate pair acceptable).

## GTX0025 (ground-truth expansion; lines 4751-4950)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate taxonomy-classification tool semantics via helptext/IO (e.g., `toolshed.g2.bx.psu.edu/repos/iuc/kraken2/kraken2/...`).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added in this batch.
- Query hygiene: Rewrote 2 queries to remove exact duplicates across nanopore microbiome tutorials while keeping intent unchanged (`microbiome-pathogen-detection-from-nanopore-foodborne-data-q029`, `microbiome-pathogen-detection-from-nanopore-foodborne-data-q030`).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0026 (ground-truth expansion; lines 4951-5150)

- Date: 2026-02-05
- Scope: Manual per-item ground-truth expansion + integrity pass for 200 items in data/benchmark/v1_items.jsonl
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review for tool existence/semantics and IO shape (e.g., proteomics database construction + MaxQuant/MetaNovo-related tool families such as `toolshed.g2.bx.psu.edu/repos/galaxyp/fasta_merge_files_and_filter_unique_sequences/fasta_merge_files_and_filter_unique_sequences/...`).
- Changes: Reviewed all 200 items; no new ground-truth alternatives were added and no query rewrites were needed in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0027 (ground-truth fix + expansion; lines 1-200)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items in data/benchmark/v1_items.jsonl, focusing on ground-truth integrity (tool existence on usegalaxy.org snapshot) and adding alternatives only when clearly equivalent.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to confirm tool presence and sanity-check semantics/IO for any replacements or potential alternative additions (e.g., confirmed `MUMmer dotplot` tool entry for whole-genome dotplot visualization).
- Changes: Replaced 7 gold tool IDs that were not present in the usegalaxy.org catalog snapshot with catalog-present, semantically equivalent tools where available (no deletions needed in this batch).
  - `chromeister` → `toolshed.g2.bx.psu.edu/repos/peterjc/mummer/mummerplot_wrapper/0.0.7` (whole-genome dotplot)
  - Toolshed `mergeCols1` wrapper → core `mergeCols1` (merge columns side-by-side)
  - `circos_interval_to_tiles` → `circos_interval_to_tile` (tile track formatting)
  - `Rules` → `__APPLY_RULES__` (rule-based mapping for collections/upload)
- Ground-truth alternatives: No new multi-tool alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0028 (ground-truth fix + expansion; lines 201-400)

- Date: 2026-02-05
- Scope: Manual per-item review for the next 200 items, prioritizing replacing missing gold tools with catalog-present, semantically equivalent tools when possible; deleting only when no equivalent exists in the usegalaxy.org tool universe snapshot.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate tool existence and semantics/IO for each replacement (e.g., confirmed `Unique lines`, `pilon`, and NetCDF `xarray` tool families via helptext/IO).
- Changes:
  - Replaced 8 missing gold tool IDs with catalog-present equivalents:
    - `bg_uniq` → `tp_uniq_tool` (unique lines/records)
    - `polypolish` → `pilon` (short-read assembly polishing)
    - `Convert_characters1` → `Convert characters1` (character cleanup)
    - `sort1` → `tp_sort_header_tool` (tabular sorting)
    - `timeseries_extraction` → `xarray_select` (extract time series at coordinate)
    - `psy_maps` → `xarray_mapplot` (geographic map plot from gridded NetCDF)
  - Deleted 5 items where no semantically equivalent tool could be found in the usegalaxy.org catalog snapshot (climate/ODV/Argo fetch + essential variability; and a generic bar-chart plotting item).
- Ground-truth alternatives: No new multi-tool alternatives were added in this batch.
- Validation: check_v1_items passes for the kept subset in this reviewed range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0029 (ground-truth fix + expansion; lines 396-595)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items (accounting for prior deletions shifting line numbers). Goal: replace missing gold tools with catalog-present, semantically equivalent tools when available; otherwise delete.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate tool existence and semantics/IO for replacements (e.g., verified the Interactive JupyterLab Notebook tool entry before using it as a replacement notebook environment).
- Changes:
  - Replaced 8 missing interactive-notebook gold tools with `interactive_tool_jupyter_notebook` (JupyterLab notebook environment) because it satisfies the query intent (“interactive notebook connected to Galaxy datasets”).
  - Deleted 27 items in this range where the gold tool was missing from the catalog and no clearly equivalent usegalaxy.org tool could be identified (notably: DIVA/DIVAnd-style objective analysis gridding, ODV interactive profile QC tools + history capture, biogeochemical calibration, and Copernicus/Sentinel discovery tools).
- Ground-truth alternatives: No new multi-tool alternatives were added in this batch.
- Validation: check_v1_items passes for the kept subset in this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0030 (ground-truth fix + expansion; lines 569-768)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on replacing missing gold tools with catalog-present equivalents and adding alternatives only when they clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate pose-scoring tool semantics/IO (e.g., confirmed SuCOS is reference-ligand overlap scoring and TransFS is deep-learning pose scoring).
- Changes:
  - Replaced 4 missing `xchem_pose_scoring` gold tools with catalog-present equivalents that match the query intent:
    - Reference-ligand pose comparison queries → `toolshed.g2.bx.psu.edu/repos/bgruening/sucos_docking_scoring/sucos_docking_scoring/2020.03.4+galaxy1`
    - “score poses beyond docking engine score” query → `toolshed.g2.bx.psu.edu/repos/bgruening/xchem_transfs_scoring/xchem_transfs_scoring/0.4.0`
  - Query hygiene: Rewrote 4 near-duplicate queries (same tools) to keep within-tool diversity while preserving intent (`computational-chemistry-htmd-analysis-q091`, `q094`, `q111`, `q083`).
- Ground-truth alternatives: No new multi-tool alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0031 (ground-truth fix + expansion; lines 769-968)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, fixing non-catalog gold IDs and expanding only when alternatives clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate GROMACS MD-step tool semantics/IO (setup vs energy minimization vs generic simulation) before replacing missing gold tools.
- Changes:
  - Replaced 16 missing NAMD-workflow placeholder gold IDs (`setup`, `minimizer`, `namd_nvt`, `namd_npt`) with catalog-present GROMACS tools that satisfy the same user intents:
    - Setup → `toolshed.g2.bx.psu.edu/repos/chemteam/gmx_setup/gmx_setup/2022+galaxy0`
    - Energy minimization → `toolshed.g2.bx.psu.edu/repos/chemteam/gmx_em/gmx_em/2022+galaxy0`
    - Equilibration/MD stages → `toolshed.g2.bx.psu.edu/repos/chemteam/gmx_sim/gmx_sim/2022+galaxy0`
  - Query hygiene: Rewrote 2 overly-generic near-duplicate table-manipulation queries to keep within-tool diversity while preserving intent (`data-science-data-manipulation-olympics-q021`, `data-science-data-manipulation-olympics-q025`).
- Ground-truth alternatives: No new multi-tool alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0032 (ground-truth fix + expansion; lines 969-1168)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on query quality (duplicates/near-duplicates) and adding ground-truth alternatives only when they clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool semantics/IO for representative tools in this range (e.g., verified the `Compute`/column-creation tool entry `Add_a_column1` via helptext/IO fields).
- Changes: No gold tool replacements or deletions were needed in this batch (all referenced tools were present in the usegalaxy.org catalog snapshot).
- Query hygiene: Rewrote 4 queries to remove one exact-duplicate pair and reduce highly repetitive near-duplicates while preserving intent (`digital-humanities-open-refine-tutorial-q013`, `data-science-data-manipulation-olympics-q128`, `data-science-data-manipulation-olympics-q136`, `data-science-data-manipulation-olympics-q103`).
- Ground-truth alternatives: No new multi-tool alternatives were added in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no exact duplicates (remaining near-duplicate pairs acceptable).

## GTX0033 (ground-truth fix + expansion; lines 1169-1368)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on ground-truth integrity and query hygiene; add alternatives only when they clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool semantics/IO for representative tools in this range (e.g., verified the NCBI BLAST+ `ncbi_blastn_wrapper` entry via helptext + `input_params_flat`/`outputs_raw`).
- Changes: No gold tool replacements, deletions, or alternative additions were needed in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0034 (ground-truth fix + expansion; lines 1369-1568)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on ground-truth integrity and strict alternative additions only when they clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool semantics/IO for representative tools in this range (e.g., verified the NCBI BLAST+ `ncbi_blastn_wrapper` entry via helptext + `input_params_flat`/`outputs_raw`).
- Changes: No gold tool replacements, deletions, query rewrites, or alternative additions were needed in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0035 (ground-truth fix + expansion; lines 1569-1768)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on ground-truth integrity and strict alternative additions only when they clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool semantics/IO for representative tools in this range (e.g., checked `Count1` / `Grouping1` helptext entries for the “frequency table / count values” intent, and validated that the tools are present on the usegalaxy.org snapshot).
- Changes: No gold tool replacements, deletions, query rewrites, or alternative additions were needed in this batch.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0036 (ground-truth fix + expansion; lines 1769-1968)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on ground-truth integrity (tool must exist on the usegalaxy.org snapshot) and strict alternative additions only when they clearly satisfy the query.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to validate proposed replacements (e.g., confirmed `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_pca/sklearn_pca/1.0.11.0` supports PCA on tabular feature matrices via helptext + `input_params_flat`).
- Changes:
  - Replaced 4 missing remote-sensing PCA gold tools (`srs_pca/0.0.1`) with a usegalaxy-present, IO-compatible PCA tool (`sklearn_pca/1.0.11.0`) and rewrote those 4 queries to match the tabular PCA intent.
  - Deleted 40 items whose gold tools are not present in the usegalaxy.org catalog snapshot and for which no clearly semantically/IO-equivalent replacement was available in-catalog (regionalGAM ecology tools, remote-sensing processing/report tool, occurrence fetching tool, interactive SDM workbench, and CDO operations).
  - Query hygiene: Rewrote 1 Count1 query (`ecology-regionalGAM-q028`) to remove a near-duplicate within-tool phrasing while preserving intent.
- Validation: check_v1_items passes for the kept items in this batch (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after the rewrite.

## GTX0037 (ground-truth fix + expansion; lines 1929-2128)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on ground-truth integrity and query diversity (avoid near-duplicates under the same tool).
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate the WIG→BigWig conversion replacement (confirmed `toolshed.g2.bx.psu.edu/repos/iuc/ucsc_wigtobigwig/ucsc_wigtobigwig/482+galaxy0` via helptext + IO fields).
- Changes:
  - Replaced 8 missing `wig_to_bigWig` gold tool IDs with the usegalaxy-present UCSC WIG-to-BigWig tool (`…/ucsc_wigtobigwig/482+galaxy0`) for both ATAC-seq and CUT&RUN items.
  - Query hygiene: Rewrote 6 CUT&RUN-side queries to reduce very high similarity with the corresponding ATAC-seq items while preserving intent/tool focus (grep/peak calling/fragment-length QC/BigWig conversion/deepTools heatmap).
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan shows no exact duplicates and only a small number of acceptable cross-tutorial near-duplicates remaining.

## GTX0038 (ground-truth fix + expansion; lines 2129-2328)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on replacing missing gold tools with usegalaxy-present, semantically/IO-compatible alternatives when available.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate replacements (e.g., `chipseeker` for peak annotation, `gprofiler_convert` for ID conversion, `gprofiler_gost` for GO enrichment) using helptext + IO fields.
- Changes:
  - Replaced 12 missing KPBIOTEAM R-wrapper tools with usegalaxy-present equivalents: peak annotation → `toolshed.g2.bx.psu.edu/repos/rnateam/chipseeker/chipseeker/1.28.3+galaxy0`, gene ID conversion → `toolshed.g2.bx.psu.edu/repos/iuc/gprofiler_convert/gprofiler_convert/0.1.7+galaxy11`, GO enrichment → `toolshed.g2.bx.psu.edu/repos/iuc/gprofiler_gost/gprofiler_gost/0.1.7+galaxy11`.
  - Deleted 4 methylation-array EWAS items whose gold tool (`minfi_analysis/2.1.0`) is not present in the usegalaxy.org catalog snapshot and had no clearly equivalent in-catalog replacement.
  - Query hygiene: Rewrote 2 queries to remove “clusterProfiler-style” phrasing after swapping to g:Profiler-based tools (intent unchanged).
- Validation: check_v1_items passes for the kept items in this batch (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after the rewrites.

## GTX0039 (ground-truth fix + expansion; lines 2325-2524)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on ground-truth integrity (tool must exist on the usegalaxy.org snapshot) and query diversity.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during replacement decisions (e.g., verified the UCSC WIG→BigWig tool entry and its expected IO via helptext + `input_params_flat`/`outputs_raw`).
- Changes:
  - Ground-truth cleanup: For 4 methylation-seq track-conversion items, removed the missing `wig_to_bigWig` ID and kept the usegalaxy-present `…/ucsc_wigtobigwig/482+galaxy0` tool as the sole gold tool (also removed now-unneeded `ground_truth_alternatives*` metadata on those items).
  - Deleted 4 “cluster from distance matrix” items whose gold tool (`…/clustering_from_distmat/1.1.1`) is not present in the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent replacement in-catalog.
  - Query hygiene: Rewrote 1 grep-style query to reduce near-duplicate phrasing within this tutorial range while preserving intent.
- Validation: check_v1_items passes for the kept items in this batch (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after the rewrite.

## GTX0040 (ground-truth fix + expansion; lines 2521-2720)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on replacing/removing gold tools that are missing from the usegalaxy.org catalog snapshot.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate replacements (e.g., confirmed `roary` pangenome IO/semantics and the tabular `tp_sort_header_tool`/`tp_uniq_tool` behavior via helptext + IO fields).
- Changes:
  - Deleted 26 items whose gold tools are not present on the usegalaxy.org snapshot and for which no clearly semantically/IO-equivalent replacement was available in-catalog (Apollo account/organism management + iframe helpers; PPanGGOLiN MSA helper).
  - Ground-truth cleanup: Dropped missing tool IDs that were previously listed as alternatives and kept the usegalaxy-present equivalents as the sole gold tool (FASTA stats + table sorting cases), removing now-unneeded `ground_truth_alternatives*` metadata.
  - Replaced 8 missing gold tools with usegalaxy-present equivalents where the intent remained satisfied:
    - FASTA summary statistics → `toolshed.g2.bx.psu.edu/repos/iuc/fasta_stats/fasta-stats/2.0`
    - Sort tabular rows → `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3`
    - Deduplicate lines → `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_uniq_tool/9.5+galaxy3`
    - Pangenome (presence/absence matrix) → `toolshed.g2.bx.psu.edu/repos/iuc/roary/roary/3.13.0+galaxy3`
- Validation: check_v1_items passes for the kept items in this batch (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0041 (ground-truth fix + expansion; lines 2695-2894)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on replacing missing gold tools with usegalaxy-present, semantically/IO-compatible equivalents when available.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate the BRAKER3 tool replacement via helptext + IO fields.
- Changes:
  - Replaced 8 missing BRAKER3 tool IDs (`toolshed.g2.bx.psu.edu/repos/iuc/braker3/braker3/3.0.8+galaxy0`) with the usegalaxy-present equivalent (`toolshed.g2.bx.psu.edu/repos/genouest/braker3/braker3/3.0.8+galaxy2`).
  - Deleted 2 PPanGGOLiN MSA items whose gold tool is not present in the usegalaxy.org catalog snapshot and had no clearly equivalent in-catalog replacement.
- Validation: check_v1_items passes for the kept items in this batch (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0042 (ground-truth fix + expansion; lines 2893-3092)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on fixing invalid/missing tool IDs and swapping to usegalaxy-present, semantically/IO-compatible equivalents where available.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate replacements (BLAST+, k-mer histogram, RepeatMasker wrapper, GenBank→GFF3 conversion, Bowtie2) using helptext + IO fields.
- Changes:
  - Fixed 4 items that had a non-existent/typo tool ID (`toolshed.g2.bx.psu.edu/view/...`) by keeping only the correct catalog-present tool (`toolshed.g2.bx.psu.edu/repos/iuc/jcvi_gff_stats/jcvi_gff_stats/0.8.4`) and removing now-unneeded `ground_truth_alternatives*` metadata.
  - Replaced 20 missing tools with usegalaxy-present equivalents where the intent remained satisfied:
    - Parallel similarity search → `toolshed.g2.bx.psu.edu/repos/devteam/ncbi_blast_plus/ncbi_blastp_wrapper/2.16.0+galaxy0` (rewrote 4 queries to be explicitly BLASTP/protein).
    - K-mer spectrum/histogram → `toolshed.g2.bx.psu.edu/repos/iuc/khmer_abundance_distribution_single/khmer_abundance_distribution_single/3.0.0a3+galaxy3` (rewrote 4 queries accordingly).
    - Repeat masking → `toolshed.g2.bx.psu.edu/repos/bgruening/repeat_masker/repeatmasker_wrapper/4.1.5+galaxy0`
    - GenBank → GFF3 → `toolshed.g2.bx.psu.edu/repos/iuc/bp_genbank2gff3/bp_genbank2gff3/1.1`
    - Short-read alignment → `toolshed.g2.bx.psu.edu/repos/devteam/bowtie2/bowtie2/2.5.4+galaxy0`
    - ZIP extraction → `CONVERTER_archive_to_directory`
  - Deleted 4 imaging items whose gold tool for downloading IDR images by IDs (`idr_download_by_ids/0.45`) is not present in the usegalaxy.org catalog snapshot and had no clearly equivalent in-catalog replacement.
- Validation: check_v1_items passes for the kept items in this batch (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after the rewrites.

## GTX0043 (ground-truth fix + expansion; lines 3089-3288)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on usegalaxy catalog presence for imaging tools (many imaging tool IDs in this slice were not present in the snapshot).
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to verify which imaging tools/versions are present on the snapshot and to validate the few safe substitutions (archive extraction + bfconvert version bump).
- Changes:
  - Deleted 66 items whose gold imaging tools are not present on the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent replacement in-catalog (QuPath interactive, Palom, CellProfiler module wrappers, several imgteam image-info/feature-extraction helpers, GraphicsMagick convert, etc.).
  - Replaced 14 missing unzip tool IDs (`imgteam/unzip`) with `CONVERTER_archive_to_directory` (archive extraction intent preserved).
  - Updated 1 bfconvert tool version to a usegalaxy-present build (`ip_convertimage/6.7.0+galaxy3`).
  - Query hygiene: Rewrote 3 imaging-introduction queries to reduce very high cross-tutorial near-duplication while preserving intent/tool focus.
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 134 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after rewrites.

## GTX0044 (ground-truth fix + expansion; lines 3223-3422)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on usegalaxy catalog presence for imaging/CellProfiler-related tools.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate representative kept tools (e.g., verified `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.6` via helptext + `input_params_flat`/`outputs_raw`) and to confirm many imaging tool IDs in this slice are absent from the snapshot.
- Changes:
  - Deleted 158 items whose gold tools are not present in the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent replacement in-catalog (primarily CellProfiler module wrappers, OMERO bridge tools, image-math/splitting helpers, and other imgteam tools not installed on this snapshot).
  - No ground-truth alternatives were added in this batch (strict “don’t add if unclear” rule).
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 42 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0045 (ground-truth fix + expansion; lines 3265-3464)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on (1) removing items whose gold tools are missing from the usegalaxy.org snapshot and (2) fixing exact duplicate queries for the same core tools.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate representative kept tools and their IO (e.g., confirmed `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1` via helptext + `input_params_flat`/`outputs_raw`), and used the catalog index to confirm missing imaging tools are not installed in this snapshot.
- Changes:
  - Deleted 40 imaging/ML items whose gold tools are not present on the usegalaxy.org catalog snapshot and had no clearly equivalent in-catalog replacement (voronoi helpers, feature extraction, image metadata tool, GraphicsMagick convert, AnyLabeling + YOLO training helpers, etc.).
  - Replaced 8 missing `imgteam/unzip` items with `CONVERTER_archive_to_directory` (archive extraction intent preserved).
  - Query hygiene: Rewrote 22 queries to eliminate a set of exact duplicates and reduce very high near-duplication within the “data manipulation olympics” slice while preserving intent/tool focus (Count1/Cut1/join1/Remove beginning1/cat1/Show beginning1/Add_a_column1/regexColumn1).
- Validation: check_v1_items passes for the kept items in this batch (after deletions: 160 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after the rewrites.

## GTX0046 (ground-truth fix + expansion; lines 3425-3624)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on query hygiene (avoid near-duplicates) and ground-truth integrity for tools present on the usegalaxy.org snapshot.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` during review to sanity-check tool semantics/IO for representative tools in this range (e.g., verified `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0` via helptext + `input_params_flat`/`outputs_raw`).
- Changes:
  - No gold tool replacements, deletions, or alternative additions were needed in this batch (all referenced tools were present in the usegalaxy.org catalog snapshot).
  - Query hygiene: Rewrote 1 `tp_sort_header_tool` query (`introduction-galaxy-intro-peaks2genes-q035`) to reduce a high-similarity cross-tutorial near-duplicate while preserving intent.
- Validation: check_v1_items passes for this range (WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after the rewrite.

## GTX0047 (ground-truth fix + expansion; lines 3625-3824)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on removing missing gold tools (usegalaxy snapshot) while keeping only clearly in-catalog equivalents.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate the MatchMS replacement decision (confirmed `toolshed.g2.bx.psu.edu/repos/recetox/matchms/matchms/0.17.0+galaxy0` exposes similarity-metric choices and produces a similarity output via helptext + IO fields).
- Changes:
  - Deleted 32 items whose gold tools are not present in the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent replacement in-catalog (muon-spectroscopy project tools; metabolomics batch correction / QC metrics / generic filtering / HMDB WSDL search tools).
  - Ground-truth cleanup: For 4 metabolomics items that listed `matchms_similarity` plus `matchms`, dropped the missing `matchms_similarity` tool and kept `matchms` as the sole gold tool (updated `metadata.tool_focus` accordingly and removed now-unneeded multi-tool metadata).
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 168 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0048 (ground-truth fix + expansion; lines 3793-3992)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on metabolomics LC-MS / MSI / mfassignr items and enforcing usegalaxy snapshot presence for every gold tool ID.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` to validate a representative kept substitution/correction (confirmed `toolshed.g2.bx.psu.edu/repos/recetox/mfassignr_kmdnoise/mfassignr_kmdnoise/1.1.2+galaxy0` semantics and IO via helptext + `input_params_flat`/`outputs_raw`) and used the catalog index to confirm a large set of MSI/Cardinal/MALDIquant-related tool IDs are absent from the snapshot.
- Changes:
  - Deleted 72 items whose gold tools are not present in the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent replacement in-catalog (generic metabolomics filtering/QC/batch-correction tools; Cardinal MSI suite; MALDIquant tools; fuzzy-join helper).
  - Fixed 4 metabolomics mfassignr items where the stored gold tool ID was a mismatched repo/tool_id path (replaced with the installed, in-catalog `mfassignr_kmdnoise` tool ID; intent preserved).
  - Query hygiene: Rewrote 2 Filter1 tool-first queries to eliminate exact duplicates within this slice while preserving the same row-filtering intent/tool focus.
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 128 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after rewrites.

## GTX0049 (ground-truth fix + expansion; lines 3921-4120)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on pruning missing gold tools (usegalaxy snapshot) and reducing cross-slice near-duplicates for the same tool focus.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` + the catalog index during review to confirm the missing tool IDs in this slice are absent from the snapshot (no helptext/IO entry to validate) and to validate representative kept tools/IO where needed.
- Changes:
  - Deleted 6 items whose gold tools are not present in the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent single-tool replacement in-catalog (xtb molecular optimization; Lotus2 end-to-end ITS2 pipeline).
  - Query hygiene: Rewrote 2 `fasta_merge_files_and_filter_unique_sequences` queries to eliminate a high-similarity near-duplicate pair across slices while preserving the same “merge FASTA + deduplicate” intent/tool focus.
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 194 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates after rewrites.

## GTX0050 (ground-truth fix + expansion; lines 4115-4314)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on pruning remaining missing gold tools (usegalaxy snapshot) and ensuring the slice stays checker-clean.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` + the catalog index to confirm the remaining Lotus2 tool IDs in this slice are absent from the usegalaxy.org snapshot (no helptext/IO entry available to validate; no clear single-tool equivalent in-catalog).
- Changes:
  - Deleted 2 items whose gold tool (`toolshed.g2.bx.psu.edu/repos/earlhaminst/lotus2/lotus2/2.32+galaxy0`) is not present in the usegalaxy.org catalog snapshot and had no clearly equivalent replacement in-catalog.
  - No other gold expansions/replacements were needed in this batch.
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 198 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0051 (ground-truth fix + expansion; lines 4313-4512)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on (1) removing items whose gold tools are absent from the usegalaxy.org snapshot and (2) salvaging any items that already had a valid in-catalog alternative.
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` + the catalog index to (a) confirm the OpenSwath / DiaPASEF / ProteoRE / BioconductorSCP tool IDs in this slice are absent from the snapshot, and (b) validate the kept Venn-diagram alternative (`toolshed.g2.bx.psu.edu/repos/peterjc/venn_list/venn_list/0.1.1`) via helptext + IO fields.
- Changes:
  - Deleted 48 items whose gold tools are not present in the usegalaxy.org catalog snapshot and had no clearly semantically/IO-equivalent single-tool replacement in-catalog (OpenSwath DIA tooling, DiaPASEF, BioconductorSCP, and multiple ProteoRE data-retrieval/ID-mapping helpers).
  - Ground-truth cleanup: For 4 proteomics biomarker-selection items that already included `venn_list` as an alternative alongside a missing `Jvenn` tool ID, dropped the missing `Jvenn` tool, kept `venn_list` as the sole gold tool, updated `metadata.tool_focus`, and removed now-unneeded multi-tool metadata.
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 152 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.

## GTX0052 (ground-truth fix + expansion; lines 4465-4664)

- Date: 2026-02-05
- Scope: Manual per-item review for 200 items, focusing on removing remaining MSI-imaging items whose gold tools are not present in the usegalaxy.org snapshot (and avoiding non-stable placeholder tool IDs).
- Review note: Consulted `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` + the catalog index to confirm MSI/Cardinal tools are absent from this snapshot and that the placeholder `MSI mz images` tool ID is not resolvable to an installed tool entry.
- Changes:
  - Deleted 8 MSI imaging items whose gold tools were missing/unresolvable on the usegalaxy.org catalog snapshot (Cardinal MSI QC report + “MSI mz images” placeholder entries); no clearly equivalent single-tool replacement was available in-catalog.
  - No other gold expansions/replacements were needed in this batch.
- Validation: check_v1_items passes for the kept items reviewed in this batch (after deletions: 192 items kept from this slice; WARN-only for core/internal ids); smell scan reports no hits/duplicates/near-duplicates.
