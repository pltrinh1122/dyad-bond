#!/usr/bin/env bash
# bin/gh.sh — dyad-bond substrate-access wrapper for gh: outward-PUBLISH + zero-publish READS (v0.2)
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
#   (Applies to the PUBLISH class only — reads publish nothing, so no self-identify is owed.)
#
# Usage:  bin/gh.sh <op...> [args...]
#         GH_SH_DRY_RUN=1 bin/gh.sh pr review 44 ...    # print the resolved command, do not execute
#
# ── DECLARED ACCESS POLICY (Operator-governed; edit THIS block to widen/narrow) ───────────
# Two classes, kept SEPARATE on purpose — the mutation/read line is what keeps the wrapper
# legible (substrate-access.md §Discipline-based permissioning). Widening either stays the
# Operator's act (ratified edit = chat-as-gate); never an Agent self-grant.
#
# PUBLISH — writes under the shared pltrinh1122 account; identity-bearing (see IDENTITY NOTE);
#   the covalent-gated set.
ALLOWED_PUBLISH_OPS=(                           # first TWO tokens of an allowed gh invocation
  "pr review"
  "pr comment"
  "pr create"
  "issue comment"
  "issue create"
  "issue close"
)
# READ — zero-publish introspection; the gh counterpart to git content-reads (log/diff/show),
#   which the classifier already auto-approves. gh reads are NOT auto-approved (they prompt),
#   so they route through this same choke-point to stay frictionless. Folded in on first bite
#   (2026-07-06, falsifying dyad-leo gate #12): a raw `gh issue view` prompted mid-falsification.
#   (`gh api` deferred — read/write-ambiguous: bare GET is a read but `-X POST` publishes; it
#   needs its own method-guard, so it waits until it actually bites. Use `--json` on the verbs
#   below instead.)
ALLOWED_READ_OPS=(
  "pr view"
  "pr diff"
  "pr list"
  "pr checks"
  "issue view"
  "issue list"
)
# ──────────────────────────────────────────────────────────────────────────────────────────

set -euo pipefail

die() { printf 'gh.sh: REFUSED — %s\n' "$1" >&2; exit 1; }

[[ $# -ge 2 ]] || die "need at least <noun> <verb> (e.g. 'pr review'). got: $*"

op="$1 $2"
class=""
for a in "${ALLOWED_PUBLISH_OPS[@]}"; do [[ "$op" == "$a" ]] && class="publish" && break; done
if [[ -z "$class" ]]; then
  for a in "${ALLOWED_READ_OPS[@]}"; do [[ "$op" == "$a" ]] && class="read" && break; done
fi
[[ -n "$class" ]] || die "op '$op' not in ALLOWED_PUBLISH_OPS or ALLOWED_READ_OPS (Operator-governed policy block)"

printf 'gh.sh: → gh %s  [%s]\n' "$*" "$class" >&2
if [[ "${GH_SH_DRY_RUN:-0}" == "1" ]]; then
  printf 'gh.sh: (dry-run; not executed)\n' >&2
  exit 0
fi
command gh "$@"
