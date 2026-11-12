# Cursor (Anysphere) coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Cursor's loop is short on puzzles and long on real code. Reports describe one to three technical screens and a paid project day inside part of the actual codebase. The named screen problems are editor-flavoured: a streaming Markdown parser, a file-tree diff, a hash tree. Cursor does not publish its stages, so treat the details as candidate reports.

## Round format

- One to three technical screens of about 60 minutes. Early ones often restrict AI tools; later ones may use the real codebase with Cursor ([TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process)).
- Project day: a paid, roughly eight-hour build of a small feature in Cursor's codebase, then a walkthrough of trade-offs ([TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process), [Exponent, Cursor SWE guide](https://www.tryexponent.com/guides/cursor-software-engineer-interview)).
- Cursor's careers pages do not publish stages or a work-trial policy ([learncursor.dev, Cursor interview process](https://www.learncursor.dev/learn/cursor-interview/cursor-interview-process)).

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Implement a streaming Markdown parser. | [TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process) | [Decode String](https://leetcode.com/problems/decode-string/), [Mini Parser](https://leetcode.com/problems/mini-parser/) |
| Model a diff between two file trees. | [TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process) | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium), [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) |
| Build a hash tree (Merkle tree) algorithm. | [TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process) | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/), [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) |
| Implement an LRU cache. | [TechPrep, Cursor's interview process](https://www.techprep.app/blog/cursor-interview-process) | [LRU Cache](https://leetcode.com/problems/lru-cache/) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Reported directly. |
| 2 | [Decode String](https://leetcode.com/problems/decode-string/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Stack-based parsing of nested markup. |
| 3 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Recursive parsing of nested input. |
| 4 | [Text Justification](https://leetcode.com/problems/text-justification/) | Hard | [Simulation and grids](../patterns/simulation-and-grids.md) | Text layout rules, close to rendering Markdown. |
| 5 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium) | Hard | [Stateful class design](../patterns/stateful-class-design.md) | File-tree model to diff against. |
| 6 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Path normalisation for tree diffs. |
| 7 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | The core of line-level diff. |
| 8 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | Diff cost between two sequences. |
| 9 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Canonical tree encoding, needed to hash subtrees. |
| 10 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Content hashing across a tree. |
| 11 | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) (Premium) | Hard | [Tries and string search](../patterns/tries-and-strings.md) | Editor-style completion over a trie. |

## Practical exercises in this repo

- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)
- [Byte-level BPE tokenizer](../practical/06-bpe-tokenizer/)

## More on the loop

- [landed's Cursor (Anysphere) interview guide](https://www.landed.jobs/resources/guides/anysphere-cursor-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-cursor): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Cursor (Anysphere) and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-cursor).
