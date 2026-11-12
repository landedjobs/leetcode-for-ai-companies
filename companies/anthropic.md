# Anthropic coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Anthropic's engineering coding rounds are practical and progressive. The online assessment, where one is used, is a single spec that unlocks in levels. Live rounds ask you to build a component with an engineer, then extend it. Concurrency is the follow-up that several public reports say went wrong for them.

## Round format

- Online assessment (some roles): one CodeSignal problem split into levels, about 90 minutes. Reported problems include an in-memory database built up over several stages ([Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe)).
- One 2026 post reports six stages instead of four, hidden tests per stage, and no AI assistance allowed ([Deepsun, Anthropic's CodeSignal assessment in 2026](https://deepsunai.substack.com/p/anthropics-codesignal-assessment)). Treat the stage count as anecdotal.
- Live technical screen and onsite: practical implementation, 50 to 60 minutes, in a shared browser editor or Colab, with follow-ups added as you go ([Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe)).
- Anthropic's performance-engineering team wrote up how it redesigned a take-home three times as Claude models caught up with strong candidates ([Anthropic, Designing AI-resistant technical evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations)). It explains why their tasks are long, novel and hard to hand to a model.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| In-memory database built in levels: basic operations first, then scans, expiry and history. | [Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe), [Deepsun, Anthropic's CodeSignal assessment in 2026](https://deepsunai.substack.com/p/anthropics-codesignal-assessment) | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/), [Snapshot Array](https://leetcode.com/problems/snapshot-array/), [LRU Cache](https://leetcode.com/problems/lru-cache/) |
| Web crawler, single-threaded first, then made concurrent with a thread-safe visited set. | [Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe), [Hello Interview, LC 1242 reports](https://www.hellointerview.com/community/questions/web-crawler-multithreaded/cm5eguhad02yw838ot9p159t6), [Blind thread on the Anthropic concurrency round](https://www.teamblind.com/post/anthropic-interview-concurrency-q5qeiwmy) | [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium), [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium), [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) |
| Image transformation pipeline driven by JSON instructions, including scaling. | [Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe) | [Rotate Image](https://leetcode.com/problems/rotate-image/), [Game of Life](https://leetcode.com/problems/game-of-life/) |
| Find duplicated files. | [Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe) | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) |
| Processing stack traces. | [Hello Interview, Anthropic SWE guide](https://www.hellointerview.com/guides/anthropic/swe) | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) |
| Write code quickly to a specification, then refactor it as new constraints are introduced. | [landed question page](https://www.landed.jobs/resources/questions/write-code-rapidly-to-a-specification-then-refactor-it-as-new-constraints-are-in-aiq-0132?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-spec-refactor) | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/), [Design SQL](https://leetcode.com/problems/design-sql/) |

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Bank or ledger system built in levels: accounts and transfers, then rankings, scheduled payments and account merges. | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/), [Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/) (Premium) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | History and time-travel reads, the later levels of the database prompt. |
| 2 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | Backups and restores as versioned reads. |
| 3 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Eviction plus O(1) operations, a common level or warm-up. |
| 4 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Keeping two structures in sync, which every leveled build needs. |
| 5 | [All O'one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | Hard | [Stateful class design](../patterns/stateful-class-design.md) | Hard version of keeping counts and ordering consistent. |
| 6 | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Level one of the ledger-style build. |
| 7 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium) | Hard | [Stateful class design](../patterns/stateful-class-design.md) | Same leveled shape: paths, files and listings that grow by requirement. |
| 8 | [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | The single-threaded crawler candidates start from. |
| 9 | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium) | Medium | [Concurrency](../patterns/concurrency.md) | The concurrent follow-up, nearly one to one with reports. |
| 10 | [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | Medium | [Concurrency](../patterns/concurrency.md) | Producer and consumer coordination for crawler workers. |
| 11 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | The reported duplicate-files prompt in LeetCode form. |
| 12 | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Parse a call log with a stack, close to stack-trace processing. |
| 13 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | In-place grid transforms for the image pipeline prompt. |

## Practical exercises in this repo

- [In-memory record store with TTL and backups](../practical/01-kv-store-with-ttl/)
- [Bank ledger with scheduled payments and merges](../practical/02-bank-ledger/)
- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)

## More on the loop

- [landed's Anthropic interview guide](https://www.landed.jobs/resources/guides/anthropic-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-anthropic): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Anthropic and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-anthropic).
