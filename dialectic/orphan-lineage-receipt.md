# Orphan-lineage cleanup receipt — verified clean *(2026-06-13)*

> **Verdict: the 5 pre-squash orphan branches carry NO unique content — safe to delete.**
> Original lineage, orphaned when `main` was re-rooted at `dbf42cd` (2026-06-03):
> `close-calibration-pr-cta`, `log-s5-cycle`, `s8-fr-response`, `stand-down-s5`, `stand-down-s8`.

## Verification *(whole-tree, content-level — NOT same-path)*
Richest tip `s8-fr-response@a3aff00` (the G/V-independence / Item-J harvest): of **145** substantive
lines, **141 present verbatim** in the current tree — chiefly `dialectic/cross-dyad-craft.md`, which
is a **superset** (extended through s14 round-trip #4 — a 4th coverage-failure mode the orphan lacks).
The 4 exact-line misses were a reformatted `F1-final` blockquote, confirmed present + extended there.
**The squash's compression was correct.** The earlier "123 absent lines" alarm was a *same-path diff
artifact* — content was relocated `relationship-craft.md → cross-dyad-craft.md`, not lost. The
parked salvage note this file replaces was therefore a false positive.

## Deletion — PENDING (Operator, GitHub-side)
Tag-push and branch-delete are both blocked (403) by the web-session git proxy, and the GitHub MCP
has no branch-delete tool → **deletion cannot be done from a web session.** `archive/*` mirror
branches were pushed before that was known → now redundant (the originals also persist and couldn't
be removed). Operator deletes manually (orphans verified clean — remove all 10):

    git push origin --delete close-calibration-pr-cta log-s5-cycle s8-fr-response stand-down-s5 stand-down-s8
    git push origin --delete archive/close-calibration-pr-cta archive/log-s5-cycle archive/s8-fr-response archive/stand-down-s5 archive/stand-down-s8

## Method — `lineage-harvest` (reusable)
For a squashed/unrelated orphan set: walk orphans by *real in-lineage ancestry* (not a diff vs main,
whose history starts after them) → collapse to dominating tip(s) → content-diff tips against the
**whole** current tree → harvest only genuinely-absent lines. Here: 4 branches ⊆ `stand-down-s8`, +1
two-commit spur (`s8-fr-response`); net unique content = zero.
