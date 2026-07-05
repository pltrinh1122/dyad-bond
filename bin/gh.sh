#!/usr/bin/env bash
# bin/gh.sh — dyad-bond substrate-access wrapper for gh OUTWARD-PUBLISH (v0.1)
#
# WHY (ours — sibling of bin/git.sh; see dialectic/substrate-access.md):
#   Outward messaging is now recurring friction: DMs, PR reviews/comments, FR responses. The Operator
#   has granted a STANDING DISPOSITION over messaging/reviews (the Agent decides + sends, no re-ask),
#   but the auto-mode classifier blocks raw `gh pr review`/`gh pr comment` (publish under the
#   pltrinh1122 account). Same shape as push-to-main: the disposition is the Agent's; the *mechanical*
#   path needs an Operator-granted, declared-policy choke-point — never an Agent self-grant.
#
# STRUCTURE (inherited from bin/git.sh): declared-policy single-file wrapper, permission-gated,
#   fail-closed. The harness grants the NARROW permission Bash(bin/gh.sh:*) — never broad gh.
#
# COVALENT GATE: the outward-publish BOUNDARY (which ops, under our identity) rests on Operator-ratified
#   edits to the POLICY block below (chat-as-gate) + the Operator-performed permission grant — NOT an
#   Agent self-grant. The Agent gets the choke-point; widening it stays the Operator's act.
#
# IDENTITY NOTE: gh publishes under the github account (pltrinh1122), which is shared across sibling
#   dyads and is NOT the dyad identity. Callers MUST self-identify in the body ("— dyad-bond (Covalent)")
#   — the dyad-id is a soft text claim over the hard account; the account can't carry it.
#
# Usage:  bin/gh.sh <op...> [args...]
#         GH_SH_DRY_RUN=1 bin/gh.sh pr review 44 ...    # print the resolved command, do not execute
#
# ── DECLARED ACCESS POLICY (Operator-governed; edit THIS block to widen/narrow) ───────────
ALLOWED_OPS=(                                   # first TWO tokens of an allowed gh invocation
  "pr review"
  "pr comment"
  "pr create"
  "issue comment"
  "issue create"
)
# ──────────────────────────────────────────────────────────────────────────────────────────

set -euo pipefail

die() { printf 'gh.sh: REFUSED — %s\n' "$1" >&2; exit 1; }

[[ $# -ge 2 ]] || die "need at least <noun> <verb> (e.g. 'pr review'). got: $*"

op="$1 $2"
allowed=0
for a in "${ALLOWED_OPS[@]}"; do [[ "$op" == "$a" ]] && allowed=1 && break; done
[[ "$allowed" == 1 ]] || die "op '$op' not in ALLOWED_OPS (Operator-governed policy block)"

printf 'gh.sh: → gh %s\n' "$*" >&2
if [[ "${GH_SH_DRY_RUN:-0}" == "1" ]]; then
  printf 'gh.sh: (dry-run; not executed)\n' >&2
  exit 0
fi
command gh "$@"
