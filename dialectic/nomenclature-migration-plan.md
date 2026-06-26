# Nomenclature migration plan — slug-canonical governed index

> **Status: DRAFT for Operator disposition** (drafted 2026-06-26, resume session). Proposes retiring the
> ad-hoc `D/R/X/U/S`+number IDs in favour of the `bond:<slug>` scheme the schema + machine shadow already
> use. Not executed — awaits your gate. Single-home for this proposal until disposed; folds into the
> work-item store on a Y.

## The disposition ask (TL;DR)
**Make `bond:<slug>` the single canonical ID for the whole governed corpus; demote `D/R/X/U/S`+number to a
display/citation handle (alias only), never an identity.** The class (`discipline`/`ratified`/`cross-dyad`/
`UI`/`substrate`) becomes a metadata field, not part of the ID.

## Why this is mostly *conformance*, not re-disposition

The s14 pass ratified the *invariants*; it did not ratify "the integer is the identity." Three grounded facts:

| Fact | Source | Implication |
|---|---|---|
| Schema mandates `ns:slug` IDs, corpus-unique | `invariant-schema.yaml:39` (`pattern ^[a-z0-9-]+:[A-Za-z0-9-]+$`) | `D10`/`R3`/`U1` **fail the ratified id-pattern** — they are not schema-conformant IDs |
| Numbers are display handles; slugs are stable identity | `anchor_dag_diff.py:96,103` ("§N = reading handle; edges resolve by stable `bond:` id, renumber-safe") | renumber-safety is **already designed in**; numbers were always meant to float |
| Machine shadow is 100% slug-keyed (17/17) | `invariants-bond.yaml` | tooling + source tier are slug-native; numbers exist only in the *derived* view + prose |

Net: the principle (slug-canonical) is **already decided by the ratified schema**. What is *not* yet done is
(a) extending slugs DOWN to the `D/R/X/U/S` tier (most have no yaml row yet) and (b) retiring the numbers in
prose. (a) is per-item authoring (naming = judgment → wants your rub); (b) is mechanical.

## The work, in two tiers

**Tier 1 — mechanical (conformance; Agent-disposable on a Y):**
- In `views/invariants-bond.md`: keep the table, change the `ID` column to the slug, add a `§/alias` column
  carrying the old `D#` as a **citation handle** (so existing cross-refs still resolve by lookup).
- Regenerate `views/invariants-bond.rendered.md` via the existing tool (no hand-edit).
- Update the ledger disciplines-index (`carry-forward.md` §Bond-disciplines) to lead with slugs.

**Tier 2 — per-item authoring (wants your rub; one slug at a time, or batch-rubbed):**
- Mint a slug for each numbered invariant that lacks one, and create its `invariants-bond.yaml` row so the
  machine shadow covers the full corpus (today it covers only the constitutional core).
- Two already exist and just need the alias recorded: `D10 = bond:anti-cave`, `U1 = bond:DFD`.

## Proposed alias map (`D#` → `bond:slug`) — *for your rub, not final*

| Old | Proposed slug | | Old | Proposed slug |
|---|---|---|---|---|
| D1 | `bond:inherit-vs-author` | | R1 | `bond:operator-rub` |
| D2 | `bond:incremental-shore-up` | | R2 | `bond:no-exemption` |
| D3 | `bond:reflection-form` | | R3 | `bond:standdown-ritual` |
| D4 | `bond:path-selection` | | R4 | `bond:primed-criterion` |
| D5 | `bond:response-economy` | | R5 | `bond:locus-schema` |
| D6 | `bond:verify-before-assert` | | R6 | `bond:grader-in-training` |
| D7 | `bond:valid-vs-reachable` | | X1 | `bond:oracle-coverage` |
| D8 | `bond:interpretation` | | X2 | `bond:independence-two-factor` |
| D9 | `bond:cec-ladder` | | X3 | `bond:green-check-tell` |
| D10 | `bond:anti-cave` *(exists)* | | U1 | `bond:DFD` *(exists)* |
| D11 | `bond:distinctness` | | U2 | `bond:IFD` |
| D12 | `bond:rom-ui` | | U3 | `bond:markers-habit-set` |
| | | | S1 | `bond:standing-substrate` |
| | | | S2 | `bond:no-self-grant` |
| | | | S3 | `bond:daemon-rearm` |

