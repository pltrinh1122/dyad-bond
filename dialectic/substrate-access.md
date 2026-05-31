# Substrate-access — the git/gh wrapper, owned for dyad-bond — LIVE CYCLE

> **Status: in-flight, not settled.** Authored 2026-05-31 on Operator [ALIGN] (*"like every other
> Dyad I operated, we ended up creating a wrapper for git and gh — reference dyad-steward and
> dyad-healer for their reason and **own our reason**"*). Triggered by hitting the live friction this
> session: the harness auto-mode classifier **blocked `git push origin main`**.

## The invariant — inherited, triangulated, NOT re-derived *(D1)*

Every sibling Dyad independently converged on a git substrate-access wrapper → **convergence = invariant**
(D1's test: independent derivation that converges is invariant, not particular). So we **inherit the
proven structure** rather than re-falsify it (re-deriving would be the thread-G trap):

- **The shared reason** *(healer `ledger.md:311`, verbatim):* "push-to-`main` is recurring friction
  (every session) but the auto-mode classifier blocks **both** a direct push **and** the Agent
  self-granting a `git push` permission (**Self-Modification**)."
- **The proven design** *(healer falsified 3 — monolithic / policy-split / native-only — and
  synthesized):* **declared-policy single-file wrapper · permission-gated · fail-closed.** The harness
  grants the **narrow** `Bash(bin/git.sh:*)`, never broad `git`. Boundary integrity = **ratified edits**
  to the policy block (chat-as-gate), not file perms.
- **Sibling-grounding hygiene** *(steward):* fetch remote/sibling state to **`/tmp`, locals untouched**;
  durable state lives **off `/tmp`**. Plus *infra-scan at Stand Up* for no-remote / unpushed-history —
  **we already practice this** (remote-sync was checked at this session's stand-up). Convergence noted.

## Owning *our* reason — the particular, authored under our gate *(D1)*

The invariant is shared; the **why-for-us** is not healer's. Healer needs the wrapper for
**boundary-integrity against foreign *patient* substrates** — *not ours* (we operate on our own repo).

**Our reason = memory durability for the relationship-craft.** This session established that the
**disk-ledger is the dyad's cross-`/exit` memory** and the **remote is its only off-disk backup**.
Therefore *unpushed history = an ungrounded memory* — a standing threat to the **research substrate our
method reads** (the observational method's Axis-1 telemetry *is* "the record we are already writing").
For a Dyad whose telos is the lived interior craft and whose evidence is its own trace, **losing the
trace is losing the experiment.** That is why *we* automate this friction — not boundary-defense, but
**substrate-continuity for the craft.**

**Our covalent gate (NON-NEGOTIABLE applied).** A self-edit-able push tool could let the Agent route
around the Operator (ionic collapse). Guard, two-part, both Operator-held:
1. **Policy is Operator-governed** — the `ALLOWED_OPS` / `PROTECTED_BRANCHES` / `FORCE_FLAGS` block is
   widened only by *ratified* edits (chat-as-gate).
2. **The permission grant is the Operator's act** — `Bash(bin/git.sh:*)` is added to settings **by the
   Operator**, never an Agent self-grant (the move the classifier correctly blocks).
   → The Agent gets the choke-point; widening it stays the Operator's. *Sharing, not transfer.*

## What was built (v0.1) — verified

`bin/git.sh` — mechanism adopted from `dyad-healer@bin/git.sh` (the invariant), header + reason
re-authored for us. **Policy: `ALLOWED_OPS=(push)`, `PROTECTED_BRANCHES=(main)`, force-flags refused on
main, fail-closed.** Dry-run verified 2026-05-31 (4 paths): push→`push origin main`; force-on-main
REFUSED; non-allowlisted op REFUSED; no-op REFUSED.

## Deferred — `gh` (our gate: don't over-build before friction bites)

The [ALIGN] named *git **and** gh*. But no recurring **gh-mutation** friction has bitten yet (this
session's `gh repo list` was read-only and unblocked). Per steward's own *premature-optimization /
wu-wei* guard: **`bin/gh.sh` follows the identical structure, instantiated on the first recurring gh
friction** — not pre-built as an empty wrapper (that's ceremony for zero ops). Slot documented; trigger =
a gh-mutation the classifier blocks, ≥ recurring.

## Falsifiable claim

The wrapper closes the push-to-main friction **once the Operator grants `Bash(bin/git.sh:*)`**: thereafter
`bin/git.sh push` runs with no classifier block and no per-push ceremony (mechanical → lightest anchor,
per D4 scope-guard 2). **Refuted if:** the grant doesn't hot-reload / still prompts (→ healer saw it
hot-reload mid-session); or the policy block proves too coarse for a real case (→ promote toward healer's
policy/mechanism split when op-count justifies); or push friction turns out *not* recurring for us (→ the
Operator's cross-Dyad evidence says it is; pose only if our own record contradicts).

## Status & next

- **PENDING the Operator's permission grant** — add `Bash(bin/git.sh:*)` to `.claude/settings.json`
  (the covalent gate; the Agent must not self-grant). Until then, push stays a manual `! git push`.
- Cross-link: `dyad-healer@bin/git.sh` + `ledger.md:311` (invariant source) · `dyad-steward`
  reflection 2026-05-29 (/tmp grounding) · `relationship-craft.md` §D4 scope-guard 2 (mechanical =
  lightest anchor — the wrapper makes push genuinely mechanical).
