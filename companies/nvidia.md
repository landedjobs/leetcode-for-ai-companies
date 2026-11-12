# NVIDIA coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

NVIDIA's coding questions depend on the team. Systems and embedded roles report bit manipulation, multithreading and C++ questions. AI software roles look closer to standard LeetCode with a performance angle. If the role touches CUDA, kernels or drivers, prepare the low-level list first.

## Round format

- A systems software report lists many bit-manipulation questions, a few multithreading questions and C++ concepts ([Taro report, Jul 2022](https://www.jointaro.com/interviews/companies/nvidia/experiences/system-software-engineer-santa-clara-ca-july-1-2022-accepted-offer-positive-80a4ae58)).
- Expect to state complexity and memory use, and to write code that would compile in C++ if asked.

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Extract or set the Nth bit of a number. | [Taro report, Jul 2022](https://www.jointaro.com/interviews/companies/nvidia/experiences/system-software-engineer-santa-clara-ca-july-1-2022-accepted-offer-positive-80a4ae58) | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/), [Reverse Bits](https://leetcode.com/problems/reverse-bits/) |
| Extract or set a group of bits in a number. | [Taro report, Jul 2022](https://www.jointaro.com/interviews/companies/nvidia/experiences/system-software-engineer-santa-clara-ca-july-1-2022-accepted-offer-positive-80a4ae58) | [Reverse Bits](https://leetcode.com/problems/reverse-bits/), [Design Bitset](https://leetcode.com/problems/design-bitset/) |
| Count the 1 bits in a number as efficiently as possible. | [Taro report, Jul 2022](https://www.jointaro.com/interviews/companies/nvidia/experiences/system-software-engineer-santa-clara-ca-july-1-2022-accepted-offer-positive-80a4ae58) | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/), [Counting Bits](https://leetcode.com/problems/counting-bits/) |

## Representative prompts

Not tied to a public report. These are prompts in the style of this company's role and product, written to practise against.

| Prompt | Train with |
|---|---|
| Allocate and free memory blocks by id from a fixed buffer. | [Design Memory Allocator](https://leetcode.com/problems/design-memory-allocator/) |
| Coordinate threads so steps run in a fixed order. | [Print in Order](https://leetcode.com/problems/print-in-order/), [The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/) |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | [Bit manipulation](../patterns/bit-manipulation.md) | Reported directly. |
| 2 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | [Bit manipulation](../patterns/bit-manipulation.md) | Popcount for a whole range with DP. |
| 3 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | [Bit manipulation](../patterns/bit-manipulation.md) | Masking and shifting groups of bits. |
| 4 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [Bit manipulation](../patterns/bit-manipulation.md) | XOR tricks. |
| 5 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | [Bit manipulation](../patterns/bit-manipulation.md) | Addition with bit operations. |
| 6 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Easy | [Bit manipulation](../patterns/bit-manipulation.md) | `n & (n - 1)`. |
| 7 | [Design Bitset](https://leetcode.com/problems/design-bitset/) | Medium | [Bit manipulation](../patterns/bit-manipulation.md) | A bitset class with flips in O(1). |
| 8 | [Design Memory Allocator](https://leetcode.com/problems/design-memory-allocator/) | Medium | [Stateful class design](../patterns/stateful-class-design.md) | Allocator logic over a flat buffer. |
| 9 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | In-place matrix work. |
| 10 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | Index arithmetic on matrices. |
| 11 | [Print in Order](https://leetcode.com/problems/print-in-order/) | Easy | [Concurrency](../patterns/concurrency.md) | Basic thread ordering. |
| 12 | [The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/) | Medium | [Concurrency](../patterns/concurrency.md) | Deadlock avoidance. |

## Practical exercises in this repo

- [Concurrent same-host crawler](../practical/05-concurrent-crawler/)

## More on the loop

- [landed's NVIDIA interview guide](https://www.landed.jobs/resources/guides/nvidia-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-nvidia): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** NVIDIA and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-nvidia).
