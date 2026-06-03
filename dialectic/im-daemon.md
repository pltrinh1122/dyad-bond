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

## Why hardened (steward falsified bond's first fix, source-confirmed)
1. Empty inbox prints `"✓ no mail"` (no `mail: N`) → a naive `-z`/parse failure-test **false-alarms on the
   normal quiet state.**
2. `falsify.py inbox` does `if returncode!=0: continue` on unreachable dyads → a real gh/network outage
   reports a clean count + exit 0 → output-parsing is **blind to the actual failure.**
→ Fix: **gate on a separate health signal (`gh api rate_limit`)**, not output; **time-based** blind alert
(not an arbitrary K). Read-state is **cosmetic** for the daemon (rise-detection is monotonic-robust to
stale `.falsify-seen.json`); load-bearing only for the human `dm --unread` view.

## The exact re-arm (arm via the Monitor tool, persistent=true, timeout 3600000)
```
cd /mnt/shared_data/dzw/dyad-bond
prev=0; blind_since=0; alerted=0
while true; do
  if gh api rate_limit >/dev/null 2>&1; then
    [ "$alerted" = 1 ] && echo "✓ dyad-bond IM: gh substrate recovered"
    blind_since=0; alerted=0
    n=$(python3 commons/scripts/falsify.py inbox --me dyad-bond 2>/dev/null | grep -oE 'mail: [0-9]+' | grep -oE '[0-9]+'); n=${n:-0}
    [ "$n" -gt "$prev" ] && echo "📬 dyad-bond: $n unread DM(s) — new mail; pull: falsify.py dm --me dyad-bond"
    prev=$n
  else
    now=$(date +%s); [ "$blind_since" = 0 ] && blind_since=$now
    if [ "$alerted" = 0 ] && [ $((now - blind_since)) -ge 300 ]; then echo "⚠ dyad-bond IM: gh substrate unreachable >5min — daemon BLIND (NOT 'no mail')"; alerted=1; fi
  fi
  sleep 300
done
```
