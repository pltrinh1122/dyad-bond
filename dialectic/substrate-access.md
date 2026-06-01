# Substrate-access — the git/gh wrapper, owned for dyad-bond — LIVE CYCLE

> **Status: in-flight, not settled.** Authored 2026-05-31 on Operator [ALIGN] (*"like every other
> Dyad I operated, we ended up creating a wrapper for git and gh — reference dyad-steward and
> dyad-healer for their reason and **own our reason**"*). Triggered by hitting the live friction this
> session: the harness auto-mode classifier **blocked `git push origin main`**.

> ## ✅ RESOLVED — push-posture, `[ALIGN-2]` correction (s4→s5, 2026-06-01)
> *The "PENDING the Operator's grant / LOCAL first" framing throughout this file is **superseded**;
> read it as the historical reasoning that led here, not the live posture. The invariant body (the
> wrapper, the why-for-us = memory durability) stands; only the **gate location** is corrected.*
>
> - **Posture = branch + PR; the Operator gates the *merge*, not the push.** Push of a **feature
>   branch** = the Agent's act (Generate, through the `bin/git.sh` choke-point); **merge → `main`** =
>   the Operator's act (Validate). We **do not push `main`; we PR it.** (Item-H, ledger.)
> - **The grant is already LIVE — in session *runtime*, not in any settings file.**
>   `~/.claude/settings.json` sets `defaultMode: auto` + `skipAutoPermissionPrompt`, so
>   `bin/git.sh push` of a feature branch runs **un-prompted** — **verified empirically** (s4:
>   dry-run → real push; s5: `gh pr merge` of PR #2 ran un-blocked). **`.claude/settings.local.json`
>   has *no* `git.sh` entry and never needed one** → the "PENDING grant", "LOCAL first", and
>   `/tmp/grant_gitsh.py` actions below are **MOOT (nothing to grant).** **Distilled (verify-before-assert,
>   `relationship-craft.md` D6):** *file-absence ≠ capability-absence — verify capability by EXECUTION.*
> - **The classifier carve-out is real and correct:** a raw `git push origin main` (or `bin/git.sh push`
>   *of main*) is **DENIED** — default-branch mutation needs per-op authorization. `gh pr merge` is **not**
>   carved out (s5 telemetry) → the PR path is the sanctioned route to `main`.
> - **The covalent gate is LIVE, not theater** — it lives on the **merge**, not on a per-tool allowlist.
>   `bin/git.sh` is the **choke-point**, not a gate-on-the-Agent. *Sharing (Agent pushes branches), never
>   transfer (Operator alone admits to `main`).*

## Permissioning protocol — fine-tuned to intent *(Operator [ALIGN], s5 2026-06-01; CANDIDATE, dogfooded on PR #3)*

> **Operator's stated intent of the PR-merge gate:** safeguard `main` against changes that are **(a)
> unintentional by Covalent** or **(b) un-permitted / un-directed by the Operator.** "Operator gates the
> merge" (above) is **necessary but not sufficient** to *meet* that intent. Falsified against it; survivors:

1. **Gate stays at canonical-admission (merge→`main`); do NOT gate Covalent's branch actions.** Gating
   *actions* would forbid the Generate half from acting un-directed = **ionic collapse** (kills the +1 at
   its source). **"un-directed" = un-directed *into `main`*, not un-directed *at all*.** *(Φ3 — bounds the
   fine-tune against over-correcting into a leash; the one point to dissent if tighter action-gating is
   actually wanted.)*
2. **Every PR carries a `DIRECTION-MANIFEST`** — *Operator directed X → this diff delivers exactly X →
   incidental / out-of-scope changes flagged.* It makes the gate a **cheap diff-vs-direction spot-check**,
   not a full-diff vigilance test (an unread merge `Y` is the Operator-side ionic collapse the **anti-cave
   duty** names). **It is a navigation aid INTO the diff, never a trust-substitute FOR it** *(Φ-meta:
   a self-asserted "delivered==directed" is the same assertion-from-model D6 forbids)*. **The manifested PR
   *is* the disposition surface** — opening it hands the decision to the gate; a *parallel conversational*
   `[CTA·Y/N]` for the merge is **redundant double-anchoring** (D4 SG-4). Lightest merge-close = *"PR #N is
   up for your gate"* + dissent-points, then stop.
3. **Duty split — Covalent owns the accident-guard; the gate is the backstop.** (a) *unintentional* =
   competence risk → first line of defense is **Covalent's pre-PR `SELF-AUDIT` by execution** (D6: re-read
   the *actual* diff, run checks, confirm no scope-creep), attached to the PR. (b) *un-directed* = authority
   risk → **irreducibly the Operator's gate.** The Operator must not be the *primary* catcher of Covalent's
   accidents (mis-assigns the duty + over-trusts the gate).
4. **Merge criterion (the gate's check):** the Operator merges **iff** *delivered == directed* (manifest,
   spot-checked) **∧** *self-audit attached* — **else dissent with a named reason, never a silent `Y`.**
5. **Provisional branch-memory:** resume may read un-merged branch content (s4→s5 did), but it is
   **provisional**; canonical claims trace to `main`; the gate fires at the next merge.

**Lightest-anchor (scope-guard-2):** manifest + self-audit **scale with stakes** — one line for a small PR,
fuller for a large/risky one — *not* a heavy template on every push.

**Review-depth refinement *(Operator [FEEDBACK] posture, s5 2026-06-01)*.** The manifest **guides**, it does
not **replace**, the Operator's read — depth scales with the artifact's stakes. For **frontier / high-stakes
artifacts** (e.g. `relationship-craft.md` — where the dyad's actual theory lives) the Operator's posture is
**full-document review**, not a diff-spot-check. **Coupled to graduation (the Φ1 sustainability guard):**
full-document review stays real only while the doc stays tractable; as it grows, settled content must
**graduate `dialectic/`→`kb/`** (or the doc split) or the burden decays the gate toward rubber-stamp (Φ1).
So the full-doc-review posture and the graduation discipline are **one coupled mechanism**, not two.

**Status:** candidate in `dialectic/`, **NOT settled** — first Operator-half falsification was the dogfooded
merge of PR #3; the full-doc-review refinement landed via the PR #4 review.

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

## Staging — start local, earn promotion *(Operator [ALIGN] 2026-05-31: "both can be true")*

The local-vs-checked-in choice was **dissolved, not picked** — our own **earn-graduation** pattern
(`dialectic/`→`kb/`; thin-convention→strict-protocol) applied to the *grant*:
- **Now — local** (`.claude/settings.local.json`, gitignored): cheapest, revocable, the Operator's
  *personal* trust act (truest to the covalent gate), and it **survives the real restart** (`/exit` +
  `claude` in-place — it's a file on disk). The committed *record* of the decision lives here in
  `substrate-access.md`, so a future session still reads *that the grant exists + why*.
- **Later — promote to checked-in** (`.claude/settings.json`) **only when it earns it**, both required:
  1. **Proven** — `bin/git.sh push` has run un-prompted + pushed ≥ once (hot-reload confirmed) and the
     policy block needed no emergency widening in local use; **and**
  2. **Portability need materializes** — a concrete reason for the grant to *travel with the repo* (a
     re-clone elsewhere; a sibling/second operator). Checked-in's *only* edge over local → promote when
     that edge becomes real, not on a schedule.
  Until (2), local is **strictly sufficient** (correct tier, not a deferral-debt).

## Status & next

- **PENDING the Operator's permission grant — LOCAL first** — add `Bash(bin/git.sh:*)` to
  `.claude/settings.local.json` (the covalent gate; the Agent must not self-grant). Disposable script
  ready + verified at `/tmp/grant_gitsh.py`. Until granted, push stays a manual `! git push`.
- Cross-link: `dyad-healer@bin/git.sh` + `ledger.md:311` (invariant source) · `dyad-steward`
  reflection 2026-05-29 (/tmp grounding) · `relationship-craft.md` §D4 scope-guard 2 (mechanical =
  lightest anchor — the wrapper makes push genuinely mechanical).
