# xAI coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

xAI's process is fast and uneven. Reports describe a 15 to 30 minute engineer screen, then two or three coding rounds that mix hard LeetCode with practical tasks: an in-memory database with transactions, or filling in one function inside a large LLM codebase with almost no spec. Speed and reading unfamiliar code both matter.

## Round format

- A short screen with an engineer, then coding rounds on the same or next day ([candidate report on Aced](https://www.aced.io/experiences/x-ai-software-engineer-interview-2fe9c1), [candidate recap on DEV](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0)).
- One candidate got a one-hour online assignment with a hard simulation problem ([Taro report, May 2025](https://www.jointaro.com/interviews/companies/xai/experiences/software-engineer-japan-may-29-2025-no-offer-neutral-6f33a8bf)).
- Expect LeetCode medium to hard plus at least one practical, stateful build.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Implement an LRU cache. | [candidate report on Aced](https://www.aced.io/experiences/x-ai-software-engineer-interview-2fe9c1), [candidate recap on DEV](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0) | [LRU Cache](https://leetcode.com/problems/lru-cache/) |
| Fill in an empty function inside a large LLM-related codebase, with no clear inputs or outputs given. | [candidate report on Aced](https://www.aced.io/experiences/x-ai-software-engineer-interview-2fe9c1) | No close LeetCode match; see the note below. |
| Word search on a grid, solved with a trie and DFS. | [candidate recap on DEV](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0) | [Word Search](https://leetcode.com/problems/word-search/), [Word Search II](https://leetcode.com/problems/word-search-ii/) |
| In-memory database with SET, GET, BEGIN, ROLLBACK and COMMIT, including nested transactions. | [candidate recap on DEV](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0) | [Min Stack](https://leetcode.com/problems/min-stack/), [Snapshot Array](https://leetcode.com/problems/snapshot-array/) |
| Hard simulation problem in a one-hour online assignment. | [Taro report, May 2025](https://www.jointaro.com/interviews/companies/xai/experiences/software-engineer-japan-may-29-2025-no-offer-neutral-6f33a8bf) | [Game of Life](https://leetcode.com/problems/game-of-life/), [Design Snake Game](https://leetcode.com/problems/design-snake-game/) (Premium) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Reported directly. |
| 2 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | [Stateful class design](../patterns/stateful-class-design.md) | The harder follow-up if LRU goes quickly. |
| 3 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Backtracking on a grid. |
| 4 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | [Tries and string search](../patterns/tries-and-strings.md) | The reported trie plus DFS version. |
| 5 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | [Tries and string search](../patterns/tries-and-strings.md) | Build the trie fast before you need it. |
| 6 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | A stack of saved states is how nested transactions roll back. |
| 7 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | Versioned state, the other way to model transactions. |
| 8 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | Simulation with in-place updates. |
| 9 | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) (Premium) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | Stateful simulation with many rules. |
| 10 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | Stack-driven simulation, quick to get wrong. |
| 11 | [Text Justification](https://leetcode.com/problems/text-justification/) | Hard | [Simulation and grids](../patterns/simulation-and-grids.md) | Pure implementation detail under time pressure. |

> [!NOTE]
> LeetCode cannot train the 'fill in a function in a big codebase' task. Practise it by cloning an open-source LLM library, picking a function, deleting its body and rewriting it from the call sites and tests.

## Practical exercises in this repo

- [In-memory record store with TTL and backups](../practical/01-kv-store-with-ttl/)

## More on the loop

- [landed's xAI interview guide](https://www.landed.jobs/resources/guides/xai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-xai): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** xAI and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-xai).
