# Databricks coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Databricks is the most LeetCode-heavy company here, and the one most likely to give you a separate concurrency round. Reported questions lean on graphs, bit manipulation and streaming, with a few design classes like LRU cache and tic-tac-toe.

## Round format

- Phone screen: one hour on CoderPad, LeetCode medium to hard ([interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions)).
- Onsite: two algorithm rounds (one implementation-heavy, one that grows in complexity) and one open-ended concurrency round, often in pseudocode ([interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions)).
- Candidate summaries also mention bit manipulation, dynamic programming and string handling ([AlgoMonster, Databricks guide](https://algo.monster/interview-guides/databricks)).

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Weighted paths in a graph (optimisation). | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/), [Network Delay Time](https://leetcode.com/problems/network-delay-time/) |
| House robber. | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [House Robber](https://leetcode.com/problems/house-robber/), [House Robber II](https://leetcode.com/problems/house-robber-ii/) |
| LRU cache. | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [LRU Cache](https://leetcode.com/problems/lru-cache/) |
| IP address to CIDR blocks. | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) (Premium) |
| Tic-tac-toe on a board of variable size. | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) (Premium) |
| Bit-level compression and decompression. | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [String Compression](https://leetcode.com/problems/string-compression/), [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) |
| Moving average from a data stream. | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) |
| Logger that processes queued messages efficiently (concurrency round). | [interviewing.io, Databricks interview questions](https://interviewing.io/databricks-interview-questions) | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium), [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Dijkstra variant for weighted paths. |
| 2 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Plain Dijkstra to warm up. |
| 3 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | Reported directly. |
| 4 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | The circular follow-up. |
| 5 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Reported directly. |
| 6 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) (Premium) | Medium | [Bit manipulation](../patterns/bit-manipulation.md) | Reported directly; lowest-set-bit arithmetic. |
| 7 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) (Premium) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | Reported directly; keep O(1) counters per row, column and diagonal. |
| 8 | [String Compression](https://leetcode.com/problems/string-compression/) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Run-length encoding in place. |
| 9 | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) | Easy | [Rate limiting and sliding windows](../patterns/rate-limiting-and-sliding-windows.md) | Reported directly. |
| 10 | [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | Medium | [Concurrency](../patterns/concurrency.md) | Producer and consumer queue for the logger round. |
| 11 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium) | Easy | [Rate limiting and sliding windows](../patterns/rate-limiting-and-sliding-windows.md) | The single-threaded logger to start from. |
| 12 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | Versioned storage, close to Delta-style table history. |

## Practical exercises in this repo

- [Rate limiter for an LLM API](../practical/03-llm-rate-limiter/)
- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)

## More on the loop

- [landed's Databricks interview guide](https://www.landed.jobs/resources/guides/databricks-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-databricks): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Databricks and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-databricks).
