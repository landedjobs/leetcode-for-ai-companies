# Tries and string search

[Back to the patterns table](../README.md#the-patterns-that-matter)

## What it is

Prefix trees and string search. Shows up in autocomplete prompts, in vocabulary lookups for tokenizers, and in grid word search. Build the trie quickly and the rest of the problem is DFS.

## Where it shows up

- Sourced reports: [xAI](../companies/xai.md).
- Also on the problem lists for: [Google DeepMind](../companies/google-deepmind.md), [Perplexity](../companies/perplexity.md), [Cursor (Anysphere)](../companies/cursor.md), [Hugging Face](../companies/hugging-face.md).
- Signal: **Low** (1 company with a sourced report).

## How to approach it

- A dict of dicts with an end marker is enough. Do not write a node class unless you need extra fields.
- For ranked autocomplete, store the top results on each node or rank at query time; say which and why.
- Prune the trie as you find words in grid search, or the hard test cases time out.

## Template

```python
class Trie:
    END = "$"

    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.END] = True

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return []
            node = node[ch]
        out, stack = [], [(node, prefix)]
        while stack:
            node, word = stack.pop()
            for ch, child in node.items():
                if ch == self.END:
                    out.append(word)
                else:
                    stack.append((child, word + ch))
        return sorted(out)
```

## Problems

| # | Problem | Difficulty | Companies that list it |
|---|---|---|---|
| 1 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | [Google DeepMind](../companies/google-deepmind.md), [xAI](../companies/xai.md), [Hugging Face](../companies/hugging-face.md) |
| 2 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | General practice |
| 3 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | [xAI](../companies/xai.md) |
| 4 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | [xAI](../companies/xai.md) |
| 5 | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) (Premium) | Hard | [Perplexity](../companies/perplexity.md), [Cursor (Anysphere)](../companies/cursor.md) |
| 6 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | General practice |
| 7 | [Stream of Characters](https://leetcode.com/problems/stream-of-characters/) | Hard | General practice |
| 8 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Scale AI](../companies/scale-ai.md), [Cohere](../companies/cohere.md), [Hugging Face](../companies/hugging-face.md) |

## Practical exercises that use it

- [Byte-level BPE tokenizer](../practical/06-bpe-tokenizer/)
