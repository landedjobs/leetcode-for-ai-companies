# Scale AI coding interview: LeetCode problems and practical prompts

[Back to the company index](../README.md#company-index)

Scale AI runs the multi-part format in its purest form. One problem, four to six parts, about an hour, and later parts only open once earlier ones work. Reports describe a task scheduler, an intervals and JSON processing problem, and a card game with many rules. Part one has to be correct and fast.

## Round format

- One question delivered in six parts with growing requirements, about an hour. The candidate said the round was about "how much code I could produce in an hour" ([Taro report, Nov 2022](https://www.jointaro.com/interviews/companies/scale-ai/experiences/software-engineer-united-states-november-1-2022-declined-offer-neutral-e52aaacc/)).
- A 2025 report lists intervals and JSON processing as one multi-part question ([Taro report, Jan 2025](https://www.jointaro.com/interviews/companies/scale-ai/experiences/software-engineer-new-york-new-york-january-1-2025-no-offer-positive-bce0f985)).
- ML and applied roles report data-handling tasks and work inside an unfamiliar repository ([landed question page](https://www.landed.jobs/resources/questions/read-a-text-or-csv-file-and-organize-the-contents-into-data-frames-aiq-0141?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-csv-frames), [landed question page](https://www.landed.jobs/resources/questions/write-helper-code-inside-an-unfamiliar-production-repository-aiq-0142?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-unfamiliar-repo)).

## Reported prompts

Each prompt below appears in a public source. Wording is ours; follow the link for the original report.

| Prompt | Source | Train with |
|---|---|---|
| Task scheduler with increasing requirements across six parts. | [Taro report, Nov 2022](https://www.jointaro.com/interviews/companies/scale-ai/experiences/software-engineer-united-states-november-1-2022-declined-offer-neutral-e52aaacc/) | [Task Scheduler](https://leetcode.com/problems/task-scheduler/), [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/), [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| Card game implementation with many constraints, hard to finish in 50 minutes. | [Taro report, Nov 2022](https://www.jointaro.com/interviews/companies/scale-ai/experiences/software-engineer-united-states-november-1-2022-declined-offer-neutral-e52aaacc/) | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) (Premium), [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) (Premium) |
| Intervals and JSON processing, multiple parts. | [Taro report, Jan 2025](https://www.jointaro.com/interviews/companies/scale-ai/experiences/software-engineer-new-york-new-york-january-1-2025-no-offer-positive-bce0f985) | [Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Insert Interval](https://leetcode.com/problems/insert-interval/), [Mini Parser](https://leetcode.com/problems/mini-parser/) |
| Read a text or CSV file and organise the contents into data frames. | [landed question page](https://www.landed.jobs/resources/questions/read-a-text-or-csv-file-and-organize-the-contents-into-data-frames-aiq-0141?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-csv-frames) | [Group Anagrams](https://leetcode.com/problems/group-anagrams/), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Write helper code inside an unfamiliar production repository. | [landed question page](https://www.landed.jobs/resources/questions/write-helper-code-inside-an-unfamiliar-production-repository-aiq-0142?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=question-unfamiliar-repo) | No close LeetCode match; see the note below. |

## LeetCode problems

| # | Problem | Difficulty | Pattern | Why it is relevant |
|---|---|---|---|---|
| 1 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | The textbook scheduler; reported prompt grows from here. |
| 2 | [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Event-driven scheduling with a heap, a likely later part. |
| 3 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | [Dependency graphs and topological sort](../patterns/dependency-graphs.md) | Task dependencies and cycle detection. |
| 4 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | [Intervals](../patterns/intervals.md) | Part one of most intervals prompts. |
| 5 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | [Intervals](../patterns/intervals.md) | Updating an interval set in place. |
| 6 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) (Premium) | Hard | [Intervals](../patterns/intervals.md) | Intervals across many lists. |
| 7 | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | Medium | [Intervals](../patterns/intervals.md) | Booking rules that change by part. |
| 8 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Medium | [Parsing and expression evaluation](../patterns/parsing-and-evaluation.md) | A small recursive parser, close to hand-parsing JSON. |
| 9 | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) (Premium) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | Rule-heavy game state. |
| 10 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) (Premium) | Medium | [Simulation and grids](../patterns/simulation-and-grids.md) | O(1) win checks; a good warm-up for card-game logic. |
| 11 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Hashing and arrays](../patterns/hashing-and-arrays.md) | Group-by with a hash map, the core of data-frame style tasks. |
| 12 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Heaps and scheduling](../patterns/heaps-and-scheduling.md) | Aggregations that end in a ranking. |

> [!NOTE]
> Scale's multi-part rounds reward getting part one fully passing before you touch part two. Design the data model for change, then write the simplest code that passes.

## Practical exercises in this repo

- [Bank ledger with scheduled payments and merges](../practical/02-bank-ledger/)
- [Spreadsheet with formulas and cycle detection](../practical/04-spreadsheet-formulas/)

## More on the loop

- [landed's Scale AI interview guide](https://www.landed.jobs/resources/guides/scale-ai-ai-interview-guide?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=guide-scale-ai): stages, what decides the offer, and practice questions across all rounds.
- [landed, Can you use AI in coding interviews?](https://www.landed.jobs/articles/use-ai-in-coding-interviews-2026?utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=article-ai-coding): round-by-round rules for AI tools.

---

**Open roles.** Scale AI and the other labs here post engineering openings that are tracked in [ai-lab-jobs](https://github.com/landedjobs/ai-lab-jobs). To have matching roles found and applied to for you, [set up auto-apply on landed](https://app.landed.jobs/signup?from=github&cta=github-guide-apply&item=leetcode-for-ai-companies&utm_source=github&utm_medium=referral&utm_campaign=github-leetcode-for-ai-companies&utm_content=company-scale-ai).
