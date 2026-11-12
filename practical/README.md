# Practical exercises

[Back to the README](../README.md)

Six multi-part exercises in the format AI labs use for coding rounds: one problem, four levels, requirements that arrive after you finish the previous level. Each folder has the prompt, the LeetCode problems that train it, and a tested reference solution in Python.

| # | Exercise | Time box | Closest reported prompts |
|---|---|---|---|
| 01 | [In-memory record store with TTL and backups](01-kv-store-with-ttl/) | 90 minutes for all four levels; aim to finish level 2 inside 35. | Anthropic in-memory DB, OpenAI time-based and persistent KV, xAI transactions |
| 02 | [Bank ledger with scheduled payments and merges](02-bank-ledger/) | 90 minutes for all four levels. | Leveled online assessments; Anthropic spec-then-refactor |
| 03 | [Rate limiter for an LLM API](03-llm-rate-limiter/) | 60 minutes. | OpenAI LLM rate limiter; Databricks logger and moving average |
| 04 | [Spreadsheet with formulas and cycle detection](04-spreadsheet-formulas/) | 75 minutes. | OpenAI spreadsheet; Perplexity and Scale AI dependency builds |
| 05 | [Concurrent same-host crawler](05-concurrent-crawler/) | 60 minutes. | Anthropic and OpenAI concurrent crawler |
| 06 | [Byte-level BPE tokenizer](06-bpe-tokenizer/) | 60 to 75 minutes. | Tokenizer tasks in ML-flavoured coding rounds |

## How to use them

1. Set a timer for the time box. Open only the setup and level 1.
2. Write tests for the example before writing the class.
3. When level 1 passes, read level 2. Notice how much of your code has to change. That number is what the real round measures.
4. After all four levels, diff your structure against `solution.py`.
5. Redo the same exercise a week later in half the time.
