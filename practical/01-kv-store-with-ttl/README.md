# In-memory record store with TTL and backups

[Back to all practical exercises](../README.md)

**Where this comes from.** Reported in leveled form at Anthropic (in-memory database with scans, expiry and history) and as time-based and persistent stores at OpenAI. xAI reports an in-memory database with transactions. See [Anthropic](../../companies/anthropic.md), [OpenAI](../../companies/openai.md), [xAI](../../companies/xai.md).

**Time box.** 90 minutes for all four levels; aim to finish level 2 inside 35.

This is an original exercise written for this repo. It follows the leveled format AI labs use: finish a level, then the next one adds requirements. Do not read the next level until the current one passes.

## Setup

Build `RecordStore`, an in-memory store of records. Each record has a key and holds fields, and each field holds a string value. Every method receives `now`, an integer timestamp. Calls arrive with non-decreasing timestamps.

## Level 1: basic records

- `set(now, key, field, value)` stores the value, creating the record if needed. Returns `True`.
- `get(now, key, field)` returns the value or `None`.
- `delete(now, key, field)` removes the field and returns `True`, or returns `False` if it did not exist. A record with no fields disappears.

## Level 2: scans

- `scan(now, key)` returns the record's fields as `"field(value)"` strings, sorted by field name. Empty list if the record does not exist.
- `scan_prefix(now, key, prefix)` does the same for fields that start with `prefix`.

## Level 3: expiry

- `set_with_ttl(now, key, field, value, ttl)` stores a field that is visible for `ttl` units: from `now` up to but not including `now + ttl`.
- Every earlier method must now ignore expired fields. Setting a field without TTL clears any earlier TTL on it.

## Level 4: backup and restore

- `backup(now)` saves the live state and returns the number of non-empty records saved. For fields with a TTL, save the remaining lifetime, not the absolute deadline.
- `restore(now, timestamp_to_restore)` replaces the state with the latest backup taken at or before `timestamp_to_restore`. Restored TTL fields expire at `now + remaining`.

## Example

```python
s = RecordStore()
s.set(1, "user:1", "email", "ada@example.com")
s.set_with_ttl(10, "session", "token", "abc", 5)
s.get(14, "session", "token")      # "abc"
s.get(15, "session", "token")      # None
s.backup(20)
s.restore(100, 20)
```

## What a strong solution shows

- One private helper that returns the live record and drops expired fields. Every public method calls it, so level 3 changes one function.
- Storing `(value, expires_at)` per field from level 1, so TTL does not force a rewrite.
- Backups that store remaining lifetime. Storing absolute deadlines is the most common level 4 bug.
- Sorted output exactly as specified. Hidden tests compare strings.

## LeetCode problems that train it

| Problem | Difficulty |
|---|---|
| [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium |
| [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium |
| [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium |
| [Design SQL](https://leetcode.com/problems/design-sql/) | Medium |
| [Min Stack](https://leetcode.com/problems/min-stack/) | Medium |

## Reference solution

[`solution.py`](solution.py) solves all four levels in plain Python 3.10+ with no dependencies. Run it to execute the checks:

```bash
python practical/01-kv-store-with-ttl/solution.py
```

Write your own version first. Then compare how each structure handled the jump between levels.
