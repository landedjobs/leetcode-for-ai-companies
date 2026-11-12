# Concurrent same-host crawler

[Back to all practical exercises](../README.md)

**Where this comes from.** Reported at Anthropic (single-threaded crawler, then concurrent) and OpenAI (multithreaded crawler with dedupe, failures and rate limits). See [Anthropic](../../companies/anthropic.md) and [OpenAI](../../companies/openai.md).

**Time box.** 60 minutes.

This is an original exercise written for this repo. It follows the leveled format AI labs use: finish a level, then the next one adds requirements. Do not read the next level until the current one passes.

## Setup

Crawl every page on the start URL's host. You get a `fetch(url)` function that returns a list of links (absolute or relative) and may raise on network errors. Do not leave the host.

## Level 1: sequential crawl

- `crawl_sequential(start, fetch)` returns every reachable same-host URL in BFS order, each once.
- Normalise URLs: resolve relative links, drop fragments, lowercase scheme and host, strip a trailing slash except on the root.

## Level 2: depth limit

- Add `max_depth`. The start page has depth 0.

## Level 3: concurrent crawl

- `crawl_concurrent(start, fetch, workers)` fetches in parallel. No URL may be fetched twice. The function must return when all work is done, without sleeping or polling.

## Level 4: failures and politeness

- Retry a failing fetch up to `retries` times, then report it as failed.
- Leave at least `per_host_interval` seconds between request starts to the same host.

## Example

```python
visited, failed = crawl_concurrent(
    "https://docs.example.com/", fetch, workers=8, retries=2, per_host_interval=0.1
)
```

## What a strong solution shows

- The visited set owned by the coordinating thread, with workers only fetching. This removes most locking.
- Completion detected by tracking in-flight futures, not by checking whether a queue is empty.
- Mark URLs seen when they are scheduled, not when they finish, or two workers fetch the same page.
- A clear answer on threads versus asyncio for I/O-bound work in Python.

## LeetCode problems that train it

| Problem | Difficulty |
|---|---|
| [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium) | Medium |
| [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) (Premium) | Medium |
| [Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) (Premium) | Medium |
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium |
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium |

## Reference solution

[`solution.py`](solution.py) solves all four levels in plain Python 3.10+ with no dependencies. Run it to execute the checks:

```bash
python practical/05-concurrent-crawler/solution.py
```

Write your own version first. Then compare how each structure handled the jump between levels.
