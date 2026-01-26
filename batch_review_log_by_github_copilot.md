# Batch review log (by GitHub Copilot)

This file records manual batch-by-batch review outcomes for `data/benchmark/v1_items.jsonl`.

Scope and rules used for each batch:
- Only add a tool as an **acceptable alternative** if it is clearly same-intent and the tool ID is verifiably present in the local usegalaxy.org snapshot (`data/tool_catalog/usegalaxy_org_all_tools.jsonl`).
- High-precision expansions only (no bulk/template additions).

## Legend
- **no-op**: reviewed, no safe same-intent alternatives found (so no benchmark edit).
- **expanded**: benchmark updated with one or more verified same-intent alternatives.
- **flag**: potential issue discovered (e.g., tool ID not found in snapshot); not changed unless explicitly handled.

---

## Batch 0033 (3201–3300)
- Status: **no-op**
- Date: 2026-01-25
- Notes:
  - Reviewed all items in the batch.
  - Multiple imaging tool IDs referenced in this batch were **not present** in the local usegalaxy.org snapshot, including:
    - `toolshed.g2.bx.psu.edu/repos/imgteam/unzip/unzip/6.0+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/image_info/ip_imageinfo/5.7.1+galaxy1`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/split_image/ip_split_image/2.2.3+galaxy1`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/graphicsmagick_image_convert/graphicsmagick_image_convert/1.3.45+galaxy0`
    - (and others)
  - Because these tool IDs are not verifiable in the snapshot, no same-intent alternatives were added.

## Batch 0034 (3301–3400)
- Status: **expanded** (with **flags**)
- Date: 2026-01-25
- Expansion summary:
  - Added snapshot-verified alternative installed versions for BioFormats bfconvert (image format conversion):
    - `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy2`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy3`
- Flags / notes:
  - The ground-truth tool ID `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy0` is **not present** in the local snapshot; the added `+galaxy2` and `+galaxy3` variants are present.
  - Tool IDs referenced in this batch but **not present** in the local usegalaxy.org snapshot:
    - `toolshed.g2.bx.psu.edu/repos/imgteam/unzip/unzip/6.0+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/unzip/unzip/0.2`
    - `toolshed.g2.bx.psu.edu/repos/watsocam/palom/palom/2022.8.2+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/goeckslab/celesta/celesta/0.0.0.9+galaxy3`
    - `toolshed.g2.bx.psu.edu/repos/goeckslab/gate_finder/gate_finder/3.5.1+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_common/cp_common/3.1.9+galaxy1`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_color_to_gray/cp_color_to_gray/3.1.9+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_identify_primary_objects/cp_identify_primary_objects/3.1.9+galaxy1`
  - Snapshot contains internal alternatives related to archives (e.g., `CONVERTER_archive_to_directory`, `__UNZIP_COLLECTION__`), but these were not added because they are not clearly same-intent replacements for a single-file unzip tool.

## Batch 0035 (3401–3500)
- Status: **expanded** (with **flags**)
- Date: 2026-01-25
- Expansion summary:
  - Added snapshot-verified alternative installed versions for:
    - `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.6` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.4`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.2`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/1.12.0+galaxy1` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/1.16.3+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/1.16.3+galaxy1`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/0.0.3-3`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_histogram_equalization/ip_histogram_equalization/0.18.1+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_histogram_equalization/ip_histogram_equalization/0.0.1-2`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.18.1+galaxy3` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.0+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.0.5-2`
    - `toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/5.1.0` ↔
      `toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/4.2`,
      `toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/4.1`,
      `toolshed.g2.bx.psu.edu/repos/nml/collapse_collections/collapse_dataset/4.0`
