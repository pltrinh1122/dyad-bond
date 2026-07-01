# Commissioning craft — term-selection invariants *(bond-side meta; CANDIDATES, lived-untested)*

> **Provenance:** s15 rub-back (2026-06-12) — the Operator's primary commissioning driver, verbatim
> intent: **minimize source-code maintenance + troubleshooting time.** Defeat-condition: *"if we
> commission and end up spending as much or more time than if we had just built it, that defeats the
> calculus."* These invariants govern HOW contract terms are selected; the per-commission spec applies
> them. Status: candidates under the operator-rub-invariant (rubbed in-session, untested by a lived
> commission). First trial = `2026-06-12-invariant-extraction-engine.md`. Second trial =
> `2026-07-01-dyad-system-engine.md` — spec-cost was template-fill, not a fresh session-arc (the TS-6
> falsifier survives this round). **Template extracted from the two-trial comparison** →
> `commission-template.md` — start new commissions there, not from a blank page.

- **TS-1 · hour-deletion test:** a term earns its place only by deleting future commissioner-hours
  (maintenance/troubleshooting), never by expressing quality preference. Selection question: *which
  future hours does this term delete?* No answer → cut.
- **TS-2 · cheap acceptance:** terms must be mechanically verifiable, else acceptance becomes the new
  maintenance. Judgment-terms (grain) fire once at delivery, never recurring.
- **TS-3 · priced trust boundary:** every Class-B precondition is a perpetual commissioner-side cost
  line — count it. Flag carried from the first spec: **the semantic tagging discipline never leaves the
  commissioner regardless of builder** — commissions delete build/code-hours, never practice-hours.
- **TS-4 · mechanical failure-attribution:** the contract assigns troubleshooting ownership by
  construction (engine-internal = builder; precondition violation = commissioner; named-state halts =
  troubleshooting-as-lookup). Ambiguous attribution = the most expensive failure mode (a future argument).
- **TS-5 · cheap exit:** dyads are mortal — terms must keep fork/re-commission cost low (size envelope +
  auditability = the right to walk away; no bus-factor on a sibling).
- **TS-6 · spec-cost budget (the meta-invariant / defeat-condition):** spec+negotiate+accept effort stays
  bounded below the build-estimate. **Pre-registered falsifier (retro-scores the whole commissioning
  model):** if the SECOND commission's spec-cost isn't dramatically lower than this first one's
  (template-fill vs session-arc), the amortization story fails → commissioning REFUTED on the Operator's
  own calculus; just build.

**Line-rule (re-grounded in the driver):** bond keeps zero-troubleshooting shapes (declared-policy
wrappers — loud, simple failures); bond commissions engine-failure-mode shapes (FSM/parser/state).
