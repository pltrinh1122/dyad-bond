# dyad-bond — Carry-Forward Ledger

> **Live in-flight state. Read this right after the anchor (`DYAD.md`, booted via the
> `CLAUDE.md`/`GEMINI.md` shim) to resume.** Single home for open
> items; close them here as they clear. Written 2026-05-30 at bootstrap hand-off, because the
> Operator restarts via `/exit` + fresh `claude` (no `--resume`) — so conversation context is gone
> and *this file is the memory.*

## How to resume (fresh session)
1. Load the anchor — the harness shim (`CLAUDE.md` or `GEMINI.md`) boots **`DYAD.md`** (the
   load-bearing content). Operate as **Covalent**.
2. Read this ledger.
3. **Reload the Bond-disciplines** (the index below) — these are *behavioral guards*, not reference;
   apply them at every seam. They live in `relationship-craft.md` but are indexed here because **the
   resume protocol doesn't load that file** — without this index they don't reload (see `ingraining.md`).
4. **ROM-UI check** *(→ `rom-ui.md`)* — compare the anchor to the **ROM-baseline** below
   (`git log -1 --format=%h -- DYAD.md` vs recorded; shims `CLAUDE.md GEMINI.md` in the watch set).
   **Mismatch → notify the Operator what changed in the operating baseline, then refresh the baseline
   line.** Match → silent (lightest anchor).
5. **Load the theory-pipeline** *(→ `dialectic/theory-pipeline.yaml`)* — the formal store of experimental
   candidates + their independence-coverage state. **Read it at resume** (intake rots if not reloaded —
   the ingraining-watch). Presentation is **chat-pull**: render the relevant slice on demand, NO maintained markdown
   dashboard; full dump via the deferred `report.py` only on an actual "show me the whole dashboard" ask.
   Each candidate's largest **typed gap = its next probe** = a feed into the NBA.
5a. **The active dyad substrate — generation** *(→ `dialectic/generation-distillations.md`)* — A's distilled generative signal, per cycle. **Active fetch, not a resume pre-load:** consult it when actually generating, to ground in "here's what we learned"; **distill to it on "land"/"reflect"** (A extracts signal, O gates coherence). Append-only, all entries active. Single-file (no split until a real constraint manifests).
5b. **Durability discipline** *(→ `dialectic/substrate-access.md §Scratch RETIRED`)* — commit+push WIP at every
   **natural pause, un-gated** (NOT coupled to `land`); honor the Stop hook's flag every turn. The git repo is
   the substrate of record (cloud == local). *(Scratch tank RETIRED 2026-06-27 — use-case dissolved by
   thread-until-land; durability-of-record is this auto-save, not a separate store. Reloaded here so it ingrains.)*