- Flags / notes:
  - Tool IDs referenced in this batch but **not present** in the local usegalaxy.org snapshot:
    - CellProfiler tools (many `cp_*`), e.g.
      - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_identify_primary_objects/cp_identify_primary_objects/3.1.9+galaxy1`
      - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_track_objects/cp_track_objects/3.1.9+galaxy0`
      - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_cellprofiler/cp_cellprofiler/3.1.9+galaxy0`
    - OMERO suite tools, e.g.
      - `toolshed.g2.bx.psu.edu/repos/ufz/omero_import/omero_import/5.18.0+galaxy3`
      - `toolshed.g2.bx.psu.edu/repos/ufz/omero_metadata_import/omero_metadata_import/5.18.0+galaxy3`
      - `toolshed.g2.bx.psu.edu/repos/ufz/omero_roi_import/omero_roi_import/5.18.0+galaxy4`
      - `toolshed.g2.bx.psu.edu/repos/ufz/omero_get_id/omero_get_id/5.18.0+galaxy0`
      - `toolshed.g2.bx.psu.edu/repos/ufz/omero_get_value/omero_get_value/5.18.0+galaxy0`
      - `toolshed.g2.bx.psu.edu/repos/ufz/omero_filter/omero_filter/5.18.0+galaxy0`
    - `toolshed.g2.bx.psu.edu/view/imgteam/imagej2_analyze_particles_binary/862af85a50ec`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/segmetrics/ip_segmetrics/1.4.0-2`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/bioimage_inference/bioimage_inference/2.4.1+galaxy3`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/split_image/ip_split_image/2.2.3+galaxy1`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/image_math/image_math/1.26.4+galaxy2`
  - Because the above tool IDs are not verifiable in the snapshot, no same-intent alternatives were added for them.

## Batch 0036 (3501–3600)
- Status: **expanded** (with **flags**)
- Date: 2026-01-25
- Expansion summary:
  - Added snapshot-verified alternative installed versions for:
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.18.1+galaxy3` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.0+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.0.5-2`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/binary2labelimage/ip_binary_to_labelimage/0.5+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/binary2labelimage/ip_binary_to_labelimage/0.6+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/binary2labelimage/ip_binary_to_labelimage/0.7.3+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/overlay_images/ip_overlay_images/0.0.4+galaxy4` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/overlay_images/ip_overlay_images/0.0.4+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/overlay_images/ip_overlay_images/0.0.5`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy3` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy2`
- Flags / notes:
  - Tool IDs referenced in this batch but **not present** in the local usegalaxy.org snapshot:
    - `toolshed.g2.bx.psu.edu/repos/imgteam/image_math/image_math/1.26.4+galaxy2`
    - IDR tool:
      - `toolshed.g2.bx.psu.edu/repos/iuc/idr_download_by_ids/idr_download_by_ids/0.45`
    - CellProfiler tools (many `cp_*`), e.g.
      - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_common/cp_common/3.1.9+galaxy2`
      - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_identify_primary_objects/cp_identify_primary_objects/3.1.9+galaxy2`
      - `toolshed.g2.bx.psu.edu/repos/bgruening/cp_cellprofiler/cp_cellprofiler/3.1.9+galaxy1`
  - `__EXTRACT_DATASET__` is present in the snapshot (Galaxy internal tool), so no expansion was needed.

## Batch 0037 (3601–3700)
- Status: **expanded** (with **flags**)
- Date: 2026-01-25
- Expansion summary:
  - Added snapshot-verified alternative installed versions for:
    - `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy3` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/bfconvert/ip_convertimage/6.7.0+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/binary2labelimage/ip_binary_to_labelimage/0.5+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/binary2labelimage/ip_binary_to_labelimage/0.6+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/binary2labelimage/ip_binary_to_labelimage/0.7.3+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/1.12.0+galaxy1` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/1.16.3+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/1.16.3+galaxy1`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_simple_filter/ip_filter_standard/0.0.3-3`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.18.1+galaxy3` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.2+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.25.0+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_auto_threshold/ip_threshold/0.0.5-2`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/overlay_images/ip_overlay_images/0.0.4+galaxy4` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/overlay_images/ip_overlay_images/0.0.4+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/imgteam/overlay_images/ip_overlay_images/0.0.5`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_histogram_equalization/ip_histogram_equalization/0.18.1+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/imgteam/2d_histogram_equalization/ip_histogram_equalization/0.0.1-2`
    - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.8+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.1.0+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1` ↔
      `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.0`,
      `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/1.6`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/1.1.1`
- Flags / notes:
  - Tool IDs referenced in this batch but **not present** in the local usegalaxy.org snapshot:
    - `toolshed.g2.bx.psu.edu/repos/imgteam/repeat_channels/repeat_channels/1.26.4+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/voronoi_tesselation/voronoi_tessellation/0.22.0+galaxy3`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/2d_feature_extraction/ip_2d_feature_extraction/0.18.1+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/image_math/image_math/1.26.4+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/colorize_labels/colorize_labels/3.2.1+galaxy3`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/image_info/ip_imageinfo/5.7.1+galaxy1`
    - `toolshed.g2.bx.psu.edu/repos/imgteam/unzip/unzip/6.0+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/graphicsmagick_image_convert/graphicsmagick_image_convert/1.3.45+galaxy0`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/json2yolosegment/json2yolosegment/8.3.0+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/yolo_training/yolo_training/8.3.0+galaxy2`
  - `toolshed.g2.bx.psu.edu/repos/imgteam/count_objects/ip_count_objects/0.0.5-2` is present in the snapshot; no additional installed versions were found to add.

