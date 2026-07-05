#!/usr/bin/env bash
# bin/quarry.sh — dyad-bond substrate-access wrapper for COMMISSION QUARRIES (v0.1)
#
# WHY (ours — sibling of bin/git.sh / bin/gh.sh; see dialectic/substrate-access.md):
#   Under the Commissioning Protocol (dyad-cairn, kb/HOW-commission.md) a commission is a standalone
#   "quarry" repo, external to bond's own anchor, that bond collaborates on as Commissioner. bin/git.sh
#   only reaches bond's OWN tree/origin; bin/gh.sh already covers Issue/PR publish for any repo. The gap
#   is git access to a quarry checkout. This wrapper closes it with the SAME posture: declared-policy,
#   permission-gated, fail-closed. Set up 2026-07-05 on Operator instruction ("set up mechanisms to
#   allow Agent to collaborate seamlessly on the repo").
#
# COVALENT GATE (same as bin/git.sh): the access BOUNDARY — which quarries, which ops — rests on
#   Operator-ratified edits to the POLICY block below (chat-as-gate) + the Operator-performed permission
#   grant (Bash(bin/quarry.sh:*)). The Agent gets the choke-point; widening it stays the Operator's act.
#   Genesis (the protocol's one direct-to-main exception) is Operator-authorized; every later mutation
#   follows the protocol's Issue -> branch -> PR -> merge, so main is touched by push only at genesis and
#   thereafter by PR-merge, never by a force/delete (refused below at the git layer).
#
# IDENTITY NOTE: pushes publish under the shared github account (pltrinh1122), NOT the dyad identity —
#   callers self-identify in commit/Issue/PR bodies ("— dyad-bond, Commissioner").
#
# Usage:  bin/quarry.sh <quarry> <op> [args...]
#         QUARRY_SH_DRY_RUN=1 bin/quarry.sh commission-dyad-system push   # resolve + print, do not run
#
# ── DECLARED ACCESS POLICY (Operator-governed; edit THIS block to widen/narrow) ───────────
QUARRY_ROOT="/mnt/shared_data/dzw"                     # where quarry checkouts live
ALLOWED_QUARRIES=(                                     # exact checkout dir names bond may touch
  "commission-dyad-system"
  "commission-invariant-engine"
)
ALLOWED_OPS=(status fetch pull switch checkout branch add commit push)  # all else refused
PROTECTED_BRANCHES=(main)                              # branches on which rewriting flags are refused
FORCE_FLAGS=(--force -f --force-with-lease --delete -d)
# ──────────────────────────────────────────────────────────────────────────────────────────

set -euo pipefail

die() { printf 'quarry.sh: REFUSED — %s\n' "$1" >&2; exit 1; }
contains() { local n="$1"; shift; local x; for x in "$@"; do [[ "$x" == "$n" ]] && return 0; done; return 1; }

[[ $# -ge 2 ]] || die "usage: quarry.sh <quarry> <op> [args] (got: $*)"
quarry="$1"; op="$2"; shift 2

contains "$quarry" "${ALLOWED_QUARRIES[@]}" || die "quarry '$quarry' not in ALLOWED_QUARRIES (policy block)"
contains "$op" "${ALLOWED_OPS[@]}"          || die "op '$op' not in ALLOWED_OPS (fail-closed)"

dir="$QUARRY_ROOT/$quarry"
[[ -d "$dir/.git" ]] || die "no git checkout at $dir (clone it first, out of band)"
cd "$dir"
origin="$(git remote get-url origin 2>/dev/null || true)"
[[ "$origin" == *"$quarry"* ]] || die "origin '$origin' does not match quarry '$quarry' (wrong tree)"

# Force/delete on a protected branch is refused at the git layer, any op that carries the flag.
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
if contains "$branch" "${PROTECTED_BRANCHES[@]}" || contains "push" "$op"; then
  for a in "$@"; do
    contains "$a" "${FORCE_FLAGS[@]}" && die "history-rewriting flag '$a' refused (protected-branch guard)"
  done
fi

printf 'quarry.sh: [%s] → git %s %s\n' "$quarry" "$op" "$*" >&2
if [[ "${QUARRY_SH_DRY_RUN:-0}" == "1" ]]; then
  printf 'quarry.sh: (dry-run; not executed)\n' >&2
  exit 0
fi

case "$op" in
  push) git push origin "$branch" "$@" ;;   # push CURRENT branch to origin (genesis: main; else feature)
  *)    git "$op" "$@" ;;
esac
