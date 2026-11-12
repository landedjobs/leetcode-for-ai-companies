"""Reference solution for the concurrent crawler exercise (levels 1 to 4).

The fetcher is injected so tests run offline. Run `python solution.py`.
"""

import threading
import time
from collections import deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from urllib.parse import urldefrag, urljoin, urlparse


def normalize(url, base=None):
    if base:
        url = urljoin(base, url)
    url, _ = urldefrag(url)
    parts = urlparse(url)
    path = parts.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    query = f"?{parts.query}" if parts.query else ""
    return f"{parts.scheme.lower()}://{parts.netloc.lower()}{path}{query}"


def host(url):
    return urlparse(url).netloc.lower()


def crawl_sequential(start, fetch, max_depth=None):
    """Levels 1 and 2: BFS on one host, deduped, optional depth limit."""
    start = normalize(start)
    seen = {start}
    queue = deque([(start, 0)])
    order = []
    while queue:
        url, depth = queue.popleft()
        order.append(url)
        if max_depth is not None and depth >= max_depth:
            continue
        for link in fetch(url):
            nxt = normalize(link, url)
            if host(nxt) == host(start) and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, depth + 1))
    return order


class HostThrottle:
    """Level 4: at least `interval` seconds between request starts to one host."""

    def __init__(self, interval):
        self.interval = interval
        self._next_slot = {}
        self._lock = threading.Lock()

    def wait_turn(self, hostname):
        with self._lock:
            now = time.monotonic()
            slot = max(now, self._next_slot.get(hostname, now))
            self._next_slot[hostname] = slot + self.interval
        delay = slot - now
        if delay > 0:
            time.sleep(delay)


def crawl_concurrent(start, fetch, workers=8, max_depth=None, retries=2, per_host_interval=0.0):
    """Levels 3 and 4: thread pool, single-owner visited set, retries, politeness."""
    start = normalize(start)
    throttle = HostThrottle(per_host_interval)
    seen = {start}
    visited, failed = [], []

    def fetch_with_retry(url):
        for attempt in range(retries + 1):
            throttle.wait_turn(host(url))
            try:
                return fetch(url)
            except Exception:
                if attempt == retries:
                    raise
        return []

    with ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {pool.submit(fetch_with_retry, start): (start, 0)}
        while pending:
            done, _ = wait(pending, return_when=FIRST_COMPLETED)
            for fut in done:
                url, depth = pending.pop(fut)
                try:
                    links = fut.result()
                except Exception:
                    failed.append(url)
                    continue
                visited.append(url)
                if max_depth is not None and depth >= max_depth:
                    continue
                for link in links:
                    nxt = normalize(link, url)
                    if host(nxt) == host(start) and nxt not in seen:
                        seen.add(nxt)
                        pending[pool.submit(fetch_with_retry, nxt)] = (nxt, depth + 1)
    return sorted(visited), sorted(failed)


def _checks():
    site = {
        "https://docs.example.com/": ["/a", "/b#intro", "https://other.com/x"],
        "https://docs.example.com/a": ["/a/", "/c", "https://docs.example.com/b"],
        "https://docs.example.com/b": ["/c", "/flaky"],
        "https://docs.example.com/c": ["/"],
        "https://docs.example.com/flaky": [],
    }
    attempts = {}
    lock = threading.Lock()

    def fetch(url):
        with lock:
            attempts[url] = attempts.get(url, 0) + 1
            n = attempts[url]
        time.sleep(0.01)
        if url.endswith("/flaky") and n < 2:
            raise ConnectionError("transient")
        return site.get(url, [])

    order = crawl_sequential("https://docs.example.com", lambda u: site.get(u, []))
    assert order[0] == "https://docs.example.com/"
    assert set(order) == set(site)
    assert len(crawl_sequential("https://docs.example.com", lambda u: site.get(u, []), max_depth=1)) == 3

    visited, failed = crawl_concurrent("https://docs.example.com/", fetch, workers=4, retries=2)
    assert visited == sorted(site) and failed == []
    assert all(n == 1 for u, n in attempts.items() if not u.endswith("/flaky"))

    def always_fails(url):
        if url.endswith("/b"):
            raise TimeoutError()
        return site.get(url, [])

    visited, failed = crawl_concurrent("https://docs.example.com/", always_fails, retries=1)
    assert failed == ["https://docs.example.com/b"]

    began = time.monotonic()
    crawl_concurrent("https://docs.example.com/", lambda u: site.get(u, []), workers=8, per_host_interval=0.05)
    assert time.monotonic() - began >= 0.2
    print("all crawler checks passed")


if __name__ == "__main__":
    _checks()
