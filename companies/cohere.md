# Cohere coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Cohere's public reports focus more on ML depth than on specific coding questions. The coding prompt we can source is a practical build: use the Cohere API to make a small application. The LeetCode list below covers what such builds lean on: ranking, merging, text processing and caching. Prompts without a link are Representative.

## Round format

- Reported practical build: a sample application on the Cohere API ([landed question page](https://www.landed.jobs/resources/questions/use-the-cohere-api-to-build-a-sample-application-aiq-0145?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-cohere-api)).
- Expect Python, clean HTTP and data handling, and questions on how you would test and evaluate the result.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Use the Cohere API to build a sample application. | [landed question page](https://www.landed.jobs/resources/questions/use-the-cohere-api-to-build-a-sample-application-aiq-0145?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-cohere-api) | [LRU Cache](https://leetcode.com/problems/lru-cache/), [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) |

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Rerank retrieved passages and return the top k. | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Train and run a small subword tokenizer. | [Word Break](https://leetcode.com/problems/word-break/), [Decode String](https://leetcode.com/problems/decode-string/) |
| Deduplicate near-identical documents before indexing. | [Group Anagrams](https://leetcode.com/problems/group-anagrams/), [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Top-k is the shape of every rerank step. |
| 2 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Nearest neighbours by distance, the toy version of vector search. |
| 3 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Merge results from several indexes. |
| 4 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Canonical keys for deduplication. |
| 5 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | [Rate limiting and sliding windows](../patterns/rate-limiting-and-sliding-windows.md) | Sliding window over text. |
| 6 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Safe framing for batched text. |
| 7 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | [Serialization and iterators](../patterns/serialization-and-iterators.md) | Consuming nested or streamed responses lazily. |
| 8 | [Decode String](https://leetcode.com/problems/decode-string/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | Stack-based text expansion. |
| 9 | [Word Break](https://leetcode.com/problems/word-break/) | Medium | [Dynamic programming](../patterns/dynamic-programming.md) | Segmentation, the idea behind subword tokenisation. |
| 10 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Caching API calls. |

## Practical exercises in this repo

- [Byte-level BPE tokenizer](../practical/06-bpe-tokenizer/)
- [Rate limiter for an LLM API](../practical/03-llm-rate-limiter/)

## More on the loop

- [landed's Cohere interview guide](https://www.landed.jobs/resources/guides/cohere-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-cohere): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Cohere and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-cohere).
