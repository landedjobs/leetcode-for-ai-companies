# Meta coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

AI engineering roles at Meta (including Meta Superintelligence Labs teams) go through Meta's software engineering loop. Since October 2025 one of the two onsite coding rounds is AI-assisted: a multi-file project where you fix a bug, build a feature and then optimise it, with an AI chat panel beside the editor. The other round stays a classic, no-AI algorithm interview.

## Round format

- Meta's hiring process page describes the overall loop ([Meta hiring process](https://www.metacareers.com/hiring-process/)).
- AI-enabled round: 60 minutes in a three-panel CoderPad with a file explorer, an editor and an AI chat that cannot edit files. Three phases: fix a bug, implement the core feature, then handle larger inputs that break your first solution ([Hello Interview, Meta's AI-enabled coding round](https://www.hellointerview.com/blog/meta-ai-enabled-coding)).
- Scoring covers problem solving, code quality, verification and communication ([Hello Interview, Meta's AI-enabled coding round](https://www.hellointerview.com/blog/meta-ai-enabled-coding)). For prompt examples see [interviewing.io, using AI in Meta's round](https://interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples); for Meta's stated reasoning see [CoderPad on Meta's AI interview](https://coderpad.io/blog/hiring-developers/ai-in-the-interview-is-not-cheating-it-is-the-job-according-to-meta/).
- The classic round is algorithm problems at medium difficulty, usually more than one per session. The problems below are well known Meta practice targets, labelled Representative because we link no per-question report.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| AI-assisted round: a bug fix in unfamiliar multi-file code, then a feature, then an optimisation for bigger inputs. | [Hello Interview, Meta's AI-enabled coding round](https://www.hellointerview.com/blog/meta-ai-enabled-coding) | [LRU Cache](https://leetcode.com/problems/lru-cache/), [Merge Intervals](https://leetcode.com/problems/merge-intervals/) |

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Minimum edits to make a parentheses string valid. | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) |
| Dot product of two sparse vectors, with follow-up on one vector being dense. | [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) (Premium) |
| Sample an index in proportion to its weight. | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/) (Premium) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | One pass from the right, a fast warm-up. |
| 2 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Stack-based validation, a Meta staple. |
| 3 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Two pointers with one allowed skip. |
| 4 | [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) (Premium) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Sparse representation trade-offs; maps to embedding math. |
| 5 | [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) (Premium) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | DFS on a nested structure. |
| 6 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | Medium | [Timestamps and binary search](../patterns/timestamps-and-binary-search.md) | Prefix sums plus binary search; same idea as weighted sampling. |
| 7 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | Recursive tree reasoning under time pressure. |
| 8 | [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Hard | [Graph traversal (BFS and DFS)](../patterns/graphs-bfs-dfs.md) | BFS with ordering rules, tests attention to detail. |
| 9 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Prefix-sum hashing, comes back in many forms. |
| 10 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Heap versus quickselect discussion. |
| 11 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | [Intervals](../patterns/intervals.md) | Sort and sweep. |
| 12 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Operator precedence without recursion. |

## Practical exercises in this repo

- [Rate limiter for an LLM API](../practical/03-llm-rate-limiter/)
- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)

## More on the loop

- [landed's Meta interview guide](https://www.landed.jobs/resources/guides/meta-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-meta): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Meta and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-meta).
