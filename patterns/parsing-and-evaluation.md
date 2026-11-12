# Parsing and expression evaluation

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Turn text into structure and then compute with it: paths, formulas, JSON-like input, stack traces, Markdown. Every version has the same two steps, a tokenizer and a parser. A small recursive-descent parser handles precedence and nesting with code you can explain line by line.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Anthropic](../companies/anthropic.md), [Scale AI](../companies/scale-ai.md), [Cursor (Anysphere)](../companies/cursor.md).
- Also on the problem lists for: [Meta](../companies/meta.md), [Cohere](../companies/cohere.md).
- Signal: **High** (4 companies with a sourced report).

## How to approach it

- Separate tokenising from parsing. Bugs in one are much easier to find when the other is already tested.
- Write the grammar as two or three lines of comments before coding: `expr = term (('+'|'-') term)*`.
- Stacks handle nesting when the grammar is small (brackets, paths). Recursion reads better when there is precedence.

## Template

```python
import re

TOKENS = re.compile(r"\s*(\d+|[-+*/()])")


def evaluate(expr):
    tokens = TOKENS.findall(expr)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def take():
        nonlocal pos
        pos += 1
        return tokens[pos - 1]

    def parse_expr():
        value = parse_term()
        while peek() in ("+", "-"):
            value = value + parse_term() if take() == "+" else value - parse_term()
        return value

    def parse_term():
        value = parse_factor()
        while peek() in ("*", "/"):
            value = value * parse_factor() if take() == "*" else int(value / parse_factor())
        return value

    def parse_factor():
        tok = take()
        if tok == "(":
            value = parse_expr()
            take()
            return value
        if tok == "-":
            return -parse_factor()
        return int(tok)

    return parse_expr()
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | General practice |
| 2 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Medium | [Meta](../companies/meta.md) |
| 3 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) (Premium) | Hard | General practice |
| 4 | [Decode String](https://leetcode.com/problems/decode-string/) | Medium | [Cohere](../companies/cohere.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 5 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | General practice |
| 6 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Medium | [Scale AI](../companies/scale-ai.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 7 | [Number of Atoms](https://leetcode.com/problems/number-of-atoms/) | Hard | General practice |
| 8 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | [OpenAI](../companies/openai.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 9 | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | Medium | [Anthropic](../companies/anthropic.md) |
| 10 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Medium | [Meta](../companies/meta.md) |

## Practical exercises that use it

- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)
- [Byte-level BPE tokenizer](../practical/06-bpe-tokenizer/)
