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
python3 -m scripts.eval.evaluate_recommendations \
  --gold data/benchmark/v1_items.jsonl \
  --predictions path/to/predictions.jsonl \
  --k 1,3,5,10 \
  --normalize-tools
```

## One-command runner (generate + evaluate)

If you want a single command that generates predictions and evaluates them:

```bash
# Build / refresh the candidate tool catalog first
python3 -m scripts.catalog.build_usegalaxy_tool_catalog --server https://usegalaxy.org --in-panel --include-io-details

OPENAI_API_KEY=... \
python3 -m scripts.eval.run_v1_agent_eval \
  --agent llm \
  --provider openai_compatible \
  --tool-catalog data/tool_catalog/usegalaxy_org_tools.jsonl \
  --candidate-k 50 \
  --top-k 10 \
  --k 1,3,5,10 \
  --normalize-tools
```

The LLM sees only:
- The user `query` text.
- A ranked shortlist of candidate tools from `--tool-catalog` (tool_id/name/description).

It does not receive `tutorial_id`, `topic`, or dataset metadata from the benchmark items.

### Other LLM providers

If your provider supports the OpenAI-compatible `POST /v1/chat/completions` API, use:

`--provider openai_compatible --api-url <your_endpoint>`

Native protocols also supported by this runner:

- Anthropic: `--provider anthropic --api-url https://api.anthropic.com/v1/messages` (uses `ANTHROPIC_API_KEY`)
- Gemini: `--provider gemini --api-url https://generativelanguage.googleapis.com/v1beta` (uses `GEMINI_API_KEY` or `GOOGLE_API_KEY`)
- Ollama: `--provider ollama --api-url http://localhost:11434/api/chat` (no key)

For a no-API sanity check, you can run the oracle:

```bash
python3 -m scripts.eval.run_v1_agent_eval --agent oracle --max-queries 50
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

Use `python3 -m scripts.benchmark.generate_llm_predictions` to ask an LLM (OpenAI-compatible endpoint by default) for ranked tool suggestions. The script
reads queries (default `tmp_stats/codex_quiers_all.jsonl`), enriches them with tutorial metadata, and writes a JSONL file with `{"id", "predictions"}` entries.

```bash
OPENAI_API_KEY=... \
python3 -m scripts.benchmark.generate_llm_predictions \
  --output tmp_stats/codex_predictions.jsonl \
  --top-k 10 \
  --model gpt-4o-mini \
  --delay 0.5 \
  --max-queries 100
```

- `--skip-existing` resumes work by skipping IDs already in the output file.
- Use `--api-key` or `OPENAI_API_KEY` to supply credentials, and point `--api-url` at another REST endpoint if you prefer a different provider.
- After predictions are complete, point `--predictions` in `python3 -m scripts.eval.evaluate_recommendations` at the generated JSONL to score your agent.
