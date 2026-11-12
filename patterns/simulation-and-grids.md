# Simulation and grids

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Follow the rules exactly: games, boards, image transforms, text layout. There is rarely a clever insight. The round tests whether you can turn a long spec into clean state and small functions without off-by-one errors. Card games, tic-tac-toe variants and image pipelines are the reported versions.

## Where it shows up

- Sourced reports: [xAI](../companies/xai.md), [Databricks](../companies/databricks.md), [Scale AI](../companies/scale-ai.md), [Anthropic](../companies/anthropic.md).
- Also on the problem lists for: [NVIDIA](../companies/nvidia.md), [Cursor (Anysphere)](../companies/cursor.md).
- Signal: **High** (4 companies with a sourced report).

## How to approach it

- Model the state in one class and write one method per rule. Long `if` chains are where bugs hide.
- Write the tiny example from the prompt as a test first, and run it after every rule you add.
- For in-place grid updates, encode old and new state together or work on a copy, and say which.

## Template

```python
class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row, col, player):
        delta = 1 if player == 1 else -1
        self.rows[row] += delta
        self.cols[col] += delta
        if row == col:
            self.diag += delta
        if row + col == self.n - 1:
            self.anti += delta
        target = delta * self.n
        if target in (self.rows[row], self.cols[col], self.diag, self.anti):
            return player
        return 0
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) (Premium) | Medium | [Scale AI](../companies/scale-ai.md), [Databricks](../companies/databricks.md) |
| 2 | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) (Premium) | Medium | [xAI](../companies/xai.md), [Scale AI](../companies/scale-ai.md) |
| 3 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | [xAI](../companies/xai.md) |
| 4 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | [Anthropic](../companies/anthropic.md), [NVIDIA](../companies/nvidia.md) |
| 5 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | [NVIDIA](../companies/nvidia.md) |
| 6 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | [xAI](../companies/xai.md) |
| 7 | [Text Justification](https://leetcode.com/problems/text-justification/) | Hard | [xAI](../companies/xai.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 8 | [Design an ATM Machine](https://leetcode.com/problems/design-an-atm-machine/) | Medium | General practice |
| 9 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | General practice |

## Practical exercises that use it

- [Bank ledger with scheduled payments and merges](../practical/02-bank-ledger/)
