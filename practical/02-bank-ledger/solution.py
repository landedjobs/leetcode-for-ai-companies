"""Reference solution for the bank ledger exercise (levels 1 to 4).

Run `python solution.py` to execute the checks at the bottom.
"""

import heapq
from bisect import bisect_right
from dataclasses import dataclass, field


@dataclass
class Account:
    created_at: int
    balance: int = 0
    outgoing: int = 0
    history: list = field(default_factory=list)


class Bank:
    def __init__(self):
        self._accounts = {}
        self._scheduled = []
        self._payments = {}
        self._payment_seq = 0
        self._merged_into = {}

    def _record(self, account_id, now):
        acct = self._accounts[account_id]
        acct.history.append((now, acct.balance))

    def _process_due(self, now):
        while self._scheduled and self._scheduled[0][0] <= now:
            due, seq, payment_id = heapq.heappop(self._scheduled)
            payment = self._payments[payment_id]
            if payment["status"] != "scheduled":
                continue
            account_id = self._resolve(payment["account"])
            acct = self._accounts.get(account_id)
            if acct is None or acct.balance < payment["amount"]:
                payment["status"] = "failed"
                continue
            acct.balance -= payment["amount"]
            acct.outgoing += payment["amount"]
            payment["status"] = "paid"
            self._record(account_id, due)

    def _resolve(self, account_id):
        while account_id in self._merged_into:
            account_id = self._merged_into[account_id]
        return account_id

    # Level 1
    def create_account(self, now, account_id):
        self._process_due(now)
        if account_id in self._accounts or account_id in self._merged_into:
            return False
        self._accounts[account_id] = Account(created_at=now)
        self._record(account_id, now)
        return True

    def deposit(self, now, account_id, amount):
        self._process_due(now)
        acct = self._accounts.get(account_id)
        if acct is None:
            return None
        acct.balance += amount
        self._record(account_id, now)
        return acct.balance

    def transfer(self, now, source, target, amount):
        self._process_due(now)
        if source == target or source not in self._accounts or target not in self._accounts:
            return None
        src, dst = self._accounts[source], self._accounts[target]
        if src.balance < amount:
            return None
        src.balance -= amount
        src.outgoing += amount
        dst.balance += amount
        self._record(source, now)
        self._record(target, now)
        return src.balance

    # Level 2
    def top_spenders(self, now, n):
        self._process_due(now)
        ranked = sorted(self._accounts.items(), key=lambda kv: (-kv[1].outgoing, kv[0]))
        return [f"{aid}({acct.outgoing})" for aid, acct in ranked[:n]]

    # Level 3
    def schedule_payment(self, now, account_id, amount, delay):
        self._process_due(now)
        if account_id not in self._accounts:
            return None
        self._payment_seq += 1
        payment_id = f"payment{self._payment_seq}"
        self._payments[payment_id] = {"account": account_id, "amount": amount, "status": "scheduled"}
        heapq.heappush(self._scheduled, (now + delay, self._payment_seq, payment_id))
        return payment_id

    def cancel_payment(self, now, account_id, payment_id):
        self._process_due(now)
        payment = self._payments.get(payment_id)
        if payment is None or payment["status"] != "scheduled":
            return False
        if self._resolve(payment["account"]) != self._resolve(account_id):
            return False
        payment["status"] = "cancelled"
        return True

    def payment_status(self, now, payment_id):
        self._process_due(now)
        payment = self._payments.get(payment_id)
        return None if payment is None else payment["status"]

    # Level 4
    def merge_accounts(self, now, keep, absorb):
        self._process_due(now)
        if keep == absorb or keep not in self._accounts or absorb not in self._accounts:
            return False
        kept, gone = self._accounts[keep], self._accounts.pop(absorb)
        kept.balance += gone.balance
        kept.outgoing += gone.outgoing
        self._merged_into[absorb] = keep
        self._record(keep, now)
        return True

    def balance_at(self, now, account_id, time_at):
        self._process_due(now)
        account_id = self._resolve(account_id)
        acct = self._accounts.get(account_id)
        if acct is None or time_at < acct.created_at:
            return None
        times = [t for t, _ in acct.history]
        i = bisect_right(times, time_at) - 1
        return acct.history[i][1]


def _checks():
    b = Bank()
    assert b.create_account(1, "a") and b.create_account(2, "b")
    assert not b.create_account(3, "a")
    assert b.deposit(4, "a", 500) == 500
    assert b.transfer(5, "a", "b", 200) == 300
    assert b.transfer(6, "a", "b", 1000) is None
    assert b.top_spenders(7, 2) == ["a(200)", "b(0)"]

    pid = b.schedule_payment(8, "a", 100, 10)
    assert b.payment_status(17, pid) == "scheduled"
    assert b.payment_status(18, pid) == "paid"
    assert b.balance_at(19, "a", 17) == 300
    assert b.balance_at(19, "a", 18) == 200

    pid2 = b.schedule_payment(20, "b", 50, 5)
    assert b.cancel_payment(21, "b", pid2)
    assert b.payment_status(30, pid2) == "cancelled"

    pid3 = b.schedule_payment(31, "b", 50, 5)
    assert b.merge_accounts(32, "a", "b")
    assert b.cancel_payment(33, "b", pid3)
    assert b.deposit(34, "b", 1) is None
    assert b.top_spenders(35, 1) == ["a(300)"]
    assert b.balance_at(36, "a", 32) == 400
    print("all bank ledger checks passed")


if __name__ == "__main__":
    _checks()
