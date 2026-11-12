"""Reference solution for the in-memory record store exercise (levels 1 to 4).

Run `python solution.py` to execute the checks at the bottom.
"""

from bisect import insort


class RecordStore:
    def __init__(self):
        self._data = {}
        self._backups = []

    def _live(self, key, now):
        record = self._data.get(key)
        if record is None:
            return None
        expired = [f for f, (_, exp) in record.items() if exp is not None and exp <= now]
        for field in expired:
            del record[field]
        if not record:
            del self._data[key]
            return None
        return record

    # Level 1
    def set(self, now, key, field, value):
        return self.set_with_ttl(now, key, field, value, None)

    def get(self, now, key, field):
        record = self._live(key, now)
        if record is None or field not in record:
            return None
        return record[field][0]

    def delete(self, now, key, field):
        record = self._live(key, now)
        if record is None or field not in record:
            return False
        del record[field]
        if not record:
            del self._data[key]
        return True

    # Level 2
    def scan(self, now, key):
        record = self._live(key, now)
        if record is None:
            return []
        return [f"{f}({v})" for f, (v, _) in sorted(record.items())]

    def scan_prefix(self, now, key, prefix):
        record = self._live(key, now)
        if record is None:
            return []
        return [f"{f}({v})" for f, (v, _) in sorted(record.items()) if f.startswith(prefix)]

    # Level 3
    def set_with_ttl(self, now, key, field, value, ttl):
        if ttl is not None and ttl <= 0:
            raise ValueError("ttl must be positive")
        self._live(key, now)
        expires_at = None if ttl is None else now + ttl
        self._data.setdefault(key, {})[field] = (value, expires_at)
        return True

    # Level 4
    def backup(self, now):
        snapshot = {}
        for key in list(self._data):
            record = self._live(key, now)
            if record is None:
                continue
            snapshot[key] = {
                f: (v, None if exp is None else exp - now)
                for f, (v, exp) in record.items()
            }
        insort(self._backups, (now, snapshot), key=lambda b: b[0])
        return len(snapshot)

    def restore(self, now, timestamp_to_restore):
        chosen = None
        for taken_at, snapshot in self._backups:
            if taken_at <= timestamp_to_restore:
                chosen = snapshot
            else:
                break
        if chosen is None:
            raise LookupError("no backup at or before that timestamp")
        self._data = {
            key: {
                f: (v, None if remaining is None else now + remaining)
                for f, (v, remaining) in fields.items()
            }
            for key, fields in chosen.items()
        }


def _checks():
    s = RecordStore()
    s.set(1, "user:1", "name", "ada")
    s.set(2, "user:1", "email", "ada@example.com")
    assert s.get(3, "user:1", "name") == "ada"
    assert s.delete(4, "user:1", "name") is True
    assert s.delete(4, "user:1", "name") is False
    assert s.get(5, "user:1", "name") is None

    s.set(6, "user:1", "emoji", "x")
    s.set(6, "user:1", "email_verified", "yes")
    assert s.scan(7, "user:1") == ["email(ada@example.com)", "email_verified(yes)", "emoji(x)"]
    assert s.scan_prefix(7, "user:1", "email") == ["email(ada@example.com)", "email_verified(yes)"]

    s.set_with_ttl(10, "session", "token", "abc", 5)
    assert s.get(14, "session", "token") == "abc"
    assert s.get(15, "session", "token") is None
    assert s.scan(15, "session") == []

    s.set_with_ttl(20, "cache", "hot", "1", 10)
    assert s.backup(22) == 2
    s.delete(23, "cache", "hot")
    s.restore(100, 22)
    assert s.get(107, "cache", "hot") == "1"
    assert s.get(108, "cache", "hot") is None
    assert s.get(108, "user:1", "email") == "ada@example.com"
    print("all record store checks passed")


if __name__ == "__main__":
    _checks()
