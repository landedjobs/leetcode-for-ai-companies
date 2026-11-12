# Bank ledger with scheduled payments and merges

[Back to all practical exercises](../README.md)

**Where this comes from.** Bank and ledger builds are a common shape for leveled online assessments, and Anthropic's reported prompts include writing code to a spec and refactoring as constraints arrive. This exercise is Representative of that format. See [Anthropic](../../companies/anthropic.md) and [Scale AI](../../companies/scale-ai.md).

**Time box.** 90 minutes for all four levels.

This is an original exercise written for this repo. It follows the leveled format AI labs use: finish a level, then the next one adds requirements. Do not read the next level until the current one passes.

## Setup

Build `Bank`, an in-memory ledger. Every method receives `now`, a non-decreasing integer timestamp. Amounts are positive integers.

## Level 1: accounts and transfers

- `create_account(now, account_id)` returns `True`, or `False` if the id is taken.
- `deposit(now, account_id, amount)` returns the new balance, or `None` if the account does not exist.
- `transfer(now, source, target, amount)` moves money and returns the source's new balance. Return `None` for missing accounts, the same account, or insufficient funds.

## Level 2: ranking

- `top_spenders(now, n)` returns up to `n` accounts as `"id(total_outgoing)"`, sorted by outgoing total descending, ties by id ascending. Outgoing counts transfers out and, from level 3, paid scheduled payments.

## Level 3: scheduled payments

- `schedule_payment(now, account_id, amount, delay)` returns an id `"payment1"`, `"payment2"`, ... and runs the payment at `now + delay`. Payments due at the same time run in creation order. A payment that cannot be covered fails and is skipped.
- `cancel_payment(now, account_id, payment_id)` returns `True` if that account's payment was still pending.
- `payment_status(now, payment_id)` returns `scheduled`, `paid`, `failed`, `cancelled` or `None`.
- Process every due payment before handling any call at time `now`.

## Level 4: merges and history

- `merge_accounts(now, keep, absorb)` moves balance, outgoing total and pending payments from `absorb` into `keep`, then removes `absorb`.
- `balance_at(now, account_id, time_at)` returns the balance at `time_at`, or `None` if the account did not exist then.

## Example

```python
b = Bank()
b.create_account(1, "a"); b.create_account(2, "b")
b.deposit(3, "a", 500)
b.transfer(4, "a", "b", 200)        # 300
pid = b.schedule_payment(5, "a", 100, 10)
b.payment_status(15, pid)           # "paid"
b.balance_at(16, "a", 14)           # 300
```

## What a strong solution shows

- A single `_process_due(now)` call at the top of every public method, backed by a heap keyed on `(due_time, sequence)`.
- Balance history appended on every change, so `balance_at` is a binary search and not a replay.
- An alias map for merged accounts, so payments scheduled on the absorbed id still resolve.
- Deterministic tie-breaking everywhere. Hidden tests depend on it.

## LeetCode problems that train it

| Problem | Difficulty |
|---|---|
| [Simple Bank System](https://leetcode.com/problems/simple-bank-system/) | Medium |
| [Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/) (Premium) | Medium |
| [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium |
| [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium |
| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium |

## Reference solution

[`solution.py`](solution.py) solves all four levels in plain Python 3.10+ with no dependencies. Run it to execute the checks:

```bash
python practical/02-bank-ledger/solution.py
```

Write your own version first. Then compare how each structure handled the jump between levels.
