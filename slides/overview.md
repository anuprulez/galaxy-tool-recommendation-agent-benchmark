# Galaxy Tool Recommendation Benchmark – Current Status

## 1. Accomplished
- Consolidated Codex batches into `tmp_stats/codex_quiers_all.{jsonl,md}` and generated a 5,152-query set for evaluation.
- Built `scripts/generate_llm_predictions.py` to prompt a configurable OpenAI-compatible LLM with tutorial/query context and capture ranked predictions (`tmp_stats/codex_predictions_sample.jsonl` covers the first 100 cases).
- Added `scripts/evaluate_recommendations.py` use to score Hit@k/MRR@nDCG@k (recent 100-query run yields Hit@1=0.84, Hit@3/5=0.95, Hit@10=0.96—see `eval_results.md`).
- Documented end-to-end workflow and evaluation run in `slides/current_workflow.md` plus the evaluation guide updates.

## 2. Future work
- Expand predictions beyond the initial 100 queries by rerunning `generate_llm_predictions.py` with larger `--max-queries` and `--skip-existing`.
- Generate/update per-topic tool catalog (`scripts/build_tool_catalog.py`) plus tool descriptions from GTN/tool shed metadata for richer prompts.
- Identify tutorials not yet converted into queries and either hand-write queries or generate them via the benchmark pipeline so every tutorial has coverage.
- Consider alternate LLM prompting strategies (e.g., grouped tool sections, context with dataset snippets) and rerun evaluations to compare.
