"""Reference solution for the spreadsheet exercise (levels 1 to 4).

Run `python solution.py` to execute the checks at the bottom.
"""

import re
from collections import defaultdict

CELL = re.compile(r"[A-Z]+[0-9]+")
TOKEN = re.compile(r"\s*(?:(\d+\.?\d*)|([A-Z]+[0-9]+:[A-Z]+[0-9]+)|(SUM)|([A-Z]+[0-9]+)|(.))")


class CycleError(ValueError):
    pass


def split_cell(name):
    m = re.fullmatch(r"([A-Z]+)([0-9]+)", name)
    col = 0
    for ch in m.group(1):
        col = col * 26 + (ord(ch) - 64)
    return col, int(m.group(2))


def join_cell(col, row):
    letters = ""
    while col:
        col, rem = divmod(col - 1, 26)
        letters = chr(65 + rem) + letters
    return f"{letters}{row}"


def expand_range(rng):
    a, b = rng.split(":")
    (c1, r1), (c2, r2) = split_cell(a), split_cell(b)
    return [join_cell(c, r) for c in range(min(c1, c2), max(c1, c2) + 1) for r in range(min(r1, r2), max(r1, r2) + 1)]


def tokenize(expr):
    tokens = []
    for num, rng, fn, cell, op in TOKEN.findall(expr):
        if num:
            tokens.append(("num", float(num)))
        elif rng:
            tokens.append(("range", rng))
        elif fn:
            tokens.append(("fn", fn))
        elif cell:
            tokens.append(("cell", cell))
        elif op.strip():
            tokens.append(("op", op))
    return tokens


class Parser:
    """Recursive descent: expr -> term (+|- term)*, term -> factor (*|/ factor)*."""

    def __init__(self, tokens, lookup):
        self.tokens = tokens
        self.pos = 0
        self.lookup = lookup

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def eat(self, kind, value=None):
        tok = self.peek()
        if tok[0] != kind or (value is not None and tok[1] != value):
            raise SyntaxError(f"expected {value or kind}, got {tok[1]}")
        self.pos += 1
        return tok[1]

    def parse(self):
        value = self.expr()
        if self.pos != len(self.tokens):
            raise SyntaxError("trailing input")
        return value

    def expr(self):
        value = self.term()
        while self.peek() in (("op", "+"), ("op", "-")):
            op = self.eat("op")
            rhs = self.term()
            value = value + rhs if op == "+" else value - rhs
        return value

    def term(self):
        value = self.factor()
        while self.peek() in (("op", "*"), ("op", "/")):
            op = self.eat("op")
            rhs = self.factor()
            value = value * rhs if op == "*" else value / rhs
        return value

    def factor(self):
        kind, val = self.peek()
        if kind == "num":
            self.pos += 1
            return val
        if kind == "cell":
            self.pos += 1
            return self.lookup(val)
        if kind == "op" and val == "-":
            self.pos += 1
            return -self.factor()
        if kind == "op" and val == "(":
            self.pos += 1
            value = self.expr()
            self.eat("op", ")")
            return value
        if kind == "fn":
            self.pos += 1
            self.eat("op", "(")
            rng = self.eat("range")
            self.eat("op", ")")
            return sum(self.lookup(c) for c in expand_range(rng))
        raise SyntaxError(f"unexpected token {val}")


def references(raw):
    if not isinstance(raw, str) or not raw.startswith("="):
        return set()
    refs = set()
    for kind, val in tokenize(raw[1:]):
        if kind == "cell":
            refs.add(val)
        elif kind == "range":
            refs.update(expand_range(val))
    return refs


class Sheet:
    def __init__(self):
        self.raw = {}
        self.values = {}
        self.deps = {}
        self.dependents = defaultdict(set)

    def get(self, name):
        return self.values.get(name, 0.0)

    def set(self, name, raw):
        new_refs = references(raw)
        if self._reaches(new_refs, name):
            raise CycleError(f"setting {name} would create a cycle")
        for ref in self.deps.get(name, set()):
            self.dependents[ref].discard(name)
        self.raw[name] = raw
        self.deps[name] = new_refs
        for ref in new_refs:
            self.dependents[ref].add(name)
        for cell in self._recompute_order(name):
            self.values[cell] = self._evaluate(cell)

    def _reaches(self, starts, target):
        stack, seen = list(starts), set()
        while stack:
            cell = stack.pop()
            if cell == target:
                return True
            if cell in seen:
                continue
            seen.add(cell)
            stack.extend(self.deps.get(cell, ()))
        return False

    def _recompute_order(self, start):
        order, visited = [], set()

        def visit(cell):
            if cell in visited:
                return
            visited.add(cell)
            for dep in self.dependents.get(cell, ()):
                visit(dep)
            order.append(cell)

        visit(start)
        return reversed(order)

    def _evaluate(self, name):
        raw = self.raw.get(name)
        if raw is None:
            return 0.0
        if isinstance(raw, (int, float)):
            return float(raw)
        if raw.startswith("="):
            return Parser(tokenize(raw[1:]), self.get).parse()
        return float(raw)


def _checks():
    s = Sheet()
    s.set("A1", 2)
    s.set("A2", "3")
    assert s.get("A1") == 2.0 and s.get("B9") == 0.0

    s.set("B1", "=A1+A2*4")
    assert s.get("B1") == 14.0
    s.set("B2", "=(A1+A2)*-2")
    assert s.get("B2") == -10.0

    s.set("A1", 10)
    assert s.get("B1") == 22.0 and s.get("B2") == -26.0
    s.set("C1", "=B1+B2")
    s.set("A2", 0)
    assert s.get("C1") == 10.0 + -20.0

    try:
        s.set("A1", "=C1")
        raise AssertionError("cycle not detected")
    except CycleError:
        pass
    assert s.get("A1") == 10.0

    s.set("D1", "=SUM(A1:B2)")
    assert s.get("D1") == 10 + 0 + 10 + -20
    s.set("B1", 1)
    assert s.get("D1") == 10 + 0 + 1 + -20
    assert expand_range("A1:B2") == ["A1", "A2", "B1", "B2"]
    assert join_cell(*split_cell("AB12")) == "AB12"
    print("all spreadsheet checks passed")


if __name__ == "__main__":
    _checks()
