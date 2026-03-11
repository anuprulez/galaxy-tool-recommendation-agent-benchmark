# v1 shortlist (manual review set)

- Generated: 2026-03-05
- Purpose: Shortlist 62 queries for manual review of tool recommendation **accuracy** (does the tool solve the query?) and **completeness** (are there better/alternative tools?), including 50 selected from `v1_items.jsonl` and 12 manually added.

## Selection criteria (heuristics)
- Prefer newer GTN tutorials (recency mode: `effective`): select items from tutorials with a recency date >= 2024-01-01 (recency date = latest recordings.date if present, else GTN git last-modified date for tutorial.md, else filesystem modified date)
- Prefer popular tools: seed selection by covering top-N Toolshed tools by frequency in `v1_items.jsonl`
- Diversity caps: max 2 items / tutorial, max 6 items / topic

## Summary
- Selected (v1) items: 50
- Manually added items: 12
- Total items in this doc: 62
- Recent-tutorial items: 62
- Multi-tool gold labels: 38
- Unique tools in shortlist: 75
- Covered topics: 13

## Items

1. **statistics-loris_model-q011**
   - Topic: statistics
   - Tutorial: Building the LORIS LLR6 PanCancer Model Using PyCaret (`topics/statistics/tutorials/loris_model`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/loris_model/tutorial.html
   - Recording date: 2025-05-07
   - Query: I have a machine learning dataset where you want to train and evaluate a predictive model. I need to benchmark a few tabular predictors quickly and pick the top performer. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

2. **statistics-machinelearning-q011**
   - Topic: statistics
   - Tutorial: Basics of machine learning (`topics/statistics/tutorials/machinelearning`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/machinelearning/tutorial.html
   - Recording date: N/A
   - Query: I have a labeled tabular dataset (feature matrix with a target/label column) and want to train an SVM classifier in Galaxy. I also want to use the trained model to predict class labels for a held-out test set. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4&version=0.1.4

3. **statistics-flexynesis_unsupervised-q014**
   - Topic: statistics
   - Tutorial: Unsupervised Analysis of Bone Marrow Cells with Flexynesis (`topics/statistics/tutorials/flexynesis_unsupervised`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/flexynesis_unsupervised/tutorial.html
   - Recording date: N/A
   - Query: I have an embedding or latent-space output and want to make exploratory plots (UMAP and cluster plots) in R and tweak plotting options interactively. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

4. **single-cell-scatac-preprocessing-tenx-q012**
   - Topic: single-cell
   - Tutorial: Pre-processing of 10X Single-Cell ATAC-seq Datasets (`topics/single-cell/tutorials/scatac-preprocessing-tenx`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scatac-preprocessing-tenx/tutorial.html
   - Recording date: N/A
   - Query: I have raw single-cell ATAC FASTQ reads and want a QC report for base quality and adapter content. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

5. **introduction-data-manipulation-olympics-q154**
   - Topic: introduction
   - Tutorial: Data Manipulation Olympics (`topics/introduction/tutorials/data-manipulation-olympics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/introduction/tutorials/data-manipulation-olympics/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to cut out selected fields from a delimited file when columns are not strictly tabular?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2, Cut1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5%2Bgalaxy3&version=9.5%2Bgalaxy3

6. **introduction-data-manipulation-olympics-q074**
   - Topic: introduction
   - Tutorial: Data Manipulation Olympics (`topics/introduction/tutorials/data-manipulation-olympics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/introduction/tutorials/data-manipulation-olympics/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to combine several text files into a single dataset by simple concatenation?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/9.5+galaxy2, cat1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/9.5%2Bgalaxy3&version=9.5%2Bgalaxy3

7. **microbiome-nanopore-16S-metagenomics-q018**
   - Topic: microbiome
   - Tutorial: 16S Microbial analysis with Nanopore data (`topics/microbiome/tutorials/nanopore-16S-metagenomics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/microbiome/tutorials/nanopore-16S-metagenomics/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool generates a combined QC report from a set of individual QC outputs?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.33+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

8. **sequence-analysis-sars-with-galaxy-on-anvil-q026**
   - Topic: sequence-analysis
   - Tutorial: SARS-CoV-2 Viral Sample Alignment and Variant Visualization (`topics/sequence-analysis/tutorials/sars-with-galaxy-on-anvil`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/sars-with-galaxy-on-anvil/tutorial.html
   - Recording date: N/A
   - Query: What Galaxy tool should I use to explore alignments and annotations in an interactive genome viewer?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/jbrowse/jbrowse/1.16.11+galaxy1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

9. **imaging-parameter-tuning-q038**
   - Topic: imaging
   - Tutorial: Parameter tuning and optimization - Evaluating nuclei segmentation with Galaxy (`topics/imaging/tutorials/parameter-tuning`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/parameter-tuning/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to collapse a collection into a single dataset for downstream analysis?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/5.1.0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

10. **single-cell-scrna-data-ingest-q020**
   - Topic: single-cell
   - Tutorial: Converting between common single cell data formats (`topics/single-cell/tutorials/scrna-data-ingest`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scrna-data-ingest/tutorial.html
   - Recording date: N/A
   - Query: I need to edit values in one column of a table using a regular expression (for example strip a suffix from cell barcodes). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regexColumn1/1.0.3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

11. **statistics-flexynesis_survival-q013**
   - Topic: statistics
   - Tutorial: Identifing Survival Markers of Brain tumor with Flexynesis (`topics/statistics/tutorials/flexynesis_survival`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.html
   - Recording date: N/A
   - Query: I need to summarize a tabular dataset by applying simple operations across columns/rows (e.g., min/max/mean or group-wise summaries). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): N/A

12. **single-cell-EBI-retrieval-q014**
   - Topic: single-cell
   - Tutorial: Importing files from public atlases (`topics/single-cell/tutorials/EBI-retrieval`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/EBI-retrieval/tutorial.html
   - Recording date: N/A
   - Query: I have a text file and want to extract only lines containing a set of keywords so I can focus on those entries. Which Galaxy tool can grep matching lines?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_grep_tool/9.5+galaxy2
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

13. **genome-annotation-tnseq-q046**
   - Topic: genome-annotation
   - Tutorial: Essential genes detection with Transposon insertion sequencing (`topics/genome-annotation/tutorials/tnseq`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/tnseq/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to sort a TSV while retaining the header line?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

14. **microbiome-nanopore-16S-metagenomics-q026**
   - Topic: microbiome
   - Tutorial: 16S Microbial analysis with Nanopore data (`topics/microbiome/tutorials/nanopore-16S-metagenomics`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/microbiome/tutorials/nanopore-16S-metagenomics/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool should I use to preprocess reads (trim + filter) in one step before downstream analysis?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1+galaxy3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

15. **genome-annotation-tnseq-q034**
   - Topic: genome-annotation
   - Tutorial: Essential genes detection with Transposon insertion sequencing (`topics/genome-annotation/tutorials/tnseq`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/tnseq/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to perform fast short-read alignment against a reference genome?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/bowtie2/bowtie2/2.5.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/devteam/bwa/bwa_mem/0.7.19&version=0.7.19

16. **transcriptomics-full-de-novo-q019**
   - Topic: transcriptomics
   - Tutorial: De novo transcriptome assembly, annotation, and differential expression analysis (`topics/transcriptomics/tutorials/full-de-novo`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/full-de-novo/tutorial.html
   - Recording date: N/A
   - Query: I want to assess the completeness of my de novo transcriptome assembly by checking for conserved single-copy orthologs. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/iuc/busco/busco/5.8.0+galaxy2
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

17. **transcriptomics-rna-seq-genes-to-pathways-q014**
   - Topic: transcriptomics
   - Tutorial: 3: RNA-seq genes to pathways (`topics/transcriptomics/tutorials/rna-seq-genes-to-pathways`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/rna-seq-genes-to-pathways/tutorial.html
   - Recording date: N/A
   - Query: I want to derive an additional column in a gene table (for example compute a statistic or add a constant label) for a pathway workflow. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

18. **single-cell-bulk-music-3-preparebulk-q012**
   - Topic: single-cell
   - Tutorial: Bulk matrix to ESet | Creating the bulk RNA-seq dataset for deconvolution (`topics/single-cell/tutorials/bulk-music-3-preparebulk`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/bulk-music-3-preparebulk/tutorial.html
   - Recording date: N/A
   - Query: I want to rewrite parts of each line using a regex rule to standardize a dataset before downstream tools. What Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regex1/1.0.3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

19. **epigenetics-tal1-binding-site-identification-q014**
   - Topic: epigenetics
   - Tutorial: Identification of the binding sites of the T-cell acute lymphocytic leukemia protein 1 (TAL1) (`topics/epigenetics/tutorials/tal1-binding-site-identification`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/tal1-binding-site-identification/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool generates a standard QC report for raw reads (per-base quality, adapter content, duplication)?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

20. **proteomics-maxquant-label-free-q022**
   - Topic: proteomics
   - Tutorial: Label-free data analysis using MaxQuant (`topics/proteomics/tutorials/maxquant-label-free`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/proteomics/tutorials/maxquant-label-free/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool should I use to run label-free quantification across multiple runs and export a protein quantification table?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/2.0.3.0+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

21. **transcriptomics-rna-seq-reads-to-counts-q013**
   - Topic: transcriptomics
   - Tutorial: 1: RNA-Seq reads to counts (`topics/transcriptomics/tutorials/rna-seq-reads-to-counts`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/rna-seq-reads-to-counts/tutorial.html
   - Recording date: N/A
   - Query: I need to trim adapters and low-quality bases from RNA-seq reads prior to alignment. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lparsons/cutadapt/cutadapt/5.2+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

22. **metabolomics-qcxms-predictions-q026**
   - Topic: metabolomics
   - Tutorial: Predicting EI+ mass spectra with QCxMS (`topics/metabolomics/tutorials/qcxms-predictions`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/qcxms-predictions/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to perform compound file format conversion (structure format A to format B)?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/openbabel_compound_convert/openbabel_compound_convert/3.1.1+galaxy1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

23. **transcriptomics-small_ncrna_clustering-q013**
   - Topic: transcriptomics
   - Tutorial: Small Non-coding RNA Clustering using BlockClust (`topics/transcriptomics/tutorials/small_ncrna_clustering`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/small_ncrna_clustering/tutorial.html
   - Recording date: N/A
   - Query: I need to sort a tabular file by a column while keeping the header intact (for example sorting cluster results by score). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

24. **single-cell-scatac-standard-processing-snapatac2-q012**
   - Topic: single-cell
   - Tutorial: Single-cell ATAC-seq standard processing with SnapATAC2 (`topics/single-cell/tutorials/scatac-standard-processing-snapatac2`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scatac-standard-processing-snapatac2/tutorial.html
   - Recording date: N/A
   - Query: I have single-cell ATAC reads and want to align them to a reference genome using a short-read aligner. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/bwa/bwa_mem/0.7.19
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/devteam/bowtie2/bowtie2/2.5.4%2Bgalaxy0&version=2.5.4%2Bgalaxy0

25. **single-cell-EBI-retrieval-q013**
   - Topic: single-cell
   - Tutorial: Importing files from public atlases (`topics/single-cell/tutorials/EBI-retrieval`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/EBI-retrieval/tutorial.html
   - Recording date: N/A
   - Query: I have a tabular dataset and need to replace specific text patterns throughout the file (for example, normalize sample labels) before analysis. Which Galaxy tool can find and replace text?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_find_and_replace/9.5+galaxy2
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): N/A

26. **introduction-galaxy-reproduce-q038**
   - Topic: introduction
   - Tutorial: How to reproduce published Galaxy analyses (`topics/introduction/tutorials/galaxy-reproduce`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-reproduce/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to turn a sorted list with repeats into a unique list?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sorted_uniq/9.5+galaxy2
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

27. **imaging-parameter-tuning-q014**
   - Topic: imaging
   - Tutorial: Parameter tuning and optimization - Evaluating nuclei segmentation with Galaxy (`topics/imaging/tutorials/parameter-tuning`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/parameter-tuning/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to partition a table into per-group datasets based on a column?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.6
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

28. **computational-chemistry-analysis-md-simulations-q053**
   - Topic: computational-chemistry
   - Tutorial: Analysis of molecular dynamics simulations (`topics/computational-chemistry/tutorials/analysis-md-simulations`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/computational-chemistry/tutorials/analysis-md-simulations/tutorial.html
   - Recording date: N/A
   - Query: Which tool should I use in Galaxy for common MD analyses when there are multiple reasonable choices depending on whether I need PCA, RMSD, RMSF, or other metrics?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_pca/bio3d_pca/2.3.4, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_rdf/mdanalysis_rdf/0.19, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_cosine_analysis/mdanalysis_cosine_analysis/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_ramachandran_plot/mdanalysis_ramachandran_plot/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_distance/mdanalysis_distance/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_dihedral/mdanalysis_dihedral/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_rmsd/bio3d_rmsd/2.3.4, toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_rmsf/bio3d_rmsf/2.3.4
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

29. **computational-chemistry-analysis-md-simulations-q049**
   - Topic: computational-chemistry
   - Tutorial: Analysis of molecular dynamics simulations (`topics/computational-chemistry/tutorials/analysis-md-simulations`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/computational-chemistry/tutorials/analysis-md-simulations/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool should I pick for MD trajectory analysis when I might need either RMSF, RMSD, PCA, or related geometric measurements?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_rmsf/bio3d_rmsf/2.3.4, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_rdf/mdanalysis_rdf/0.19, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_cosine_analysis/mdanalysis_cosine_analysis/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_ramachandran_plot/mdanalysis_ramachandran_plot/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_distance/mdanalysis_distance/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/mdanalysis_dihedral/mdanalysis_dihedral/1.0.0+galaxy0, toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_rmsd/bio3d_rmsd/2.3.4, toolshed.g2.bx.psu.edu/repos/chemteam/bio3d_pca/bio3d_pca/2.3.4
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

30. **metabolomics-gc_ms_with_xcms-q066**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: GC-MS data processing (with XCMS, RAMClustR, RIAssigner, and matchms) (`topics/metabolomics/tutorials/gc_ms_with_xcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/gc_ms_with_xcms/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to denoise a metabolomics intensity table with batch effects using an independent component method?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/recetox/waveica/waveica/0.2.0+galaxy9
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

31. **metabolomics-gc_ms_with_xcms-q065**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: GC-MS data processing (with XCMS, RAMClustR, RIAssigner, and matchms) (`topics/metabolomics/tutorials/gc_ms_with_xcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/gc_ms_with_xcms/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool can correct unwanted variation/batch effects in a metabolomics feature matrix using an ICA-based approach?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/recetox/waveica/waveica/0.2.0+galaxy9
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

32. **imaging-voronoi-segmentation-q034**
   - Topic: imaging
   - Tutorial: Voronoi segmentation (`topics/imaging/tutorials/voronoi-segmentation`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/voronoi-segmentation/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I run to convert an image into a binary mask using automatic thresholding?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

33. **imaging-voronoi-segmentation-q033**
   - Topic: imaging
   - Tutorial: Voronoi segmentation (`topics/imaging/tutorials/voronoi-segmentation`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/voronoi-segmentation/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool can apply an auto-threshold method to images and output a binary mask suitable for segmentation workflows?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

34. **imaging-process-image-bioimageio-q026**
   - Topic: imaging
   - Tutorial: Using BioImage.IO models for image analysis in Galaxy (`topics/imaging/tutorials/process-image-bioimageio`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/process-image-bioimageio/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool can turn a processed grayscale image into a binary mask by applying an automatic threshold method?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

35. **imaging-process-image-bioimageio-q025**
   - Topic: imaging
   - Tutorial: Using BioImage.IO models for image analysis in Galaxy (`topics/imaging/tutorials/process-image-bioimageio`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/imaging/tutorials/process-image-bioimageio/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool should I use to apply automatic thresholding to produce a binary segmentation image as input for labeling objects?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

36. **sequence-analysis-ncbi-blast-against-the-madland-q026**
   - Topic: sequence-analysis
   - Tutorial: NCBI BLAST+ against the MAdLand (`topics/sequence-analysis/tutorials/ncbi-blast-against-the-madland`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/ncbi-blast-against-the-madland/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool provides high-speed protein alignments for annotation workflows?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/diamond/bg_diamond/2.1.16+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/toolshed/view/devteam/ncbi_blast_plus

37. **sequence-analysis-ncbi-blast-against-the-madland-q025**
   - Topic: sequence-analysis
   - Tutorial: NCBI BLAST+ against the MAdLand (`topics/sequence-analysis/tutorials/ncbi-blast-against-the-madland`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/ncbi-blast-against-the-madland/tutorial.html
   - Recording date: N/A
   - Query: In Galaxy, what tool should I use for fast protein or translated sequence searches against large reference databases?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/bgruening/diamond/bg_diamond/2.1.16+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/toolshed/view/devteam/ncbi_blast_plus

38. **metabolomics-lcms-q052**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: LC-MS analysis (`topics/metabolomics/tutorials/lcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/lcms/tutorial.html
   - Recording date: N/A
   - Query: I want to merge the per-sample LC-MS feature detection outputs into one dataset so I can build a single feature intensity matrix later. What Galaxy tool can merge the sample objects?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lecorguille/xcms_merge/xcms_merge/3.12.0+galaxy3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

39. **metabolomics-lcms-q051**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: LC-MS analysis (`topics/metabolomics/tutorials/lcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/lcms/tutorial.html
   - Recording date: N/A
   - Query: Before grouping shared ions/features, I want to combine all per-sample RData results (and optionally a sample metadata table) into one merged RData file. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lecorguille/xcms_merge/xcms_merge/3.12.0+galaxy3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

40. **metabolomics-gcms-q038**
   - Topic: metabolomics
   - Tutorial: Mass spectrometry: GC-MS analysis with the metaMS package (`topics/metabolomics/tutorials/gcms`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/metabolomics/tutorials/gcms/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool should I use to complete a grouped LC-MS feature table by filling in missing peak values?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/lecorguille/xcms_fillpeaks/abims_xcms_fillPeaks/3.12.0+galaxy3
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)

41. **sequence-analysis-sars-with-galaxy-on-anvil-q018**
   - Topic: sequence-analysis
   - Tutorial: SARS-CoV-2 Viral Sample Alignment and Variant Visualization (`topics/sequence-analysis/tutorials/sars-with-galaxy-on-anvil`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/sars-with-galaxy-on-anvil/tutorial.html
   - Recording date: N/A
   - Query: What Galaxy tool should I run to check read quality and overrepresented sequences in FASTQ datasets?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

42. **epigenetics-tal1-binding-site-identification-q013**
   - Topic: epigenetics
   - Tutorial: Identification of the binding sites of the T-cell acute lymphocytic leukemia protein 1 (TAL1) (`topics/epigenetics/tutorials/tal1-binding-site-identification`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/tal1-binding-site-identification/tutorial.html
   - Recording date: N/A
   - Query: I need a per-sample read quality report for my raw sequencing reads before alignment. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

43. **epigenetics-methylation-seq-q014**
   - Topic: epigenetics
   - Tutorial: DNA Methylation data analysis (`topics/epigenetics/tutorials/methylation-seq`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/methylation-seq/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool generates a standard read-quality report for raw sequencing reads before alignment?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

44. **epigenetics-methylation-seq-q013**
   - Topic: epigenetics
   - Tutorial: DNA Methylation data analysis (`topics/epigenetics/tutorials/methylation-seq`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/methylation-seq/tutorial.html
   - Recording date: N/A
   - Query: I need a QC report for my raw sequencing reads (per-base quality, adapters, duplication, etc.). Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

45. **epigenetics-formation_of_super-structures_on_xi-q014**
   - Topic: epigenetics
   - Tutorial: Formation of the Super-Structures on the Inactive X (`topics/epigenetics/tutorials/formation_of_super-structures_on_xi`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/formation_of_super-structures_on_xi/tutorial.html
   - Recording date: N/A
   - Query: What tool should I use in Galaxy to produce a read QC report I can review before proceeding?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4%2Bgalaxy0&version=1.2.4%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

46. **epigenetics-formation_of_super-structures_on_xi-q013**
   - Topic: epigenetics
   - Tutorial: Formation of the Super-Structures on the Inactive X (`topics/epigenetics/tutorials/formation_of_super-structures_on_xi`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/formation_of_super-structures_on_xi/tutorial.html
   - Recording date: N/A
   - Query: Which Galaxy tool should I use to assess read quality and generate QC summaries across my samples?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.33%2Bgalaxy0&version=1.33%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

47. **assembly-unicycler-assembly-q016**
   - Topic: assembly
   - Tutorial: Unicycler Assembly (`topics/assembly/tutorials/unicycler-assembly`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/assembly/tutorials/unicycler-assembly/tutorial.html
   - Recording date: N/A
   - Query: I have a collection of read datasets and want to run per-sample QC efficiently and keep comparable reports for each sample. Which QC tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.33%2Bgalaxy0&version=1.33%2Bgalaxy0, https://usegalaxy.org/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1%2Bgalaxy3&version=1.0.1%2Bgalaxy3

48. **assembly-unicycler-assembly-q011**
   - Topic: assembly
   - Tutorial: Unicycler Assembly (`topics/assembly/tutorials/unicycler-assembly`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/assembly/tutorials/unicycler-assembly/tutorial.html
   - Recording date: N/A
   - Query: I have paired-end short reads from a bacterial isolate and want a quick quality-control report before assembly. Which tool should I run?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): N/A

49. **assembly-mrsa-nanopore-q023**
   - Topic: assembly
   - Tutorial: Genome Assembly of MRSA from Oxford Nanopore MinION data (and optionally Illumina data) (`topics/assembly/tutorials/mrsa-nanopore`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/assembly/tutorials/mrsa-nanopore/tutorial.html
   - Recording date: N/A
   - Query: Which tool should I use to generate a per-base quality report for paired-end sequencing reads before I start assembly?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): N/A

50. **assembly-mrsa-nanopore-q012**
   - Topic: assembly
   - Tutorial: Genome Assembly of MRSA from Oxford Nanopore MinION data (and optionally Illumina data) (`topics/assembly/tutorials/mrsa-nanopore`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/assembly/tutorials/mrsa-nanopore/tutorial.html
   - Recording date: N/A
   - Query: I want a quick QC report for my read dataset to check base qualities and overrepresented sequences before long-read filtering. Which Galaxy tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.74+galaxy1, toolshed.g2.bx.psu.edu/repos/iuc/falco/falco/1.2.4+galaxy0
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): N/A

51. **manual-statistics-image-learner-q001**
   - Topic: statistics
   - Tutorial: GLEAM Image Learner - Validating Skin Lesion Classification on HAM10000 (`topics/statistics/tutorials/image_learner`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/image_learner/tutorial.html
   - Recording date: N/A
   - Query: I have labeled images and want to train a deep-learning image classifier in Galaxy. Which tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/image_learner/image_learner/0.1.5
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)
   - Source: data/benchmark/stats_learner_additions.jsonl

54. **manual-statistics-image-learner-q004**
   - Topic: statistics
   - Tutorial: GLEAM Image Learner - Validating Skin Lesion Classification on HAM10000 (`topics/statistics/tutorials/image_learner`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/image_learner/tutorial.html
   - Recording date: N/A
   - Query: I need a Galaxy tool to fine-tune a pre-trained vision model on my labeled image dataset. Which tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/image_learner/image_learner/0.1.5
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)
   - Source: data/benchmark/stats_learner_additions.jsonl

55. **manual-statistics-multimodal-learner-q001**
   - Topic: statistics
   - Tutorial: Gleam Multimodal Learner - Head and Neck cancer Recurrence Prediction with HANCOCK (`topics/statistics/tutorials/multimodal_learner`)
   - Tutorial URL: https://training.galaxyproject.org/training-material/topics/statistics/tutorials/multimodal_learner/tutorial.html
   - Recording date: N/A
   - Query: I have a dataset with multiple input modalities (e.g., tabular features plus text) and want to train a single predictive model in Galaxy. Which tool should I use?
   - Gold tools: toolshed.g2.bx.psu.edu/repos/goeckslab/multimodal_learner/multimodal_learner/0.1.5
   - Candidate alternative tool URLs on usegalaxy.org (present, not suitability-verified): (none)
   - Source: data/benchmark/stats_learner_additions.jsonl
