# Heaps and scheduling

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Use a heap whenever you repeatedly need the smallest or largest item: the next task to run, the room that frees up first, the top k results. Scheduling prompts add a clock, so the loop becomes an event simulation that pops the next event from a heap.

## Where it shows up

- Sourced reports: [Scale AI](../companies/scale-ai.md), [OpenAI](../companies/openai.md).
- Also on the problem lists for: [Google DeepMind](../companies/google-deepmind.md), [Meta](../companies/meta.md), [Perplexity](../companies/perplexity.md), [Cohere](../companies/cohere.md), [Mistral AI](../companies/mistral.md), [Hugging Face](../companies/hugging-face.md).
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Put a tie-breaker in heap entries (`(time, seq, item)`) so Python never compares the payloads.
- For top-k over n items, a size-k heap is O(n log k). Mention bucket sort when counts are bounded.
- In event simulations, advance the clock to the next event instead of ticking one unit at a time.

## Template

```python
import heapq


def run_tasks(tasks):
    """tasks: list of (enqueue_time, duration, task_id). Shortest job first when idle."""
    tasks = sorted(tasks)
    ready, order = [], []
    clock, i = 0, 0
    while i < len(tasks) or ready:
        if not ready and clock < tasks[i][0]:
            clock = tasks[i][0]
        while i < len(tasks) and tasks[i][0] <= clock:
            start, duration, tid = tasks[i]
            heapq.heappush(ready, (duration, tid))
            i += 1
        duration, tid = heapq.heappop(ready)
        clock += duration
        order.append(tid)
    return order
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | [Scale AI](../companies/scale-ai.md), [Perplexity](../companies/perplexity.md), [Mistral AI](../companies/mistral.md) |
| 2 | [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium | [Scale AI](../companies/scale-ai.md), [Mistral AI](../companies/mistral.md) |
| 3 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium) | Medium | [OpenAI](../companies/openai.md) |
| 4 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Google DeepMind](../companies/google-deepmind.md), [Scale AI](../companies/scale-ai.md), [Perplexity](../companies/perplexity.md), [Cohere](../companies/cohere.md), [Hugging Face](../companies/hugging-face.md) |
| 5 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | [Meta](../companies/meta.md) |
| 6 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | [Perplexity](../companies/perplexity.md), [Cohere](../companies/cohere.md), [Mistral AI](../companies/mistral.md), [Hugging Face](../companies/hugging-face.md) |
| 7 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | [Google DeepMind](../companies/google-deepmind.md), [Mistral AI](../companies/mistral.md) |
| 8 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | [Cohere](../companies/cohere.md) |
| 9 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | General practice |

## Practical exercises that use it

- [Bank ledger with scheduled payments and merges](../practical/02-bank-ledger/)
