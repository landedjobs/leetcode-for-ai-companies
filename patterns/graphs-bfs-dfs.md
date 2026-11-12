# Graph traversal (BFS and DFS)

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Breadth-first and depth-first search over explicit graphs, grids and implicit graphs like web links. A crawler is BFS with a visited set. Weighted paths are Dijkstra. Most AI-lab prompts that look like systems questions reduce to one of these once you strip the I/O.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md), [Databricks](../companies/databricks.md), [Perplexity](../companies/perplexity.md).
- Also on the problem lists for: [Google DeepMind](../companies/google-deepmind.md), [Meta](../companies/meta.md), [xAI](../companies/xai.md).
- Signal: **High** (4 companies with a sourced report).

## How to approach it

- Mark nodes visited when you enqueue them, not when you pop them. It prevents duplicate work and matches what concurrent versions need.
- Prefer iterative traversal when inputs can be large. Python's default recursion limit is 1000.
- For weighted graphs, say why BFS is wrong and reach for a heap.

## Template

```python
import heapq
from collections import deque


def bfs(start, neighbors):
    seen = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in neighbors(node):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return order


def dijkstra(source, edges):
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue
        for nxt, w in edges.get(node, []):
            nd = d + w
            if nd < dist.get(nxt, float("inf")):
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Web Crawler](https://leetcode.com/problems/web-crawler/) (Premium) | Medium | [Anthropic](../companies/anthropic.md) |
| 2 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | [Perplexity](../companies/perplexity.md) |
| 3 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | [Perplexity](../companies/perplexity.md) |
| 4 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | [Google DeepMind](../companies/google-deepmind.md) |
| 5 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | [Google DeepMind](../companies/google-deepmind.md) |
| 6 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | [Google DeepMind](../companies/google-deepmind.md), [Databricks](../companies/databricks.md) |
| 7 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | [Databricks](../companies/databricks.md) |
| 8 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | General practice |
| 9 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | General practice |
| 10 | [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium | [Perplexity](../companies/perplexity.md) |

## Practical exercises that use it

- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)
