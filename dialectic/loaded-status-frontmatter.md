---
locus: phenotype   # bond's own harness-adjacent tooling proposal — not yet built, not yet used. Key → MAP.md.
---

# Loaded-status front-matter — a `loaded:` key, CANDIDATE (dialectic/, NOT settled, n=2)

> **Spawned from a live miss, 2026-07-04:** explaining Dyad-UI's role, the Agent read `dyad-ui.md` in full
> (rich, unloaded design-reasoning) and asserted it as "the signal/surface" — even though the file's own
> body twice states the operational reference lives in `GLOSSARY.md` (boot-loaded) instead. The caveat was
> *in the file*, in prose, and still didn't survive into the summary claim. Root cause named at the time:
> detail-richness stood in for operative-status — the file read most thoroughly felt authoritative,
> independent of whether it's actually live at boot.

## The candidate

A **`loaded:`** front-matter key, parallel to the existing `locus:` key (`MAP.md`'s scheme), stating
**where in the read-cycle a file actually enters context** — scannable *before* the body, not
reconstructed from prose that may or may not get propagated correctly:

- `boot` — harness-injected or shim-instructed-immediate-read, every session: `CLAUDE.md`/`GEMINI.md`
  (harness system-reminder) + `DYAD.md` (the shim's own "Read immediately"). Matches `standup.sh`'s
  `ANCHOR_FILES` exactly — no more, no less.
- `resume-protocol` — read as part of the standard resume path (`carry-forward.md §How to resume`) but
  not harness-enforced: `GLOSSARY.md` (the `DYAD.md §Frame` pointer — **corrected from an earlier `boot`
  guess, see Open question 1**), `carry-forward.md` itself, the disciplines-index, `theory-pipeline.yaml`.
- `active-fetch` — consulted only when the matching activity happens: `generation-distillations.md` (on
  generate), `commission-template.md` (on "commission:") — both already self-describe this way in prose.
- `on-demand` — everything else, `dialectic/`'s default: read only if grepped for or explicitly pointed
  to (`dyad-ui.md`, `rom-ui.md`, this file).

## N — validated, not asserted (2026-07-04)

**Front-matter instances: zero.** Scanned every file with a genuine YAML block in the repo — only
`locus:` (provenance axis), `MAP.md`/`README.md`'s derived-view keys, and `dm/` message headers exist.
No prior front-matter attempt at loaded-status. `loaded:` would be the first of its kind structurally.

**Phenomenon instances: two, independent.** Clause 2's floor counts occurrences of the *pattern*, not
prior formalization attempts (`discipline-lint.py`'s own founding case was a first attempt too):
1. **2026-07-03, the token/mode-gate redesign arc** (`relationship-craft.md:2012-2013`) — *"`GLOSSARY.md`
   made the self-sufficient operational reference (`dyad-ui.md` wasn't boot-loaded, a real, named
   cost)"* — a prior session's own encounter with this exact fact costing something, independent of
   today.
2. **2026-07-04, today** — the reach-error that spawned this file, same fact, missed anyway despite #1
   already on record.
- **Not counted** (related genus, not this species — flagged rather than folded in to avoid inflating
  n): the `d-reflect` presentation-drift retro (`relationship-craft.md:2070-2073`), named *"the same
  exact conflation... just at a different layer"* — a broader definition-vs-practice pattern, not
  specifically about loaded-status.
- **Bonus:** the value-set isn't invented from these two either — `carry-forward.md`'s own resume
  protocol already independently uses `active fetch, not a resume pre-load` for two separate targets,
  and `boot` is already mechanically real (`standup.sh`'s `ANCHOR_FILES`). The taxonomy converges with
  existing usage rather than proposing categories from n=1.

**Conceded:** n≥2 holds for the shape. Per clause 2, formalizing it (writing the key) is no longer
premature on the count. Per clauses 1+4, a **linter remains a separate, later, still-ungated decision**
— this concession unlocks the front-matter, not automation.

## Why (the failure this targets)

`locus:` answers *"is this ours to claim?"* — a fact about **provenance**. It says nothing about
**reach** — whether a file is actually in a fresh session's context at the moment a claim about it gets
made. The miss above was a reach error wearing a provenance-shaped file (`dyad-ui.md` correctly says
`locus: phenotype` — that was never in question). A `loaded:` tag would let the check happen as a
grep/front-matter read, the same class of win `locus:` already delivers for the claim axis.

## The tradeoff (named, not hidden)

This is **another single-home fact to keep in sync** — the same risk class `RESTART-PENDING` and the
`inv:rom-currency` per-file line already exist to guard against (both of which have gone stale in this
ledger before, most recently caught this session's own resume). Worse: unlike `locus:`, nothing currently
*validates* a `loaded:` claim against reality — `bin/invariant-eval.py` gates `locus` via schema; a
`loaded:` tag would ship un-gated, so a stale or wrong tag could sit unnoticed, arguably worse than no
tag (a confidently-wrong structural signal beats an absent one only if it's checked). **Mechanization is
the load-bearing open question, not the tag's existence** — an un-mechanized `loaded:` key risks becoming
exactly the kind of prose-caveat-nobody-propagates it's meant to replace, just relocated to YAML.

## Open questions (attack surface, converge-open)

1. **RESOLVED, 2026-07-04:** `GLOSSARY.md` is `resume-protocol`, not `boot` — `dyad-ui.md` calling it
   "boot-loaded" was aspirational, not mechanically true (`standup.sh`'s `ANCHOR_FILES` never included
   it; empirically this session `GLOSSARY.md` was `Read` on-demand at the topic's first mention, not
   present from turn one the way `CLAUDE.md`/`DYAD.md` were). The schema above reflects the correction.
2. **Mechanization — still open, deliberately.** Does a validator (extending `bin/invariant-eval.py` or
   a sibling script, CI-wired) check a `loaded:` claim against real session behavior, or does it ship as
   an honor-system tag? n≥2 unlocks writing the *key*; it does not unlock this — clauses 1/4 of the
   mechanism-building discipline gate the linter as a separate, later decision (see "N — validated"
   above). Un-mechanized, a wrong tag can sit unnoticed, same risk class as `inv:rom-currency` going
   stale.
3. **Scope — still open.** Every `dialectic/`+`kb/` file, or only the ones already explicit about their
   own loaded-status in prose? The four worked examples below are the provable-first slice; wider
   rollout is a separate disposition.

## Worked examples (the decidable core, for review)

| File | `loaded:` | Why |
|---|---|---|
| `DYAD.md` | `boot` | shim-instructed immediate read, every session |
| `GLOSSARY.md` | `resume-protocol` | `DYAD.md §Frame` pointer; read early by convention, not harness-injected |
| `dialectic/generation-distillations.md` | `active-fetch` | already self-describes this way; consulted on generate |
| `dialectic/dyad-ui.md` | `on-demand` | design-reasoning; this session's own reach-error target |

## Falsifiable claim

A `loaded:` front-matter key reduces reach-errors (asserting a file's content is live/operative when it
isn't, or vice versa) below the rate of relying on prose caveats alone. **Test:** the next time an Agent
(this one or a fresh instance) needs to state whether some file is "the" operative reference for a topic,
does it check the tag first — and does the tag, when checked, match reality? **Refuted if:** the tag goes
stale the same way `inv:rom-currency` already has (asserted once, never re-verified), or if writing tags
consumes more attention than the reach-errors it prevents (over-production, the tell already flagged
several times this corpus — Q1 above is itself evidence this could go either way).

## Status

**CANDIDATE · `dialectic/` · NOT settled · n=2 (validated)** — shape conceded formalizable, schema
drafted with 4 worked examples. **Operator `Y` 2026-07-04: all 4 worked examples applied** —
`DYAD.md@boot` (the anchor's first-ever front-matter block — a new precedent, not just a new key),
`GLOSSARY.md@resume-protocol`, `dialectic/generation-distillations.md@active-fetch`,
`dialectic/dyad-ui.md@on-demand`. Mechanization (a linter/CI) remains explicitly deferred — a separate,
later, still-ungated decision (Open question 2, unchanged). Wider rollout past these 4 is a separate
disposition. Spawn: `loaded-status-frontmatter`.
