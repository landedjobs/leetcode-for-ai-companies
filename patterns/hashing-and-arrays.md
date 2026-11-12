# Hashing and arrays

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Hash maps, prefix sums and two pointers. These are the warm-ups and the building blocks inside every larger prompt. The reported AI-lab versions are data chores: find duplicate files by content, group rows from a CSV, count events per key.

## Where it shows up

- Sourced reports: [Anthropic](../companies/anthropic.md), [Scale AI](../companies/scale-ai.md).
- Also on the problem lists for: [Meta](../companies/meta.md), [Cohere](../companies/cohere.md), [Cursor (Anysphere)](../companies/cursor.md), [Hugging Face](../companies/hugging-face.md).
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Pick a canonical key: sorted letters, a content hash, a normalised URL. Most grouping problems are just that.
- Prefix sums with a hash map turn "subarray with property X" from O(n^2) into O(n).
- Say what happens with memory at scale, and when you would stream instead of loading everything.

## Template

```python
import hashlib
from collections import defaultdict


def group_by_content(files):
    """files: dict of path -> bytes. Returns lists of paths with identical content."""
    groups = defaultdict(list)
    for path, data in files.items():
        groups[hashlib.sha256(data).hexdigest()].append(path)
    return [paths for paths in groups.values() if len(paths) > 1]


def count_subarrays_with_sum(nums, k):
    seen = defaultdict(int)
    seen[0] = 1
    total = count = 0
    for x in nums:
        total += x
        count += seen[total - k]
        seen[total] += 1
    return count
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | General practice |
| 2 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Scale AI](../companies/scale-ai.md), [Cohere](../companies/cohere.md), [Hugging Face](../companies/hugging-face.md) |
| 3 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | [Meta](../companies/meta.md) |
| 4 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | General practice |
| 5 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Medium | [Anthropic](../companies/anthropic.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 6 | [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) (Premium) | Medium | [Meta](../companies/meta.md) |
| 7 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | [Meta](../companies/meta.md) |
| 8 | [Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/) (Premium) | Medium | [Meta](../companies/meta.md) |
