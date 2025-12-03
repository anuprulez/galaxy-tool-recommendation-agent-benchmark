# GTN → Galaxy Benchmark Dataset Generator

This repository hosts a small Python toolchain that turns a selection of GTN (Galaxy Training Network) tutorials into a benchmark dataset for Galaxy agents. The dataset pairs natural-language queries with the full set of Galaxy tools and workflows referenced in each tutorial.

## Quick start

1. Create a Python 3.11+ virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```
2. Copy `.env.example` to `.env` and fill in your Jetstream API details.
3. Ensure you have a local checkout of [`galaxyproject/training-material`](https://github.com/galaxyproject/training-material).
4. Run the generator:
   ```bash
   python scripts/generate_benchmark.py \
       --gtn-root /path/to/training-material \
       --tutorial-list data/tutorial_list.yaml \
       --out-dir data/benchmark \
       --raw-dir data/raw_llm
   ```

The command will parse each tutorial listed in `data/tutorial_list.yaml`, call the Jetstream LLM to generate realistic user queries, and write `data/benchmark/v0_items.jsonl` and `data/benchmark/v0_summary.yaml`.

### Optional flags

- `--full-context`: Send full tutorial body + headings to the LLM (default only sends metadata + summary to keep prompts small).
- `--download-datasets`: Download tutorial datasets (based on GTN metadata) into `--datasets-dir`.

See `plan_benchmark.md` for the full project plan.
