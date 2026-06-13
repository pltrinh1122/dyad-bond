#!/usr/bin/env bash
# bin/standup.sh — dyad-bond stand-up / resume automation (K6, mechanical spine)
#
# WHY (ours — Item-K6, 2026-06-13): the resume routine (carry-forward.md §How to resume) opens with
#   DETERMINISTIC checks a fresh Covalent otherwise hand-runs every session — the ROM-UI diff (anchor
#   hash vs the recorded baseline), the memory-durability check (uncommitted/unpushed = ungrounded
#   memory), and the substrate probe (is the IM daemon even armable here?). Mechanizing them removes a
#   per-session trigger AND removes hand-error. Wired as a Claude Code **SessionStart** hook, `--hook`
#   mode emits the result as `additionalContext` so it loads at boot WITHOUT a `read: carry-forward`.
#
# WHAT IT IS NOT: it does not JUDGE. It SURFACES — the mismatch, the dirty tree, the dark inbox — and
#   hands the disposition to the agent (refresh the baseline? set RESTART-PENDING?). auto-trigger ≠
#   auto-judgment (K6 constraint b). The agent still reads the ledger; this primes the seams.
#
# COVALENT GATE (K6 constraint a / S2): installing it as a hook is the Operator's act
#   (`bin/install_hooks.py`) — never an Agent self-grant. The script is inert until wired.
#
# Usage:  bin/standup.sh           # human-readable resume report (stdout)
#         bin/standup.sh --hook    # emit SessionStart additionalContext JSON (hook body)

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LEDGER="dialectic/carry-forward.md"
ANCHOR_FILES=(DYAD.md CLAUDE.md GEMINI.md)

lines=()
add() { lines+=("$1"); }

# ── ROM-UI check (stateless: live anchor commit vs the baseline recorded in the ledger) ──────
recorded="$(grep -m1 'ROM-baseline (anchor commit' "$LEDGER" 2>/dev/null \
            | grep -oE '`[0-9a-f]{7,40}`' | head -1 | tr -d '`' || true)"
if [[ -z "$recorded" ]]; then
  add "ROM-UI: ⚠ could not parse ROM-baseline from $LEDGER — check the ledger by hand."
else
  mism=()
  for f in "${ANCHOR_FILES[@]}"; do
    cur="$(git log -1 --format=%H -- "$f" 2>/dev/null || true)"
    [[ -n "$cur" && "$cur" == "$recorded"* ]] || mism+=("$f@${cur:0:7}")
  done
  if ((${#mism[@]})); then
    add "ROM-UI: ⚠ MISMATCH vs baseline \`$recorded\` — moved: ${mism[*]}."
    add "        → verify the shim boot-chain fired (you read DYAD.md because the shim said to),"
    add "          then notify the Operator + refresh the ROM-baseline line in $LEDGER."
  else
    add "ROM-UI: ✓ MATCH (anchor + shims at baseline \`$recorded\`)."
  fi
fi

# ── Memory-durability (uncommitted/unpushed = ungrounded memory; the standing substrate threat) ─
dirty="$(git status --porcelain 2>/dev/null || true)"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
unpushed="$(git log --oneline '@{u}..' 2>/dev/null | wc -l | tr -d ' ' || echo 0)"
if [[ -n "$dirty" ]]; then
  add "Durability: ⚠ working tree DIRTY on \`$branch\` ($(printf '%s\n' "$dirty" | wc -l | tr -d ' ') paths) — commit before relying on the ledger as memory."
elif [[ "$unpushed" != "0" ]]; then
  add "Durability: ⚠ $unpushed unpushed commit(s) on \`$branch\` — push (bin/git.sh) so the remote backs up the memory."
else
  add "Durability: ✓ clean + in sync on \`$branch\`."
fi

# ── Substrate probe (is this the durable home, or an ephemeral clone? is the IM daemon armable?) ─
home_ok=0; gh_ok=0; falsify_ok=0
[[ -d /mnt/shared_data/dzw ]] && home_ok=1
command -v gh >/dev/null 2>&1 && gh_ok=1
{ [[ -e commons/scripts/falsify.py ]] || find commons -name falsify.py 2>/dev/null | grep -q .; } && falsify_ok=1
if ((home_ok && gh_ok && falsify_ok)); then
  add "Substrate: ✓ durable home + gh + falsify.py present → IM daemon armable (step 6, im-daemon.md verbatim)."
else
  miss=()
  ((home_ok))   || miss+=("no /mnt/shared_data/dzw mount")
  ((gh_ok))     || miss+=("no gh")
  ((falsify_ok))|| miss+=("no commons/falsify.py")
  missjoin="$(printf '%s, ' "${miss[@]}")"; missjoin="${missjoin%, }"
  add "Substrate: ⚠ ephemeral/partial ($missjoin) → IM daemon NOT armable here; DM-watch is dark this session."
fi

# ── Output ───────────────────────────────────────────────────────────────────────────────────
header="dyad-bond stand-up (bin/standup.sh) — mechanical resume checks. Operate as Covalent; read $LEDGER; then take the NBA / Item-K queue."
body="$(printf '%s\n' "$header" '' "${lines[@]}")"

if [[ "${1:-}" == "--hook" ]]; then
  CTX="$body" python3 - <<'PY'
import json, os
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": os.environ["CTX"],
}}))
PY
else
  printf '%s\n' "$body"
fi