## Batch 0040 (3901–4000)
- Status: **expanded**
- Date: 2026-01-25
- Commit: `6547d45` (message includes: prev batch no-op)
- Expansion summary:
  - Added verified Toolshed alternative for the built-in Cut tool:
    - `Cut1` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2`

## Batch 0041 (4001–4100)
- Status: **expanded**
- Date: 2026-01-25
- Commit: `e5451ff`
- Expansion summary:
  - Added verified Toolshed alternatives for built-in text processing tools:
    - `cat1` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/9.5+galaxy2`
    - `Cut1` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2`

## Batch 0038 (3701–3800)
- Status: **expanded** (with **flags**)
- Date: 2026-01-26
- Expansion summary:
  - Added snapshot-verified alternative installed versions for:
    - `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1` ↔
      `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.0`,
      `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/1.6`
    - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.8+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.1.0+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.6` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.4`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/split_file_on_column/tp_split_on_column/0.2`
    - `toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regexColumn1/1.0.3` ↔
      `toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regexColumn1/1.0.1`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sorted_uniq/9.5+galaxy2` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sorted_uniq/1.1.0`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/1.1.1`
  - Added snapshot-verified same-intent alternatives between built-in and Toolshed text tools:
    - `Cut1` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2`
    - `cat1` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/9.5+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/9.5+galaxy2` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cat/0.1.1`,
      `cat1`
- Flags / notes:
  - Observed benchmark ↔ snapshot ID mismatch for built-ins:
    - benchmark: `Remove_beginning1` / `Show_beginning1`
    - snapshot: `Remove beginning1` / `Show beginning1`
    - Kept the benchmark IDs but added the snapshot-valid variants as acceptable alternatives.
  - Template placeholders in tools lists are not verifiable tool IDs and were left unchanged, e.g.:
    - `{{version_wc}}`, `{{version_replace_text_column}}`, `{{version_replace_text_line}}`, `{{version_join}}`, `{{version_cat}}`, `{{version_remove_columns_by_header}}`, `{{version_paste}}`

## Batch 0039 (3801–3900)
- Status: **expanded** (with **flags**)
- Date: 2026-01-26
- Expansion summary:
  - Added snapshot-verified same-intent alternatives between built-in and Toolshed text tools:
    - `Cut1` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2`
    - `tp_cut_tool` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/1.1.0`, `Cut1`
  - Added snapshot-verified alternative installed versions for common text processing tools:
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sorted_uniq/9.5+galaxy2` ↔ `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sorted_uniq/1.1.0`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/1.1.1`
    - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy2` ↔
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy3`,
      `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/1.1.0`
    - `toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regex1/1.0.3` ↔ `toolshed.g2.bx.psu.edu/repos/galaxyp/regex_find_replace/regex1/1.0.1`
    - `toolshed.g2.bx.psu.edu/repos/iuc/column_remove_by_header/column_remove_by_header/1.0` ↔ `toolshed.g2.bx.psu.edu/repos/iuc/column_remove_by_header/column_remove_by_header/0.0.1`
  - Added snapshot-verified alternative installed versions for tutorial tools:
    - `toolshed.g2.bx.psu.edu/repos/iuc/bedtools/bedtools_intersectbed/2.31.1+galaxy0` ↔ `toolshed.g2.bx.psu.edu/repos/iuc/bedtools/bedtools_intersectbed/2.30.0+galaxy1`
    - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0` ↔
      `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.8+galaxy0`,
      `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.1.0+galaxy2`
    - `toolshed.g2.bx.psu.edu/repos/iuc/ggplot2_point/ggplot2_point/3.4.0+galaxy1` ↔ `toolshed.g2.bx.psu.edu/repos/iuc/ggplot2_point/ggplot2_point/3.3.5+galaxy0`
  - Added snapshot-verified alternative installed versions for NGS data logistics tools:
    - `toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/1.0.1+galaxy3` ↔ `toolshed.g2.bx.psu.edu/repos/iuc/fastp/fastp/0.24.0+galaxy4`
    - `toolshed.g2.bx.psu.edu/repos/iuc/samtools_view/samtools_view/1.22+galaxy1` ↔ `toolshed.g2.bx.psu.edu/repos/iuc/samtools_view/samtools_view/1.20+galaxy3`
    - `toolshed.g2.bx.psu.edu/repos/devteam/samtools_stats/samtools_stats/2.0.8` ↔ `toolshed.g2.bx.psu.edu/repos/devteam/samtools_stats/samtools_stats/2.0.5`
- Flags / notes:
  - Template placeholders in tools lists are not verifiable tool IDs and were left unchanged, e.g. `{{version_split}}` (and `{{version_paste}}`, though `Paste1` was added as a concrete acceptable alternative).
  - Observed benchmark ↔ snapshot ID mismatch for built-ins:
    - benchmark: `Remove_beginning1`
    - snapshot: `Remove beginning1`
    - Kept the benchmark IDs but added the snapshot-valid variants as acceptable alternatives.
