# Concurrency

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Make correct code run on several threads or tasks at once. The reported version is almost always a crawler or a queue: fetch in parallel, never fetch the same URL twice, know when you are done. LeetCode's concurrency set is small but it drills the primitives: locks, conditions, semaphores and queues.

## Where it shows up

- Sourced reports: [Anthropic](../companies/anthropic.md), [OpenAI](../companies/openai.md), [Databricks](../companies/databricks.md), [NVIDIA](../companies/nvidia.md).
- Also on the problem lists for: [Mistral AI](../companies/mistral.md).
- Signal: **High** (4 companies with a sourced report).

## How to approach it

- Write the single-threaded version first and keep it. Interviewers usually ask for it before the concurrent one.
- Keep shared state owned by one thread when you can. A coordinator that submits work and collects futures avoids most locking bugs.
- Termination is the trap. Track in-flight work explicitly, not by checking whether a queue is empty.
- In Python, say when threads help (I/O-bound fetching) and when they do not (CPU-bound work under the GIL).

## Template

```python
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait


def crawl(start, fetch_links, workers=8):
    seen = {start}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {pool.submit(fetch_links, start)}
        while pending:
            done, pending = wait(pending, return_when=FIRST_COMPLETED)
            for fut in done:
                for url in fut.result():
                    if url not in seen:
                        seen.add(url)
                        pending.add(pool.submit(fetch_links, url))
    return seen
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium) | Medium | [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md) |
| 2 | [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | Medium | [Anthropic](../companies/anthropic.md), [Databricks](../companies/databricks.md), [Mistral AI](../companies/mistral.md) |
| 3 | [Print in Order](https://leetcode.com/problems/print-in-order/) | Easy | [NVIDIA](../companies/nvidia.md) |
| 4 | [Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/) | Medium | General practice |
| 5 | [The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/) | Medium | [NVIDIA](../companies/nvidia.md) |
| 6 | [Building H2O](https://leetcode.com/problems/building-h2o/) | Medium | General practice |
| 7 | [Fizz Buzz Multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/) | Medium | General practice |

## Practical exercises that use it

- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)
- [Rate limiter for an LLM API](../practical/03-llm-rate-limiter/)
