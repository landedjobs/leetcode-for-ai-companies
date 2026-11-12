# Rate limiting and sliding windows

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Count or aggregate events inside a moving window. In practical rounds this is the rate limiter: per key, per window, sometimes weighted by token count for an LLM API. In LeetCode form it is the sliding-window family over arrays and strings.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Databricks](../companies/databricks.md).
- Also on the problem lists for: [Cohere](../companies/cohere.md), [Mistral AI](../companies/mistral.md).
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Pick the algorithm by the requirement: fixed window is simplest, a deque of timestamps is exact, a token bucket allows bursts and weighted costs.
- Pass `now` in as an argument. Tests become deterministic and the interviewer can probe edge cases quickly.
- Say how it works across processes: shared store, atomic increment, and what happens when the store is slow.

## Template

```python
from collections import defaultdict, deque


class SlidingWindowLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.hits = defaultdict(deque)

    def allow(self, key, now):
        q = self.hits[key]
        while q and q[0] <= now - self.window:
            q.popleft()
        if len(q) >= self.limit:
            return False
        q.append(now)
        return True
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium) | Easy | [OpenAI](../companies/openai.md), [Databricks](../companies/databricks.md), [Mistral AI](../companies/mistral.md) |
| 2 | [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) | Medium | [OpenAI](../companies/openai.md), [Mistral AI](../companies/mistral.md) |
| 3 | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) | Easy | [Databricks](../companies/databricks.md) |
| 4 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | [Mistral AI](../companies/mistral.md) |
| 5 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | General practice |
| 6 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | General practice |
| 7 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | [Cohere](../companies/cohere.md) |
| 8 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | General practice |

## Practical exercises that use it

- [Rate limiter for an LLM API](../practical/03-llm-rate-limiter/)
