# Dependency graphs and topological sort

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Things depend on other things: spreadsheet cells, tasks in a to-do list, build steps. You need a valid order, a way to recompute what changed, and cycle detection. Kahn's algorithm (indegree plus queue) gives both order and cycle detection in one pass.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Perplexity](../companies/perplexity.md), [Scale AI](../companies/scale-ai.md).
- Also on the problem lists for: no other companies.
- Signal: **Medium** (3 companies with a sourced report).

## How to approach it

- Store edges in the direction you will traverse them. For recompute-on-change you want dependents, not dependencies.
- Check for a cycle before you commit a change, so a rejected update leaves the old state intact.
- Large final tests often include deep chains. Use an iterative traversal or raise the recursion limit and say why.

## Template

```python
from collections import defaultdict, deque


def topo_order(nodes, edges):
    indegree = {n: 0 for n in nodes}
    out = defaultdict(list)
    for before, after in edges:
        out[before].append(after)
        indegree[after] += 1
    queue = deque(n for n in nodes if indegree[n] == 0)
    order = []
    while queue:
        n = queue.popleft()
        order.append(n)
        for m in out[n]:
            indegree[m] -= 1
            if indegree[m] == 0:
                queue.append(m)
    if len(order) != len(indegree):
        raise ValueError("cycle")
    return order
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | [Perplexity](../companies/perplexity.md) |
| 2 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | [OpenAI](../companies/openai.md), [Scale AI](../companies/scale-ai.md), [Perplexity](../companies/perplexity.md) |
| 3 | [Parallel Courses](https://leetcode.com/problems/parallel-courses/) (Premium) | Medium | [Perplexity](../companies/perplexity.md) |
| 4 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (Premium) | Hard | General practice |
| 5 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Medium | General practice |
| 6 | [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) (Premium) | Hard | [OpenAI](../companies/openai.md) |
| 7 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | General practice |

## Practical exercises that use it

- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)
