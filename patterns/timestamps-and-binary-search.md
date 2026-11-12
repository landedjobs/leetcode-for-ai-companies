# Timestamps and binary search

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Store values with a timestamp or version and answer "what was true at time t". Appends arrive in time order, so each key keeps a sorted list and reads use binary search. The same move powers snapshots, backups, TTL expiry and audit history, which is why it keeps appearing in the later levels of store prompts.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md).
- Also on the problem lists for: [Google DeepMind](../companies/google-deepmind.md), [Meta](../companies/meta.md), [xAI](../companies/xai.md), [Databricks](../companies/databricks.md).
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Ask whether timestamps are strictly increasing per key. If yes, append and bisect. If not, you need insort or a sorted container.
- Decide the boundary: is a value set at t visible at t? Most prompts say yes, so use `bisect_right(...) - 1`.
- For expiry, store `expires_at` and check it on read. Lazy deletion is simpler than a background sweep and fine in an interview.

## Template

```python
from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key, value, timestamp):
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key, timestamp):
        i = bisect_right(self.times[key], timestamp) - 1
        return self.values[key][i] if i >= 0 else ""
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md) |
| 2 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md), [xAI](../companies/xai.md), [Databricks](../companies/databricks.md) |
| 3 | [Stock Price Fluctuation ](https://leetcode.com/problems/stock-price-fluctuation/) | Medium | General practice |
| 4 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | Medium | [Meta](../companies/meta.md) |
| 5 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | General practice |
| 6 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | General practice |
| 7 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | General practice |
| 8 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | [Google DeepMind](../companies/google-deepmind.md) |

## Practical exercises that use it

- [In-memory record store with TTL and backups](../practical/01-kv-store-with-ttl/)
- [Bank ledger with scheduled payments and merges](../practical/02-bank-ledger/)
