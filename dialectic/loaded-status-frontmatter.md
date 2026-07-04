---
locus: phenotype   # bond's own harness-adjacent tooling proposal — not yet built, not yet used. Key → MAP.md.
---

# Loaded-status front-matter — a `loaded:` key, CANDIDATE (dialectic/, NOT settled, n=0)

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

- `boot` — injected every session via the shim/anchor chain (today: `CLAUDE.md`, `DYAD.md`; arguably
  `GLOSSARY.md` by virtue of `DYAD.md §Frame`'s pointer, though see **Open question 1**).
- `resume-protocol` — read at every Stand-Up per `carry-forward.md §How to resume` (the ledger itself,
  the disciplines-index, `theory-pipeline.yaml`).
- `active-fetch` — consulted only when the matching activity happens (`generation-distillations.md` on
  generate, `commission-template.md` on "commission:").
- `on-demand` — everything else, `dialectic/`'s default: read only if grepped for or explicitly pointed to.

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

1. **Is `GLOSSARY.md` actually `boot`, or `resume-protocol`?** `dyad-ui.md` calls it "boot-loaded"; the
   harness's own ROM mechanics (`CLAUDE.md §Harness overlay`) only names `CLAUDE.md`+`DYAD.md` as
   session-boot-injected. Empirically this session: `CLAUDE.md`'s content re-appeared via
   system-reminder repeatedly; `DYAD.md`/`GLOSSARY.md` did not — both were `Read` explicitly. If
   "boot-loaded" in `dyad-ui.md` is aspirational rather than mechanically true, the new key would
   **correct** that claim on introduction, not just formalize it — worth resolving before writing the
   first tag, not after.
2. **Mechanization** — does a validator (extending `bin/invariant-eval.py`, or a sibling script) check a
   `loaded:` claim against real session behavior, or does it ship as an honor-system tag? Un-mechanized,
   this proposal's own tradeoff paragraph argues it shouldn't graduate past CANDIDATE.
3. **Scope** — every `dialectic/`+`kb/` file, or only the ones already explicit about their own
   loaded-status in prose (`dyad-ui.md`, `rom-ui.md`, several `carry-forward.md` resume-steps)? Tagging
   everything is more consistent; tagging only the ones that already say so in prose is a smaller,
   provable-first slice.

## Falsifiable claim

A `loaded:` front-matter key reduces reach-errors (asserting a file's content is live/operative when it
isn't, or vice versa) below the rate of relying on prose caveats alone. **Test:** the next time an Agent
(this one or a fresh instance) needs to state whether some file is "the" operative reference for a topic,
does it check the tag first — and does the tag, when checked, match reality? **Refuted if:** the tag goes
stale the same way `inv:rom-currency` already has (asserted once, never re-verified), or if writing tags
consumes more attention than the reach-errors it prevents (over-production, the tell already flagged
several times this corpus — Q1 above is itself evidence this could go either way).

## Status

**CANDIDATE · `dialectic/` · NOT settled · n=0** (proposed, not yet applied to a single file). Converged
here (`raff:`) as a draft for the Operator's disposition — not landed; no file has been re-tagged, no
schema extended. Spawn: `loaded-status-frontmatter`.
