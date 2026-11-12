# Serialization and iterators

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Encode state so it survives a round trip, and walk a structure lazily so you can stop and resume. Both show up in store prompts ("now persist it") and in data-pipeline prompts ("now stream it"). The key idea for encoding is length prefixes, which make any byte safe. For iterators it is keeping just enough state to produce the next element.

## Where it shows up

- Sourced reports: [OpenAI](../companies/openai.md), [Databricks](../companies/databricks.md).
- Also on the problem lists for: [Cohere](../companies/cohere.md), [Cursor (Anysphere)](../companies/cursor.md), [Hugging Face](../companies/hugging-face.md).
- Signal: **Medium** (2 companies with a sourced report).

## How to approach it

- Never rely on a delimiter that can appear in the data. Prefix each item with its length.
- For iterators, implement `has_next` by preparing the next item, not by peeking into internal lists.
- State the format version in your encoding if the interviewer hints at later changes.

## Template

```python
def encode(items):
    return "".join(f"{len(s)}:{s}" for s in items)


def decode(blob):
    out, i = [], 0
    while i < len(blob):
        j = blob.index(":", i)
        n = int(blob[i:j])
        out.append(blob[j + 1:j + 1 + n])
        i = j + 1 + n
    return out


class ResumableIterator:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def state(self):
        return self.pos

    def restore(self, pos):
        self.pos = pos

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.data):
            raise StopIteration
        self.pos += 1
        return self.data[self.pos - 1]
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) | Medium | [OpenAI](../companies/openai.md), [Cohere](../companies/cohere.md), [Hugging Face](../companies/hugging-face.md) |
| 2 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | [OpenAI](../companies/openai.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 3 | [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) | Medium | General practice |
| 4 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | [OpenAI](../companies/openai.md), [Cohere](../companies/cohere.md), [Hugging Face](../companies/hugging-face.md) |
| 5 | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Medium | [OpenAI](../companies/openai.md), [Hugging Face](../companies/hugging-face.md) |
| 6 | [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/) (Premium) | Medium | General practice |
| 7 | [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/) (Premium) | Medium | General practice |
| 8 | [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/) (Premium) | Easy | General practice |
| 9 | [String Compression](https://leetcode.com/problems/string-compression/) | Medium | [Databricks](../companies/databricks.md) |

## Practical exercises that use it

- [In-memory record store with TTL and backups](../practical/01-kv-store-with-ttl/)
