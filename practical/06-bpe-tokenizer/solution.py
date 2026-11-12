"""Reference solution for the byte-level BPE tokenizer exercise (levels 1 to 4).

Run `python solution.py` to execute the checks at the bottom.
"""

import re
from collections import Counter

PRETOKEN = re.compile(r" ?[A-Za-z]+| ?[0-9]+| ?[^\sA-Za-z0-9]+|\s+")


def pair_counts(words):
    counts = Counter()
    for word, freq in words.items():
        for a, b in zip(word, word[1:]):
            counts[(a, b)] += freq
    return counts


def merge_word(word, pair, new_id):
    out, i = [], 0
    while i < len(word):
        if i + 1 < len(word) and (word[i], word[i + 1]) == pair:
            out.append(new_id)
            i += 2
        else:
            out.append(word[i])
            i += 1
    return tuple(out)


class BPETokenizer:
    def __init__(self, special_tokens=()):
        self.merges = {}
        self.vocab = {i: bytes([i]) for i in range(256)}
        self.special = {}
        for tok in special_tokens:
            self.add_special(tok)

    # Level 1
    def train(self, text, vocab_size):
        words = Counter(tuple(chunk.encode("utf-8")) for chunk in PRETOKEN.findall(text))
        next_id = max(self.vocab) + 1
        while len(self.vocab) < vocab_size:
            counts = pair_counts(words)
            if not counts:
                break
            pair = max(counts, key=lambda p: (counts[p], -p[0], -p[1]))
            if counts[pair] < 2:
                break
            self.merges[pair] = next_id
            self.vocab[next_id] = self.vocab[pair[0]] + self.vocab[pair[1]]
            words = Counter({merge_word(w, pair, next_id): f for w, f in words.items()})
            next_id += 1
        for tok in list(self.special):
            self.special[tok] = None
            self.add_special(tok)

    # Level 2
    def _encode_chunk(self, chunk):
        ids = list(chunk.encode("utf-8"))
        while len(ids) > 1:
            ranked = [(self.merges[p], i) for i, p in enumerate(zip(ids, ids[1:])) if p in self.merges]
            if not ranked:
                break
            rank, _ = min(ranked)
            pair = next(p for p, v in self.merges.items() if v == rank)
            ids = list(merge_word(tuple(ids), pair, rank))
        return ids

    def encode(self, text):
        if not self.special:
            return [i for chunk in PRETOKEN.findall(text) for i in self._encode_chunk(chunk)]
        pattern = "(" + "|".join(re.escape(t) for t in sorted(self.special, key=len, reverse=True)) + ")"
        out = []
        for part in re.split(pattern, text):
            if part in self.special:
                out.append(self.special[part])
            elif part:
                out.extend(i for chunk in PRETOKEN.findall(part) for i in self._encode_chunk(chunk))
        return out

    # Level 3
    def decode(self, ids):
        inverse = {v: k for k, v in self.special.items()}
        buf = bytearray()
        for i in ids:
            if i in inverse:
                buf.extend(inverse[i].encode("utf-8"))
            elif i in self.vocab:
                buf.extend(self.vocab[i])
            else:
                raise KeyError(f"unknown token id {i}")
        return buf.decode("utf-8", errors="replace")

    # Level 4
    def add_special(self, token):
        if self.special.get(token) is not None:
            return self.special[token]
        new_id = max(list(self.vocab) + [v for v in self.special.values() if v is not None]) + 1
        self.special[token] = new_id
        return new_id


def _checks():
    corpus = "low lower lowest newer newest wider widest " * 20
    tok = BPETokenizer()
    tok.train(corpus, vocab_size=280)
    assert len(tok.vocab) <= 280 and len(tok.merges) > 0

    ids = tok.encode("lowest newer")
    assert len(ids) < len("lowest newer".encode("utf-8"))
    assert tok.decode(ids) == "lowest newer"

    for text in ["unseen words 123!", "naïve café", "emoji 🙂 ok", ""]:
        assert tok.decode(tok.encode(text)) == text

    tok2 = BPETokenizer(special_tokens=["<|eot|>"])
    tok2.train(corpus, vocab_size=270)
    eot = tok2.special["<|eot|>"]
    assert eot not in tok2.vocab
    ids = tok2.encode("lower<|eot|>wider")
    assert eot in ids and ids.count(eot) == 1
    assert tok2.decode(ids) == "lower<|eot|>wider"
    assert tok2.encode("<|eot|>") == [eot]
    print("all tokenizer checks passed")


if __name__ == "__main__":
    _checks()
