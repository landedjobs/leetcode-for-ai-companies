# Rate limiter for an LLM API

[Back to all practical exercises](../README.md)

**Where this comes from.** Reported at OpenAI as "implement a rate limiter for an LLM API". Databricks reports a logger and a moving-average stream. See [OpenAI](../../companies/openai.md) and [Databricks](../../companies/databricks.md).

**Time box.** 60 minutes.

This is an original exercise written for this repo. It follows the leveled format AI labs use: finish a level, then the next one adds requirements. Do not read the next level until the current one passes.

## Setup

Protect an LLM API. Requests come from a user who belongs to an org. Time is passed in as `now` (seconds, float) so tests are deterministic.

## Level 1: request limit

- `SlidingWindowLimiter(limit, window).allow(key, now)` allows at most `limit` requests per key in any window of `window` seconds.

## Level 2: token cost

- A request now costs its token count. `TokenBucket(capacity, rate)` refills `rate` tokens per second up to `capacity`. A request is allowed only if the bucket holds at least its cost.
- `wait_time(cost, now)` returns how long until the request would fit, or `None` if it never can.

## Level 3: two tiers

- `TieredLimiter.request(user, org, cost, now)` must pass both the user's bucket and the org's bucket. If either fails, neither is charged.
- Return `(allowed, retry_after)` where `retry_after` is the longer of the two waits.

## Level 4: threads

- Many threads call `request` at once. No bucket may go negative and no request may be charged twice.
- Explain, without coding, how you would share limits across several API servers.

## Example

```python
lim = TieredLimiter(user_capacity=1000, user_rate=100, org_capacity=1500, org_rate=100)
lim.request("alice", "acme", 900, 0)    # (True, 0.0)
lim.request("bob", "acme", 900, 0)      # (False, 3.0)  org bucket has 600 left
lim.request("bob", "acme", 900, 3)      # (True, 0.0)
```

## What a strong solution shows

- Check-then-charge on both tiers inside one lock, so a failure in the org tier never leaves the user tier charged.
- Lazy refill on access instead of a timer thread.
- A clear answer for distribution: a shared store with an atomic script, or local buckets with a slice of the global budget, and what each costs.
- Handling a cost larger than capacity. It should fail fast, not wait forever.

## LeetCode problems that train it

| Problem | Difficulty |
|---|---|
| [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium) | Easy |
| [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) | Medium |
| [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) | Easy |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard |
| [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | Medium |

## Reference solution

[`solution.py`](solution.py) solves all four levels in plain Python 3.10+ with no dependencies. Run it to execute the checks:

```bash
python practical/03-llm-rate-limiter/solution.py
```

Write your own version first. Then compare how each structure handled the jump between levels.
