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
    - `Remove_beginning1` → `Remove beginning1` (clinical MP discovery/verification rows in this batch)
  - Added snapshot-installed alternate versions to `tools[]` (and recorded a manual note) for common steps, including:
    - `filter_tabular`, `query_tabular`, `msconvert`, `maxquant`, `unipept`

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
