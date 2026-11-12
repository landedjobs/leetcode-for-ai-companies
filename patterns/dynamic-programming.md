# Dynamic programming

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Overlapping subproblems with an order you can fill. Less common at AI labs than at big tech, but Databricks and Google-style loops still ask it, and sequence DP (edit distance, LCS) maps directly onto diffs and tokenisation.

## Where it shows up

- Sourced reports: [Databricks](../companies/databricks.md).
- Also on the problem lists for: [Google DeepMind](../companies/google-deepmind.md), [Cohere](../companies/cohere.md), [Cursor (Anysphere)](../companies/cursor.md), [Hugging Face](../companies/hugging-face.md).
- Signal: **Low** (1 company with a sourced report).

## How to approach it

- Write the state and the transition in one sentence before coding: `dp[i] = best answer using the first i items`.
- Start top-down with `functools.cache` if it is faster to get right, then convert if asked about memory.
- Sequence DP is the useful family here. Edit distance and LCS are diffs; word break is segmentation.

## Template

```python
def edit_distance(a, b):
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev = cur
    return prev[-1]
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | [Databricks](../companies/databricks.md) |
| 2 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | [Databricks](../companies/databricks.md) |
| 3 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | [Hugging Face](../companies/hugging-face.md) |
| 4 | [Word Break](https://leetcode.com/problems/word-break/) | Medium | [Cohere](../companies/cohere.md), [Hugging Face](../companies/hugging-face.md) |
| 5 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | [Google DeepMind](../companies/google-deepmind.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 6 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | [Cursor (Anysphere)](../companies/cursor.md) |
| 7 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | [Google DeepMind](../companies/google-deepmind.md) |
| 8 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | General practice |
| 9 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | General practice |
