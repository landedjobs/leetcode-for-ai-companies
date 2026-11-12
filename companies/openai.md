# OpenAI coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

OpenAI's software engineering coding rounds are the clearest example of the AI-lab style. Candidates describe an hour of steady typing on one component that keeps growing: a key-value store that has to persist, an iterator that has to resume, a crawler that has to go concurrent. Puzzle tricks rarely decide these rounds. Clean state, edge cases and the speed of your first working version do.

## Round format

- Coding rounds run about 60 minutes. Candidates report spending the whole hour writing code, with more code than a typical big-tech round ([Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions)).
- Problems are framed as components with an API, not as a single function. Expect follow-ups that change the requirements once the first version works.
- You are judged on structure as much as correctness: readable classes, sensible names, edge cases handled, and tests you run yourself.
- OpenAI publishes an official interview guide on openai.com, and it does not state a universal AI-tool policy. Ask the recruiter, round by round.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Key-value store that serializes to bytes and restores, where keys and values may contain any character, including your delimiter. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium), [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |
| Time-based key-value store: set a value with a timestamp, read the value as of any time. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions), [Hello Interview, time-based KV store reports](https://www.hellointerview.com/community/questions/time-key-value-store/cm5eguhad02rn838o3ttrkt0w) | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/), [Snapshot Array](https://leetcode.com/problems/snapshot-array/) |
| Resumable iterator with pause, resume, skip and reset. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/), [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) |
| In-memory database with tables, inserts and filtered selects, possibly joins. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Design SQL](https://leetcode.com/problems/design-sql/) |
| Unix `cd` that handles `.`, `..`, absolute paths and symbolic links, with cycle detection. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Simplify Path](https://leetcode.com/problems/simplify-path/), [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium) |
| Multithreaded web crawler that avoids duplicate visits, handles failures and limits its rate. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium), [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium) |
| Spreadsheet that evaluates formulas in dependency order and rejects circular references. | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/), [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) (Premium), [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| Meeting-room scheduling (reported as an alternative to a SQL executor). | [Hello Interview, OpenAI coding questions](https://www.hellointerview.com/blog/openai-coding-questions) | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium) |
| Implement a rate limiter for an LLM API. | [landed question page](https://www.landed.jobs/resources/questions/coding-and-system-design-implement-a-rate-limiter-for-an-llm-api-gateway?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-rate-limiter) | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium), [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | The reported time-travel store, nearly one to one. |
| 2 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | Same versioned-read idea with integer snapshots. |
| 3 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Length-prefix encoding is the answer to 'values can contain the delimiter'. |
| 4 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Round-trip a structure to a string and back, then test it. |
| 5 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Iterator state you can pause and resume. |
| 6 | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Wrapping an iterator without losing an element, the core of skip and reset. |
| 7 | [Design SQL](https://leetcode.com/problems/design-sql/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | A small table store with inserts, deletes and selects. |
| 8 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | The `cd` prompt without symlinks. |
| 9 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium) | Hard | [Stateful class design](../patterns/stateful-class-design.md) | Path resolution over a tree you maintain. |
| 10 | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium) | Medium | [Concurrency](../patterns/concurrency.md) | The reported crawler, concurrent version. |
| 11 | [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Cell storage plus simple formulas. |
| 12 | [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) (Premium) | Hard | [Dependency graphs and topological sort](../patterns/dependency-graphs.md) | Formulas that reference other cells and must update. |
| 13 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | [Dependency graphs and topological sort](../patterns/dependency-graphs.md) | Topological order and cycle detection for formula dependencies. |
| 14 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | The meeting-room variant, solved with a min-heap of end times. |
| 15 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium) | Easy | [Rate limiting and sliding windows](../patterns/rate-limiting-and-sliding-windows.md) | Smallest version of a per-key limiter. |
| 16 | [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) | Medium | [Rate limiting and sliding windows](../patterns/rate-limiting-and-sliding-windows.md) | Sliding-window counting, the base of most rate limiters. |
| 17 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Reported at xAI, Databricks and Cursor; the base move for any cache sub-part. |

## Practical exercises in this repo

- [In-memory record store with TTL and backups](../practical/01-kv-store-with-ttl/)
- [Rate limiter for an LLM API](../practical/03-llm-rate-limiter/)
- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)
- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)

## More on the loop

- [landed's OpenAI interview guide](https://www.landed.jobs/resources/guides/openai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-openai): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** OpenAI and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-openai).
