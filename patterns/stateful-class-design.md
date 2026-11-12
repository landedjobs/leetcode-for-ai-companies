# Stateful class design

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

You write a class that owns some state and exposes a handful of methods. The algorithm is usually easy. The difficulty is keeping two or three structures consistent while requirements change: a dict for lookup, a linked list or heap for order, a history list for time travel. This is the single most common shape in AI-lab coding rounds, because it looks like real backend work and grows naturally into levels.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md), [xAI](../companies/xai.md), [Scale AI](../companies/scale-ai.md), [Databricks](../companies/databricks.md), [Perplexity](../companies/perplexity.md), [Cursor (Anysphere)](../companies/cursor.md).
- Also on the problem lists for: [Cohere](../companies/cohere.md), [Mistral AI](../companies/mistral.md), [NVIDIA](../companies/nvidia.md), [Hugging Face](../companies/hugging-face.md).
- Signal: **High** (7 companies with a sourced report).

## How to approach it

- Write the method signatures and the invariants first. Say out loud which structure is the source of truth.
- Route every write through one private helper so later levels (TTL, history, merges) change one place.
- Return values and error cases matter. Ask what to return for a missing key before you code.
- Run a short scripted scenario after each method. Graders in leveled rounds use hidden tests just like that.

## Template

```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = OrderedDict()

    def get(self, key):
        if key not in self.items:
            return -1
        self.items.move_to_end(key)
        return self.items[key]

    def put(self, key, value):
        if key in self.items:
            self.items.move_to_end(key)
        self.items[key] = value
        if len(self.items) > self.capacity:
            self.items.popitem(last=False)
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md), [xAI](../companies/xai.md), [Databricks](../companies/databricks.md), [Perplexity](../companies/perplexity.md), [Cohere](../companies/cohere.md), [Mistral AI](../companies/mistral.md), [Cursor (Anysphere)](../companies/cursor.md), [Hugging Face](../companies/hugging-face.md) |
| 2 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | [xAI](../companies/xai.md), [Mistral AI](../companies/mistral.md) |
| 3 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | [Anthropic](../companies/anthropic.md) |
| 4 | [All O'one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | Hard | [Anthropic](../companies/anthropic.md) |
| 5 | [Design SQL](https://leetcode.com/problems/design-sql/) | Medium | [OpenAI](../companies/openai.md) |
| 6 | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/) | Medium | [Anthropic](../companies/anthropic.md) |
| 7 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) (Premium) | Hard | [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 8 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | [xAI](../companies/xai.md) |
| 9 | [Design Memory Allocator](https://leetcode.com/problems/design-memory-allocator/) | Medium | [NVIDIA](../companies/nvidia.md) |
| 10 | [Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/) (Premium) | Medium | General practice |

## Practical exercises that use it

- [In-memory record store with TTL and backups](../practical/01-kv-store-with-ttl/)
- [Bank ledger with scheduled payments and merges](../practical/02-bank-ledger/)
