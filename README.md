<a name="top"></a>

<div align="center">

<a href="https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=repo-home"><picture><source media="(prefers-color-scheme: dark)" srcset="https://static.b100x.ai/github-repos/images/brand/landed-wordmark-dark.png"><img src="https://static.b100x.ai/email/landed-wordmark.png" alt="Landed" width="200"></picture></a>

<img src="https://static.b100x.ai/github-repos/images/leetcode-for-ai-companies/banner.svg" alt="LeetCode for AI Companies" width="100%">

[![Stars](https://img.shields.io/github/stars/landedjobs/leetcode-for-ai-companies?style=social)](https://github.com/landedjobs/leetcode-for-ai-companies)
[![License: MIT](https://img.shields.io/badge/License-MIT-6C2BD9.svg)](LICENSE)
[![Updated](https://img.shields.io/badge/updated-2026--11-00A86B)](#how-ai-company-coding-rounds-differ)
[![Problems](https://img.shields.io/badge/LeetCode%20problems-133-6C2BD9)](patterns/)
[![Companies](https://img.shields.io/badge/companies-13-6C2BD9)](companies/)
[![Visit Landed](https://img.shields.io/badge/Visit-Landed-6C2BD9?logo=rocket&logoColor=white)](https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=repo-home)

**The coding problems AI companies ask in 2026**: 43 sourced prompts from 13 companies, mapped to 133 LeetCode problems, 15 patterns and 6 practical exercises with Python solutions.

*Maintained by [Landed](https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=repo-home): daily AI-native job matches, agent help with every application, and mock-interview prep.*

</div>

<!-- landed-apply-cta -->
<table><tr><td>
<b>⚡ <a href="https://app.landed.jobs/signup?from=github&amp;cta=github-guide-apply&amp;item=leetcode-for-ai-companies&amp;utm_source=github&amp;utm_medium=referral&amp;utm_campaign=github-leetcode-for-ai-companies&amp;utm_content=guide-apply">Auto-apply to AI lab engineering jobs that match you →</a></b><br>
Upload your resume once. <a href="https://www.landed.jobs">landed</a> finds the roles that fit you and applies within hours of them going live, so you actually hear back.
</td></tr></table>


---

AI labs rarely ask you to find the clever trick in a 20-line puzzle. They hand you a spec for a small piece of software, an in-memory database, a rate limiter, a crawler, a spreadsheet, and watch how much working, readable code you ship in an hour while the requirements change underneath you.

LeetCode still helps. It just helps in a specific way: a few dozen problems teach exactly the moves those practical rounds need. This repo maps one to the other. Every company page lists what candidates publicly report, with a link to the report, and the LeetCode problems that train it. Anything without a source is labelled **Representative**.

Coding only. For ML theory, system design and behavioral rounds, see [awesome-ai-engineer-interview](https://github.com/landedjobs/awesome-ai-engineer-interview).

## Contents

- [How AI-company coding rounds differ](#how-ai-company-coding-rounds-differ)
- [Practical prompts and the LeetCode problems that train them](#practical-prompts-and-the-leetcode-problems-that-train-them)
- [The patterns that matter](#the-patterns-that-matter)
- [Start here: 30 problems](#start-here-30-problems)
- [Company index](#company-index)
- [Study plans](#study-plans)
- [FAQ](#faq)
- [How labels and sources work](#how-labels-and-sources-work)
- [Contributing](#contributing)

## How AI-company coding rounds differ

| | Classic big-tech round | Typical AI-lab round |
|---|---|---|
| Problem | One algorithm question, sometimes two | One component that grows over 3 to 6 parts or levels |
| What is graded | Optimal complexity, clean explanation | Working code, structure that survives new requirements, tests passing |
| Typical prompt | "Find the longest substring without repeats" | "Build a key-value store. Now add TTL. Now add backups." |
| Code volume | Often under 60 lines | Often well over 100 lines in an hour |
| Follow-ups | Complexity, edge cases | Concurrency, persistence, scale, a changed spec |
| Environment | Shared editor | Shared editor, CodeSignal with hidden tests, Colab, or a real codebase |
| AI tools | Usually banned | Banned, allowed or required, depending on the round |

What that means for prep:

1. **Speed to a correct first version beats elegance.** In leveled rounds you cannot see level 3 until level 1 passes. Scale AI candidates describe the round as a test of how much code they could produce in an hour ([Taro report, Nov 2022](https://www.jointaro.com/interviews/companies/scale-ai/experiences/software-engineer-united-states-november-1-2022-declined-offer-neutral-e52aaacc/)).
2. **Design state for change.** Store `(value, expires_at)` from the start. Route every write through one helper. The second level should cost you ten lines, not a rewrite.
3. **Concurrency is the standard follow-up.** The crawler that must go multithreaded is the single most repeated prompt in public reports for Anthropic and OpenAI.
4. **Read code fast.** Meta's AI-assisted round starts with a bug in a multi-file project ([Hello Interview, Meta's AI-enabled coding round](https://www.hellointerview.com/blog/meta-ai-enabled-coding)), xAI and Scale AI report tasks inside an unfamiliar codebase, and Cursor runs a full project day in its own repo.
5. **Know the LeetCode core anyway.** Databricks, Google DeepMind and Meta's classic round still ask medium-to-hard algorithm problems.

## Practical prompts and the LeetCode problems that train them

The reported practical prompts, the companies they come from, and the problems that build the same muscles. Six of them have a full multi-level exercise with a tested Python solution in [`practical/`](practical/).

| Practical prompt | Where it is reported | LeetCode problems that train it | Exercise |
|---|---|---|---|
| In-memory database or key-value store with TTL, scans and backups | Anthropic, OpenAI, xAI | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/), [Snapshot Array](https://leetcode.com/problems/snapshot-array/), [LRU Cache](https://leetcode.com/problems/lru-cache/), [Design SQL](https://leetcode.com/problems/design-sql/) | [In-memory record store with TTL and backups](practical/01-kv-store-with-ttl/) |
| Bank or ledger system with progressive levels | Leveled assessments (Representative) | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/), [Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/) (Premium), [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | [Bank ledger with scheduled payments and merges](practical/02-bank-ledger/) |
| Rate limiter for an LLM API | OpenAI, Databricks | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium), [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium), [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) | [Rate limiter for an LLM API](practical/03-llm-rate-limiter/) |
| Spreadsheet with formulas and dependencies | OpenAI | [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/), [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) (Premium), [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | [Spreadsheet with formulas and cycle detection](practical/04-spreadsheet-formulas/) |
| Web crawler made concurrent | Anthropic, OpenAI | [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium), [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium), [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | [Concurrent same-host crawler](practical/05-concurrent-crawler/) |
| Tokenizer (BPE) | Recaps of ML-flavoured rounds (Representative) | [Word Break](https://leetcode.com/problems/word-break/), [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Byte-level BPE tokenizer](practical/06-bpe-tokenizer/) |
| Task list or scheduler with dependencies, in parts | Perplexity, Scale AI | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/), [Task Scheduler](https://leetcode.com/problems/task-scheduler/), [Parallel Courses](https://leetcode.com/problems/parallel-courses/) (Premium) | Coming next |
| Serialize a store; resumable iterator | OpenAI | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium), [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/), [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Coming next |
| Unix `cd` with symlinks; file-tree diff | OpenAI, Cursor | [Simplify Path](https://leetcode.com/problems/simplify-path/), [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium), [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Coming next |

Problems marked (Premium) need a LeetCode subscription. Each has a free problem nearby in the same pattern file.

## The patterns that matter

Signal is the number of companies in this repo with at least one **sourced** report that maps to the pattern: High is 4 or more, Medium 2 to 3, Low 1. It tells you where to look first. It is not a measure of how often any company asks the topic.

| Pattern | Signal | Sourced at | Typical AI-lab prompt | Problems |
|---|---|---|---|---|
| [Stateful class design](patterns/stateful-class-design.md) | High | OpenAI, Anthropic, xAI, Scale AI, Databricks, Perplexity, Cursor (Anysphere) | In-memory DB, LRU cache, to-do list, ledger | 10 |
| [Timestamps and binary search](patterns/timestamps-and-binary-search.md) | Medium | OpenAI, Anthropic | Time-travel reads, TTL, backups | 8 |
| [Rate limiting and sliding windows](patterns/rate-limiting-and-sliding-windows.md) | Medium | OpenAI, Databricks | LLM API rate limiter, moving averages | 8 |
| [Concurrency](patterns/concurrency.md) | High | Anthropic, OpenAI, Databricks, NVIDIA | Crawler goes multithreaded; logger queue | 7 |
| [Dependency graphs and topological sort](patterns/dependency-graphs.md) | Medium | OpenAI, Perplexity, Scale AI | Spreadsheet recompute, task dependencies | 7 |
| [Parsing and expression evaluation](patterns/parsing-and-evaluation.md) | High | OpenAI, Anthropic, Scale AI, Cursor (Anysphere) | `cd` with symlinks, formulas, Markdown, stack traces | 10 |
| [Serialization and iterators](patterns/serialization-and-iterators.md) | Medium | OpenAI, Databricks | Persist a KV store, resumable iterator | 9 |
| [Graph traversal (BFS and DFS)](patterns/graphs-bfs-dfs.md) | High | OpenAI, Anthropic, Databricks, Perplexity | Crawl a site, weighted paths | 10 |
| [Simulation and grids](patterns/simulation-and-grids.md) | High | xAI, Databricks, Scale AI, Anthropic | Card game, tic-tac-toe, image pipeline | 9 |
| [Heaps and scheduling](patterns/heaps-and-scheduling.md) | Medium | Scale AI, OpenAI | Task scheduler, meeting rooms, top-k | 9 |
| [Intervals](patterns/intervals.md) | Medium | Scale AI, OpenAI | Intervals plus JSON processing | 10 |
| [Hashing and arrays](patterns/hashing-and-arrays.md) | Medium | Anthropic, Scale AI | Duplicate files, CSV to frames | 8 |
| [Bit manipulation](patterns/bit-manipulation.md) | Medium | NVIDIA, Databricks | Set and count bits, IP to CIDR | 8 |
| [Tries and string search](patterns/tries-and-strings.md) | Low | xAI | Grid word search, autocomplete | 8 |
| [Dynamic programming](patterns/dynamic-programming.md) | Low | Databricks | House robber, diffs | 9 |

## Start here: 30 problems

If you only have time for thirty, do these in order. They cover every pattern that has a sourced report, weighted toward the stateful and concurrent work AI labs favour. Aim for a working solution in 25 minutes each, then re-solve the ones that took longer a week later.

| # | Problem | Difficulty | Pattern | Why |
|---|---|---|---|---|
| 1 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](patterns/stateful-class-design.md) | Reported at xAI, Databricks and Cursor. Learn it cold. |
| 2 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | [Timestamps and binary search](patterns/timestamps-and-binary-search.md) | Reported at OpenAI; the core of Anthropic's later levels. |
| 3 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | [Timestamps and binary search](patterns/timestamps-and-binary-search.md) | Versioned state for backups and transactions. |
| 4 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | [Stateful class design](patterns/stateful-class-design.md) | Two structures kept in sync. |
| 5 | [Design SQL](https://leetcode.com/problems/design-sql/) | Medium | [Stateful class design](patterns/stateful-class-design.md) | A tiny in-memory database. |
| 6 | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/) | Medium | [Stateful class design](patterns/stateful-class-design.md) | Level one of every ledger build. |
| 7 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium) | Hard | [Stateful class design](patterns/stateful-class-design.md) | Paths and trees inside a class. |
| 8 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium) | Easy | [Rate limiting and sliding windows](patterns/rate-limiting-and-sliding-windows.md) | Smallest rate limiter. |
| 9 | [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) | Medium | [Rate limiting and sliding windows](patterns/rate-limiting-and-sliding-windows.md) | Windowed counts. |
| 10 | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) | Easy | [Rate limiting and sliding windows](patterns/rate-limiting-and-sliding-windows.md) | Reported at Databricks. |
| 11 | [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium) | Medium | [Graph traversal (BFS and DFS)](patterns/graphs-bfs-dfs.md) | The single-threaded crawler. |
| 12 | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium) | Medium | [Concurrency](patterns/concurrency.md) | Reported at Anthropic and OpenAI. |
| 13 | [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | Medium | [Concurrency](patterns/concurrency.md) | Producer and consumer basics. |
| 14 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) | Medium | [Serialization and iterators](patterns/serialization-and-iterators.md) | Length-prefix framing for persisted stores. |
| 15 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | [Serialization and iterators](patterns/serialization-and-iterators.md) | Iterator state, close to OpenAI's resumable iterator. |
| 16 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | [Parsing and expression evaluation](patterns/parsing-and-evaluation.md) | OpenAI's `cd` prompt without symlinks. |
| 17 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Medium | [Parsing and expression evaluation](patterns/parsing-and-evaluation.md) | Precedence without recursion. |
| 18 | [Decode String](https://leetcode.com/problems/decode-string/) | Medium | [Parsing and expression evaluation](patterns/parsing-and-evaluation.md) | Nested parsing with a stack. |
| 19 | [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/) | Medium | [Parsing and expression evaluation](patterns/parsing-and-evaluation.md) | Cells plus formulas. |
| 20 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | [Dependency graphs and topological sort](patterns/dependency-graphs.md) | Dependencies and cycle detection. |
| 21 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Medium | [Dependency graphs and topological sort](patterns/dependency-graphs.md) | Graph built from equations. |
| 22 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | [Intervals](patterns/intervals.md) | Part one of every intervals prompt. |
| 23 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium) | Medium | [Heaps and scheduling](patterns/heaps-and-scheduling.md) | Reported at OpenAI. |
| 24 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | [Heaps and scheduling](patterns/heaps-and-scheduling.md) | Reported at Scale AI in a six-part form. |
| 25 | [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium | [Heaps and scheduling](patterns/heaps-and-scheduling.md) | Event simulation with a heap. |
| 26 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Heaps and scheduling](patterns/heaps-and-scheduling.md) | Ranking, everywhere. |
| 27 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | [Graph traversal (BFS and DFS)](patterns/graphs-bfs-dfs.md) | Dijkstra for weighted-path prompts. |
| 28 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) (Premium) | Medium | [Simulation and grids](patterns/simulation-and-grids.md) | Reported at Databricks. |
| 29 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | [Tries and string search](patterns/tries-and-strings.md) | Reported at xAI. |
| 30 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) (Premium) | Medium | [Bit manipulation](patterns/bit-manipulation.md) | Reported at Databricks. |

## Company index

| Company | Coding round in one line | Sourced prompts | Problems | Page | landed guide |
|---|---|---|---|---|---|
| **OpenAI** | Production-style components in about an hour: stores, iterators, crawlers, spreadsheets. | 9 | 17 | [companies/openai.md](companies/openai.md) | [Guide](https://www.landed.jobs/resources/guides/openai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-openai) |
| **Anthropic** | A leveled CodeSignal build, then live practical rounds with concurrency follow-ups. | 6 | 13 | [companies/anthropic.md](companies/anthropic.md) | [Guide](https://www.landed.jobs/resources/guides/anthropic-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-anthropic) |
| **Google DeepMind** | Google-style algorithm rounds; a Gemini-assisted round is being piloted at Google. | None yet (Representative) | 11 | [companies/google-deepmind.md](companies/google-deepmind.md) | [Guide](https://www.landed.jobs/resources/guides/google-deepmind-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-google-deepmind) |
| **Meta** | One classic algorithm round plus a 60-minute AI-assisted round in a multi-file project. | 1 | 12 | [companies/meta.md](companies/meta.md) | [Guide](https://www.landed.jobs/resources/guides/meta-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-meta) |
| **xAI** | Short screens, then hard LeetCode mixed with code-in-a-codebase and in-memory DB tasks. | 5 | 11 | [companies/xai.md](companies/xai.md) | [Guide](https://www.landed.jobs/resources/guides/xai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-xai) |
| **Scale AI** | One problem in many parts, scored by how much working code you ship in an hour. | 5 | 12 | [companies/scale-ai.md](companies/scale-ai.md) | [Guide](https://www.landed.jobs/resources/guides/scale-ai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-scale-ai) |
| **Databricks** | LeetCode medium to hard plus a dedicated concurrency round. | 8 | 12 | [companies/databricks.md](companies/databricks.md) | [Guide](https://www.landed.jobs/resources/guides/databricks-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-databricks) |
| **Perplexity** | Fast, multi-part Python builds with tests per part; dependency handling recurs. | 1 | 11 | [companies/perplexity.md](companies/perplexity.md) | [Guide](https://www.landed.jobs/resources/guides/perplexity-ai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-perplexity) |
| **Cohere** | Applied builds with the Cohere API; retrieval and text-processing patterns. | 1 | 10 | [companies/cohere.md](companies/cohere.md) | [Guide](https://www.landed.jobs/resources/guides/cohere-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-cohere) |
| **Mistral AI** | Few public coding reports; inference and platform patterns are the safest prep. | None yet (Representative) | 10 | [companies/mistral.md](companies/mistral.md) | [Guide](https://www.landed.jobs/resources/guides/mistral-ai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-mistral) |
| **NVIDIA** | Bit manipulation, multithreading and C++ for systems roles; LeetCode for the rest. | 3 | 12 | [companies/nvidia.md](companies/nvidia.md) | [Guide](https://www.landed.jobs/resources/guides/nvidia-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-nvidia) |
| **Cursor (Anysphere)** | Practical screens, then a paid project day inside the real codebase. | 4 | 11 | [companies/cursor.md](companies/cursor.md) | [Guide](https://www.landed.jobs/resources/guides/anysphere-cursor-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-cursor) |
| **Hugging Face** | Open-source style work: tokenizers, data handling, readable library code. | None yet (Representative) | 10 | [companies/hugging-face.md](companies/hugging-face.md) | [Guide](https://www.landed.jobs/resources/guides/hugging-face-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=index-hugging-face) |

Missing a company you interviewed at? [Add a sourced report](CONTRIBUTING.md).

## Study plans

### 2 weeks: you have an onsite booked

| Days | Do | Output |
|---|---|---|
| 1 to 2 | [Stateful class design](patterns/stateful-class-design.md) and [timestamps](patterns/timestamps-and-binary-search.md): problems 1 to 7 of the start-here list | LRU and time-based store from memory in under 15 minutes each |
| 3 | [Practical 01: record store](practical/01-kv-store-with-ttl/) under a 90-minute timer | All four levels, then diff against the solution |
| 4 to 5 | [Concurrency](patterns/concurrency.md) and [graphs](patterns/graphs-bfs-dfs.md): problems 11 to 13 and 27 | A crawler you can convert to threads in 15 minutes |
| 6 | [Practical 05: concurrent crawler](practical/05-concurrent-crawler/) | Explain completion detection out loud |
| 7 | Your target company's page: every reported prompt | One page of notes per prompt |
| 8 to 9 | [Parsing](patterns/parsing-and-evaluation.md) and [dependency graphs](patterns/dependency-graphs.md): problems 14 to 21 | Recursive-descent parser without notes |
| 10 | [Practical 04: spreadsheet](practical/04-spreadsheet-formulas/) or [03: rate limiter](practical/03-llm-rate-limiter/), whichever fits your company | Timed, with tests |
| 11 to 12 | Problems 22 to 30 | Clean solutions, complexity stated |
| 13 | One mock with a friend: they read levels to you one at a time | Note where your design broke |
| 14 | Re-solve the three problems that took longest. Rest. | |

### 4 weeks: building toward the loop

| Week | Focus | Do |
|---|---|---|
| 1 | Core LeetCode | Start-here list 1 to 30, one pattern file per day for the rest of the week's time |
| 2 | Stateful builds | Practicals [01](practical/01-kv-store-with-ttl/) and [02](practical/02-bank-ledger/), plus every problem in [stateful class design](patterns/stateful-class-design.md) and [serialization](patterns/serialization-and-iterators.md) |
| 3 | Concurrency, parsing, dependencies | Practicals [03](practical/03-llm-rate-limiter/), [04](practical/04-spreadsheet-formulas/), [05](practical/05-concurrent-crawler/); the [concurrency](patterns/concurrency.md) problem set in Python with `threading` |
| 4 | Company-specific | Your target company page end to end, practical [06](practical/06-bpe-tokenizer/) if the role touches models, two timed mocks, then rest before the loop |

Practise half your sessions with AI tools off and half with them on, then review what the assistant got wrong. That matches how loops now split rounds ([landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding)).

## FAQ

**Do AI companies ask LeetCode questions?**
Some do, most mix. Databricks and Google-style loops (including DeepMind) still run classic algorithm rounds. Meta keeps one classic round next to its AI-assisted one. OpenAI, Anthropic, Scale AI, Perplexity and Cursor lean on practical, multi-part builds. LeetCode is still the fastest way to learn the moves those builds need.

**What is the most common coding prompt at AI labs?**
In the public reports linked here, two prompts recur across companies: an in-memory key-value store or database that grows in levels (Anthropic, OpenAI, xAI), and a web crawler that has to become concurrent (Anthropic, OpenAI). LRU cache is the most repeated single LeetCode problem (xAI, Databricks, Cursor).

**Can I use AI tools in these coding rounds?**
Only when the company says so for that round. Policies differ inside one loop. Meta's AI-enabled round gives you an assistant in CoderPad that can read but not edit your files, and it is scored on problem solving, code quality, verification and communication ([Hello Interview, Meta's AI-enabled coding round](https://www.hellointerview.com/blog/meta-ai-enabled-coding)). One 2026 account says Anthropic's online assessment does not allow AI help ([Deepsun, Anthropic's CodeSignal assessment in 2026](https://deepsunai.substack.com/p/anthropics-codesignal-assessment)). Cursor's early screens often restrict AI and later rounds may use it in the real codebase ([TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process)). Ask the recruiter in writing, round by round. [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding) has a round-by-round table and a note you can send.

**How do I prepare for an AI-assisted coding round?**
Practise reading unfamiliar code and fixing a bug in it before you write anything new. Ask the assistant for narrow pieces (a test matrix, one function, a review), check every suggestion, and say what you are checking. Run the code often. The grader is watching your judgment, not the assistant's.

**Do I need LeetCode Premium?**
No. About a fifth of the problems here are Premium, mostly design problems such as Logger Rate Limiter and Web Crawler Multithreaded. Each pattern file includes free problems that train the same move, and the [practical exercises](practical/) cover the Premium-heavy topics with full solutions.

**Which language should I use?**
Python, unless the role says otherwise. Every reported prompt here was solvable in Python, and the volume of code in practical rounds favours a terse language. Use C++ for NVIDIA systems roles if that is what the team writes.

**How is this different from company-tagged LeetCode lists?**
Tagged lists tell you which LeetCode problems someone saw. They miss the practical prompts that make up most AI-lab rounds, and they do not link to sources. Here every reported prompt links to a public report, every problem says why it is on the list, and the practical exercises cover what LeetCode cannot.

## How labels and sources work

- **Reported** means a public page describes the prompt at that company: an interview-prep write-up, a candidate post on Blind, Taro, Aced or DEV, an official engineering blog, or a landed question page. The prompt is paraphrased; the link has the original.
- **Representative** means we wrote the prompt in the style of the company's work to give you something to practise. It was not seen in a report.
- Reports are anonymous and loops change. Treat each report as one data point. Where sources disagree (for example the four-level versus six-stage Anthropic assessment), the company page says so.
- LeetCode links were checked against LeetCode's API on 12 Nov 2026. All 133 exist; Premium ones are marked.

---

## Contributing

PRs and issues welcome: a sourced report from your own loop, a better LeetCode mapping, a new practical exercise, or a fix. Every "Reported" prompt needs a public link. See **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

### Part of the Landed AI-native jobs family

Guides and job lists for AI-native roles, each in its own repo.

- 🎯 [awesome-ai-engineer-interview](https://github.com/landedjobs/awesome-ai-engineer-interview): the full AI engineer loop: questions, system designs, company loops
- ❓ [ai-interview-questions](https://github.com/landedjobs/ai-interview-questions): AI interview questions with answers
- 📘 [ai-interview-guides](https://github.com/landedjobs/ai-interview-guides): interview guides for 200 companies
- 🔎 [rag-engineer-interview-questions](https://github.com/landedjobs/rag-engineer-interview-questions): RAG engineer interview questions
- 🏛️ [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs): open roles at AI labs
- 🚀 [ai-engineer-jobs](https://github.com/landedjobs/ai-engineer-jobs): live AI engineer roles, auto-updated
- 🧠 [llm-engineer-jobs](https://github.com/landedjobs/llm-engineer-jobs): LLM engineer roles
- 🧭 [ai-job-hunt-os](https://github.com/landedjobs/ai-job-hunt-os): a system for running an AI job search
- 🧪 [projects-to-land-an-ai-job](https://github.com/landedjobs/projects-to-land-an-ai-job): portfolio projects that get you hired

---

<div align="center">

### Stop spraying. Get **matched**, get **prepped**, get **Landed**.

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)](https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=repo-home)

<sub>Maintained by [Landed](https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=repo-home) · No affiliation with the companies named. Content MIT-licensed; linked resources retain their own licenses. LeetCode is a trademark of its owner; problems are linked, not copied. Reported prompts cite public sources.</sub>

<br/>

[![Star History Chart](https://api.star-history.com/svg?repos=landedjobs/leetcode-for-ai-companies&type=Date)](https://star-history.com/#landedjobs/leetcode-for-ai-companies&Date)

</div>
