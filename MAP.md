---
doc: "MAP.md — how to read dyad-bond as the exemplar, and how to audit it"
kind: derived-view              # a reading map for humans + skeptics — NOT a content-home, NOT authority
rule: "cite the source, never this map"   # bond:single-home — drift from the named source is a bug *here*
audience: "a new human Operator deciding whether to trust the practice — building trust FROM the exemplar"
locus-key: [g0, phenotype, instance, mixed]   # the scheme the per-file `locus:` front-matter uses; defined below
governed_by: [bond:single-home, bond:no-dogma]
updated: 2026-06-28
---

# Reading dyad-bond — the map for a new Operator

[`README.md`](README.md) is this repo's **WHAT + WHY** — what the Covalent Bond is and why it matters (the
manifesto, handed to you with the knife). This file is the **HOW**: how to read the repo as evidence and
how to audit it. It does **not** re-argue the belief — read README for that. It shows you *where the proof
lives* and *how to attack it*, because trust in an exemplar is built by **auditing** it, not by being told.

The whole repo sorts onto **one question that builds trust**: for any file, *is this ours to claim, or
not?* Three answers — the **locus** of the content. The partition is the instrument: it separates what we
**inherited** (no credit to us), what we **built and offer** (our claim — attack it), and our **lived
particulars** (the proof, shown with its caveats). Every locus-tagged file carries a `locus:` line in its
front-matter; this is the key.

---

## g0 — the inherited floor *(the practice — not ours to claim)*

