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

## Batch 0038–0039 (3701–3900)
- Status: **flag**
- Date: 2026-01-25
- Notes:
  - A scan found multiple items using `Cut1` and `cat1` that likely support the same-intent Toolshed alternatives above.
  - Also observed ID mismatches vs snapshot for:
    - benchmark: `Remove_beginning1` / `Show_beginning1`
    - snapshot: `Remove beginning1` / `Show beginning1`
  - These batches were not yet fully re-reviewed and backfilled as edits at the time this entry was created.
