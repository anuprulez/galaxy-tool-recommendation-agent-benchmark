# Evaluation Guide

This project evaluates tool recommendations as a ranked retrieval task. Use top-k metrics to avoid the “stuff top-k with many tools” issue and to handle multiple acceptable tools.

## Inputs

### Gold file (JSONL)
Use the benchmark items file (e.g., `data/benchmark/v1_items.jsonl`). Each line should contain:
- `id` (query id)
- `tools` (list of gold tool IDs)

Example:
```json
{"id": "example-q01", "tools": ["toolshed.g2.bx.psu.edu/repos/iuc/fastqc/fastqc/0.73+galaxy0"]}
```

### Predictions file (JSONL)
Each line must contain:
- `id` (query id, matching gold)
- `predictions` (ranked list of tool IDs)

Example:
```json
{"id": "example-q01", "predictions": [
  "toolshed.g2.bx.psu.edu/repos/iuc/fastqc/fastqc/0.73+galaxy0",
  "toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.12+galaxy0"
]}
```

## Metrics

The evaluator reports for each cutoff `k`:
- **Hit@k**: 1 if any gold tool appears in top-k, else 0.
- **MRR@k**: reciprocal rank of the first gold tool within top-k.
- **nDCG@k**: ranking quality with binary relevance for gold tools.

These are standard retrieval metrics and are robust to “top-k stuffing.”

## Tool Normalization

If you want to ignore version differences for toolshed IDs, use:
```
--normalize-tools
```
This drops the final path segment (version) from `toolshed.g2.bx.psu.edu/...` IDs.

## Run

```bash
python3 scripts/evaluate_recommendations.py \
  --gold data/benchmark/v1_items.jsonl \
  --predictions path/to/predictions.jsonl \
  --k 1,3,5,10 \
  --normalize-tools
```

Output is JSON printed to stdout, e.g.:
```json
{
  "1": {"hit": 0.52, "mrr": 0.52, "ndcg": 0.52},
  "3": {"hit": 0.71, "mrr": 0.60, "ndcg": 0.63},
  "10": {"hit": 0.85, "mrr": 0.64, "ndcg": 0.69},
  "count": {"queries": 1234}
}
```

## Notes

- If a query has multiple gold tools, any of them counts as relevant.
- If a query has no gold tools, it contributes 0 to all metrics.
- Predictions are de-duplicated in order before scoring.

## Generating predictions with an LLM-based agent

Use `scripts/generate_llm_predictions.py` to ask an LLM (OpenAI-compatible endpoint by default) for ranked tool suggestions. The script
reads queries (default `tmp_stats/codex_quiers_all.jsonl`), enriches them with tutorial metadata, and writes a JSONL file with `{"id", "predictions"}` entries.

```bash
OPENAI_API_KEY=... \
python3 scripts/generate_llm_predictions.py \
  --output tmp_stats/codex_predictions.jsonl \
  --top-k 10 \
  --model gpt-4o-mini \
  --delay 0.5 \
  --max-queries 100
```

- `--skip-existing` resumes work by skipping IDs already in the output file.
- Use `--api-key` or `OPENAI_API_KEY` to supply credentials, and point `--api-url` at another REST endpoint if you prefer a different provider.
- After predictions are complete, point `--predictions` in `scripts/evaluate_recommendations.py` at the generated JSONL to score your agent.
