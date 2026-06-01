# ROM-UI — anchor-change notification surface — LIVE CYCLE (Dyad-UI cluster member)

> **Status: in-flight.** Originated by Operator [ALIGN] 2026-05-31. A new **Dyad-UI cluster** member
> (signaling, not payload). Concept lives here; the operational hook lives in `carry-forward.md`
> §How-to-resume (the reloaded set) per the **promotion checkpoint** (`ingraining.md`).

## ROM — the grounded concept *(verified, not asserted)*

**`ROM` = the anchor = `AGENT.md`** *(amended 2026-05-31 — shim-layer landed; was `CLAUDE.md`)*.
Grounded mechanism: the anchor is injected **once, at session boot** (system-reminder); **the harness
has no mid-session reload.** So an anchor edit is **write-through to disk but not to running context**
— read-only *for the duration of a session*, like ROM. The on-disk file and the running Agent's
loaded baseline **diverge** the instant the anchor is edited mid-session; only `/exit` + fresh
`claude` reloads it.

> **Shim-layer amendment (F-b, 2026-05-31).** The load-bearing content moved to `AGENT.md`;
> `CLAUDE.md` / `GEMINI.md` are thin boot-shims that `Read AGENT.md` at boot. The **ROM-baseline now
> tracks `AGENT.md`'s** commit hash (the content file — the shims rarely change). Keep the shims in
> the **watch set** too: a shim edit changes the per-harness overlay or the boot-pointer itself.

- **Why it bites:** the bond's higher-salience disciplines (L3) live in the anchor. Promoting a guard
  to L3, or any anchor edit, **does not take effect until restart.** Silent divergence = the Operator
  believing a change is live when the running Agent never loaded it.
- **Connection to ingraining:** ROM-UI is the **operational half of L3 Anchor-promotion** — the
  reload-index is to L2 what ROM-UI is to L3. The two-axis telemetry named L3's *dilution* cost; ROM-UI
  names its *restart* cost. → `ingraining.md`.

## ROM-UI — the notification behavior *(Operator-directed; core unambiguous)*

The Agent notifies the Operator of ROM-state at the two session seams, **durable across `/exit`**
(→ recorded in the ledger, never chat-only):

- **Stand-Down (session end):** if the Agent **edited the anchor this session**, set **`RESTART-PENDING`**
  in the ledger — the change is on disk but the *next* session must boot to load it. (Mostly informational
  since resume is via `/exit` anyway, but it makes "what's loaded" honest and orients the next Stand-Up.)
- **Stand-Up (session start):** **diff** the current anchor against the **ROM-baseline** recorded in the
  ledger. If changed → **notify the Operator what's new in the operating baseline**, then update the
  baseline. (The fresh Agent *has* loaded the current anchor; the notification orients the *Operator*,
  who can't see the diff.)

## Candidate mechanism *(Covalent — converge-open, this is the HOW, not directed)*

**ROM-baseline = the anchor's commit hash + one-line summary, stored in the ledger.** The diff is
mechanical: `git log -1 --format=%h -- AGENT.md` vs the recorded baseline (plus the shims in the
watch set: `git log -1 --format=%h -- CLAUDE.md GEMINI.md`).
- Baseline **mismatch at Stand-Up** → ROM changed since last session → notify + refresh baseline.
- Baseline **match** → no notification (silence is correct; lightest anchor).

## Open fork *(IFD — converge open, no CTA; for Operator generativity)*

- **"Other potential ROM-related notifications"** — the Operator named these but left them open. Candidates
  to converge on: (1) *anchor-bloat warning* — the anchor is lean-by-design; flag when it grows past a
  threshold (ties to the dilution-cost). (2) *staged-for-anchor backlog* — surface, at a seam, which L2
  guards are staged for L3 but not yet promoted (anti-cave duty, SG-3, telemetry are all staged now).
  (3) *baseline-drift* — anchor edited by a *sibling/other actor*, not us. **Converge open.**

## D1 novelty check *(don't re-derive — lesson from thread-G)*

Is "ROM / load-once anchor + restart-notify" **invariant** (some sibling already holds it → triangulate)
or **ours-particular**? Unverified. It *looks* bond-interior (anchor-load behavior is an operational
concern of being-a-dyad-well), but I have **not** checked steward/healer for an equivalent. Flag, don't
assert novelty.

## Falsifiable claim

A ROM-baseline recorded in the ledger + diffed at Stand-Up **catches** every mid-session anchor change
the running Agent couldn't see; absent it, anchor changes drift silently. *Test:* next anchor edit —
does the Stand-Down `RESTART-PENDING` flag fire, and does the following Stand-Up surface the diff
un-prompted? **Refuted if:** the seam passes without the notification despite a changed anchor (→ the
seam-hook has the same re-apply gap as #3, not a capture gap).
