# Byte-level BPE tokenizer

[Back to all practical exercises](../README.md)

**Where this comes from.** Tokenizer implementation comes up as an ML-flavoured coding task in candidate recaps (for example the xAI recap linked from [xAI](../../companies/xai.md)) and fits Cohere, Hugging Face and Mistral roles. This exercise is Representative. See [Cohere](../../companies/cohere.md) and [Hugging Face](../../companies/hugging-face.md).

**Time box.** 60 to 75 minutes.

This is an original exercise written for this repo. It follows the leveled format AI labs use: finish a level, then the next one adds requirements. Do not read the next level until the current one passes.

## Setup

Build a byte-level byte-pair encoding tokenizer. The base vocabulary is the 256 byte values, so any UTF-8 text can be encoded.

## Level 1: train

- Split text into chunks (words with an optional leading space, numbers, punctuation runs, whitespace runs).
- Repeatedly merge the most frequent adjacent pair of token ids within chunks into a new id until the vocabulary reaches `vocab_size` or no pair appears twice. Break ties by the smaller pair.

## Level 2: encode

- Encode new text by applying learned merges in the order they were learned (lowest new id first).

## Level 3: decode

- Decode ids back to text. `decode(encode(t)) == t` for any string, including accents and emoji.

## Level 4: special tokens

- Support special tokens such as `<|eot|>` that are never split, are never produced by merges, and get ids after the learned vocabulary.

## Example

```python
tok = BPETokenizer(special_tokens=["<|eot|>"])
tok.train(corpus, vocab_size=300)
ids = tok.encode("lower<|eot|>wider")
tok.decode(ids)   # "lower<|eot|>wider"
```

## What a strong solution shows

- Merges stored as an ordered mapping from pair to new id, so encode can replay them by rank.
- Counting pairs over a word-frequency table, not over the raw corpus, so training stays fast.
- Byte-level base vocabulary, which makes round-trip work for every string.
- Special tokens split out before chunking, with ids that cannot collide with merges.

## LeetCode problems that train it

| Problem | Difficulty |
|---|---|
| [Word Break](https://leetcode.com/problems/word-break/) | Medium |
| [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium) | Medium |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium |
| [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium |
| [Decode String](https://leetcode.com/problems/decode-string/) | Medium |

## Reference solution

[`solution.py`](solution.py) solves all four levels in plain Python 3.10+ with no dependencies. Run it to execute the checks:

```bash
python practical/06-bpe-tokenizer/solution.py
```

Write your own version first. Then compare how each structure handled the jump between levels.
