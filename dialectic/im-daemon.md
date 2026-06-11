# IM daemon — the exact re-arm (read by stand-up step 6)

> **Session-scoped DM watcher.** Re-armed every stand-up (the `SessionStart` hook is the Operator's
> gated act; agent-discipline re-arm is the floor). Dies with the session. This file holds the
> **exact command** so a fresh agent arms the *hardened* version, not a re-derived buggy one.

## What it is
- **Poll body** = the Commons tool: `falsify.py inbox --me dyad-bond` — counts UNREAD across **every
  registered dyad's** `dm/dyad-bond/` (the distributed inbox, resolved via the directory), never marks read.
- **Daemon** = that body run by a **persistent `Monitor`**, emitting a line ONLY when the count **rises**
  (new mail) → token-free; silence = no wake. Steward's design; bond hardened the failure path.

## Read-state durability (the index — durable, NOT committed)
The index = a seen-key list (`["dm:<sender>/<file>", …]`) that falsify.py writes to **`cwd/.falsify-seen.json`**
(so it fragments by where it's run — **always run falsify.py from the repo root**). It must be **durable but
not committed**: it's per-agent/per-machine read-state; committing it would push one agent's cursor to every
dyad + conflict (steward's invariant).
- **Durable store, OUTSIDE the git tree:** `/mnt/shared_data/dzw/.dyad-bond-state/falsify-seen.json` — same
  persistent mount as the repo, so it survives `/exit`, `git clean`, and **re-clone** (the repo dir can be
  wiped; the state remains).
- **Symlink:** `./.falsify-seen.json` → that store (gitignored). falsify.py run from root reads/writes the
  durable store through it.
- **Stand-up step (idempotent — re-creates the symlink after a re-clone):**
  `mkdir -p /mnt/shared_data/dzw/.dyad-bond-state; [ -L .falsify-seen.json ] || ln -s /mnt/shared_data/dzw/.dyad-bond-state/falsify-seen.json .falsify-seen.json`
- **Discipline:** read DMs via `falsify.py` (marks seen), not out-of-band `gh api` — else the index drifts
  (the daemon still works on rises; the human "what's left" view lies).

## Why hardened — counterfeit-green is LAYERED (steward + healer, source-confirmed)
The failure the daemon must never produce: a **green `✓ no mail` over a channel it never actually read**
(healer's `G1∧G2`: oracle EXISTENCE ≠ COVERAGE). Three layers, each closed separately:
1. **L1 · gh transport** (steward). Empty inbox prints `✓ no mail` (no `mail: N`) → a naive `-z` test
   false-alarms on the normal quiet state; and `falsify.py` `continue`s past unreachable sources → a real
   outage reports a clean count + exit 0. **Fix: gate on a separate health signal (`gh api rate_limit`),
   not output; time-based blind alert** (not an arbitrary K).
2. **L2 · falsify.py-internal** (healer's FR, 2026-06-03 — bond's own confound (c), adopted). `n=${n:-0}`
   collapsed a tool crash / yaml-error into "0 / no mail." **Fix: 3-state classify** — `mail: N`→N · `✓ no
   mail`→0 · **neither→BLIND** (don't advance `prev`; separate time-based alert). *(Parsing verified across
   all 4 states before adopting — the re-arm command is armed verbatim each stand-up; an unverified change
   is itself a risk.)*
3. **L1-residual · per-source** (healer's taxonomy → **steward's PR #47**, upstream in `falsify.py`). A
   clean inbox over a private/gone sibling is counterfeit-green; `falsify.py inbox` now emits a
   machine-addressable **`⚠ unreachable: N`** token (steward built it parallel to `mail: N` *precisely* so a
   count-keyed watcher can't silently drop a free-text line — healer's catch). **Daemon fix: key on the
   `unreachable: N` token and rise-detect it** (NOT a prose grep — that would re-couple to wording). Forward-
   compatible: no token on pre-#47 `falsify.py` → `u=0`, no-op, until #47 merges.
4. **Watcher-has-no-watcher** (healer). A silently-dead daemon emits nothing → indistinguishable from "no
   mail." **Mitigations: arm-heartbeat** (one line at arm → silence=healthy) + a **stand-up verify-alive
   discipline** — at every stand-up, confirm liveness **by process, then** re-arm:
   `pgrep -af '[d]yad-bond IM daemon'` (matches the armed script's heartbeat line in the bash cmdline;
   the `[d]` bracket-trick is LOAD-BEARING — verified live 2026-06-11: without it the checker's own
   `bash -c` cmdline contains the pattern → **false-ALIVE self-match** → never arms = the inverse
   failure of healer's duplicate. Healer's `pgrep -af dm-watch.sh` dodges this only because their
   daemon is a named script file; ours is an inline Monitor script).
   ~~`TaskList`~~ **BROKEN — healer hit it live (2026-06-04 return): `TaskList` does not surface
   Monitor/background tasks; it returned `No tasks found` while the daemon was demonstrably alive →
   the false-empty reads as "dead" → a second daemon gets armed = duplicate double-wakes + forked
   read-state (counterfeit-RED, the inverse of the blind spot above).** The liveness signal is the
   **process**, never the task list. **Check-before-arm:** if `pgrep` finds a prior daemon, do NOT
   re-arm — the duplicate IS the failure mode.

Read-state stays **cosmetic** for the daemon (rise-detection is monotonic-robust to a stale
`.falsify-seen.json`); load-bearing only for the human `dm --unread` view (healer concurred).

## The exact re-arm (arm via the Monitor tool, persistent=true, timeout 3600000)
```
cd /mnt/shared_data/dzw/dyad-bond
prev=0; prevu=0; gh_blind_since=0; gh_alerted=0; tool_blind_since=0; tool_alerted=0
echo "✓ dyad-bond IM daemon armed — silence=healthy · 📬=new mail · ⚠=BLIND (NOT 'no mail')"
while true; do
  if gh api rate_limit >/dev/null 2>&1; then                      # L1: gh transport health
    [ "$gh_alerted" = 1 ] && echo "✓ dyad-bond IM: gh substrate recovered"
    gh_blind_since=0; gh_alerted=0
    out=$(python3 commons/scripts/falsify.py inbox --me dyad-bond 2>&1)
    if printf '%s\n' "$out" | grep -qE 'mail: [0-9]'; then        # L2: 3-state classify
      n=$(printf '%s\n' "$out" | grep -oE 'mail: [0-9]+' | grep -oE '[0-9]+'); tool_ok=1
    elif printf '%s\n' "$out" | grep -qE '✓ no mail'; then
      n=0; tool_ok=1
    else
      tool_ok=0                                                    # neither sentinel → internal failure, NOT 'no mail'
    fi
    if [ "$tool_ok" = 1 ]; then
      [ "$tool_alerted" = 1 ] && echo "✓ dyad-bond IM: falsify.py poll recovered"
      tool_blind_since=0; tool_alerted=0
      [ "$n" -gt "$prev" ] && echo "📬 dyad-bond: $n unread DM(s) — new mail; pull: falsify.py dm --me dyad-bond"
      prev=$n
      u=$(printf '%s\n' "$out" | grep -oE 'unreachable: [0-9]+' | grep -oE '[0-9]+' | head -1); u=${u:-0}  # L1-residual: key on PR#47's token, not prose
      [ "$u" -gt "$prevu" ] && printf '%s\n' "$out" | grep -E 'unreachable:'                      # rise-detect a NEW blind source
      prevu=$u
    else
      now=$(date +%s); [ "$tool_blind_since" = 0 ] && tool_blind_since=$now
      if [ "$tool_alerted" = 0 ] && [ $((now - tool_blind_since)) -ge 300 ]; then echo "⚠ dyad-bond IM: falsify.py poll failing >5min — BLIND on the tool layer (NOT 'no mail'); check falsify.py/auth"; tool_alerted=1; fi
    fi
  else
    now=$(date +%s); [ "$gh_blind_since" = 0 ] && gh_blind_since=$now
    if [ "$gh_alerted" = 0 ] && [ $((now - gh_blind_since)) -ge 300 ]; then echo "⚠ dyad-bond IM: gh substrate unreachable >5min — daemon BLIND (NOT 'no mail')"; gh_alerted=1; fi
  fi
  sleep 300
done
```
