# Bit manipulation

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Masks, shifts and popcounts. Rare at most labs, common at NVIDIA systems teams and in Databricks reports (IP to CIDR, bit-level compression). If you have not touched it in a while, one evening with the problems below is enough.

## Where it shows up

- Sourced reports: [NVIDIA](../companies/nvidia.md), [Databricks](../companies/databricks.md).
- Also on the problem lists for: no other companies.
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Know the four moves: test `x >> i & 1`, set `x | 1 << i`, clear `x & ~(1 << i)`, lowest set bit `x & -x`.
- Python integers are unbounded, so mask with `& 0xFFFFFFFF` when the prompt assumes 32 bits.
- Say how you would write the same thing in C++ if the role is low-level.

## Template

```python
def get_bits(x, start, width):
    return (x >> start) & ((1 << width) - 1)


def set_bits(x, start, width, value):
    mask = ((1 << width) - 1) << start
    return (x & ~mask) | ((value << start) & mask)


def popcount(x):
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | [NVIDIA](../companies/nvidia.md) |
| 2 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | [NVIDIA](../companies/nvidia.md) |
| 3 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | [NVIDIA](../companies/nvidia.md) |
| 4 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [NVIDIA](../companies/nvidia.md) |
| 5 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | [NVIDIA](../companies/nvidia.md) |
| 6 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Easy | [NVIDIA](../companies/nvidia.md) |
| 7 | [Design Bitset](https://leetcode.com/problems/design-bitset/) | Medium | [NVIDIA](../companies/nvidia.md) |
| 8 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) (Premium) | Medium | [Databricks](../companies/databricks.md) |
