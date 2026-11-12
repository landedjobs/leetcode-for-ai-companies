# Google DeepMind coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Software and research engineering roles at Google DeepMind largely follow Google's structured hiring, so the coding rounds look more like classic algorithm interviews than the build-a-component rounds at OpenAI or Anthropic. Research engineer loops add ML coding, which this repo does not cover. We found no public, linkable report of a specific DeepMind coding question, so every prompt below is labelled Representative.

## Round format

- Google describes structured technical interviews scored against a shared rubric ([Google, how we hire](https://www.google.com/about/careers/applications/how-we-hire/)).
- Google has piloted an AI-assisted coding interview where candidates work with Gemini ([Northeastern careers, Google's AI-assisted coding interview](https://careers.northeastern.edu/blog/2026/05/13/googles-ai-assisted-coding-interview-2026-guide/)). Check with your recruiter whether your loop uses it.
- Expect data structures and algorithms at medium to hard difficulty, with complexity analysis and follow-ups on scale.

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Given a stream of training-job events, return the k longest-running jobs at any moment. | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/), [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |
| Shortest route on a grid or graph with obstacles or weighted edges. | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/), [Network Delay Time](https://leetcode.com/problems/network-delay-time/) |
| Merge overlapping evaluation windows and report gaps. | [Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Employee Free Time](https://leetcode.com/problems/employee-free-time/) (Premium) |
| Edit distance between two token sequences. | [Edit Distance](https://leetcode.com/problems/edit-distance/) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Top-k with a heap or bucket sort, asked everywhere. |
| 2 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Two heaps over a stream, a common streaming follow-up. |
| 3 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Heap or binary search on answer, good for discussing trade-offs. |
| 4 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | BFS on a grid with clean termination. |
| 5 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Dijkstra in its plainest form. |
| 6 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | BFS where building the graph is the hard part. |
| 7 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | [Intervals](../patterns/intervals.md) | Sort and sweep, then extend to streaming input. |
| 8 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | [Tries and string search](../patterns/tries-and-strings.md) | Prefix structures for autocomplete-style prompts. |
| 9 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | Classic 2D DP that maps to sequence comparison. |
| 10 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | O(n log n) patience sorting is a common follow-up. |
| 11 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | Binary search on partitions, a standard hard. |

## Practical exercises in this repo

- [Byte-level BPE tokenizer](../practical/06-bpe-tokenizer/)

## More on the loop

- [landed's Google DeepMind interview guide](https://www.landed.jobs/resources/guides/google-deepmind-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-google-deepmind): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Google DeepMind and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-google-deepmind).
