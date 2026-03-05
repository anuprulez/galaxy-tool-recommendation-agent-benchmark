# Galaxy Tool Recommendation Benchmark (v2 shortlist)

## Difficulty distribution
- **L1**: 13 queries
- **L2**: 12 queries
- **L3**: 9 queries
- **L4**: 1 query

## Summary
- Total items in this doc: 35
- Recent-tutorial items: 35
- Multi-tool gold labels: 20
- Unique tools in shortlist: 74
- Covered topics: 11

## Difficulty levels
- **L1**: Basic table/text manipulation (no domain knowledge required)
- **L2**: Common bioinformatics tasks (QC, trimming, mapping, visualization)
- **L3**: Specialized analysis tools (ML, metabolomics, proteomics, etc.)
- **L4**: Complex or multi-tool analytical tasks

## Items

### I. Machine Learning & Statistics (GLEAM/AutoML)

1. **statistics-loris_model-q011**
   - Topic: statistics
   - Tutorial: Building the LORIS LLR6 PanCancer Model Using PyCaret (`topics/statistics/tutorials/loris_model`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/loris_model/tutorial.html
   - Recording date: 2025-05-07
   - Difficulty: **L3**
   - Query: I want to benchmark multiple tabular predictors on my clinical dataset and automatically generate a leaderboard of model performance. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
   - Gold tool(s) (name / id): Tabular Learner (`tabular_learner`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

2. **statistics-machinelearning-q011**
   - Topic: statistics
   - Tutorial: Basics of machine learning (`topics/statistics/tutorials/machinelearning`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/machinelearning/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I need to train an SVM classifier on a labeled feature matrix and then apply the trained model to predict labels for a test dataset. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0
   - Gold tool(s) (name / id): Support Vector Machine (SVM) (`sklearn_svm_classifier`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): Tabular Learner (`tabular_learner`)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

3. **statistics-flexynesis_unsupervised-q014**
   - Topic: statistics
   - Tutorial: Unsupervised Analysis of Bone Marrow Cells with Flexynesis (`topics/statistics/tutorials/flexynesis_unsupervised`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/flexynesis_unsupervised/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: I have an embedding/latent-space representation of my samples and want to explore it interactively in R (e.g., adjusting UMAP parameters or clustering visualization). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0
   - Gold tool(s) (name / id): Interactive RStudio (Bioconductor) (`interactive_tool_rstudio_bioconductor`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

4. **manual-statistics-image-learner-q001**
   - Topic: statistics
   - Tutorial: GLEAM Image Learner - Validating Skin Lesion Classification on HAM10000 (`topics/statistics/tutorials/image_learner`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/image_learner/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: I have a collection of labeled images and want to train a deep-learning classifier to predict phenotypes. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/image_learner/image_learner/0.1.5
   - Gold tool(s) (name / id): Image Learner (`image_learner`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)
   - Source: data/benchmark/stats_learner_additions.jsonl

5. **manual-statistics-image-learner-q004**
   - Topic: statistics
   - Tutorial: GLEAM Image Learner - Validating Skin Lesion Classification on HAM10000 (`topics/statistics/tutorials/image_learner`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/image_learner/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: I want to fine-tune a pretrained vision model on my labeled image dataset using transfer learning. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/image_learner/image_learner/0.1.5
   - Gold tool(s) (name / id): Image Learner (`image_learner`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)
   - Source: data/benchmark/stats_learner_additions.jsonl

6. **manual-statistics-multimodal-learner-q001**
   - Topic: statistics
   - Tutorial: Gleam Multimodal Learner - Head and Neck cancer Recurrence Prediction with HANCOCK (`topics/statistics/tutorials/multimodal_learner`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/multimodal_learner/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: My dataset contains multiple modalities (structured tabular features plus text data). Which Galaxy tool can train a single model that uses both modalities together?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/multimodal_learner/multimodal_learner/0.1.5
   - Gold tool(s) (name / id): Multimodal Learner (`multimodal_learner`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)
   - Source: data/benchmark/stats_learner_additions.jsonl

### II. Data Manipulation & Cleaning

7. **introduction-data-manipulation-olympics-q154**
   - Topic: introduction
   - Tutorial: Data Manipulation Olympics (`topics/introduction/tutorials/data-manipulation-olympics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/introduction/tutorials/data-manipulation-olympics/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: My delimited file contains many columns, but I only need a few specific ones (for example the 3rd and 7th). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2, Cut1
   - Gold tool(s) (name / id): Advanced Cut (`tp_cut_tool`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

8. **introduction-data-manipulation-olympics-q074**
   - Topic: introduction
   - Tutorial: Data Manipulation Olympics (`topics/introduction/tutorials/data-manipulation-olympics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/introduction/tutorials/data-manipulation-olympics/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I have several text files produced from different runs and want to combine them into one single dataset. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/9.5+galaxy2, cat1
   - Gold tool(s) (name / id): Concatenate datasets (`tp_cat`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

9. **single-cell-scrna-data-ingest-q020**
   - Topic: single-cell
   - Tutorial: Converting between common single cell data formats (`topics/single-cell/tutorials/scrna-data-ingest`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scrna-data-ingest/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: My cell barcode column contains values like “AAACCTGAG-1”. I need to remove the trailing suffix (such as “-1”) from that column before merging tables. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regexColumn1/1.0.3
   - Gold tool(s) (name / id): Regex Find And Replace (in a column) (`regexColumn1`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

10. **statistics-flexynesis_survival-q013**
   - Topic: statistics
   - Tutorial: Identifing Survival Markers of Brain tumor with Flexynesis (`topics/statistics/tutorials/flexynesis_survival`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I need to compute grouped statistics (such as mean or maximum values) for rows sharing the same Gene ID in a large table. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0
   - Gold tool(s) (name / id): Datamash (`datamash_ops`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

11. **single-cell-EBI-retrieval-q014**
   - Topic: single-cell
   - Tutorial: Importing files from public atlases (`topics/single-cell/tutorials/EBI-retrieval`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/EBI-retrieval/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I have a very large tabular dataset and only want to keep rows containing specific gene symbols such as TP53 or BRCA1. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_grep_tool/9.5+galaxy2
   - Gold tool(s) (name / id): Search in text files (grep) (`tp_grep_tool`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

12. **genome-annotation-tnseq-q046**
   - Topic: genome-annotation
   - Tutorial: Essential genes detection with Transposon insertion sequencing (`topics/genome-annotation/tutorials/tnseq`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/tnseq/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I need to sort a TSV file by a numeric score column while keeping the column header unchanged at the top. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2
   - Gold tool(s) (name / id): Sort (with header) (`tp_sort_header_tool`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

13. **introduction-galaxy-reproduce-q038**
   - Topic: introduction
   - Tutorial: How to reproduce published Galaxy analyses (`topics/introduction/tutorials/galaxy-reproduce`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-reproduce/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: After merging several lists of gene IDs I now have many duplicates. Which Galaxy tool should I use to keep only unique entries?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sorted_uniq/9.5+galaxy2
   - Gold tool(s) (name / id): Unique lines (`tp_sorted_uniq`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

14. **imaging-parameter-tuning-q014**
   - Topic: imaging
   - Tutorial: Parameter tuning and optimization - Evaluating nuclei segmentation with Galaxy (`topics/imaging/tutorials/parameter-tuning`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/parameter-tuning/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I need to split one large table into separate datasets based on values in a column (for example Batch ID). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.6
   - Gold tool(s) (name / id): Split file on a column (`tp_split_on_column`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

### III. Genomics, Transcriptomics & Mapping (QC to Mapping)

15. **single-cell-scatac-preprocessing-tenx-q012**
   - Topic: single-cell
   - Tutorial: Pre-processing of 10X Single-Cell ATAC-seq Datasets (`topics/single-cell/tutorials/scatac-preprocessing-tenx`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scatac-preprocessing-tenx/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I just obtained raw FASTQ reads from a sequencing experiment and want a standard quality-control report summarizing base quality and other metrics. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1
   - Gold tool(s) (name / id): FastQC (`fastqc`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): Falco (`falco`)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): fastp (`fastp`)
   - Notes: fastp performs QC + trimming rather than pure QC; use it only if trimming is acceptable for your workflow.
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

16. **microbiome-nanopore-16S-metagenomics-q018**
   - Topic: microbiome
   - Tutorial: 16S Microbial analysis with Nanopore data (`topics/microbiome/tutorials/nanopore-16S-metagenomics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/microbiome/tutorials/nanopore-16S-metagenomics/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I ran QC on many sequencing samples and want to combine all QC reports into a single summary dashboard. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.33+galaxy0
   - Gold tool(s) (name / id): MultiQC (`multiqc`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

17. **microbiome-nanopore-16S-metagenomics-q026**
   - Topic: microbiome
   - Tutorial: 16S Microbial analysis with Nanopore data (`topics/microbiome/tutorials/nanopore-16S-metagenomics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/microbiome/tutorials/nanopore-16S-metagenomics/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I want to remove sequencing adapters and filter reads by quality in a single step while also producing a summary report. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1+galaxy3
   - Gold tool(s) (name / id): fastp (`fastp`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

18. **genome-annotation-tnseq-q034**
   - Topic: genome-annotation
   - Tutorial: Essential genes detection with Transposon insertion sequencing (`topics/genome-annotation/tutorials/tnseq`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/tnseq/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I have short-read DNA sequencing data and a reference genome and want to align the reads efficiently. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/bowtie2/bowtie2/2.5.4+galaxy0
   - Gold tool(s) (name / id): Bowtie2 (`bowtie2`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): Map with BWA-MEM (`bwa_mem`)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

19. **single-cell-scatac-standard-processing-snapatac2-q012**
   - Topic: single-cell
   - Tutorial: Single-cell ATAC-seq standard processing with SnapATAC2 (`topics/single-cell/tutorials/scatac-standard-processing-snapatac2`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scatac-standard-processing-snapatac2/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I need to align single-cell ATAC-seq reads to a large reference genome such as human. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/bwa/bwa_mem/0.7.19
   - Gold tool(s) (name / id): Map with BWA-MEM (`bwa_mem`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): Bowtie2 (`bowtie2`)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

20. **transcriptomics-full-de-novo-q019**
   - Topic: transcriptomics
   - Tutorial: De novo transcriptome assembly, annotation, and differential expression analysis (`topics/transcriptomics/tutorials/full-de-novo`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/full-de-novo/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I completed a de novo transcriptome assembly and want to evaluate its completeness using conserved single-copy orthologs. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/busco/busco/5.8.0+galaxy2
   - Gold tool(s) (name / id): BUSCO (`busco`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

21. **sequence-analysis-ncbi-blast-against-the-madland-q026**
   - Topic: sequence-analysis
   - Tutorial: NCBI BLAST+ against the MAdLand (`topics/sequence-analysis/tutorials/ncbi-blast-against-the-madland`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/ncbi-blast-against-the-madland/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I have thousands of protein sequences and need a fast alignment tool for large-scale similarity searches. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/diamond/bg_diamond/2.1.16+galaxy0
   - Gold tool(s) (name / id): DIAMOND (`bg_diamond`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): NCBI BLAST+ (suite) (`ncbi_blast_plus`)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

22. **transcriptomics-rna-seq-reads-to-counts-q013**
   - Topic: transcriptomics
   - Tutorial: 1: RNA-Seq reads to counts (`topics/transcriptomics/tutorials/rna-seq-reads-to-counts`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/rna-seq-reads-to-counts/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: My RNA-seq reads contain adapter sequences that must be removed before alignment. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lparsons/cutadapt/cutadapt/5.2+galaxy0
   - Gold tool(s) (name / id): Cutadapt (`cutadapt`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): fastp (`fastp`)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

23. **sequence-analysis-sars-with-galaxy-on-anvil-q026**
   - Topic: sequence-analysis
   - Tutorial: SARS-CoV-2 Viral Sample Alignment and Variant Visualization (`topics/sequence-analysis/tutorials/sars-with-galaxy-on-anvil`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/sars-with-galaxy-on-anvil/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I want to visually inspect read alignments and genomic annotations interactively in a genome browser. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/jbrowse/jbrowse/1.16.11+galaxy1
   - Gold tool(s) (name / id): JBrowse (`jbrowse`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

### IV. Proteomics, Metabolomics & Chemistry

24. **proteomics-maxquant-label-free-q022**
   - Topic: proteomics
   - Tutorial: Label-free data analysis using MaxQuant (`topics/proteomics/tutorials/maxquant-label-free`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/proteomics/tutorials/maxquant-label-free/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: I have mass spectrometry data and need to perform label-free protein quantification. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/2.0.3.0+galaxy0
   - Gold tool(s) (name / id): MaxQuant (`maxquant`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

25. **metabolomics-lcms-q052**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: LC-MS analysis (`topics/metabolomics/tutorials/lcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/lcms/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: I detected features in several LC-MS runs and need to merge them into a single dataset for comparison. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lecorguille/xcms_merge/xcms_merge/3.12.0+galaxy3
   - Gold tool(s) (name / id): XCMS merge (`xcms_merge`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

26. **metabolomics-gcms-q038**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: GC-MS analysis with the metaMS package (`topics/metabolomics/tutorials/gcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/gcms/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: I have missing peaks in my metabolomics feature table and want to recover them from the raw data. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lecorguille/xcms_fillpeaks/abims_xcms_fillPeaks/3.12.0+galaxy3
   - Gold tool(s) (name / id): XCMS fillPeaks (`abims_xcms_fillPeaks`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

27. **metabolomics-qcxms-predictions-q026**
   - Topic: metabolomics
   - Tutorial: Predicting EI+ mass spectra with QCxMS (`topics/metabolomics/tutorials/qcxms-predictions`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/qcxms-predictions/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I need to convert molecular structure files between chemistry formats (for example SDF to MOL2). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/openbabel_compound_convert/openbabel_compound_convert/3.1.1+galaxy1
   - Gold tool(s) (name / id): OpenBabel compound convert (`openbabel_compound_convert`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

28. **metabolomics-gc_ms_with_xcms-q066**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: GC-MS data processing (with XCMS, RAMClustR, RIAssigner, and matchms) (`topics/metabolomics/tutorials/gc_ms_with_xcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/gc_ms_with_xcms/tutorial.html
   - Recording date: N/A
   - Difficulty: **L3**
   - Query: My metabolomics dataset has batch effects and I want to apply an ICA-based correction method. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/recetox/waveica/waveica/0.2.0+galaxy9
   - Gold tool(s) (name / id): WaveICA (`waveica`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

29. **computational-chemistry-analysis-md-simulations-q053**
   - Topic: computational-chemistry
   - Tutorial: Analysis of molecular dynamics simulations (`topics/computational-chemistry/tutorials/analysis-md-simulations`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/computational-chemistry/tutorials/analysis-md-simulations/tutorial.html
   - Recording date: N/A
   - Difficulty: **L4**
   - Query: I finished a molecular dynamics simulation and want to compute trajectory analyses such as RMSD, RMSF, and PCA. Which Galaxy tools should I use?
   - Gold tools(all of them): toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_pca/bio3d_pca/2.3.4, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_rdf/mdanalysis_rdf/0.19, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_cosine_analysis/mdanalysis_cosine_analysis/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_ramachandran_plot/mdanalysis_ramachandran_plot/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_distance/mdanalysis_distance/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_dihedral/mdanalysis_dihedral/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_rmsd/bio3d_rmsd/2.3.4, toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_rmsf/bio3d_rmsf/2.3.4
   - Gold tool(s) (name / id): Bio3D RMSD (`bio3d_rmsd`); Bio3D RMSF (`bio3d_rmsf`); Bio3D PCA (`bio3d_pca`); MDAnalysis: RDF (`mdanalysis_rdf`); MDAnalysis: Cosine analysis (`mdanalysis_cosine_analysis`); MDAnalysis: Ramachandran plot (`mdanalysis_ramachandran_plot`); MDAnalysis: Distance (`mdanalysis_distance`); MDAnalysis: Dihedral (`mdanalysis_dihedral`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

### V. Imaging & Specialized Tasks

30. **imaging-voronoi-segmentation-q034**
   - Topic: imaging
   - Tutorial: Voronoi segmentation (`topics/imaging/tutorials/voronoi-segmentation`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/voronoi-segmentation/tutorial.html
   - Recording date: N/A
   - Difficulty: **L2**
   - Query: I have grayscale microscopy images and want to automatically convert them into binary masks using an automatic threshold method. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0
   - Gold tool(s) (name / id): Threshold (`ip_threshold`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

31. **imaging-parameter-tuning-q038**
   - Topic: imaging
   - Tutorial: Parameter tuning and optimization - Evaluating nuclei segmentation with Galaxy (`topics/imaging/tutorials/parameter-tuning`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/parameter-tuning/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I have a dataset collection and need to collapse it into a single dataset. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/5.1.0
   - Gold tool(s) (name / id): Collapse Collection (`collapse_dataset`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

32. **transcriptomics-rna-seq-genes-to-pathways-q014**
   - Topic: transcriptomics
   - Tutorial: 3: RNA-seq genes to pathways (`topics/transcriptomics/tutorials/rna-seq-genes-to-pathways`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/rna-seq-genes-to-pathways/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I need to add a new column to a table using a calculation based on existing columns. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1
   - Gold tool(s) (name / id): Column maker (`Add_a_column1`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

33. **single-cell-bulk-music-3-preparebulk-q012**
   - Topic: single-cell
   - Tutorial: Bulk matrix to ESet | Creating the bulk RNA-seq dataset for deconvolution (`topics/single-cell/tutorials/bulk-music-3-preparebulk`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/bulk-music-3-preparebulk/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I need to standardize identifiers across an entire text file by transforming each line in a consistent way (for example removing a suffix). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regex1/1.0.3
   - Gold tool(s) (name / id): Regex Find And Replace (`regex1`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

34. **transcriptomics-small_ncrna_clustering-q013**
   - Topic: transcriptomics
   - Tutorial: Small Non-coding RNA Clustering using BlockClust (`topics/transcriptomics/tutorials/small_ncrna_clustering`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/small_ncrna_clustering/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: I want to sort rows in a tabular dataset by a score column while keeping the column header fixed at the top. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3
   - Gold tool(s) (name / id): Sort (with header) (`tp_sort_header_tool`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

35. **single-cell-EBI-retrieval-q013**
   - Topic: single-cell
   - Tutorial: Importing files from public atlases (`topics/single-cell/tutorials/EBI-retrieval`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/EBI-retrieval/tutorial.html
   - Recording date: N/A
   - Difficulty: **L1**
   - Query: My metadata table contains inconsistent labels and I want to standardize them by replacing certain strings across the dataset. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_find_and_replace/9.5+galaxy2
   - Gold tool(s) (name / id): Find and replace (`tp_find_and_replace`)
   - Valid alternative tools (name / id; verified on usegalaxy.org): (none)
   - Candidate alternatives (name / id; present on usegalaxy.org, not necessarily equivalent): (none)
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

## Benchmark summary
- Items: **35**
- Difficulty distribution: **L1=13**, **L2=12**, **L3=9**, **L4=1**
