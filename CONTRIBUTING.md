# Contributing

Thanks for helping map what AI companies actually ask in coding rounds. The repo is only useful if readers can trust it, so contributions clear a bar. This file is that bar.

Maintained by [Landed](https://www.landed.jobs). No affiliation with any company named in this repo.

---

## What we accept

- **Reported prompts.** A coding prompt you saw, or a public report of one, added to the right file in [`companies/`](companies/) with a link.
- **LeetCode mappings.** A better problem for a prompt, with one line on why it trains the same skill.
- **Pattern improvements.** Clearer templates or sharper problem lists in [`patterns/`](patterns/).
- **Practical exercises.** New multi-level exercises in [`practical/`](practical/), with a tested reference solution.
- **New companies.** An AI company with at least one sourced coding report.
- **Fixes.** Broken links, wrong difficulty, stale round formats, mislabeled prompts.

Coding rounds only. ML theory, system design and behavioral questions belong in [awesome-ai-engineer-interview](https://github.com/landedjobs/awesome-ai-engineer-interview).

## The rules

### 1. Every "Reported" prompt has a public link

A prompt is **Reported** only if a public page describes it at that company: a candidate post, an interview-prep write-up, an official engineering blog, or a landed question page. Paraphrase the prompt and link the page.

No public link means the prompt is **Representative**. That is fine and useful. Never present a made-up prompt as reported.

Do not paste confidential material. If you signed an NDA covering the questions, do not contribute them.

### 2. LeetCode links use the canonical slug

Use `https://leetcode.com/problems/<slug>/`. Check that the slug exists (LeetCode's GraphQL API answers `question(titleSlug: ...)`), state the difficulty as LeetCode lists it, and mark Premium problems with `(Premium)`. Every row says why the problem is relevant to the company or prompt.

### 3. Practical exercises are original

Write your own prompt and your own solution. Do not copy an assessment's text, test cases or starter code. Reference solutions:

- Plain Python 3.10+, standard library only.
- Four-space indentation, no unneeded comments.
- Checks under `if __name__ == "__main__":` that pass with `python solution.py`.

### 4. Style

- Plain, specific sentences. Sentence-case headings.
- Tables over prose for anything comparable.
- Opinions are welcome when you can back them with a report or with code.
- No promotional language in the body.

## How to contribute

1. Open an issue with a [template](.github/ISSUE_TEMPLATE/), or go straight to a PR for small fixes.
2. Fork, branch, edit.
3. Keep internal links relative (`../patterns/concurrency.md`). CI runs [lychee](.github/workflows/links.yml) on local links for every PR.
4. Fill in the [PR checklist](.github/PULL_REQUEST_TEMPLATE.md).

## Reported prompt format

Add a row to the company's "Reported prompts" table:

```markdown
| Short paraphrase of the prompt. | [Source name, date if known](https://...) | [Problem](https://leetcode.com/problems/slug/), [Problem](https://leetcode.com/problems/slug/) |
```

## Recognition

Contributors are credited in release notes.