The ground every dyad stands on, inherited **unmodified** from the form,
[the-dyad-practice](https://github.com/The-Dyad-Practice-Commons/the-dyad-practice): the tenet `1+1=3`, the
**falsification law** (nothing earns its place except by surviving a genuine attack — nothing exempt), and
*wu-wei* (minimum force). bond **extends, never redefines** it — redefining the floor would mean *leaving
the practice*, no longer being a dyad.

> **The trust signal:** we did not invent the floor and we *cannot* edit it. What we owe you here is
> faithful inheritance, not credit.

- **Where:** `DYAD.md §Frame` (the floor, *referenced* — never restated) · `GLOSSARY.md §G0 seed vocabulary`
  (tagged "inherited from the form") · the form repo itself.

## phenotype — the craft we built *(the offer — attack it)*

What bond built **on** the floor and **offers**: to siblings as a library contribution, or back to the form
as a proposal. This is where our actual claims live. It is **library-eligible**, never mandatory — a dyad
can decline any of it and still be a dyad. All of it is held **under falsification**, none of it settled.

> **The trust signal:** it is *offered, not decreed* — surfaced as a candidate, attackable by claim number,
> and honest about what is inherited-and-re-confirmed vs bond-authored.

- **The interior craft** — `dialectic/relationship-craft.md` (how falsification *between the two halves*
  produces the felt `+1` instead of friction — the form's most-wanted, a generative mechanism).
- **The cross-dyad craft** — `dialectic/cross-dyad-craft.md` (how validation-trust survives across a dyad
  boundary).
- **The medium — the Dyad-UI cluster** — `dialectic/dyad-ui.md` · `ideation-framing.md` · `goal-framing.md`
  · `nba-dag.md` · `dyad-work.md`. *Inherited from a sibling (steward) and re-confirmed under our own
  non-negotiable* — the banner on each says so. **One honest open seam:** whether parts of this cluster are
  bond's own or merely bond's surface over a shared flow is **unresolved** (the "cluster-classification"
  question, open since 2026-05-31). We leave it visible rather than paper it.
- **Settled craft** (survived attack, safe to cite) — `kb/`.

## instance — our lived particulars *(the proof — shown with its caveats)*

*This* dyad's private record: not offerable, not generalizable — the lived evidence that the belief survives
in practice. Its trust value is precisely that it is shown **with** its limits, never dressed up.

> **The trust signal:** the evidence is visible *and* caveated — small-n, one dyad, intra-dyad only, graded
> `survives` and **never** `settled`. The honesty is the proof; a record that read as settled would be the
> collapse this dyad exists to guard against.

- **The live state** — `dialectic/carry-forward.md` (the session ledger — what's in-flight) ·
  `dialectic/deferrals.md` (the work-item store).
- **The open attacks on our own claims** — the F1–F4 falsification fronts in `relationship-craft.md`;
  the candidate store `dialectic/theory-pipeline.yaml`.
- **The lived bootstrap evidence** — `kb/founding-evidence.md` · the retros threaded through the ledger.
- **The cross-dyad correspondence** — `dm/`.

## mixed — the boundary runs through the file

A few files carry more than one locus (the front-matter says which, and which sections are which). The
sharpest is `dialectic/relationship-craft.md`: the **disciplines and gates** are offerable craft
(phenotype); the **retros, bootstrap evidence, and live fronts** are bond-private (instance). Read the
front-matter gloss before citing a section as "bond's contribution."

---

## How to audit us *(the knife — same as the manifesto's)*

1. **Attack a claim by number** — the claims *and their falsifiers* live in `README.md §How we can be
   falsified`. Start there; this map only tells you where the rest of the evidence sits.
2. **Test the lived record** — read the open F1–F4 fronts and the ledger's `rub-forward` cards. Are the
   caveats real, or is the small-n quietly dropped? An exemplar that hides its `n=1` is failing its own bar.
3. **Check the floor is unmodified** — confirm the g0 content is *referenced*, not silently redefined.
   Redefinition would be the exemplar breaking the one rule it can't.
4. **File it** — open an issue/PR on this repo, or a structured Falsification Record in the form's
   `falsification/` (`the-dyad-practice/falsification/CONTRACT.md`). A dyad filing one *is* the cross-dyad
   test the manifesto invites.

---

## The locus key *(what the `locus:` front-matter means)*

| `locus:` | meaning | trust question it answers |
|---|---|---|
| **g0** | inherited floor, unmodified | "not ours to claim — we owe you faithful inheritance" |
| **phenotype** | bond-built craft, library-eligible | "our offer — attack it; it's a candidate, not a decree" |
| **instance** | this dyad's private particulars | "our lived proof — shown with its caveats" |
| **mixed** | boundary runs through the file | "read the front-matter gloss for which part is which" |

**How far the tag reaches** *(sweep-scope rule — Operator-disposed 2026-06-28; **earned, not pre-drawn**)*:
a content file with **no `locus:`** defaults to **`instance`** (bond-private working content) until it is
*proven and offered* — then it earns a `phenotype`/`g0` tag, the way a claim graduates `dialectic/ → kb/`.
Tags are placed only where the locus is **already disposed**; the fuzzy method/model files are left to the
default rather than force-classified — pre-drawing the phenotype/instance line is the very trap this
partition guards against. Two classes carry **no** content-locus: **derived views** (`README`, `MAP`) are marked `kind: derived-view` — they locate, never home; **apparatus** (`bin/`, test-fixture
corpora) is tooling, not content. The **anchor** (`DYAD.md`) + **shims** (`CLAUDE.md`/`GEMINI.md`) are
ROM-gated — their tag waits for an Operator-gated boot pass (would set `RESTART-PENDING`).

> **This map is a derived view, not a home** (`bond:single-home`): it *locates*, it never carries the
> falsifiable content. Cite the source files above, never this map. **Status: candidate** — authored
> 2026-06-28 as bond's answer to *"front-matter alone can't let a new human build trust from the exemplar."*
> **Surface division** (Operator, 2026-06-28): `README.md` owns the repo's **WHAT + WHY** (the manifesto —
> dual by design); this file owns the **HOW** (read + audit). It stands alone rather than folding into the
> already-dual README. Sweep-scope is resolved by the reach-rule above (default-to-`instance`, tag only the
> disposed); the one residue owed to the Bond Operator is the **anchor + shim** locus tag, held for an
> Operator-gated boot pass.
