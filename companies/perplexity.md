# Perplexity coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Perplexity's coding rounds move fast. The reported phone screen is a multi-part Python build, a to-do list for an AI agent, where each part has predefined tests and later parts add state changes and dependency cycles. One candidate passed every test except the final large one, which timed out.

## Round format

- Multi-part coding with predefined tests per part; new requirements land after you finish each part ([Taro report, Nov 2025](https://www.jointaro.com/interviews/companies/perplexity/experiences/senior-software-engineer-united-states-november-17-2025-no-offer-negative-4f971f9b/)).
- Performance matters on the last tests. A DFS that is fine on small inputs can time out on the large case, so know the iterative version and the complexity.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Implement a to-do list that grows by parts, with state changes and dependency cycles. | [Taro report, Nov 2025](https://www.jointaro.com/interviews/companies/perplexity/experiences/senior-software-engineer-united-states-november-17-2025-no-offer-negative-4f971f9b/) | [Course Schedule](https://leetcode.com/problems/course-schedule/), [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/), [Parallel Courses](https://leetcode.com/problems/parallel-courses/) (Premium) |

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Merge ranked results from several retrievers into one top-k list. | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Cache answers to repeated queries with eviction. | [LRU Cache](https://leetcode.com/problems/lru-cache/) |
| Autocomplete for search queries. | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) (Premium) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | [Dependency graphs and topological sort](../patterns/dependency-graphs.md) | Cycle detection on task dependencies. |
| 2 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | [Dependency graphs and topological sort](../patterns/dependency-graphs.md) | Return a valid order, the next part. |
| 3 | [Parallel Courses](https://leetcode.com/problems/parallel-courses/) (Premium) | Medium | [Dependency graphs and topological sort](../patterns/dependency-graphs.md) | Levels of a DAG; models tasks that can run together. |
| 4 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Scheduling with cooldowns. |
| 5 | [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | DFS enumeration; watch the recursion depth. |
| 6 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Iterative DFS or BFS to avoid recursion limits. |
| 7 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Graph copy with a visited map. |
| 8 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Merging ranked lists. |
| 9 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Ranking with a heap. |
| 10 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Query caching. |
| 11 | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) (Premium) | Hard | [Tries and string search](../patterns/tries-and-strings.md) | Trie with ranked completions. |

## Practical exercises in this repo

- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)
- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)

## More on the loop

- [landed's Perplexity interview guide](https://www.landed.jobs/resources/guides/perplexity-ai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-perplexity): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Perplexity and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-perplexity).
