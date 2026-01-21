# GTN → Galaxy Benchmark Dataset Generator

This repository hosts a small Python toolchain that turns a selection of GTN (Galaxy Training Network) tutorials into a benchmark dataset for Galaxy agents.

## Quick start

1. Create a Python 3.11+ virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```
2. (Optional) Copy `.env.example` to `.env` and set `OPENAI_API_KEY` if you plan to run `scripts/generate_llm_predictions.py`.

### Optional flags

- See `scripts/` for utilities to build tool catalogs, expand ground-truth tools, and export readable benchmark files.
