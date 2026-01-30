# Helptext Extraction for Galaxy Tools

This script extracts help text from Galaxy tools on usegalaxy.org.

## Purpose

Extracts tool help text from Galaxy tool wrappers to support:
- Tool recommendation systems
- Semantic similarity analysis
- Tool documentation indexing

## Setup

1. Create a conda environment:
```bash
conda env create -f environment.yml
conda activate helptext-analysis
```

## Usage

### Basic usage (fetch from usegalaxy.org)
```bash
python extract_helptext.py
```

### Using cached API response
```bash
# First, download the tools list (optional)
curl -o tools.json https://usegalaxy.org/api/tools

# Then use the cached file
python extract_helptext.py --input_json tools.json
```

### Custom output paths
```bash
python extract_helptext.py \
  --out-json data/my_tools.json \
  --out-table data/my_metadata.tsv \
  --out-table-helptext data/my_helptext.tsv
```

## Output Files

### `data/tools_only.json`
Complete JSON export of all tool objects from the Galaxy API, including:
- Tool ID
- Name
- Description
- Version
- Panel section information
- Links and other metadata

### `data/tools_metadata.tsv`
Tab-separated file with columns:
- `tool_id` - Unique tool identifier
- `name` - Tool name
- `description` - Short tool description
- `panel_section_id` - Panel section ID
- `panel_section_name` - Panel section name

### `data/tools_helptext.tsv`
Tab-separated file with columns:
- `tool_id` - Unique tool identifier
- `help_text` - Full help text from the tool wrapper

## Notes

- The script processes tools sequentially to avoid overloading the server
- Progress is printed every 100 tools
- Tools without help text are logged and included with empty help_text
- Processing ~3500 tools may take 30-60 minutes depending on network speed

## Future Work

This is the first phase of helptext analysis. Future work will include:
- Computing dense embeddings using sentence transformers
- Building a similarity matrix between tools
- Extracting top-K similar tools for each tool
