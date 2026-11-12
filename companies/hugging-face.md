# Hugging Face coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Hugging Face's public reports lean toward ML depth, and we could not tie a specific coding question to a public source, so the prompts below are Representative. The company ships open-source libraries, so expect to be judged on code other people can read and extend, and on text-processing fundamentals.

## Round format

- No sourced description of the coding format. Prepare for practical Python on text and data, plus questions about API design and tests.

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Train a byte-pair encoding tokenizer and round-trip text through it. | [Word Break](https://leetcode.com/problems/word-break/), [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) |
| Stream a large dataset in batches without loading it into memory. | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/), [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) |
| Cache downloaded model files with a size limit. | [LRU Cache](https://leetcode.com/problems/lru-cache/) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Word Break](https://leetcode.com/problems/word-break/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | Segmentation with a vocabulary. |
| 2 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | Counting segmentations. |
| 3 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Lossless framing of arbitrary text. |
| 4 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Lazy iteration over nested data. |
| 5 | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Batching needs lookahead. |
| 6 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | [Tries and string search](../patterns/tries-and-strings.md) | Vocabulary lookups. |
| 7 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Grouping by canonical key. |
| 8 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Size-limited caches. |
| 9 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Merging sharded outputs. |
| 10 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Counting tokens and picking the top merges. |

## Practical exercises in this repo

- [Byte-level BPE tokenizer](../practical/06-bpe-tokenizer/)

## More on the loop

- [landed's Hugging Face interview guide](https://www.landed.jobs/resources/guides/hugging-face-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-hugging-face): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Hugging Face and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-hugging-face).
