# Intervals

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Ranges with a start and an end: bookings, evaluation windows, time slots, IP ranges. Sort by start, then sweep and merge. Multi-part prompts typically add inserts, deletes and queries on top of the merged set.

## Where it shows up

- Sourced reports: [Scale AI](../companies/scale-ai.md), [OpenAI](../companies/openai.md).
- Also on the problem lists for: [Google DeepMind](../companies/google-deepmind.md), [Meta](../companies/meta.md).
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Confirm whether ends are inclusive. `[1, 2]` and `[2, 3]` merge in some prompts and not in others.
- When the set changes over time, keep it sorted and use binary search to find neighbours.
- Counting overlaps is a sweep over +1/-1 events, not pairwise comparison.

## Template

```python
def merge(intervals):
    out = []
    for start, end in sorted(intervals):
        if out and start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out


def max_overlap(intervals):
    events = sorted([(s, 1) for s, _ in intervals] + [(e, -1) for _, e in intervals])
    best = cur = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | [Google DeepMind](../companies/google-deepmind.md), [Meta](../companies/meta.md), [Scale AI](../companies/scale-ai.md) |
| 2 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | [Scale AI](../companies/scale-ai.md) |
| 3 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Premium) | Easy | General practice |
| 4 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium) | Medium | [OpenAI](../companies/openai.md) |
| 5 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) (Premium) | Hard | [Scale AI](../companies/scale-ai.md) |
| 6 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | General practice |
| 7 | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | Medium | [Scale AI](../companies/scale-ai.md) |
| 8 | [Range Module](https://leetcode.com/problems/range-module/) | Hard | General practice |
| 9 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Medium | General practice |
| 10 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | General practice |
