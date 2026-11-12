# Spreadsheet with formulas and cycle detection

[Back to all practical exercises](../README.md)

**Where this comes from.** Reported at OpenAI as spreadsheet formula evaluation with dependencies and circular reference detection. Perplexity and Scale AI report dependency handling in multi-part builds. See [OpenAI](../../companies/openai.md), [Perplexity](../../companies/perplexity.md), [Scale AI](../../companies/scale-ai.md).

**Time box.** 75 minutes.

This is an original exercise written for this repo. It follows the leveled format AI labs use: finish a level, then the next one adds requirements. Do not read the next level until the current one passes.

## Setup

Build `Sheet`. Cells are named like `A1` or `AB12`. Empty cells read as `0.0`.

## Level 1: values

- `set(name, raw)` stores a number or numeric string. `get(name)` returns a float.

## Level 2: formulas

- A raw value starting with `=` is a formula with `+ - * /`, parentheses, unary minus, numbers and cell names. `=A1+B2*3` follows normal precedence.

## Level 3: dependencies

- When a cell changes, every cell that depends on it, directly or not, updates before `set` returns.
- A `set` that would create a cycle raises an error and leaves the sheet unchanged.

## Level 4: ranges

- Support `SUM(A1:B3)` inside formulas. The range is inclusive and may be written in either corner order.

## Example

```python
s = Sheet()
s.set("A1", 2); s.set("A2", 3)
s.set("B1", "=A1+A2*4")    # 14.0
s.set("A1", 10)            # B1 becomes 22.0
s.set("A1", "=B1")         # raises CycleError, A1 stays 10.0
s.set("C1", "=SUM(A1:B1)") # 32.0
```

## What a strong solution shows

- Tokenizer and parser kept apart from the dependency graph.
- Edges stored both ways: what a cell reads, and who reads it. Recompute walks the second set in topological order.
- Cycle check before mutation, so a rejected update leaves no partial state.
- Old dependency edges removed when a formula changes. Forgetting this causes phantom updates.

## LeetCode problems that train it

| Problem | Difficulty |
|---|---|
| [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/) | Medium |
| [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) (Premium) | Hard |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium |
| [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Medium |
| [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard |
| [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Medium |

## Reference solution

[`solution.py`](solution.py) solves all four levels in plain Python 3.10+ with no dependencies. Run it to execute the checks:

```bash
python practical/04-spreadsheet-formulas/solution.py
```

Write your own version first. Then compare how each structure handled the jump between levels.
