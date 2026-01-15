# Query & Agent Workflow (Slide Notes)

## 1. How we build the query set
- we use the Codex coding agent to generate science-first and tool-first variants per tutorial by ingesting the tutorial ID/topic/datasets plus a fixed template that asks for both request styles; each response becomes a query in `data/benchmark/v1_items.jsonl`, and we keep the metadata fields (`query_type`, dataset references, tool focus) so downstream steps know which style is being evaluated.
- All batches are merged into `v1_items.{jsonl,md}` before scoring; the current set holds **5,152 total queries**.
- Example pairs from *topics/climate/tutorials/ocean-variables*:
  - **Science-first**: “I have scattered oceanographic measurements and need a gridded field to analyze spatial patterns. How should I proceed?” (`ocean-variables-q011`, dataset “Ocean’s variables study”, expected tool `divand_full_analysis`).
  - **Tool-first**: “Which Galaxy tool performs full analysis and gridding for ocean variable datasets?” (`ocean-variables-q013`, same expected tool).

## 2. Coverage constraints
- Our curated tutorial list contains **449 entries** (`data/tutorial_list.yaml`), but we only convert tutorials that expose real Galaxy tools (we skip introductions, interactive meta tutorials, and ones that currently lack associated tool references).
- So far **186 unique tutorials** have Codex-generated queries and matching tool contexts; the rest (~263) are pending query generation once they gain tool metadata.

## 3. Prediction agent
- `scripts/generate_llm_predictions.py` loads `.env` via `python-dotenv`, reads the merged query list, and builds a prompt per query containing:
-  - contextual hints (topic, datasets when available/preview snippets) so the LLM has domain flavor without exposing full tutorial data;
-  - the candidate tool set extracted from `data/benchmark/v1_items.jsonl` (the canonical “gold” benchmark listing each tutorial’s toolshed URLs/versions and serving as the evaluation reference);
-  - explicit instructions to return a JSON object of ordered `{"predictions": [...]}` tool IDs.
- The prompt is sent to a configurable OpenAI-compatible model (default `gpt-4o-mini` hitting `https://api.openai.com/v1/chat/completions`), and `extract_predictions` de-duplicates/truncates to `--top-k`, writing the results to `tmp_stats/codex_predictions_sample.jsonl`.
- Agent knobs: `--top-k`, `--model`, `--delay`, `--max-queries`, `--skip-existing`, `--api-url`, `--output`.

```
╔════════════════════════════════════════╗
║ Prediction agent flow                   ║
║ Inputs → agent(LLM) → Outputs           ║
╠════════════════════════════════════════╣
║ Inputs:                                 ║
║  • Codex query + topic/dataset hint     ║
║  • Candidate tools from the gold file   ║
║  • API key/model/delay params            ║
╠════════════════════════════════════════╣
║ Process: send prompt to the LLM         ║
║ Outputs: JSONL predictions + logging    ║
╚════════════════════════════════════════╝
```
## 4. Evaluation approach
- Gold refers to `data/benchmark/v1_items.jsonl`, our authoritative benchmark specifying which Galaxy tools each tutorial truly uses; both the prompt’s candidate set and evaluator rely on it.
- Run `scripts/evaluate_recommendations.py` with the gold file, the predictions JSONL, and cutoffs such as `k=1,3,5,10`.
- The evaluator normalizes/deduplicates tool IDs (`--normalize-tools`), then reports Hit@k, MRR@k, and nDCG@k per cutoff; entries with no gold tools contribute zeros.
- The latest 100-query snapshot (recorded in `eval_results.md`) yielded Hit@1=0.84, Hit@3/5=0.95, Hit@10=0.96.
## 5. Next steps
- Generate queries for the remaining tutorials (the ~263 not yet covered) once they acquire tool metadata, then continue LLM scoring with `--skip-existing --max-queries`.
- Current accuracy is elevated because each tutorial’s candidate tool set is tiny; we plan to maintain a topic/tag → tool catalog so the agent can build a richer candidate pool before ranking and produce more realistic scores.