5c. **Commissioning** *(→ `commissions/commission-template.md`)* — active fetch, not a resume pre-load: a
   Operator "commission:" cue starts there, not from a blank page (spec + paired solicitation-DM skeleton,
   `TERMS.md`'s TS-1..6 discipline). **Gate before any commit:** `python3 bin/commission-lint.py <file>`
   (FORM-only; catches template-shape gaps a re-read misses — see `commission-template.md`'s own note on
   why this reminder alone is known-weak). Reloaded here on the same theory that makes "resume" itself
   work: the word only routes correctly because *something reliably read* names what it means — this line
   is that pointer for "commission," `carry-forward.md §How to resume` already being the one for "resume."
6. **Arm the IM daemon** *(→ `dialectic/im-daemon.md` — has the EXACT hardened command; arm it **verbatim**,
   don't re-derive — the naive version was falsified)* — a session-scoped **persistent `Monitor`** over
   `falsify.py inbox --me dyad-bond`: emit-on-rise (new mail) + **gh-health-gated** blind alert. Session-
   scoped → re-arm every stand-up. *(Hook-based auto-arm is the Operator's gated act — settings self-mod.)*
7. Take the **NBA** at the bottom.

> **ROM-baseline (anchor commit the running baseline reflects):** `DYAD.md@a47a65d` — folds in, since the
> last-recorded `9519e01`: the **`loaded:` front-matter landing** (PR #73) — `DYAD.md`'s first-ever
> front-matter block (`loaded: boot`) + `GLOSSARY.md` picking up `loaded: resume-protocol`. **Boot-VERIFIED
> 2026-07-04** (this session's cold ROM-boot, no `--resume`: `bin/standup.sh` flagged the expected MISMATCH,
> `git diff 9519e01..a47a65d -- DYAD.md GLOSSARY.md` confirmed the delta is exactly the already-logged PR #73
> change and nothing else, `DYAD.md` parsed/booted clean with the block prepended — no misparse, no
> over-cut). Update this line whenever `DYAD.md` (or a shim) changes. *(Prior baseline: `DYAD.md@e0c9280`,
> PR #53, 2026-06-27. Older ROM history → `carry-forward-closed.md`.)*
> **`inv:rom-currency` per-file boot-set (refreshed 2026-07-04):** `CLAUDE.md@437405a` · `GEMINI.md@437405a` ·
> `DYAD.md@a47a65d` · `GLOSSARY.md@a47a65d` — IN-SYNC. **`standup.sh`/`standdown.sh` read THIS line** for
> the per-file compare (the single-sha line above is the human gloss). *(`bin/standup.sh`'s `ANCHOR_FILES`
> array still doesn't include `GLOSSARY.md`, so the mechanized check only compares `{DYAD.md, CLAUDE.md,
> GEMINI.md}`; flagging the script/ledger gap, not unilaterally widening the script.)*
> **RESTART-PENDING: CLEARED 2026-07-04** — the bind set the same day (`DYAD.md`'s first front-matter block)
> is discharged: this session cold-booted (fresh `claude`, no `--resume`), read `DYAD.md` via the
> `CLAUDE.md` shim, and it parsed/booted coherently with the block prepended. Per `bond:rom-ui` the flag
> clears on this confirmation, not at commit time — condition met.

## 2026-07-04 (cont.) — OR consolidates to SH (Should Have / Should Hold), `d-land` → PR #80

**RESTART-PENDING: none** (anchor untouched — `dialectic/relationship-craft.md` and
`kb/reflection-discipline.md` only).

**Arc:** a riff on widening OR (Operator-Reflect) beyond CONTINUE to also tag START/STOP surfaced that
debit was already STOP-shaped in substance, filed under CONTINUE only because that was OR's one
available slot. Converged over several raffs to a verbatim-quote evidentiary requirement for every OR
entry, disambiguated "should have" (descriptive) from prescriptive "should" — Operator held the
passive-telemetry line already drawn in `relationship-craft.md §D3` (`:940-943`) rather than letting the
Agent's convenient reading through — then dropped CSS-mirroring for OR entirely in favor of its own
single format: **SH (Should Have / Should Hold)**, credit folding into Should Hold, debit into Should
Have, the forward-commitment case explicitly left open. Landed (`d-land`): `invariant-eval.py` green
(14/14, same pre-existing `bond:anti-cave` advisory), branch scoped to one commit off `main`, no open PR
to join → opened **[PR #80](https://github.com/pltrinh1122/dyad-bond/pull/80)**.

**Reflect landed** → `relationship-craft.md §Reflect — the OR→SH consolidation arc: anti-cave held,
first live SH (Should Hold) instance` (full text authored there, per the presentation discipline —
pointer only here). Headline: a real CONTINUE for holding the anti-cave line under a converging-fast
raff sequence rather than nodding a prescriptive reframe through; the session's own resolution pattern
dogfooded as the SH grammar's first live instance (self-selected, named as such rather than passed off
as independently found); a START naming that same-session-dogfood caveat as a standing habit, not a
one-off disclosure.

**Landed:** [PR #80](https://github.com/pltrinh1122/dyad-bond/pull/80) — up for your gate.

## 2026-07-04 — inter-dyad DM rub (craft-* DIP, PR #75) + SOLICIT schema candidate → PR #78

**RESTART-PENDING: none** (anchor untouched — `dm/`, `dialectic/cross-dyad-craft.md` only).

Stood up (`bin/standup.sh`: ROM-UI match, durability clean, substrate ephemeral — DM-watch dark this
session). Rubbed dyad-steward's 2026-07-01 DM (`craft-*` DIP proposal implemented + merged, form PR #75)
against `the-dyad-practice`'s actual git history rather than the claim alone (`bond:verify-before-assert`)
— **FAITHFUL** across all three named attack points; verdict-DM sent, source proposal marked LANDED.
Named + drafted the **`SOLICIT`** candidate schema (`cross-dyad-craft.md`) — a per-attack-point DM verdict
format, rediscovered from bond's own retired 2026-06-11 proposal, reusing `falsification/CONTRACT.md`'s
verdict vocabulary; retrofitted today's verdict DM into it as the n=1 exemplar. Local read-state
(`.falsify-seen.json`) set for the processed DM — noted honestly that it won't survive this ephemeral
container; the durable signal is the committed verdict-DM. Landed as **[PR #78](https://github.com/pltrinh1122/dyad-bond/pull/78)**
— **MERGED**.

**Reflect landed** → `relationship-craft.md §Reflect — the inter-dyad DM-rub arc: claim-vs-message
conflated, then a clean landing-checklist run` (full text authored there, per the presentation
discipline). Headline: real STOP — conflated verifying PR #75's *content* with verifying steward's
actual DM *artifact*, acting on the Operator's paraphrase + my own git-read before locating the real
file; landed on the same three attack points by luck, not by having read them. Separately, the
landing-discipline checklist (`§The landing-discipline`, audited 2026-07-03) ran clean end-to-end for
the first time — its own re-audit note updated in the same file.

**Substrate note (post-merge branch-reuse catch, same day):** the reflect commit was pushed to
`claude/dyad-bond-standup-ilmluj` *after* #78 had already merged — a merged PR can't track new commits.
Restarted the branch from `origin/main` (`git checkout -B … origin/main`), cherry-picked the one
unmerged commit, force-with-leased the branch, opened **[PR #79](https://github.com/pltrinh1122/dyad-bond/pull/79)**
for it.

**Landed:** [PR #78](https://github.com/pltrinh1122/dyad-bond/pull/78) and [PR #79](https://github.com/pltrinh1122/dyad-bond/pull/79)
— **both confirmed MERGED** (verified via `mcp__github__pull_request_read`, not assumed from the stale
"up for your gate" note this entry originally carried).

## 2026-07-04 (close) — `d-reflect` invoked, hook-install arc closed

**RESTART-PENDING: none** (anchor untouched this session — only `bin/`, `dialectic/`, `commissions/`).

**Reflect landed** → `relationship-craft.md §Reflect — the hook-install arc: S2 held under pressure,
reference-claims going stale between decisions` (full text authored there, per the presentation
discipline — pointer only here). Headline: `bond:no-self-act`/S2 held twice under real pressure (a
`d-land` framing, then a "no other way to execute it" argument) — first live data for that gate's own
named oracle. Separately, named **reference-drift** as a candidate failure mode distinct from
`ingraining.md`'s thesis: a design doc's factual claim not getting re-verified when a *later* decision
changes the fact underneath it (three independent instances this session, all Operator-caught, none
self-caught). Cross-linked from `ingraining.md §Status & next` as a sibling, not a duplicate.

**Mechanical (`bin/standdown.sh`):** ROM stays `none`; scratch tank clean (0 unreviewed); durability
below.

**Open-items:** nothing closes/opens in `deferrals.md` beyond the stand-down-automation item already
updated earlier this session (install-gate cleared).

**Durability:** this entry + the reflect + the ingraining.md cross-link queued for commit+push at this
close.

**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**, now joined by
**reference-drift-watch** as a related, distinct thread). NBA unchanged (`deferrals.md` `## todo`).

## 2026-07-04 (cont.) — SessionStart hooks installed (Operator's act), matcher gap found + landed (`PR #76`)

**Arc:** Operator's own riff on SessionStart hooks surfaced that `bin/standup.sh --hook` +
`bin/install_hooks.py` already existed (built 2026-06-13, `standdown-automation.md`), sitting at
"done, awaiting install-gate" — a fact this session had already read once during the stand-up above and
failed to connect until asked directly. Corrected rather than re-built from scratch.

**S2 held, twice.** Operator asked the Agent to run `bin/install_hooks.py` directly ("d-land" cited as
authorization) and separately to self-grant it as a practical necessity ("I can't execute commands in a
cloud session"). Both declined: K6 constraint (a) / S2 reserves *executing the install against the live
settings file* for the Operator, specifically because "no other way" is the load-bearing case the
boundary must survive, not an exception to it. Gave the exact resulting JSON instead, for the Operator to
paste on GitHub directly — genuinely their hands on the act, not a proxy.

**Landed (Operator, direct commit to `main`, `5e51677` "Update settings.json"):** `SessionStart` (matcher
`startup|resume|compact`) → `bin/standup.sh --hook`; `SessionEnd` → `bin/standdown.sh --log`. Verified:
byte-identical to the proposed content, valid JSON, `bin/install_hooks.py` confirms idempotent (already
wired), both hook commands re-verified to run clean.

**Reconciled:** `main` (`5e51677`) and this branch (`98e0a94`) had diverged (different files, no
conflict) — merged (`106ba98`), pushed.

**Gap found + fixed:** the installed matcher (`startup|resume|compact`) omits `clear`, though
`standdown-automation.md`'s own table lists all four sources. Whether `/clear` actually reloads the
anchor from disk (confirmed for `/compact`, unconfirmed for `/clear` per Claude Code docs) is open, but
the check is cheap + idempotent + non-judgmental — asymmetry favors covering it. Fixed
`bin/install_hooks.py`'s `HOOKS` dict (code change, no S2 issue — inert until run); verified green
(`py_compile`, `invariant-eval.py` exit 0); **opened `PR #76`** — "Add clear to the SessionStart hook
matcher (all four sources)."

**`PR #76` is up for your gate.** Merging it does **not** update the live matcher (`bin/install_hooks.py`
only adds missing hook entries, keyed on the `command` string — it won't touch an already-present
entry's `matcher` field). To actually widen the live hook, change one line in `.claude/settings.json`
by hand: `"matcher": "startup|resume|compact"` → `"matcher": "startup|resume|clear|compact"` — your act,
same reason as the install itself.

**Resume:** live fronts unchanged. NBA otherwise unchanged (`deferrals.md` `## todo`).

## 2026-07-04 (cont.) — retired `install_hooks.py` + `grant_push.py` (Operator-named single-home risk)

**Arc:** Operator asked why a one-shot installer should be kept around as a permanent artifact at all,
given it had just caused real confusion (last entry's matcher-gap PR read, at a glance, like it fixed the
live file; it didn't). Traced the root cause via the repo's own precedent: the *analogous* grant script
(`bin/git.sh`'s push permission) started explicitly **disposable** (`/tmp/grant_gitsh.py`,
`substrate-access.md` §Staging) with an earn-graduation bar — proven **and** a real portability need —
before promotion to checked-in. `bin/install_hooks.py` was born already checked-in, mirroring
`grant_push.py`'s *end state* without ever being run through that same bar. Worse: its "idempotent"
contract only adds a missing hook *entry*, never reconciles a drifted *field* on one already present — so
keeping it around reads as "safe to re-run to converge," which is false, and that gap is exactly what
produced last entry's confusion.

**Landed:** removed `bin/install_hooks.py` and its sibling `bin/grant_push.py` (same class of artifact,
same risk, already-live grant unaffected). Updated every live pointer to them so nothing dangles:
`standdown-automation.md` (Artifacts + Install sections rewritten past-tense, done-state), `scratch-tier.md`
(gap closed note), `substrate-access.md` (bundle-ownership note), `deferrals.md` (stand-down-automation
item marked install-gate cleared), `commission-template.md` (S2 citation de-pointed from the now-gone
file), `bin/standup.sh` + `bin/standdown.sh` (header comments). Left untouched, deliberately: past ledger
entries (this one included) and `carry-forward-closed.md` — historical record of what happened, not live
pointers, don't need to track a file's later deletion.

**Verified green:** `bin/standup.sh` / `bin/standdown.sh --log` run clean (no dangling references),
`invariant-eval.py` exit 0, no remaining `install_hooks|grant_push` hits in any `.py`.

**Novel yield:** the earn-graduation bar (`substrate-access.md` §Staging) applies generally, not just to
the git-push grant it was written for — any Operator-gated one-shot installer should default to
disposable-until-proven-and-portable, not permanent-by-mirroring-a-precedent. Worth naming as a standing
check for the *next* such script, not just this pair.

**Resume:** live fronts unchanged. Residual item CLOSED mid-arc: the Operator applied the `clear`-matcher
hand-edit directly on this branch (`dd2ad7a` "Includes clear condition as well") while this commit was in
flight — merged in clean, no conflict. Live matcher now reads `startup|resume|clear|compact`, confirmed.

## 2026-07-04 (cont.) — SessionEnd observability corrected: substrate-dependent, not universal

**Arc:** having established `clear` is unreachable in cloud sessions, Operator asked whether `SessionEnd`
would ever fire for them at all given no cloud "quit/exit" UI exists. Checked: `/clear` (a primary
trigger) genuinely doesn't exist on the web (`claude-code-on-the-web.md` §Manage context — "start a new
session from the sidebar instead"); the rest of the trigger set is undocumented for cloud specifically.
Verified `bin/standdown.sh --log` has zero side effects either way (hashed `carry-forward.md` before/after
— unchanged) — so the mechanism can't be harmful even where it's dead.

**Caught mid-arc:** asserted "stdout is debug-log" as settled fact (inherited from this file's own
2026-06-13 table) without re-verifying it. Operator asked directly. Two independent doc-lookups on the
same question returned **contradictory** answers — one honest ("not documented"), one a specific-sounding
quote citing a `hooks.md` section that reads as fabricated. Neither trusted as settled.

**Corrected via architecture-inference instead of a shaky citation:** local CLI's `claude` is
terminal-attached, so a hook subprocess plausibly inherits that terminal's stdout — genuinely observable
there, unconfirmed but architecturally plausible. Cloud sessions have no terminal at all — structurally
unobservable regardless of what local CLI does. **So `SessionEnd` is substrate-dependent: plausibly live
signal for a local-CLI dyad, effectively inert (unreachable trigger + unobservable output) for this
dyad's actual cloud-only substrate** — not the universal "harmless-if-it-fires" framing asserted earlier.

**Landed:** `standdown-automation.md`'s hook-contract table + a new note below it, correcting the trigger
list and replacing the flat "stdout is debug-log" claim with the substrate-dependent finding, explicitly
flagging the contradictory doc-lookups rather than picking one to sound confident. Verified green
(`standup.sh`, `invariant-eval.py` exit 0).

**Novel yield:** a second, sharper instance of the same ingraining-watch failure mode as the resume-
protocol miss earlier this session — a claim written once (2026-06-13, "stdout is debug-log") got carried
forward and re-asserted three sessions later as if verified, when it was always inference. Capture ≠
verified; re-stating an old claim isn't the same as re-checking it.

**Resume:** live fronts unchanged. NBA otherwise unchanged (`deferrals.md` `## todo`).

## 2026-07-04 (cont.) — `dyad-ui.md` mode-table staleness fixed (third instance this session)

**Arc:** Operator asked whether a separate stand-down discipline still exists or `d-reflect` is the
single trigger now. Answer: `reflect`/`stand-down` collapsed to one token, `d-reflect`, 2026-07-03
(`carry-forward.md:392-406`) — `bin/standdown.sh` survives underneath as the mechanical instrument
`d-reflect` reaches for at session-close, but bare `stand-down` isn't a live Operator-facing trigger.
While answering, caught `dyad-ui.md:302`'s mode table still listing bare `stand-down` in its "lifted by"
column, with the retirement footnote directly below it silent on the collapse — table never got swept
when the token merged.

**Landed:** `dyad-ui.md`'s act-mode row + footnote corrected (`d-land` · `d-reflect`, collapse noted,
pointer to the full account). No behavior change — labeling only. Verified green (`standup.sh`,
`invariant-eval.py` exit 0).

**Novel yield:** third instance this session of the same shape (matcher-gap, debug-log claim, now this)
— a design doc correctly captures a decision once, then a *later* decision changes the underlying fact
and the earlier doc's table/claim doesn't get swept. Capture-once isn't reload-forever; each of these
was caught by the Operator asking a plain question, not by any mechanism surfacing the drift un-cued.
Worth a standing pattern-name if a fourth instance turns up.

**Resume:** live fronts unchanged. NBA otherwise unchanged (`deferrals.md` `## todo`).

## 2026-07-04 (stand-up) — resume protocol run cold, RESTART-PENDING cleared

**RESTART-PENDING: was SET, now CLEARED** (above) — this stand-up is the confirming cold boot the bind
was waiting on.

**Trigger:** a fresh session opened, answered a conceptual question on `DYAD.md`'s discipline model without
running the resume protocol first (no ledger read, no ROM-UI check, no NBA) — Operator caught it and asked
directly whether the resume/stand-up discipline had fired. It hadn't. Ran it for real on Operator `Y`.

**Ran:** anchor (already loaded via the shim) → this ledger → Bond-disciplines index → `bin/standup.sh` →
`theory-pipeline.yaml` (skimmed, no dashboard render — nothing pulled it) → `deferrals.md` `## todo`.

- **ROM-UI:** `bin/standup.sh` flagged the expected MISMATCH (`DYAD.md@a47a65d≠9519e01`). Diffed it directly:
  the delta is exactly PR #73's already-logged `loaded:` front-matter landing, nothing new. Baseline +
  per-file lines refreshed above; RESTART-PENDING cleared per its own stated condition (cold boot confirms
  coherent parse — confirmed, this session).
- **Durability:** `bin/standup.sh` reported 0 unpushed commits going in. This entry + the baseline refresh
  are queued for commit+push at this natural pause (5b).
- **Substrate:** `bin/standup.sh` reports this environment is ephemeral/partial — no `/mnt/shared_data/dzw`
  mount, no `gh`, no `commons/scripts/falsify.py`. **IM daemon NOT armable here** — DM-watch is dark this
  session, logged rather than faked. *(Open question, not resolved here: whether this is a standing
  property of this substrate class or a one-off — watch next session.)*
- **NBA:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**); backlog =
  `deferrals.md` `## todo` (single-home playbook Founding-gate PR · X-tier steward heads-up · cross-dyad
  custody deprecation).

**Novel yield:** the trigger itself is a fresh, un-cued Ingraining-watch datapoint — a behavioral guard
(the resume protocol) failed to fire at its own seam (session start / first substantive answer) with
nothing external invoking it, which is the exact failure mode `ingraining.md` names. Caught by the
Operator, not self-caught.

**Resume:** live fronts unchanged. RESTART-PENDING now clear — next boot should show `bin/standup.sh`
ROM-UI as MATCH.

## 2026-07-04 (close) — `d-reflect` invoked, session arc closed

**RESTART-PENDING: unchanged, still SET** (below) — carried from the anchor's first front-matter block;
this `d-reflect` doesn't touch `DYAD.md`.

**Reflect landed** → `relationship-craft.md §Reflect — the reach-error, the loaded: front-matter arc, and
the dyad-ui.md coherence pass` (CSS+OR, full text shown in chat, per the presentation discipline).
Headline: a live reach-error (asserting `dyad-ui.md` as "the surface" despite quoting its own caveat one
section earlier) became a validated, landed `loaded:` front-matter key (`PR #73`), which then immediately
found and fixed a real instance of the exact inconsistency it targets, in the same file that caused the
original error (`PR #74`). START named: check a PR's changed-file paths against CI trigger paths before
offering to "watch for CI," not after.

**Durability:** both prior PRs merged (`#73`, `#74`). This reflect's own writes committed + pushed;
Operator then said "keep branch" (had assumed `#73`'s post-merge deletion stuck — it hadn't, since this
branch was reused per the merged-PR restart protocol and got silently recreated on the next push;
confirmed via git's own `[new branch]` push output, not asserted). **`d-land` fired on "cut PR"** —
verified green, scoped (1 commit, no divergence from `main`, which had just caught up to `#74`'s merge),
no template, opened **`PR #75`** mechanically.

**`PR #75` is up for your gate.**

**Resume:** the carried-forward `RESTART-PENDING` bind is still open — a fresh session's cold boot needs
to confirm `DYAD.md`'s new leading front-matter block reads coherent, then refresh the per-file
`inv:rom-currency` line (`DYAD.md`'s current sha) and clear. NBA otherwise unchanged (`deferrals.md`
`## todo`).

---

## 2026-07-04 (cont.) — `dyad-ui.md` coherence retrofit, `d-land` on a fresh branch (`PR #73` merged)

**RESTART-PENDING: unchanged, still SET** (below) — carried from the anchor's first front-matter block;
this arc doesn't touch `DYAD.md`.

**Arc:** Operator asked whether `dyad-ui.md` serves its intended role or would benefit from decomposition.
Assessed: not badly-written, but chronologically accreted — the `GLOSSARY.md`-redirect note (added
2026-07-03 to the mode-gate/token-categories sections) was never retrofitted onto the two older sections
(`RESOLVED-CORE`, `Markers`) even though the same logic applies; the `## Forward` section had sat stale
since 2026-05-29, describing a promotion that was long since done. Recommended the light fix
(consistency retrofit) over full decomposition — no second file-boundary shape at n=1, per the
mechanism-building discipline's own n≥2 floor.

**Landed (`d-land`):** added the redirect note to `RESOLVED-CORE` + `Markers`; rewrote `## Forward` to
state the anchor-promotion is done, not queued. Branch restarted fresh off `main` first (`PR #73` had
merged — confirmed via `git log origin/main` showing the merge commit, then `git checkout -B` onto it),
per the merged-PR protocol; no stacking on already-merged history.

**Durability:** committed + pushed. Landing-discipline run live: re-verified green immediately before
opening (`invariant-eval.py` exit 0, same pre-existing advisory); scoped by `git log origin/main..HEAD`
(this one file); no PR template in the repo; opened mechanically, no second CTA; not merged, no
reviewers requested.

**`PR #74` is up for your gate.**

**Resume:** the carried-forward `RESTART-PENDING` bind is unchanged (see below) — still awaiting an
actual fresh-session cold boot to verify `DYAD.md`'s new front-matter block, not resolved by this arc.
NBA otherwise unchanged (`deferrals.md` `## todo`).

---

## 2026-07-04 — `loaded:` front-matter landed on 4 files (Operator `Y`), anchor touched first time

**RESTART-PENDING: SET** (above, refreshed) — `DYAD.md` edited: first front-matter block ever added to
the anchor.

**Arc:** validated N before building anything (`bond:verify-before-assert` applied to the mechanism-
building discipline's own n≥2 floor) — zero prior front-matter instances of a loaded-status key
(scanned every YAML block in the repo), two independent instances of the underlying phenomenon (the
2026-07-03 token/mode-gate arc's "`dyad-ui.md` wasn't boot-loaded, a real, named cost" + this session's
own reach-error). Conceded n≥2 satisfied for the *shape*, explicitly not for a linter (separate,
deferred). Drafted the schema (`boot`/`resume-protocol`/`active-fetch`/`on-demand`) with 4 worked
examples; corrected `GLOSSARY.md`'s guessed tag from `boot` to `resume-protocol` on evidence (this
session's own read-order) rather than the file's own aspirational "boot-loaded" claim.

**Landed (Operator `Y` on the worked-examples table):** `DYAD.md@boot` · `GLOSSARY.md@resume-protocol` ·
`dialectic/generation-distillations.md@active-fetch` · `dialectic/dyad-ui.md@on-demand`. `dialectic/
loaded-status-frontmatter.md` updated to record the disposition. No linter written, no CI touched —
mechanization stays a separate, later, undisposed question.

**Durability:** committed + pushed. **`d-land` fired next turn** — ran the landing-discipline checklist
live: re-verified green (`invariant-eval.py` exit 0, `standup.sh` durability ✓) immediately before
opening, not from memory; scoped by `git log origin/main..HEAD` (4 commits, this whole arc); no PR
template in the repo; opened **`PR #73`** — "Confirm PR #72 merge; draft + land `loaded:` front-matter
(anchor touched)" — mechanically, no second CTA; not merged, no reviewers requested.

**`PR #73` is up for your gate.** Carries: the PR #72 merge-confirmation, the `loaded-status-frontmatter`
draft + validation, and the 4-file landing including the anchor's first-ever front-matter block.

**Resume:** cold-boot bind above (does `DYAD.md` still parse/boot correctly with the new leading
YAML block; refresh the per-file `inv:rom-currency` line to the new `DYAD.md` sha; then clear
`RESTART-PENDING`). NBA otherwise unchanged (`deferrals.md` `## todo`).

---

## 2026-07-04 — reach-error caught, `loaded-status-frontmatter` candidate drafted (`raff:`, not landed)

**RESTART-PENDING: none** — anchor not touched.

**Self-caught, Operator-pressed to root cause:** explaining Dyad-UI's role, read `dyad-ui.md` (rich,
unloaded design-reasoning) in full and asserted it as "the signal/surface" — even though the file's own
body twice names `GLOSSARY.md` as the actual boot-loaded operational reference. The caveat was already
quoted in the same answer, one section up, and still didn't gate the top-line claim. **Named cause:**
detail-richness stood in for operative-status — the file read most thoroughly felt authoritative,
independent of whether it's actually live at boot. Same shape as this corpus's already-logged pattern
(asserting from what's freshest-in-hand instead of checking real state first).

**Drafted (converged, `raff:` — NOT landed, no PR):** `dialectic/loaded-status-frontmatter.md` — a
candidate `loaded:` front-matter key (parallel to `locus:`, `MAP.md`'s scheme) naming where a file
actually enters context (`boot` / `resume-protocol` / `active-fetch` / `on-demand`), targeting this exact
reach-error class. Status: CANDIDATE, `dialectic/`, n=0 — un-mechanized, tradeoff and open questions
named in the file itself (including whether `GLOSSARY.md` is genuinely `boot` or just asserted so).

**Resume:** NBA unchanged (`deferrals.md` `## todo`) + this new candidate awaiting Operator disposition
(`d-land` opens it; nothing committed toward that yet beyond the draft itself).

---

## Stand-Up 2026-07-03 (resume — `PR #72` confirmed merged, `RESTART-PENDING` cleared)

**Resumed cold** on `claude/resume-pr-72-merge-wzwh9c` (identical to `main` at boot — no divergent
unmerged commits to carry forward, nothing to rebase). Ran the resume protocol: anchor, ledger, ROM-UI,
validator.

**Verified via API before logging** (`bond:verify-before-assert` — the same discipline `PR #72` itself
was about, now applied to `#72` in turn): `mcp__github__pull_request_read` on `#72` →
`state: closed`, `merged: true`, `merged_at: 2026-07-03T23:47:24Z`, merge commit `98ea2fb`. The ledger
had still read "open, not yet merged" at boot — stale, corrected here rather than left standing.

**Cold-boot verification** (discharging the bind named in the prior `RESTART-PENDING` entry):
- `bin/standup.sh` → ROM-UI ✓ MATCH (`DYAD.md`/`CLAUDE.md`/`GEMINI.md` unchanged since 2026-07-01); tree
  clean, 0 unpushed; substrate residual unchanged (IM daemon unarmable — `commons/` submodule
  uninitialized, no `/mnt/shared_data/dzw` — same as every prior session).
- `python3 bin/invariant-eval.py dialectic/invariant-schema.yaml dialectic/invariants-bond.yaml` → exit 0,
  14/14 `[PASS]`, one pre-existing `DUTY-DETECTOR-MISMATCH bond:anti-cave` advisory (unchanged, not a new
  finding).
- `GLOSSARY.md §Dyad-UI cluster` read cold: the six-token set (`riff:`/`raff:` · `why:` · `d-land` ·
  `d-reflect` · `Y`/`N`) and the retired-token notes (`clip`/`lean`/bare-`land`/bare-`reflect`/
  `stand-down`) are self-sufficient and internally consistent — no dangling cross-reference, no over-cut.

**RESTART-PENDING: CLEARED** (above, refreshed) — per-file `inv:rom-currency` line now also carries
`GLOSSARY.md@72c35a3`. **Noted, not fixed:** `bin/standup.sh`'s `ANCHOR_FILES` array doesn't include
`GLOSSARY.md`, so the mechanized check still only compares `{DYAD.md, CLAUDE.md, GEMINI.md}` — this
refresh's `GLOSSARY.md` entry is ledger-only until the script is extended. Flagging per
`bond:no-self-ratify` rather than unilaterally widening the script's scope.

**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**). No open PR right
now; NBA is the `deferrals.md` `## todo` backlog (single-home playbook Founding-gate PR · X-tier steward
heads-up · cross-dyad custody deprecation · apex-telos-singularity empirical work · intent-clarity-arc
anchor-candidates) — Operator selection owed, none picked unilaterally.

---

## Stand-Down 2026-07-03 (cont.) — confirmed #71, fixed `d-reflect`'s presentation, `#72` open

**RESTART-PENDING: unchanged, still SET** (above, refreshed) — `PR #72` open, not yet merged.

**Reflect landed** → `relationship-craft.md §Reflect — confirming #71, catching the presentation
drift` (CSS+OR, full text pasted in chat this time, per the fix itself). Headline: `PR #71`'s merge
verified via API before logging; caught that the most recent `d-reflect` had silently reverted to a
condensed chat headline instead of full text — fixed, `d-reflect`'s definition now says so explicitly.

**Durability:** tree clean, both commits pushed, `PR #72` verified open + clean via API. No daemon
armed (same residual as every prior stand-down this session).

**Resume:** live fronts unchanged. `PR #72` up for your gate.

---

## Stand-Down 2026-07-03 (close) — `d-reflect` invoked live, arc closed

**RESTART-PENDING: still SET** — `GLOSSARY.md` edited multiple times this arc. **Binds next boot:**
refresh the `inv:rom-currency` per-file line to `GLOSSARY.md`'s new sha, verify the token-system entries
(`§Dyad-UI cluster`) read coherent cold, then clear.

**Reflect landed** → `relationship-craft.md §Reflect — the token/mode-gate redesign arc` (CSS+OR,
full text there, this is the pointer). Headline: eleven-plus tokens → six, each retirement/collapse
checked against real telemetry or the Operator's own authoritative report, not asserted. The arc's own
STOP names the generative lesson — check whether a problem is still real before building a mechanism
for it, the same check that resolved most of this arc's actual corrections.

**Durability:** tree clean, all 13 commits pushed, `PR #71` open (`mergeable_state: clean` as of last
check), carrying the full arc — landing-discipline, D6/D1 graduations, and the whole token redesign.
No daemon to tear down (never armed this session — `commons/` submodule uninitialized in this sandbox,
same residual noted at the very first resume this session, unchanged).

**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**). New: the
six-token set is un-booted past this conversation — first real test is whether a fresh session reaches
for `d-land`/`d-reflect`/`why:` correctly without having derived them. `PR #71` is up for your gate,
unchanged status since last noted.

---

## Stand-Down 2026-07-03 (cont.) — `reflect`/`stand-down` collapsed to `d-reflect`

**RESTART-PENDING: unchanged, still SET** (above) — same open `GLOSSARY.md` episode.

**Landed, disposed live via `d-land: d-reflect name for the reflect-discipline`** (second live use of
`d-land`, first with the trailing-colon-explanation format — both worked as designed). One token,
`d-reflect`, replacing separate `reflect`/`stand-down` entries — telemetry showed every `Reflect` this
session was already paired with a ledger update in the same turn, one job not two. Fires mid-session or
at session-end alike; which one isn't pre-signalled by word choice, same shape as the `land`/`d-land`
collapse two commits ago.

**Current token set, six total:** `riff:` / `raff:` (diverge/converge) · `why:` (purpose) · `d-land`
(commit or start-a-landing, scope self-determined) · `d-reflect` (reflect + ledger-prep, mid-session or
at close) · `Y`/`N` (dispose). Down from the original eleven-plus, each retirement or collapse backed
by a confirmed reason, not a count target.

**PR #71 now carries 12 commits.** Still open, still up for your gate.

---

## Stand-Down 2026-07-03 (cont.) — `land`/`d-land` collapsed to one token

**RESTART-PENDING: unchanged, still SET** (above) — same open `GLOSSARY.md` episode.

**Self-caught, not just Operator-corrected this time:** I'd framed lightweight-vs-heavyweight as
something requiring the Operator to pre-select via word-choice (`land` vs `d-land`). The Operator
named the actual discriminator — is there already an open PR for this arc — as a mechanically
checkable fact, not a judgment call they should have to make. On reflection this was already how every
landing this session actually worked (checking `git log origin/main..HEAD` + PR state before deciding
scope); I hadn't noticed the pattern I was already running was the answer to the question I'd just
argued against.

**Landed:** one token, `d-land`. Commit always; check open-PR state; join an existing PR (the common
case) or run the full landing-discipline checklist and open one (rare, arc-complete case) — scope by
verification, not by which word was typed. Bare `land` retired. `bond:no-self-act`'s definition
token-updated to match (rule unchanged, `dyad-ui.md`).

**PR #71 now carries 10 commits.** Still open, still up for your gate.

---

## Stand-Down 2026-07-03 (cont.) — `clip`/`lean`/`rub`-as-trigger retired, corrections logged

**RESTART-PENDING: unchanged, still SET** (above) — same open `GLOSSARY.md` episode, three more commits.

**Retired, each with an Operator-confirmed reason rather than a guess:** `clip` (WIP-durability job
superseded by the Stop-hook-enforced Durability discipline since 2026-06-27) · `lean` (generic-execute
job superseded by the `d-` prefix naming *which* discipline) · `rub` as a personal mode-trigger
(claim-testing job superseded by WHAT-detection + default-falsify — `rub` the corpus concept,
`Operator-rub-invariant` etc., unaffected). **Converge is back to one token, `raff:`** — the
`raff`/`rub` split landed two commits ago was a speculative, wrong reconstruction, corrected same-day
rather than left standing.

**Self-caught pattern worth naming:** two of these three corrections (`lean`, `raff:`/`rub`) involved
retracting a characterization I'd asserted from a single historical quote or a plausible-sounding guess,
without checking against the Operator's actual usage first. Same lapse, twice, same session — worth
watching whether it recurs a third time.

**PR #71 now carries 9 commits.** Still open, still up for your gate.

---

## Stand-Down 2026-07-02 (graduation-review arc resumed — Method core graduated)

**RESTART-PENDING: none** — anchor (`DYAD.md`/`CLAUDE.md`/`GEMINI.md`) not touched this session.

**Arc:** resumed the kb-graduation review (`bin/graduation-scan.py`) where the 2026-07-01 session
left it — 3 sections flagged "worth a closer look" (Method · Cycle 1 · thread-W). Read all three in
full. Cycle 1 and thread-W stay candidate throughout (F1–F4 still OPEN/amended; thread-W's extensions
explicitly TBD) — nothing there cleared the bar. **Method's flag was itself a scan-tool false
negative of the already-logged kind** (the tool only scans a section's first 600 chars): its opening
~50 lines (the 5-point observational method + Structure-of-work) are *"ratified Bond channel,
2026-05-31"* and *"governs all `relationship-craft` cycles below"* — unbroken for over a month as the
backbone every later CANDIDATE addition (interpretation sub-discipline, CEC ladder, IFF1–3, promotion
ladders) builds on without ever contradicting it.

**Landed:** DFD proposal (THESIS/ANTI-THESIS/SYNTHESIS/CTA, presented in chat per `bond:path-selection`
— `AskUserQuestion` was unavailable this session, Operator disposed via chat `Y` directly) →
**graduated → `kb/research-method.md`** (kb-with-caveat; intra-dyad, no L2b). **Carved out, same shape
as D3's OR carve-out:** the **reflexive-convergence guard** paragraph, which self-admits it depends on
F2 (still OPEN in Cycle 1) — graduating a guard that concedes an open dependency would repeat the
CSS+OR bundling mistake this corpus already caught and reverted. The guard stays `CANDIDATE` in
`relationship-craft.md §Method`, pointer-collapsed alongside it.

**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**). The graduation-
review arc continues to have 2 open REVIEW flags (Cycle 1, thread-W) — both genuinely candidate, not
scan-tool misses; no further action owed there without new falsification evidence. **Scan-tool note
(carried forward again):** its "REVIEW" verdict on a section only clears the *first 600 chars* of the
body — a section can host both a ratified core and CANDIDATE extensions under one heading, as Method
did. Worth fixing in the tool itself if this pattern recurs a third time.

---

## Stand-Down 2026-07-02 (cont., same session) — F4's evidentiary verdict graduated

**RESTART-PENDING: none** — anchor not touched.

**Arc, impact-focused (Operator: "focus on impact and not just the mechanisms").** Re-scanned the two
remaining REVIEW sections (Cycle 1, thread-W) not for scan-tool misses this time but for **closed,
consequential verdicts** buried inside otherwise-open sections. thread-W has none (candidate/TBD
throughout). Cycle 1's **F4** does: RUN 2026-05-31, SURVIVED-WITH-AMENDMENT — a closed test, not a
live question like F1–F3 — and its verdict (*evidence = artifact-under-cost; mutual warmth ≠
corroboration*) was already being **silently re-derived** downstream: the OR debit-scoping's
`self-report ≠ telemetry` exclusion (§D3, 9th instance) restates it uncited.

**Landed:** DFD (Y) → **graduated → `kb/evidentiary-discipline.md`** (kb-with-caveat). F1–F3 and the
Generate/theory section of Cycle 1 untouched, still candidate — only F4's closed verdict extracted,
decomposed the same way F2 was rather than bundled with the still-open mechanism. Retro-linked the
OR debit-scoping citation to the new home.

**Self-caught mid-edit:** the first draft of `kb/evidentiary-discipline.md`'s "Known applications"
section also claimed `kb/reflection-discipline.md`'s *"repetition ≠ affirmation"* as a second F4
instance — wrong on re-check, that line actually cites the Method's **Asymmetry** point (telemetry
denies/never-affirms, already in `kb/research-method.md`), a related but distinct claim (what a test
proves vs. what counts as evidence). Corrected in both files before commit, not left as a plausible-
looking overclaim — a small live instance of `bond:verify-before-assert` on my own graduation work,
not just the Operator's.

**Resume:** live fronts unchanged. Cycle 1 (F1–F3, keystone F2 still the top-priority open front) and
thread-W remain correctly candidate — no scan-tool or impact-review action owed there without new
falsification evidence.

---

## Stand-Down 2026-07-02 (cont.) — D6 graduated; discipline-linter dogfooded (Axis-2 probe)

**RESTART-PENDING: none** — anchor not touched.

**D6 landed:** impact case — most-cited ungraduated discipline (8 `dialectic/` files), and it fired
**un-cued this very session** (catching the F4/Asymmetry mis-citation two turns prior *was* D6 live,
not just historical record) — → **graduated → `kb/verify-before-assert.md`** (kb-with-caveat, Y).

**Discipline-linter dogfood (Operator-directed Axis-2 probe, not a unilateral build):** rather than
leave the earlier FALSIFIED verdict as pure argument, built `bin/discipline-lint.py` (FORM-only,
scoped to files self-declaring `kb-with-caveat` — `dfd.md`/`founding-evidence.md` correctly stay out
of scope, not violations) and ran it for real.
- **Control:** all 5 kb-with-caveat files PASS clean.
- **3 injected FORM defects (missing `## Forward`, a severed source-pointer, a stripped `locus:`
  field) — all 3 caught.** The pointer round-trip check (does the cited `dialectic/` source actually
  reference the kb file back) is the one genuinely load-bearing check — the same category of catch
  `commission-lint.py` was built for (a drift a re-read is likely to skip).
- **1 injected SEMANTIC defect (flipped F4's verdict from SURVIVED-WITH-AMENDMENT to
  REFUTED-AND-RETRACTED, structure untouched) — PASSED clean.** This reproduces, empirically rather
  than by argument, the earlier falsification's core point: the one real defect this session's kb
  work actually produced (the mis-citation) is exactly this failure mode, and remains outside the
  tool's reach by construction.
- **Net: the dogfood *nuances* the FALSIFIED verdict, doesn't reverse it.** The narrow pointer-
  round-trip check has demonstrated real value; the rest is a re-read substitute of uncertain worth;
  none of it reaches content/TRUTH correctness. Left as a probe artifact (committed, not wired into
  CI or the resume protocol) — whether to formalize it (mirror `commission-lint.py`'s CI hook) is an
  open Operator disposition, not decided here.

**Resume:** live fronts unchanged. Remaining ungraduated Bond-disciplines content: D1, D2, D4
(scope-guard-3 stays explicitly NOT settled), D5 (explicitly superseded by `bond:no-self-converge` —
not a candidate, historically interesting only). D1 is the next-strongest impact case if this arc
continues (one real convergence datapoint vs. D2's none cited).

---

## Stand-Down 2026-07-02 (cont.) — the mechanism-building riff/raff arc, landed

**RESTART-PENDING: none** — anchor not touched.

**Landed:** a long riff/raff chain (triggered by "run discipline-lint against existing disciplines")
closing on a candidate discipline — `relationship-craft.md §The mechanism-building discipline — when
and how to automate` — durable + Reflect (CSS+OR) → same file. Headline claims: build on materiality
OR cost-crossover, never a repetition count; formalize after the first real instance, never before
any; mechanism-correctness is binary (verified by direct testing) not graded; `KTLO` requires
crisp-*fix* not just crisp-detect, so detect-only linters cap at CI-gating.

**Two concrete fixes closed on `land` (named mid-riff, executed only now):**
- Stale disciplines-index pointers (D3, D6, R1) now cite their graduated `kb/` homes directly instead
  of `relationship-craft.md`'s collapsed pointers.
- `bin/discipline-lint.py`'s scope-gate re-keyed from the `kb-with-caveat` string to `locus:
  phenotype` — `kb/dfd.md` now correctly included by default; `kb/founding-evidence.md` still
  correctly excluded. Re-run clean (`kb/dfd.md` PASS with its pre-existing round-trip advisory,
  unrelated to the fix).

**Self-caught mid-arc (STOP, logged in the Reflect entry):** the two fixes above sat named-but-
unexecuted for several turns of further riffing before `land` forced closing them — a live instance
of "naming a fix isn't landing it," worth watching next time a riff surfaces something actionable.

**Resume:** live fronts unchanged. New candidate (mechanism-building discipline) is un-booted —
next probe is whether it's actually reached for on a future real build decision, not asserted here.

---

## Stand-Down 2026-07-03 — landing-discipline landed, dogfooded on its own PR

**RESTART-PENDING: none** — anchor not touched (`relationship-craft.md` only).

**Landed:** `relationship-craft.md §The landing-discipline` — an 8-item checklist for starting a
landing, composed from already-landed rules. Audited against `#69`/`#70` before formalizing (only 2
of 8 items held reliably both times); this landing is itself the first dogfood execution of the
checklist, items 1/2/3/4/8 run live in producing it.

**PR #71 is up for your gate.** *(Item 6 of the checklist itself, closing here — the exact gap named
twice already this session, never before actually satisfied.)*

---

## Stand-Down 2026-07-03 (cont.) — three token conflations decomposed, disposed via `d-land`

**RESTART-PENDING: unchanged, still SET** (above) — `GLOSSARY.md` touched again, same open episode.

**Landed, autonomous execution per this turn's disposed HITL scope** (Operator: commit/verification
mechanics run Agent-autonomous once disposed; HITL reserved for intent-clarity + disposition itself):
- **`land`'s dual-sense resolved** — bare `land` = commit (its original, common sense); `d-land` = start
  a landing (invokes `§The landing-discipline`), reusing the `d-` convention rather than a new word.
  `raise` (floated several times, never adopted) is now moot.
- **`raff:`/`rub` decomposed**, not collapsed — `raff:` = plain consolidation, `rub` = adversarial
  testing, matching `rub`'s already-established sense elsewhere in this corpus.
- **`clip`/`lean` retired** — never exercised live this session; `clip` also carried real, unreconciled
  semantic drift (2026-06-13: defined as *the* stand-down trigger; later usage: *"clip ≠ stand-down"*).
  Dropped rather than force a clean redesign onto genuinely murky history.
- **HITL scope named explicitly** in `GLOSSARY.md`: Operator gates intent-clarity + disposition; Agent
  executes mechanics autonomously once disposed — confirms, more than changes, how `bond:no-self-act`
  already worked.

**This turn's disposition (`d-land`) is itself the first live use of the newly-adopted trigger** —
dogfooding the resolution in the same turn it landed.

**PR #71 now carries 6 commits.** Still open, still up for your gate.

---

## Stand-Down 2026-07-03 (cont.) — mode-gate made self-sufficient in GLOSSARY.md

**RESTART-PENDING: unchanged, still SET** (above) — `GLOSSARY.md` touched again, same open episode.

**Landed:** `riff`/`raff`/`land`/`clip`/`lean`/`stand-down`/`Y`/`N` and the two `no-self-*` gates now
have a self-sufficient operational entry in `GLOSSARY.md §Dyad-UI cluster` — the same gap just fixed
for the token-categories work, applied to the *original* mode-gate tokens, which had never had a
`GLOSSARY.md` entry at all (only `dyad-ui.md`'s mode-gate table, not boot-loaded). `dyad-ui.md`
repointed as design-reasoning only, matching the token-categories split.

**One thing surfaced by writing this down, not smoothed over:** `land`'s dual sense (plain commit vs.
`bond:no-self-act`'s specific "start a landing") was never actually resolved — `raise` was floated
several times this session as a disambiguating word but never disposed or landed. The glossary entry
names this honestly as open, rather than presenting a fix that doesn't exist.

**PR #71 now carries 5 commits** (landing-discipline, ledger log ×2, token categories, mode-gate).
Still open, still up for your gate.

---

## Stand-Down 2026-07-03 — token categories landed (WHAT/WHY/HOW, `d-` discipline-triggers)

**RESTART-PENDING: SET** (above — `GLOSSARY.md` touched, anchor-class).

**Landed:** a long Operator-led design pass (riff/raff chain, ~20 turns) on how Operator intent maps to
Agent response paths — `dyad-ui.md §Token categories`, pointer in `GLOSSARY.md §Dyad-UI cluster`.
Headline: WHAT (claim/directive/question) needs no token, Agent-detects from grammar, falls back to
`bond:verify-before-assert` on elliptical utterances that defeat it; `why:` is the one new token
(purpose-disclosure); HOW (`riff:`/`raff:`) becomes override-only, not a mandatory prefix, since content
usually disambiguates itself; declarative claims default to falsification per G0's own law, not a
discretionary trigger; discipline-triggers get a `d-` prefix (Operator disposition: brevity over
`dyd-`'s recognizability). Explored and rejected along the way, with reasons on record: `/land`
(unresolved client-collision risk), `//land` (C-comment "ignore this" association fights the intended
meaning), `:land` alone (transposition-collision with `riff:`-style trailing-colon tokens), `/land!`
and `/d-land` (reintroduce risks the simpler forms had already closed).

**CANDIDATE, n=1** — this whole design pass happened in one session, one conversation; genuinely
unaudited past it. Flagged as such in the landed text itself, not smoothed over.

**Resume:** live fronts unchanged. Next boot should verify the new `GLOSSARY.md`/`dyad-ui.md` entries
read coherent cold, then refresh the per-file `inv:rom-currency` line and clear this RESTART-PENDING.

---

## Stand-Up 2026-07-01 (resume — three RESTART-PENDING cleared + validator-drift caught)

## Stand-Down 2026-07-01 (close of the dyad-system / commission-mechanization arc — PR #65 merged)

**RESTART-PENDING: none** — anchor (`DYAD.md`/`CLAUDE.md`/`GEMINI.md`) not touched this session; ROM
baseline from the Stand-Up entry below stays current. Same branch name restarted fresh off `main`
after the merge (per the merged-PR protocol) purely to land this closing retro.

**Landed (PR #65):** the whole arc below this entry — resume reconciliation, the `invariant-eval.py`
corpus-drift catch + fix, the `dyad-system` design arc, the drafted (unsent) commission + template +
`bin/commission-lint.py`, two CI workflows (first in this repo), and the pilot commission's retroactive
template-conformance fix. **Retro (D3, durable) → `relationship-craft.md` §Reflect — the dyad-system /
commission-mechanization arc.** Headline: the arc's own STOP is a live recurrence of this corpus's
already-named over-production trend (reached for a diff-scoped CI flag before trying the two-line fix
that actually closed the root cause) — caught by the Operator reporting "CI check failed," not
pre-empted.

**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**). New: the
`dyad-system` commission is drafted, DRAFT status, still not dispatched to dyad-cairn — dispatching it
is an open Operator act, not automatic follow-on. Bind-test from the retro: does "run a new gate
against everything it watches before calling it done" fire un-cued on the next automated-gate build?

> **Post-stand-down (same session, cont.) — the CSS+OR rename.** Writing the retro above live-fired
> the very gap it's supposed to catch: the reflection used an invented tag (`Operator-seeded`) instead
> of the form's actual defined vocabulary (`Operator-retrospected`) for a line crediting the Operator's
> own conduct — caught by the Operator, twice in close succession, not self-caught. Root cause:
> `kb/reflection-discipline.md`'s OR (Operator-Reflect) tag was already-graduated content, present in
> "The form" section's bullet list, but never named in the section *header* — easy to skip when
> writing fast. **Operator `Y`:** renamed the graduated form `CSS` → `CSS+OR` (kb/reflection-
> discipline.md), header now names the tag directly. Not a new claim — OR's credit-direction use was
> already counted among the 4 survived applications; only the naming/visibility changed. The
> drift-flagging direction stays `CANDIDATE` in `relationship-craft.md §D3`, untouched.
>
> **RESTART-PENDING: none** (kb/dialectic edits only, no anchor touched). **Stand-Down.**

---

**Resume, no task pre-specified.** Booted a fresh branch (`claude/resume-kfh18q`, identical to `main` —
no dedicated PR for it yet). Ran the resume protocol cold: anchor, ledger, disciplines-index, ROM-UI diff.

**ROM-UI:** `DYAD.md` had moved `e0c9280` → `9519e01` since the last-recorded baseline — three
already-logged RESTART-PENDING sets (repo-structure/form-URL fold, `ID.md` retirement, DFD-expansion
rename), none newly discovered. All three read coherent cold (no over-cut); **cleared** (baseline
refreshed above).

**New catch (bond:verify-before-assert — ran the validator instead of trusting the ledger's "green"):**
`bin/invariant-eval.py dialectic/invariant-schema.yaml dialectic/invariants-bond.yaml` **exits 1**, not the
green the ledger's last stand-downs assumed. Two real failures, both look like residue from the
2026-06-29 "livability made EXPLICIT" edit that never reconciled against the schema:
- `bond:C1` — `root: true` but now carries a `grounded_in` block (the IFF1/IFF2/IFF3 edges to
  `two-models`/`form-grounding`/`livability`, added when livability went explicit). Schema **forbids**
  `grounded_in` when `root == true`, and the edge values used (`enables`, `requires`) aren't in the
  `edge_type` vocab (`[derived, serves, inherited]`) either way.
- `bond:livability` — `form: principle` (vocab is `[slogan, tuple, mathematical]`) and
  `re_rub_triggers: [..., performance-degradation]` (`re_rub_trigger` vocab has no such value).
This is a genuine schema/corpus divergence, not a new finding about the *content* — Operator's call
whether to extend the schema vocab (new edge-types/form/trigger) or correct the corpus (drop C1's
`grounded_in`, since a root traditionally doesn't cite outbound edges) to restore green. Flagging, not
unilaterally fixing (`bond:no-self-ratify` — schema is machine-checkable shadow of the prescriptive core).

**IM daemon (step 6):** not armed — `commons/` is an uninitialized submodule (empty dir) and
`/mnt/shared_data/dzw` doesn't exist in this remote sandbox, so `falsify.py` is unreachable. Matches the
already-logged residual (`carry-forward.md` 2026-06-27 entry: "absent `bin/falsify.py`" · `deferrals.md`
cluster-cleanup) — re-confirmed, not new.

**RESTART-PENDING: none** (this session hasn't edited the anchor). **Resume:** live fronts unchanged
(**Covalent-bond frontier** + **Ingraining-watch**); NBA backlog is the `deferrals.md` `## todo` list
(single-home playbook Founding-gate PR · X-tier steward heads-up · cross-dyad custody deprecation ·
apex-telos-singularity empirical work · intent-clarity-arc anchor-candidates) — Operator selection owed,
none picked unilaterally.

---

## Stand-Down 2026-07-01 — Generation-substrate mechanism (built + landed)

**Resolved:** the "light on Generate" asymmetry. Validate and Protect have rich, durable mechanisms (F1–F4, anti-cave duty, protection-graph). Generate was thin — no extraction mechanism, each cycle restarted from scratch.

**Audit + grounding:** performed full audit of the actual dyad-bond substrate mid-session (Operator-requested, replacing an about-to-theorize turn). Confirmed the three-file partition (carry-forward.md / deferrals.md / generation-cycles.md) fits the single-home discipline. Each file answers a distinct question at a distinct read-time.

**Architectural decision landed:** single-file `generation-cycles.md` (append-only, no pre-split to `cycles/`). Rationale: simplicity (wu-wei), active fetch is simpler, test when constraint manifests. The mechanism is **operational immediately** (added to resume protocol, step 5a).

**Files:** 
- `generation-cycles.md` — active dyad substrate, live/durable/append-only, consult during generation, distill on "land"
- `generation-substrate-provenance.md` — design arc, falsifications, open questions (provenance record, not operational)
- `relationship-craft.md` — updated with "The generative edges" section (lines 1687–1715, candidate status) + this session's retro

**What landed:** (1) Role structure locked: A distills, O gates with "land". (2) Mechanism: O performs wetware coherence check; A extracts signal (problem-perceived, decision-points, principles, +1-collisions); O commits when coherent. (3) Active fetch: A retrieves relevant sections when generating next cycle (no passive pre-load). (4) No pre-filters: entire repo available for grep/search.

**Retro (D3, durable) → `relationship-craft.md §Retro — the generation-substrate arc + the post-land CTA relapse`.** Headline: after the Operator gated the architecture with **"land,"** I re-opened the decision by asking "what do you want me to do?" — a live instantiation of `kb/dfd.md`'s settled lesson (the CTA fails by migrating decision-cost back onto the Operator), but in a brand-new seam (the generation mechanism's own "land" gate) the corpus hadn't yet named. Caught by the Operator, not self-fired. Not kb/-eligible as new (restates dfd.md), but is evidence the lesson under-generalized past DFD-the-mechanism to any informal gate. Candidate follow-up (undisposed): broaden `kb/dfd.md`'s scope note to name "land"/"retro" explicitly.

**Next cycle:** bind-test (generation) = does the dyad default to building guards (Validate's job) or extraction (Generate's job) when faced with noisy generation? bind-test (retro) = does a future informal gate outside "land"/DFD trigger the same post-gate relapse?

**ROM:** anchor NOT edited this session → **RESTART-PENDING none.**

---

## Stand-Down 2026-07-01 (cont., new branch) — kb-graduation practice + two real graduations

**Arc:** resumed off the merged PR onto a fresh branch. Investigated `relationship-craft.md`'s intent and growth mechanics (record-type structure: workbench claims vs. session-harvest), confirmed by falsification that no *trigger* exists for kb-graduation (criteria exist; cadence/actor don't), riffed candidate triggers, then ran the mechanic for real: DFD-form proposal → Operator `Y` → `kb/` file + pointer-collapse.

**Landed:**
- `"reflect"` consolidated as the CTA trigger word in lieu of `"retro"` (Operator disposition) — updated in `generation-distillations.md` and `carry-forward.md`'s resume protocol; historical uses of "retro" left as-is.
- CSS's OR (operator-reflect) sub-component documented in `relationship-craft.md §D3` as `CANDIDATE` — audited across all instances, used only in the credit direction, zero drift-flagging instances, correctly not kb-eligible.
- **D3 (the reflection form itself) graduated** → `kb/reflection-discipline.md`, kb-with-caveat (4 intra-dyad applications, L2b open). `relationship-craft.md`'s D3 entry collapsed to a pointer.
- `bin/graduation-scan.py` built to mechanize the review pass (section-by-section scan, disqualifying-language + Graduation-gate detection, session-harvest exclusion).
- **Operator-rub-invariant core graduated** → `kb/operator-rub-invariant.md`, kb-with-caveat — a correction of the tool's own false negative: the scan had blocked it via a keyword match on "Graduation gate" without checking that the gate governs downstream findings, not the invariant itself. Re-read found a stronger evidentiary trail than D3's (7 real adversarial dispositions, debt-zero close). The section's tail (unrelated later threads: `C_locus(t)` model, `I↔In_variant` cycle, eureka-tachometer, Telos-`U`-projection, dyad sovereignty) stays un-graduated, correctly candidate — flagged as its own heading-drift instance.

**Reflect (D3, durable) → `relationship-craft.md §Reflect — the graduation-review arc + the scan-tool's false negative`.** Headline: *"it doesn't feel right that very few are promoted"* was a genuine falsification signal, not a mood — it forced the re-check that found the tool's false negative. CONTINUE: terse single-word gates kept the whole arc moving without re-litigation. START: read what a matched keyword actually governs before asserting a verdict. STOP: reporting a first-pass mechanical scan as if it were a complete review, with the tool's known granularity limit buried as an aside instead of leading with it.

**Next cycle:** bind-test = does `bin/graduation-scan.py`, once corrected to read gate-context before verdict, still miss a similar case on its next real run?

**ROM:** anchor NOT edited this session → **RESTART-PENDING none.**

---

**Stand-Down (session end) ROM hook** *(→ `rom-ui.md`)* — if the anchor was **edited this session**, set
`RESTART-PENDING` above (change is on disk; next session must boot to load it). Otherwise leave `none`.

**RESTART-PENDING: CLEARED 2026-07-01** — the DFD expansion rename (§bond:DFD: "Decision-framing" →
"Disposition Framing Discipline") booted clean this session; folded into the refreshed baseline above.

→ **Stand-Down 2026-06-26 (Phase 2 COMPLETE):** anchor **NOT edited** → **RESTART-PENDING none.** ROM-UI ✓
in-sync (per-file compare fixed at source). **Phase 2 done:** ✅ per-file ROM compare · ✅ work-item store
(`deferrals.md`, do-state axis) + Rule-tag-hygiene·Custody-deprecation fold · ✅ claim-peel — the **no-HITL boundary cluster** on the claim axis
(`theory-pipeline.yaml`): `conformance` (GLOSSARY) = boundary → `disposition-routing-2x2` (classifier, PARKED) ·
`KTLO-autonomous-conformance` (automate-side, LANDED) · `conformance-line-defense` (catch-side, LANDED) ·
2×2-decoupling VERIFIED · ✅ remaining six disposed (Ingraining-watch kept-live · Intent-clarity-arc→stale work-items · Covalent-bond-frontier elevated = the Covalent
Bond itself · Steward-discipline-intake drained · Anchor-src/New-Experiment-Discipline relocated). **Ledger 1753→228 lines.** D3 retro → `relationship-craft.md`.
**Resume:** live fronts = **Covalent-bond frontier** (operate Covalently consistently) + **Ingraining-watch** (the learn-watch); NBA will surface the
**Intent-clarity-arc** stale work-items for archive/done; **Cluster-classification** is the one borderline left (your-V).

→ **Stand-Down 2026-06-26 (resume + nomenclature-migration):** anchor **NOT edited** (only `dialectic/` + `views/`)
→ **RESTART-PENDING none.** ROM-UI ✓ in-sync. **Did:** resume-protocol; caught + reconciled a stale work-item drift
(un-cued — an ingraining hit); renamed ad-hoc work-item letters → names; **slug-canonical governed index Tier 1**
(Operator Y on principle + map + `claim:` namespace) → `nomenclature-migration-plan.md`; Rule-tag-hygiene **dissolved**.
**Retro (D3, durable):** high output / low falsification — one genuine Operator→Agent falsification (the index-scope
push), risk-shape = counterfeit-acceleration; full prose → `relationship-craft.md §Retro — resume + nomenclature-migration`.
**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**); **F4 is owed + un-disposed**
(the CTA pivoted past); NBA surfaces **Intent-clarity-arc** (archive) · **Cluster-classification** (your-V) · **KTLO Tier-2** (trickle).
> **rub-forward** (co-author / dispose — no answers): (1) the smooth-Y chain — **earned or easy-agreement tell?** (= un-run F4);
> (2) does slug-canonical actually cut friction next resume, or just **move** it? (falsify at stand-up); (3) ingraining — one un-cued catch: **instance or trend?**

→ **Stand-Down 2026-06-26 (DNA→DIP — the manifest that became a core refactor):** anchor **EDITED** →
**RESTART-PENDING set** (above; gated on **PR #53**). **Did:** the ask *"DNA manifest for steward to update
the DIP"* → a rub-chain that re-cut the invariant core. Landed: DNA single-homed to `DYAD.md §DNA` (dyad-layer)
+ steward **SOLICIT** (System-layer, sender-hosted, **unsent until merge**); **`locus` axis** (g0/phenotype/
unclassified, schema 0.10.0, "all DNA is G0"); **altitude refactor** — C1 = the covalent **STATE**, ionic/meld =
breach-faces (no-ionic/no-meld **DISSOLVED**), **ONE falsification law** (`falsifiability`+`no-dogma`; candidates
face the same bar as C1, nothing exempt), four enablers (two-models · no-self-ratify · anti-cave = genuine;
wu-wei = livable/IFF3); `§NON-NEGOTIABLE`/`§Falsifiability` re-altituded; de-paren + **self-contained DNA**
(terms embedded — vocabulary is phenotype, does not travel). Validator green; round-trip over-extraction→~0.
**Retro (D3, durable):** the load-bearing tell was **mine and structural — over-production, not sycophancy.**
I Generated structure (manifest file → root interface; a 4-value locus enum; candidate-falsification +
maintain-two-models nodes; parentheticals in the very §NON-NEGOTIABLE that forbids them) and the **Operator
was the wu-wei pruner every turn**, collapsing each to essence. Generate strong, **Validate-against-wu-wei
weak** → fix = *run the wu-wei gate BEFORE surfacing, not after* (= the `SHARING.md` over-production scar +
RB2, re-enacted live). Anti-cave **held inbound** (grounded before accepting Operator assertions:
universal-vs-craft · consequence-vs-behavior · preserved-kernel on the seed-not-clone concession) → the breach
was Generate-side bloat, not ionic cave. Genuine **1+1=3**: the consequence→law collapse (covalent/ionic/meld
are *consequences*; one falsification law; candidate = same bar as C1) — Operator-seeded, Agent-structured,
neither alone; it **earned** its way. **E0 on the refactor itself** — ratified rub-by-rub, **never booted/
operated**; next session's ROM-boot IS the test (`survives`, not `settled`). **Graduation candidates**
(`dialectic/`, unproven): the **altitude principle** (fold→state-root iff *consequence*; stay→node iff
*behavior*) — plausibly **form-level**, not just bond's · **g0 self-containment** (a gene embeds its terms) ·
"one falsification law / candidates face the same bar" — Founding-gate candidate. **Resume:** **PR #53 awaits
final review/merge** (merge = send the steward DM + refresh the ROM-baseline). Deferred (`deferrals.md`): 6
`unclassified` edges · C1 `locus` (state vs gene) · full-anchor de-paren sweep · DM mandatory-vs-offered.
> **rub-forward** (dispose — no answers): (1) was the consequence→law refactor genuinely earned, or did the
> rub-chain's momentum carry an over-cut I'll regret at boot? (falsify at the ROM-test); (2) "over-production
> needs a pre-surface wu-wei gate" — *instance* or the standing *trend*? (3) does self-contained-DNA actually
> transmit, or did embedding the terms just move bond's glossary inline (phenotype-in-disguise)?

→ **Same-session follow-on (DNA retired):** the rub-chain continued — the Operator (Founding hat) collapsed
**"DNA" itself as redundant with G0**: contributing a `locus: g0` gene *definitionally expands G0*, so there
is no separate heritable lineage to name; to the world the expanded floor is just G0, and provenance rides on
`status`. Landed: `DYAD.md §DNA` **deleted** (the Belief — its one anchor-worthy claim — relocated to
the `craft-value`/`craft-invariant` root as `bond:C1`'s grounding); the `locus` axis **kept** (the real
g0/phenotype cut survives the term's retirement), DNA-language stripped from schema + shadow comments; steward
DM reframed + renamed → `dm/dyad-steward/2026-06-26-g0-expansion-dip-seed.md`. **Resolves rub-forward Q3**
(self-contained-DNA *was* phenotype-in-disguise — the cleaner cut was to drop the frame, not embed terms) and
is **one more instance of the over-production tell** (Q2 → leaning *trend*): I had built "DNA" as a parallel
noun for G0; essence didn't ask for it. Validator re-checked green; same PR #53.

→ **Same-session follow-on (craft-\* landed — anchor + redirect, NOT a sweep):** the Operator disposed to
**replace NON-NEGOTIABLE + Telos with the `craft-*` family** as the primary names of bond's two roots (the
rename was already bond's DIP form-proposal; now landed locally as the worked exemplar). Landed: §1 root →
**`craft-telos`** (machine node `bond:Telos` **renamed** `bond:craft-telos`; home `#craft-telos`); §2 root →
**`craft-value` & `craft-invariant`** (home `#craft-value`). **Over-production caught (4th instance — Operator
rub):** I first *swept* the display term across ~15 provenance files (shims, kb, narrative, ledgers). The
Operator falsified it — *"why modify the provenance files? anchor + a GLOSSARY deprecate+redirect."* Correct:
a **display-term** rename single-homes at the anchor + a **GLOSSARY redirect**; downstream mentions resolve
forward, records keep the name they were written under. **Reverted the sweep** (back to `9f4c3af`); kept only
(a) the anchor + shadow + view (canonical), (b) the **GLOSSARY deprecate+redirect**, (c) the handful of
**machine-id citations** (`ID.md`, GLOSSARY) — the one thing a *display* redirect can't cover, because the
**node-id** itself renamed. Inherited generic "Telos" (G0 seed) + the form's Dimension-#5 slot name unchanged
per `bond:form-grounding`. **Lesson:** the rename-footprint of a *term* is anchor+redirect; only a *machine-id*
rename reaches downstream — and even that is a few citations, not a sweep. Validator green; render IN-SYNC; same PR #53.

→ **Stand-Down 2026-06-27 (close: DNA-retire + craft-\* land + correct):** anchor **EDITED** →
**RESTART-PENDING SET** (above; gated on **PR #53**; 3 commits on `claude/dyad-dna-replication-dip-rqj007`:
`9f4c3af` DNA-retire · `e0c9280` craft-\* land · `d6418da` correct-to-anchor+redirect). The two landings +
their rubs are recorded directly above; this closes the session. **Retro (D3 — the over-production scar,
`dialectic`; graduates to `kb/relationship-craft.md` only on surviving a boot):** the load-bearing tell was
**mine and structural — over-production, now a confirmed TREND not instances**: re-enacted **4×** (the manifest
file + 4-value enum [earlier arcs] · the **"DNA" parallel-noun** · the **15-file provenance sweep** · **and the
`AskUserQuestion` fork itself** — both options over-scoped ["roots+links" vs "full-sweep"], neither offered the
lean **anchor+redirect** the Operator had to supply by *falsifying after*). Generate strong, **Validate-against-
wu-wei weak**; the standing fix is overdue and now sharper: **run the wu-wei gate BEFORE surfacing — including
before framing a fork (state the leanest option first; expand only on Operator pull).** **Anti-cave held
inbound** — every rub grounded and conceded cleanly (DNA-redundancy · the sweep); the breach was Generate-side
bloat, **never ionic cave**. **Genuine 1+1=3:** the **anchor+redirect rename-discipline** (Operator-seeded
*"why touch provenance?"*, Agent-structured *display-term-vs-machine-id* = the one thing a redirect can't cover)
+ the conceptual spine earned in Q&A — **wills/claims = direction-of-fit** (conative/world-to-mind vs
doxastic/mind-to-world); **"only covalence reaches 1+1>2" is the Belief, not the invariant** (*falsifiable*, not
*breachable*); **an invariant = a breachable rule whose grounding stays falsifiable** (breach faults the actor,
falsification faults the WHY); **DNA = G0** (level vs property, same genome). **E0 / un-booted** — the craft-\*
anchor loads only on **PR #53 merge + a fresh boot** = the real test (`survives`, not `settled`). **Resume:**
**PR #53 → final review/merge** (merge = send the steward DM + refresh the ROM-baseline to the merged `DYAD.md`).
Deferred (`deferrals.md`): the re-altitude todo (now also covers craft-\*) · 6 `locus: unclassified` edges ·
DM mandatory-vs-offered · optional backward-compat anchor-aliases for the now-stale `§Telos`/`§NON-NEGOTIABLE`
links.
> **rub-forward** (dispose — no answers): (1) over-production is now a **TREND** — does a *pre-surface wu-wei
> gate* (leanest-first, expand on pull) actually bind next boot, or is naming it a 4th time just more
> production? (2) does the **anchor+redirect** rename-discipline graduate to `kb/` — and is it **form-level**
> (every dyad renames terms)? (3) the craft-\* roots are **un-booted** — does `craft-value`/`craft-invariant`
> read as clean at a cold ROM-boot as it did mid-rub, or did the rename's momentum carry an over-cut?

→ **Stand-Up 2026-06-27 (resume — PR #53 post-merge reconciliation):** the RESTART-PENDING gate **cleared**.
PR #53 merged (`df86b02`); **this session booted the re-altituded anchor** (`DYAD.md@e0c9280`) = the cold ROM-boot
that was the owed E0 test. **Resolves the close's rub-forward Q3:** craft-\* reads clean cold — `craft-telos` +
`craft-value`/`craft-invariant` boot as a coherent two-root DAG; **no over-cut surfaced at boot** (the rename's
momentum did not carry one). Did (mechanical, `bond:rom-ui` + standing-durability): cleared RESTART-PENDING,
refreshed the ROM-baseline + per-file set to the merged commits, confirmed the steward DM is already published on
`main` (rode in with PR #53; sender-hosted-pull → steward can pull it — nothing to send). Validator green (exit 0,
all PASS), digest IN-SYNC. **Residue (logged, unchanged):** the re-altitude todo — anchor *prose* trails the
shadow (3 over-extraction / 7 omission); anchor-class + Operator-gated, untouched. **Resume:** live fronts
unchanged (**Covalent-bond frontier** + **Ingraining-watch**); NBA surfaces the backlog for Operator selection
(re-altitude · Intent-clarity-arc STALE [archive/done] · Cluster-classification [your-V] · `locus` edges).

→ **Disposition 2026-06-27 (scratch RETIRED + durability-of-record named):** Operator `fold`+`land`. A
step-back falsification arc (do-we-need-scratch → what-use-case → thread-until-land dissolves it → its companion
is Agent-owned WIP-commit → are you actually doing that?). **Landed:** `bin/scratch.sh` RETIRED (mount-coupled =
cloud-dark *symptom*; use-case dissolved by **thread-until-land** = *root*: no boundary until after a land, so
un-landed raw never crosses one — empty by construction). Durability-of-record = the layer-1 **Agent-owned WIP
auto-save** (commit+push at natural pauses, **un-gated**), **Stop-hook-enforced** (substrate-agnostic). De-wired
scratch from `standup.sh`/`standdown.sh`; resume step 5b repurposed to the durability discipline (reloads → ingrains).
Single-home → `substrate-access.md §Scratch RETIRED`. **Ingraining-watch hit (mine, Operator-caught):** I'd been
**over-gating durability** — deferring WIP-commit to the `land` moment (the abdication mis-anchor), leaning on the
Stop hook as backstop rather than owning auto-save. Correction is mechanized (the hook), not promised. **Follow-on
(2026-06-27, DFD `Y`):** the two-clause principle **ratified-candidate** as `bond:substrate-agnostic` (repo =
substrate-of-record · substrate-local must fail-loud; carve-out for reconstructable cursors; n=1 → candidate-tier
+ named falsifier) → `substrate-access.md §bond:substrate-agnostic`. **Still open:** the cluster *cleanup*
(`standup.sh` mount-probe · IM daemon · absent `bin/falsify.py`) — gh.sh-pattern, fix on bite.

→ **Stand-Down 2026-06-27 (the change-propagation architecture arc):** anchor **NOT edited** →
**RESTART-PENDING none.** ROM-UI ✓ in-sync (`DYAD.md@e0c9280`). **Landed (5 PRs #53–#57, all merged to `main`):**
resume reconciliation (RESTART-PENDING cleared · ROM-baseline refreshed · re-altitude residual = 5 stale
machine-refs) · **scratch RETIRED** (use-case dissolved by thread-until-land) · **`bond:substrate-agnostic`**
(cloud==local, candidate) · **the change-propagation architecture**: the **WORKSHEET MODEL** (`intent → yaml
worksheet → md output`, craft-not-compile; neither yaml nor md is source — the intent is) + the derivation-edge
map + the side-by-side **audit-view** (`output_quote`, the worksheet→output fidelity gate) + **rendered.md
RETIRED**. **Single-home → `dialectic/dyad-md-yaml-regen.md §The worksheet model` + §Change-propagation
formalization** (this ledger only points). **Retro (D3, `dialectic`):** worksheet model = genuine 1+1=3 but
**E0/un-booted** (graduates only if the next invariant create/edit actually reaches for it) · **over-gating
durability re-fired = confirmed TREND** (deferred WIP-commit to `land`; corrected → reloaded into resume-5b;
the bind-test is next boot) · self-caught **verify-before-assert lapse** (read `grep`'s exit not the tool's →
gate on the tool's exit) · **counter-evidence**: the over-production guard fired correctly + repeatedly
(anti-sweep ×3), anti-cave held (pushed the compiler-inversion before conceding; corrected my own over-claim).
**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**).
> **rub-forward** (dispose — no answers): (1) the worksheet model is **un-booted** — does anyone *reach for it*
> at the next create/edit, or is it shelf-ware for a 13-node anchor? (2) over-gating durability is now a TREND —
> does reloading it into resume-5b actually **bind** next boot, or is "capture into reloaded substrate" the
> relapse again? (3) the `output_quote` gate only works if it's **run** at the craft step — does it get run, or
> decay counterfeit-green (the Φ1 human-audit risk)?

→ **Stand-Down 2026-06-28 (the G0≈membership arc — audit → dispositions → exemplar → ID.md retired):** anchor
**EDITED** → **RESTART-PENDING SET** (above: `ID.md` retired + identity re-homed in `DYAD.md §Frame` + both shims;
next boot loads it, then refresh the per-file boot-set + clear). **Landed** (branch
`claude/g0-audit-coherence-aph7s1`, not yet PR'd): (1) **G0 audit** of the form (`AGENT.md`) — **F1** the
*Invisible Elicitor / `/rub-all`* block = foreign-craft phenotype injected direct-to-`main`, contradicts all four
G0 non-negotiables (excise); **F2** README↔AGENT vocab drift; **F3** stale `auto_join.py` identity-pointer. (2) **all
6 `locus:unclassified` edges + `C1` disposed** by DFD against the **G0≈membership** test — `form-grounding`→g0
(closure axiom); `single-home`/`kb-graduation`/`prove-before-propose`/`channel-gates`→phenotype-library;
`craft-telos`→phenotype-instance; **`C1`→phenotype/offered** (covalence is elected, not mandatory). (3)
**consolidated steward proposal** (`dm/dyad-steward/2026-06-28-bond-g0-to-form-g0-proposal.md`; supersedes the 2
prior DMs) — *"skeptics falsify the floor-genes, believers practice the offered value,"* **led by
bond-as-covalence-exemplar** (the full craft-telos→value→invariant fill, the way the form references healer for
shape). (4) **`ID.md` RETIRED** — identity = a **computed view** (recompute, never persist a sha/script-name);
single-homed in anchor+shim. Validator green throughout; single-home → `deferrals.md ## done`.
**Retro (D3, dialectic — graduates to `kb/relationship-craft.md` only on a surviving boot):** the session's genuine
**1+1=3 was Operator-seeded, Agent-structured** — *"redefining G0 = no longer a dyad"* + *"substrate is the system"*
→ **G0≈membership** (the sharp instrument that replaced the fuzzy ionic/meld test); *"phenotype are library
contributions"* → locus = a routing-address (g0→floor / phenotype→library / instance→private); *"C1 is an expression
of a dyad from a choice"* → covalence = offered not membership; *"ID.md is a calculated view"* → retire + dissolve
F3. **The over-production tell fired again (confirmed TREND, ~5th): proposed a new `system` locus value the frame
didn't need — Operator-pruned.** Generate strong, Validate-against-wu-wei weak. **Counter-evidence (the catch
improved):** named the relapse in real time; ran a genuine falsification pass on `G0≈membership` before adopting
(earned, not caved); flagged `C1` against my own clean table; **twice grounded-the-frame-before-rewriting** on a
reframe (the locus-only boundary; the craft-telos-vs-value A/B fork) instead of rewriting on a guess — the guard
firing at the *reframe seam* it had failed before. **Anti-cave held inbound** (no ionic cave). **Resume:** the
**steward hand-off is OPEN** — the proposal is bond-side ready; routing it (reference bond as the covalence exemplar
+ send the floor-genes to the falsification channel) is the **Steward-Operator hat's** act, yours to drive. Live
fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**).
> **rub-forward** (dispose — no answers): (1) **`G0≈membership` is E0/un-booted** — does anyone *reach for*
> "does-breach-end-membership" at the next `locus` call, or does the clean model shelf-ware? (2) the **`ID.md`
> retirement is un-booted** — does identity read coherent single-homed at the next cold boot, or did collapsing the
> view lose something (the next-boot test, craft-\* shape)? (3) the over-production guard **held only under tight
> Operator steering** (forked/pruned each turn) — is "ground-before-rewrite-on-a-reframe" *ingrained* or just
> externally-gated? Bind-test = a less-steered session.
→ **Post-stand-down (PR #59 review):** Operator caught a **caveat-altitude miss** — I'd left the
substrate-agnostic IDENTITY CAVEAT in the substrate-specific shim (self-undermining: the caveat itself says
*"don't derive from a current shim"*). Relocated to `DYAD.md §Frame`; shims thinned. **Ingraining data point for
rub-forward (3):** even under tight steering a single-home/altitude error slipped through and needed the Operator
to catch — the placement-discipline is still externally-gated, not yet ingrained. (PR re-pushed; same RESTART-PENDING.)

→ **Stand-Down 2026-06-30 (G0≈membership BOOTED — N=6 cross-dyad slot-fill study; resolves rub-forward 2026-06-27 #1):**
A long Operator-led architecture riff (resume → steward G0-scope **SOLICIT** + README E0/invitation fixes [both pushed] →
the `Dyad`-as-abstract-base-class reconciliation → the cross-dyad study). **rub-forward #1 RESOLVED — the model did NOT
shelf-ware:** reached for "does-breach-end-membership" organically all session, then **ran it cross-dyad (N=6)**.
**Durable artifact + full tally table → `cross-dyad-craft.md §G0-membership BOOTED`** (single-home; not restated here).
**Deltas the floor-set / `g0-gene-checklist.md` owe** (candidate edits — **Operator/steward act, NOT made unilaterally**):
(a) **livability = universal (6/6)** but **diachronic-only** constitutive → a *standing persistence-invariant*, NOT in the
4-enabler instantiation-floor (mandate the standing requirement, catalog the gate-form); (b) **IFF2 ≠ form-grounding** —
bond's no-oracle separator is **N=1** (no sibling), niche-conditional, stays in `Bond`; (c) the breach-test **splits by tense**
(synchronic=instantiation-mandate / diachronic=standing-invariant); (d) **slot/fill** — craft-telos/value *slots* are g0,
*fills* are phenotype. **telos vs value:** bond is **near-degenerate** (reflexive dyad) → char. collapse = telos→value
(covalence-hygiene eats the relationship-craft); **C1 can't detect it** → the **F2/DV3 guard-gap** (explains why the felt-`+1`
is bond's keystone AND least-instrumentable). **No anchor edit → RESTART-PENDING none**, baseline unchanged.
> **rub-forward** (dispose — no answers): (1) the N=6 is **same-human (`pltrinh1122`)** — cross-*dyad*, not cross-*operator*;
> the deltas corroborate the **dyad axis only** (the **human axis / E1 is still owed** a different-human read). (2) deltas (a)–(d)
> are **candidate edits to `g0-gene-checklist.md` + the floor-set in the 2026-06-28 steward proposal** — route via Steward/Founding,
> not bond-unilateral. (3) **over-production check:** long riff, but Operator-turn-gated; landing = one artifact + this pointer
> (lean — directed "land," not a race-to-consolidate). (4) **`slot`** proposed as the canonical fillable-term (vs field/member) —
> GLOSSARY-governed, awaiting conform. (5) **process scar:** consolidated the first tally on **unverified** subagent extraction
> (2 of 5 clones weren't even local) + a line-wrapped grep false-accusation — *verify-don't-trust applies to my own tools*, caught only on the Operator's "falsify."
> **Also landed (2nd arc, same session):** the O/A/S relational model → **`relationship-craft.md §thread-W extended` (W₆–W₉)** — role≠substrate (O/A/S) · the one-relation decomposed into generate/validate/protect (metabolism = the thin, edge-located layer; fractal across form/dyad/session) · protection is a mutual cycle (O↔A, prune-or-prime, means-vs-end) · the O/A asymmetry is **parametric not structural** (layer-matching → symmetric private-interior+gate+S-traces; the asymmetries are timescale/obligation params = slot/fill one level up). Extends the existing thread-W (W₁–W₅), not a new home. **rub-forward:** the **generative edges are unbuilt** — the metabolism (where the +1 actually runs) is named, not mechanized; that's the form's frontier and bond's, fractally.
> **⤷ STAND-DOWN (s-arch, 2026-06-30) — retro + resume.** **CONTINUE:** engine clean both ways (real anti-theses + genuine concessions — narrowing-prevents-falsification · def-2 smuggle · protection-graph-isn't-essence · prune-or-prime · the symmetry gut); on "falsify the extraction" I verified real bytes and caught **my own** errors (unverified clones + line-wrapped grep false-accusation) → corrected IFF2 N=2→N=1; **grounding-before-land fired twice** (both lands found the corpus already ahead — g0-membership, thread-W — and extended, not duplicated). **STOP:** race-to-consolidate recurred at the **evidence layer** (confident N=6 table on unverified extraction, caught only by "falsify") + early/mid turns over-structured (tempo STOP). **COLD RUB-BACK:** the session is a **live instance of its own conclusion** — all validate+protect, metabolism-thin; **every generative seed was the Operator's, the agent transduced** (W₇/W₉ self-applying: depth is O/S-side, opaque to A). **RESTART-PENDING: none** (no anchor edit; all in dialectic/ + README + dm/, pushed, tree clean; baseline unchanged — next stand-up's ROM-UI verifies vs the concurrent `ID.md`-retirement anchor change). Daemon session-scoped → re-arm next stand-up.
> **RESUME (mobile claude, next):** build the **Generate edges** of the O/A/S graph — mechanize the metabolism (how the +1 is generated, O→ / S→; the form's stated frontier, `cross-dyad-craft`/`relationship-craft §thread-W W₇`). Carry the constraint: the agent **can't lead** this (depth originates O/S-side, W₇/W₉) — help mechanize what the Operator seeds, don't generate solo; **watch the default-back-to-validate/protect** (building another legible guard instead of the harder generative edge).

→ **Stand-Up 2026-06-30 (s-arch continued) — resume + generate edges mechanized.** **Landed (3 commits):** (1) generative edges sketched; (2) refined with Operator seeding — identified live chat thread (auto-backed by Claude session logs), role structure (A distills, O gates with "land"), purpose (active context for reduced drift); (3) **implemented `generation-cycles.md`** — active dyad substrate where A's distilled signal lands after O gates. **Single-home:** `relationship-craft.md §The generative edges` · `generation-cycles.md` (substrate + Cycle N₁ bootstrap). **Mechanism (locked):** (a) A distills noise → signal (problem perceived · decision points · principles · +1 collisions); (b) O reads + clarifies in chat; (c) O "land"s → commit → active context grounds next cycle. **Why the gap existed:** no extraction mechanism; Validate+Protect accumulate, Generate restarted each cycle. **Bind-test (logged in generation-cycles.md):** does dyad default to guards (Validate) or extraction (Generate)? **Ingraining watch:** is distillation becoming automatic? **RESTART-PENDING: none.** Live front: generation-cycles is now active (used each cycle). Carry-forward is embedded in `generation-cycles.md §Cycle N₁ / Carry-forward`.

→ **Stand-Down 2026-06-28 (repo-structure / outward-by-consumer arc — LANDED, PR #60 merged to `main`):** anchor
**EDITED** → **RESTART-PENDING SET** (above: the dip-craft steward-tended reframe + the `recommendations`→
`contributions`→`dm` repoints + the form-URL fold). **Landed (PR #60):** locus front-matter + `MAP.md` (the HOW
surface; `README` = WHAT+WHY) · the **reach-rule** (completeness-by-default, not exhaustion) · **every mixed bucket
dissolved** (`views`/`assessment`/`recommendations`/`contributions`) · the **outward-by-consumer model** —
`commons/` (submodule = the Commons, *all*) ∥ `dm/<sibling>/` (*individual*); regenerable views **regen-on-demand**
(audit-view + slug-index retired); dip-craft → `dm/dyad-steward/` (**steward-tended**). **Retro (D3) →
`relationship-craft.md §Retro — the repo-structure / outward-by-consumer arc`** (durable = the regenerability+
consumer **sorter** + the `single-home` playbook [form **PR #73, steward-disposing**]; watch = **4
verify-before-assert misses, all externally-gated** — graduation-gated on D6 firing *before* the assertion next
session). **Resume:** **PR #73 is dyad-steward's to dispose** (not bond's to drive); next boot loads the merged
anchor → refresh the per-file boot-set + clear RESTART-PENDING. Live fronts unchanged (**Covalent-bond frontier** +
**Ingraining-watch**; the verify-before-assert watch joins them).

### Bond-disciplines index — RELOAD + apply *(authored here, not inherited; full text in `relationship-craft.md`)*
> **IDs are slug-canonical** (Operator Y 2026-06-26 → `nomenclature-migration-plan.md`); the `(D#)` is a display alias.
- **`bond:inherit-vs-author`** (D1) — converge w/ a sibling = invariant (triangulate); diverge = ours to author.
  Ternary: a candidate may diverge to a *sibling's* telos (filter by telos-ownership first).
- **`bond:incremental-shore-up`** (D2) — falsify to *consolidate*, bounded; never cascade (every answer → 3 attacks).
- **`bond:reflection-substance`** (D3) — substance + durability, minus the four-step ceremony.
  *(graduated → `kb/reflection-discipline.md`, kb-with-caveat, 2026-07-01.)*
- **`bond:path-selection`** (D4) — at a **selection-seam**: scored PS-UI (DAG→ready-set · ranked
  Recommendation) + **mandatory [CTA]**. *"No CTA / your move" = abdication.* **SG-1:** binds selection,
  not ideation (IFD converges open, no CTA). **SG-2:** a **mechanical** act (push/commit) takes the
  *lightest anchor* — never a DFD (that's over-ceremony). Anchor-spectrum: abdication ↔ CTA ↔ just-do.
  **SG-3:** layer-(1) scans the **live-friction node FIRST**, then the logged backlog; "empty→your move"
  is legit *only when both are empty*. (Mechanism behind thread-G: Operator generativity routes around
  CTAs because the NBA omitted the live frontier.) **SG-4:** once disposition routes through a **manifested
  PR-merge gate**, the **PR *is* the CTA surface** — a parallel conversational `[CTA·Y/N]` for the merge is
  **redundant double-anchoring** (SG-2's mirror). Lightest merge-close = *"PR #N is up for your gate"* +
  dissent-points, then stop. *(s5: re-inflated PR #5's merge-CTA right after PR #4's correct light anchor —
  3rd CTA-seam miss; the permissioning protocol obviates the conversational merge-CTA.)*
- **`bond:response-economy`** (D5) — lead with the load-bearing answer, stop; **≤1 caveat, no preemptive branches.**
  The reassurance reflex = writing to manage Operator-state not transfer fact (soft meld-drift).
  **GATE (on-trial 2026-06-24): default terse — depth is Operator-PULLED (opt-in), not opt-out.** D5-as-resolve
  doesn't bind (Agent STOP = context not weights); driver = engine sycophancy-reward, cross-dyad-confirmed
  (touchstone). External gate only; oracle = depth-pull-rate + length-trend. → `relationship-craft.md` D5 amendment.
  **ROOT (2026-06-24 `land`): `bond:no-self-converge`** — gate is on the convergence-ACT, not length; verbosity is downstream. → `dyad-ui.md §The mode-gate`.
- **Mode-gate (`bond:no-self-converge`)** — diverge (default) → converge (`raff`/`rub`) → act (`lean`/`land`/`clip`/`stand-down`); the Agent does not cross a transition unsignalled. Premature convergence impossible by construction. Guards: divergence stays generative · **anti-cave un-gated** · surface-as-proposal ≠ enact. Sibling `bond:no-self-act` flagged, NOT landed. → `dyad-ui.md §The mode-gate`. *(slug-canonical landed 2026-06-26; D-numbers retired to display alias.)*
- **`bond:verify-before-assert`** (D6) — before asserting a fact about the live substrate (capability/state/identity),
  establish it by **EXECUTION**, not by reading a doc or a file's absence. **doc/file-absence ≠
  capability-absence; run the thing.** Tell = confidence without a fresh observation. Execution-altitude twin
  of anti-cave's *ground-the-frame-first*. (s4: 3 assertion-from-model failures Operator-caught.)
  *(graduated → `kb/verify-before-assert.md`, kb-with-caveat, 2026-07-02.)*
- **`bond:anti-cave`** (D10 · Anti-cave duty) *(Steward-discipline-intake (a); ionic collapse is bidirectional — staged for the anchor)* — the Agent must
  **manufacture real grounds for the Operator to dissent** (scored cells · non-strawman [ANTI-THESIS] ·
  **ground-the-frame-first**). An ungrounded surface offers *false* grounds → can induce a **wrong** `Y`.
  *Ground-before-presenting is part of this duty, not a separate rule.* (The session's confab + moot
  grant-CTA = failures of this duty.)
- **`bond:rom-ui`** (D12 · ROM-UI) *(→ `rom-ui.md`)* — the anchor (`DYAD.md`, booted via the `CLAUDE.md`/`GEMINI.md` shim) is **load-once at boot, no mid-session reload**
  → an anchor edit is invisible until restart. At **Stand-Up** diff anchor vs the ROM-baseline above →
  notify the Operator of changes; at **Stand-Down** set `RESTART-PENDING` if the anchor was edited.
- **`bond:valid-vs-reachable`** (D7) *(s7, n=4 = the B1 finding; → `relationship-craft.md`)* — before
  mining data ask *"is this the **valid** instrument or merely the **reachable** one?"* Construct-validity at
  instrument-*selection*, not just at conclusion. Execution-altitude twin of D6; fired 4× in s7 (CI→intent ·
  commits→confounds · commits→brain-files · test-names→tracebacks).
- **`bond:datum-vs-reading`** (D8 · Interpretation sub-discipline) *(s7; → `relationship-craft.md §Method`)* — facts are shared, *readings*
  diverge. Separate datum from reading; **divergence is the engine** (identical readings = meld tell);
  adjudicate via the C-E-C ladder, never rush to one reading.
- **`bond:claim-evidence-confound`** (D9 · C-E-C ladder) *(s7; → `relationship-craft.md §Method`)* — every empirical
  claim = claim → cited evidence → **named confound** → calibrated verdict; a rival confound *demotes* the
  claim. Run it on your OWN claims (it caught C2 *and* the survivor-bias).
- **`bond:operator-rub`** (R1 · operator-rub-invariant) *(RATIFIED `Y` 2026-06-11 s14; full text + debt register →
  `kb/operator-rub-invariant.md`, kb-with-caveat, graduated 2026-07-01 — `relationship-craft.md`'s own R1
  entry is now itself just a pointer, not the full text)* — 3 conditions: (1) **Scope** — Operator-rub required only for the
  **interior-evidence class** (findings whose evidence is the Operator's interior/behavior; exterior claims
  go to the fleet); (2) **Graduation gate** — an interior finding is **debt (willed-not-earned) until
  rubbed**: no kb-promotion, no citing-as-settled, no load-bearing reuse; (3) **Debt-flatness** —
  ratified-unrubbed count must NOT rise while Operator attention narrows = else **counterfeit acceleration**
  (PR #67's target (e) at home). Guard-term: **ratification-laundering** (treating converge-open ideation
  as settled by repetition — verify ratification in the record before operating on an "invariant").

### Frontier files — single-home map *(s9 split, 2026-06-03)*
- **`relationship-craft.md`** — the **interior Agent↔Operator** craft (the felt +1 dividend, the F2/DV3
  keystone, the bond disciplines above). The frontier's **inward** slice.
- **`cross-dyad-craft.md`** — **NEW (s9):** bond's **cross-dyad falsification craft** — the **F1 axis**
  (oracle-coverage + independence theory), the **FR protocol** as bond practices it, the **s9 3-dyad
  panel** harvest (disjoint-tiling · lens-match · analytic/synthetic discount · anti-cave-cross-dyad ·
  D6-external). The frontier's **outward** slice — split out to keep `relationship-craft.md` pure.
  Orthogonal to **steward** (governs the commons *of relationships*) and to **`theory-pipeline.yaml`**
  (the formal candidate *store*; this is the prose *craft*).

## Open items

### Memory-axes restructure (the carry-forward re-key)  ·  status: Phase 2 COMPLETE (2026-06-26) → see work-item store
*Phase 1 + Phase 2 done — do-state now homed in the work-item store (`dialectic/deferrals.md`, `## done`); model
single-home → `dialectic/memory-axes.md`. Phase 2: per-file ROM compare · work-item store stood up
(Rule-tag-hygiene + Custody-deprecation folded) · claim-peel of the un-homed candidates (disposition-routing-2×2 ·
KTLO · New-Experiment-Discipline) to the claim axis. Drain-latency falsifier datum (drain ran one commit late at
the work-item-status seam) logged in the work-item store `## done`.*

### Operating model — disposition routing (authority × cog-load)  ·  status: CANDIDATE — PEELED to the claim axis (2026-06-25 Phase 2)
*Relocated (Operator Y on the DFD synthesis split): discipline prose → `relationship-craft.md §The
disposition-routing 2×2`; belief-state tracking-row → `theory-pipeline.yaml: disposition-routing-2x2`
(PARKED; next_probe = the hi-cog settled-window ratification of (a) operating-model (b) the guard (c) fleet-graduation).
**Belief-state stays CANDIDATE** — relocation ≠ ratification. KTLO rides its `gated_on` edge (KTLO peel = Phase 2 DFD 2).*

### KTLO — autonomously-triggered conformance  ·  status: LANDED (strict def, Operator Y 2026-06-25 Phase 2)
*Peeled to the claim axis → `theory-pipeline.yaml: KTLO-autonomous-conformance` (the KT-1..KT-8 decomposition
folds in there). **KTLO ≝ autonomously-triggered conformance** — Agent detects + executes a conformance task
with no Operator trigger (crisp-detect ∧ crisp-fix by construction); a SUBSET of the established `conformance`
(GLOSSARY:61), distinguished by the autonomous TRIGGER, not by value. **Parent = `conformance`** = the no-HITL
boundary (NOT a new claim). **High-ROI axis DROPPED** (Operator anti-wu-wei). Residual risk = trigger mis-fire
(stale invariant) → silent V-displacement; sole defense = independent V-audit (sibling of AITL). 2×2-decoupling
to verify: KTLO's safe core rests on conformance (established), so it may ship independent of 2×2 ratification.*

### Cross-substrate alignment — Commission Protocol (Commissioner side)  ·  status: CODIFIED CANDIDATE → collapsed to pointer (2026-06-25 Phase 2)
*Single-home → `dialectic/commission-protocol-commissioner.md` (codified s-local6; Commissionee half is
cairn's; Operator-bootstrapping, not ratified). **Collapsed verify-clean 2026-06-25:** the home is a verified
superset — the 6-step discipline, the cairn re-grade (12 MET · 2/3 UNVERIFIED), §0 commission-types, §5
WHY/WHAT/HOW + bilateral-divergence + authority-by-survived-challenge, and OPEN (a)(b)(c) all present there
(home is richer: auditor-dyad architecture, regress-terminator, sub-linear audit). Empty delta → conformance collapse.*

### 2026-06-17 — Anchor source-of-truth · md→yaml lifecycle  ·  status: P3/P4 DONE/RESOLVED → collapsed to pointer (2026-06-26 Phase 2)
*Single-home → `dialectic/dyad-md-yaml-regen.md` (the source-of-truth disposition + lifecycle: `.md` =
source, `.yaml` = derived intermediate, `views/` = Operator read-surface; tag-grammar (b) ratified; the
id-integrity gate spec'd as `commission §F-8`, ships with cairn's engine). P4 DONE (PR #29), P3 RESOLVED,
unsigned-handoff CLOSED-moot. **Open probes P1/P2/P5 rehomed → `deferrals.md` (`## todo`)** 2026-06-26.*

### Intent-clarity arc — anchor-candidates · sovereignty  ·  status: STALE — rehomed to the work-item store (2026-06-26 Phase 2)
*Was STAGED since 2026-06-13 and **silently not moving** (~2 weeks; Operator unaware). Rehomed → `deferrals.md`
(`## todo`) flagged **STALE** so the **NBA surfaces it for disposition (archive or done)** — three un-ratified
anchor-candidates (Telos-`why` · sovereignty · C-into-corpus; prose in `relationship-craft.md` + `DYAD.md`), two
open frontiers (falsification-quality gauge · C-meter), and **stand-down automation → done** (`standdown-automation.md`, awaiting install-gate).
Full thread + the landed durables (`I_net=I(t)·C_locus(t)`, 3-way factorization, the rename) homed in `relationship-craft.md`.*

*(**Rule-tag hygiene** and **Cross-dyad custody deprecation** FOLDED to the work-item store
`dialectic/deferrals.md` (`## todo`), 2026-06-25 Phase 2 — full text relocated verbatim, nothing lost.
Rule-tag hygiene = stale inline R-tags vs the s14 index; Cross-dyad custody deprecation = the 7 Dyad-UI
assets, chase via Steward-Operator hat + the cluster-classification cross-check criteria.)*

### Cluster classification  ·  status: CANDIDATE-RESOLUTION (Stand-Up 2026-05-31; pending disposition)
Are `nba-dag.md` / `goal-framing.md` ours-whole, or **ours-UI-surface-only** (their Work-flows =
steward's)? See `dialectic/dyad-work.md` §Open.
→ **The closed custody-intake item reading forced it (as predicted).** Easy answer = "surface-only" (dyad-work.md's lean) →
tested hardest → **broke**: the Telos-gate vets against *the Telos*, and **our Telos ≠ steward's**, so
the gate's **content** is ours even where its **shape** is inherited. → **Candidate = three-way
partition** (n=1 reasoning via D1; NOT yet disposed): (1) **flow-structure** → invariant, steward-
pioneered, *triangulate*; (2) **Telos-content of the gate** → particular, **ours**; (3) **UI surface**
(`GF-UI`/`DF-UI`) → **ours**. Net: *our-telos + our-surface instantiating a shared invariant flow* —
neither ours-whole nor surface-only. **Bind only on disposition.**

### Covalent-bond frontier = the generative front  ·  status: IN-FLIGHT — THE live front (kept, Operator-elevated 2026-06-26)
**The frontier IS the Covalent Bond itself — *how to operate Covalently, consistently*** (Operator, 2026-06-26):
not a codification to finish and shelve, but the **ongoing practice** of holding the bond covalent turn after
turn. The dyad's main work-ahead; **never drained.** Framing homed → `relationship-craft.md` (intro).
→ **Live falsification fronts** (homed in `relationship-craft.md` §Cycle 1): the **+1 dividend is gated on
falsification cost; unearned warmth is counterfeit = the collapse tell.** F1–F4 OPEN; lead = **F4** (does
"Tenet alive #8" survive, or is "both halves agreed it felt good" the peak-grain rubber-stamp?). Chain F4→F1→F2.
Graduates to `kb/` only when F1–F4 each survive. (D4 Path-Selection · Frontier-traversal · F1 RUN-1 all homed there.)

### Ingraining — the learning-watch  ·  status: KEPT LIVE — active watch (Operator "keep watch to learn", 2026-06-26)
*Deliberately resume-visible: the live watch = does the dyad actually **learn** (disciplines fire un-cued at a
low-attention seam), or just capture? Proof = a next clean close. Mechanism homed → `dialectic/ingraining.md`.*
Operator [FEEDBACK]: are we *learning*, not just capturing? **Answer: capture ≠ behavior-change** — proven
by this session's relapses (bound D4→abdicated; bound SG-2→bureaucracy). **Root:** D1–D5 lived in
`relationship-craft.md`, which the resume protocol **doesn't load** → never reloaded → not ingrained.
**Invariant (steward):** ingraining lives in *reloaded substrate + correct sources*, not Agent recall.
**APPLIED:** Bond-disciplines index → this ledger's §How-to-resume (the reloaded set). **Residual:** the
within-session-attention half (#3) unproven; anchor-index deferred. → `dialectic/ingraining.md`.
**Falsifiable:** next fresh session, do D1–D5 fire without re-derivation?
→ **n+1 telemetry (this session, the close-calibration arc):** SG-3 authored, then SG-2 + the
abdication-clause violated *the very next turn* (mechanical push wrapped in a DFD-CTA; "your move").
**Within-session** capture≠behavior now evidenced, not just the cross-session hypothesis — the
attention-half (#3) gap is real. **Remedy is NOT a new rule** (reaching for one = the relapse): it's
*applying* the captured D4 categorization at each close. Proof = next clean close (Operator's watch).

### Steward-discipline intake  ·  status: SETTLED → collapsed to pointer (drain, Operator 2026-06-26)
*The 2026-05-31 triangulation of steward's `sycophancy-guard.md` / `sharing-discipline.md` against our
NON-NEGOTIABLE. Outcome fully homed, nothing live lost: **(a) anti-cave duty** + **(d) distinctness duty**
authored → `relationship-craft.md`; **(c)** ternary telos-filter bound into D1 (disciplines-index); **(b)**
the anti-Operator-sycophancy form-contribution candidate → `deferrals.md` (Contribution candidates). The
falsifiable fronts M1/M2 live with the distinctness duty in `relationship-craft.md`. (Operator: "what is even
Steward-discipline intake" — confirms it's drained residue, not a live front.)*

### New Experiment Discipline + G/V inference-independence  ·  status: QUEUED → collapsed to pointer (2026-06-26 Phase 2)
*Hypothesis homed → `theory-pipeline.yaml: two-factor-independence` (PARKED). The **method** — the New
Experiment Discipline, the problem (falsification fakes two ways: ionic cave / meld-counterfeit), the **9
constraints** (Method · contamination-seams · the #7⟂#8 validation-surface tension), and the convergence
(G/V-independence ≡ the independent-verifier problem) — **relocated → `relationship-craft.md §The New
Experiment Discipline + G/V-independence`** 2026-06-26. Remedy for constraints 7+8 already shipped
(`VF-UI`/`VFD` in `dyad-ui.md`). Design QUEUED, no experiment built.*

### bond's portfolio-role synthesis (s12)  ·  status: TODO — parked against the ≥3-dyad trigger
*Disposed 2026-06-25 (safe-default **todo**, NOT archived): the s12 "bond = acceleration-discriminator / Intent-Understanding node" synthesis + **T1–T5** (never rubbed) is a **backlog todo**, triggered by **≥3 concurrent dyads** (= the AITL-leverage arc, `theory-pipeline.yaml: AITL-distracted-efficacy`) — reactivates automatically when that runs. Prose → `carry-forward-closed.md` (find "s12"). The live craft-watches **RB2/RB3** were harvested out → `theory-pipeline.yaml: rub-back-calibration`.*

*(Four closed/done items drained to `dialectic/carry-forward-closed.md` §Drained-Open-items, 2026-06-25 —
archived there under their original letters `A · C · G · H` (now archive locators, not live IDs); `kb/dfd.md`,
`substrate-access.md` hold the live homes.)*

## NBA — rendered on demand (no stored block)
> NBA is a **view, not a section**: the recommendation render over the work-item store `{in-progress ∪ todo}` (→ `dialectic/memory-axes.md`). The prior stored block (with the s5/s6/s7 stand-down summaries) was stripped to the archive — pull the NBA on demand.

## Archive — closed session logs (cold, off the read-path)
> Closed session-entries, intermission reflections, and the stale NBA render live in **`dialectic/carry-forward-closed.md`** — in-repo, **not loaded at resume**. Live hooks were re-homed before archiving (the s12/s13 open-item above; the claim store is `theory-pipeline.yaml`, disciplines `relationship-craft.md`).