## Blast radius (where numbered IDs are referenced)
Grounded scan (`grep` over `*.md`/`*.yaml`, false-positives like the anchor-thesis "S1" excluded by hand at
edit time). Heaviest live carriers: `relationship-craft.md` (~60), `carry-forward-closed.md` (~82, **cold
archive — leave as historical**), `views/invariants-bond.md` (27, the index itself), `substrate-access.md`
(~12, the S-tier home), `cross-dyad-craft.md` (~10, the X-tier home), `ingraining.md`, `spaor.md`,
`dyad-ui.md`. Strategy: rewrite **live read-path + home files**; leave **closed archives + commission/
recommendation records** with the number as a frozen historical handle (an alias-map lookup covers them).

## Tooling check
- `anchor_dag_diff.py` / `invariant-eval.py` read the **yaml**, which is slug-keyed → **no tooling change
  needed** for Tier 1. Tier 2 only *adds* yaml rows (the validators already enforce the slug pattern).
- `install_hooks.py` numbered hits (`S2`, `K6`) are **prose/comments**, not keys → cosmetic only.

## Cross-dyad / Founding gate check (the real external cost)
- **`X1–X3` are cross-dyad candidates** (`cross-dyad-craft.md`). If a sibling dyad cites "bond's `X2`,"
  renaming breaks that reference → coordinate via the **Steward-Operator hat** before retiring X-numbers
  (keep `X2` as a published alias at minimum).
- **Namespace collision to resolve:** `X1 (oracle-coverage)` and `X2 (two-factor)` collide by *name* with
  CLAIM ids in `theory-pipeline.yaml` (`bond-F1-oracle-axis`, `two-factor-independence`). Claims currently
  use bare slugs **without** the `bond:` prefix; invariants use `bond:`. The schema's `unique: corpus` means
  we must decide whether claims and invariants share one namespace (then disambiguate these two) or claims get
  their own prefix (e.g. `claim:`). **Recommend: `claim:` prefix for the theory-pipeline tier** — cleanest,
  and it standardizes the claim axis too (a free win, same friction-source).
- No Founding gate for the `D`-tier (disciplines are bond-authored, not inherited form). `U`-laws are
  partly inherited but renaming the **local** id is not a form-contribution (the gate is only for proposing
  *back*). So: **Bond-Operator disposition + a Steward-hat heads-up on `X#`.**

## Risks / anti-thesis (kept live)
1. **A bad slug re-imports friction** — the map above is a first draft; some (e.g. `bond:reflection-form`,
   `bond:interpretation`) are weak. Wants your rub before it freezes. Mitigation: slugs are cheap to revise
   *before* they propagate; revise during Tier 2, not after.
2. **Partial migration is worse than none** — a half-renamed corpus has *three* schemes live at once. Mitigation:
   Tier 1 is atomic (one commit, the view + index together); Tier 2 can trickle per-item because each yaml row
   is independent and the alias keeps numbers resolving throughout.
3. **The number-as-citation-handle is genuinely useful in prose** ("see D4") — short, ordinal. Retiring it
   fully may cost more than capping it. Mitigation: we *keep* it as a display alias (the `anchor_dag_diff`
   "§N" pattern already endorses this) — the change is only that it stops being the *identity*.

## Recommended sequencing
1. **You rub the alias map** (fix weak slugs; confirm the `claim:` namespace decision).
2. **Tier 1 in one commit** — view + ledger index → slug-primary, number-as-alias-column; regenerate rendered.
3. **Steward-hat heads-up** on `X1–X3` aliases.
4. **Tier 2 trickles** — mint each missing yaml row as its invariant next comes up under falsification
   (wu-wei: don't bulk-author 15 rows speculatively; let live work pull each one in). This also dissolves the
   standing **Rule-tag-hygiene** todo (slugs can't collide) — fold that item closed when Tier 1 lands.

## The gate
Need from you: (1) Y/N on slug-canonical as the principle; (2) rub the alias map (or flag the weak ones);
(3) the `claim:`-namespace call for the theory-pipeline tier. On a Y I execute Tier 1 and queue Tier 2.
