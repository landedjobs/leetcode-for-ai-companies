"""Reference solution for the LLM API rate limiter exercise (levels 1 to 4).

Time is passed in explicitly so tests are deterministic. Run `python solution.py`.
"""

import threading
from collections import defaultdict, deque


class SlidingWindowLimiter:
    """Level 1: at most `limit` requests per key in any `window` seconds."""

    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self._hits = defaultdict(deque)

    def allow(self, key, now):
        hits = self._hits[key]
        while hits and hits[0] <= now - self.window:
            hits.popleft()
        if len(hits) >= self.limit:
            return False
        hits.append(now)
        return True


class TokenBucket:
    """Level 2: a request costs its LLM token count, refilled at `rate` per second."""

    def __init__(self, capacity, rate, now=0.0):
        self.capacity = capacity
        self.rate = rate
        self.tokens = float(capacity)
        self.updated = now

    def _refill(self, now):
        if now > self.updated:
            self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
            self.updated = now

    def can_take(self, cost, now):
        self._refill(now)
        return cost <= self.tokens

    def take(self, cost):
        self.tokens -= cost

    def wait_time(self, cost, now):
        self._refill(now)
        if cost > self.capacity:
            return None
        missing = cost - self.tokens
        if missing <= 0:
            return 0.0
        return None if self.rate == 0 else missing / self.rate


class TieredLimiter:
    """Levels 3 and 4: user and org buckets must both pass; thread-safe; retry hints."""

    def __init__(self, user_capacity, user_rate, org_capacity, org_rate):
        self._user_cfg = (user_capacity, user_rate)
        self._org_cfg = (org_capacity, org_rate)
        self._users = {}
        self._orgs = {}
        self._lock = threading.Lock()

    def _bucket(self, table, key, cfg, now):
        if key not in table:
            table[key] = TokenBucket(cfg[0], cfg[1], now)
        return table[key]

    def request(self, user, org, cost, now):
        with self._lock:
            ub = self._bucket(self._users, user, self._user_cfg, now)
            ob = self._bucket(self._orgs, org, self._org_cfg, now)
            if ub.can_take(cost, now) and ob.can_take(cost, now):
                ub.take(cost)
                ob.take(cost)
                return True, 0.0
            waits = [ub.wait_time(cost, now), ob.wait_time(cost, now)]
            if None in waits:
                return False, None
            return False, max(waits)


def _checks():
    sw = SlidingWindowLimiter(limit=2, window=10)
    assert sw.allow("k", 0) and sw.allow("k", 1)
    assert not sw.allow("k", 5)
    assert sw.allow("k", 10)

    tb = TokenBucket(capacity=1000, rate=100)
    assert tb.can_take(800, 0)
    tb.take(800)
    assert not tb.can_take(500, 0)
    assert tb.wait_time(500, 0) == 3.0
    assert tb.can_take(500, 3)

    lim = TieredLimiter(user_capacity=1000, user_rate=100, org_capacity=1500, org_rate=100)
    assert lim.request("alice", "acme", 900, 0) == (True, 0.0)
    ok, wait = lim.request("bob", "acme", 900, 0)
    assert not ok and wait == 3.0
    assert lim.request("bob", "acme", 900, 3)[0]
    assert lim.request("carol", "acme", 5000, 3) == (False, None)

    lim2 = TieredLimiter(10_000, 0, 10_000, 0)
    granted = []

    def worker():
        for _ in range(100):
            if lim2.request("u", "o", 10, 0)[0]:
                granted.append(1)

    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(granted) == 800
    lim3 = TieredLimiter(100, 0, 100, 0)
    results = []
    threads = [threading.Thread(target=lambda: results.append(lim3.request("u", "o", 10, 0)[0])) for _ in range(50)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sum(results) == 10
    print("all rate limiter checks passed")


if __name__ == "__main__":
    _checks()
