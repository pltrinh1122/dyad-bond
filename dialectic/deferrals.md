# dyad-bond — Work-item store  *(the work-item axis; was "deferrals", widened 2026-06-25 Phase 2)*

> **The work-item axis** (→ `dialectic/memory-axes.md`). Each item carries a **do-state**:
> `todo` (parked / backlog) → `in-progress` (active / WIP) → `done` · `archived`. The **NBA** is the
> render over `{in-progress ∪ todo}` (the TOTAL live set — backlog stays in sight); `{done · archived}`
> drain out. **Safe default = `todo`** — `archived` is a positive **Operator** dispose-as-dead (a
> judgment, like claim-graduation), never an Agent auto-filter. *(Filename kept as `deferrals.md`; the
> name is now a legacy misnomer — rename is a later surgery-detail.)*
>
> **Axis boundary:** this store holds **work-items** (do-state). **Claims** (belief-state) live on the
> claim axis (`theory-pipeline.yaml` + `relationship-craft.md`). A claim's open probe *emits* a work-item
> here; claims couple to the NBA **through** the store, never around it. The **Contribution candidates**
> below are claim-axis items (no do-state) — kept here pending the claim-peel relocation (Phase 2 gate).

## in-progress

- **Memory-axes restructure (the carry-forward re-key)** — Phase 1 landed (`carry-forward` ~89k→~20k tok);
  Phase 2 underway (work-item fold + `standup.sh` per-file compare DONE; claim-peel of the un-homed
  CANDIDATEs pending the Operator gate). Single-home → `dialectic/memory-axes.md`.
  *Live falsifier: drain-latency — does this drain get used at stand-down, or does the backlog re-accrete?*

## todo

- **[L] Rule-tag hygiene: stale inline R-tags collide with the ratified s14 index** *(relocated from the
  carry-forward Open-items, 2026-06-25 Phase 2 fold)* — The canonical invariant index is
  `views/invariants-bond.md` (ratified **s14**, 2026-06-11): **D1–D12 · R1–R6 · X1–X3 · U1–U3 · S1–S3** —
  R/RB are **not** un-indexed (a prior-session partial-grep claimed so; search artifact, refuted by reading
  `views/`). **Real defect:** older *inline* ledger tags reuse R-numbers with pre-s14 meanings that now
  collide with the ratified set — caught live: **`R3` reads "Theory≠Prediction" in the 2026-05-31 NBA but
  ratified `R3` = Stand-down 3-check ritual.** This collision produced a mis-grounding in the 2026-06-13
  rub-back chain. **Fix (deferred, lean, D2-bounded):** when next editing those files, retire or footnote
  the pre-s14 inline tags as historical; do **NOT** renumber the ratified table (it is the single home).
  Low-urgency corpus-integrity. *(prov: rub-back `RB?` → `R1/R4` read, 2026-06-13.)*

- **[B] Cross-dyad custody deprecation** *(relocated from the carry-forward Open-items, 2026-06-25 Phase 2
  fold; chase via the Steward-Operator hat)* — The 7 Dyad-UI cluster assets were received from
  `dyad-steward@31d53c0` (receipt `03550dc`, shed `f5480eb`). The Bond Operator will, wearing the **Steward
  Operator** hat, have `dyad-steward` mark those 7 paths **transferred → dyad-bond + deprecated**.
  - **Stand-Up check 2026-05-31:** steward's `dialectic/` *still carries* `dyad-ui`, `ideation-framing`,
    `goal-framing`, `nba-dag`, `dyad-work` with **no transfer/deprecation marker** at listing level →
    **not done.** Confidence caveat: a tree-view can't see an in-file deprecation header, so this is "no
    evidence of completion," not proof.
  - **Side-catch:** steward has grown new disciplines since custody — `sycophancy-guard.md`,
    `sharing-discipline.md`, `reflection-discipline.md`, `telos-vision.md`, `ingraining.md`, `stand-downs/`.
    `sycophancy-guard` sits on our NON-NEGOTIABLE → candidate for triangulation/intake (was Item F).
  - **MOTION LIVE (Steward-Operator notice, 2026-05-31):** steward is *actively asserting orthogonality* to
    release its claim; will **notify of the survivor for Covalent cross-check.** Status: in motion,
    steward-side, **awaiting survivor.** This forces the cluster classification (below). **Cross-check
    criteria when survivor lands:** (1) does orthogonality genuinely hold — is each released asset in *our*
    telos (interior craft / UI-surface) and NOT steward's (commons integrity / Work-flow)? (2) did steward
    actually mark paths transferred→dyad-bond + deprecated, or merely assert? (3) **the tell** — if release
    is total + frictionless, **test hardest**, esp. `nba-dag`/`goal-framing` (likely ours-UI-surface-only,
    NOT ours-whole). (4) test under *our* NON-NEGOTIABLE — steward's falsification ≠ ours (cf. `dfd.md`
    caveat).

- **Cluster classification:** are `nba-dag`/`goal-framing` ours-whole, or ours-UI-surface-only (their
  Work-flows = steward's)? → flagged in `dialectic/dyad-work.md`. *(Forced by [B]'s motion; bind only on
  disposition — candidate = three-way partition: flow-structure (invariant, triangulate) · Telos-content
  of the gate (ours) · UI surface (ours).)*

- **⏳ PENDING PICKUP (workstation) — deposit FR `bond-apex-telos-singularity` to the Commons.** Staged +
  conformant (`dialectic/fr-apex-telos-singularity.staged.yaml`); executable handoff in
  `dialectic/fr-deposit-pickup.md`. The s-cloud-mobile session lacked Commons write creds; deposit is the
  self-authorizing `auto-merge-falsification` lane (no human gate). **Downstream PARKED:** `AGENT.md` dim-1
  amendment → Founding, *only if* the claim survives §J-decisive. (2026-06-21, s-cloud-mobile.)

- **types-of-work** sub-area (shed with the Work-layer) — revisit only if the relationship-craft needs it.

- **Relationship-craft codification** — the interior disciplines of being-a-dyad-well are largely
  *unbuilt*. This is our generative frontier. *(Live front; prose home → `relationship-craft.md`.)*

## done

- **✅ message-tracker (`bin/msg_tracker.py`, 2026-06-18 s-local3)** — a per-dyad *thread-state* ledger over
  the DM channels: tracks per message {sent/received · read/unread · responded-to · supersedes/reply-to} and
  surfaces a **diff-against-prior** on each new inbound. Built on `falsify.py`'s `.falsify-seen.json`
  seen-state + the IM daemon's rise-detect. **Learning (claim-axis — peel to `relationship-craft.md` at the
  claim-peel):** mechanizes *"diff-against-prior by re-reading, never recite a prior message from memory"*
  (D6 at the message layer) — racked because s-local3 Covalent asserted a prior DM's content from memory and
  missed a real delta (cairn's self-ratification softening). *(Build = apparatus class, agent-disposable.)*

## Contribution candidates — propose back to the form *(claim-axis; via the Founding-Operator gate; `bond:prove-before-propose`)*

> **NOT work-items** (no do-state) — claim-axis items pending the Founding-Operator gate. Listed here
> pending the Phase 2 claim-peel relocation to the claim axis (`theory-pipeline.yaml` / `relationship-craft.md`).

- **Library track** (prove synergy): `DFD`, `IFD`, the **UI↔Work pairing**.
- **Frontier track** (prove synergy **and** orthogonality — the form's *most-wanted*, a **generative**
  mechanism): **the relationship-craft** — e.g. how falsification *between the halves* produces the felt
  **+1 dividend** (not frustration). We hold lived evidence (the bootstrap); codify it.
