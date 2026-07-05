#!/usr/bin/env bash
# bin/land.sh — dyad-bond `d-land` mechanical spine (sync → re-branch → commit → push)
#
# WHY: `d-land`'s local-nav (fetch/checkout -B when a prior PR for this branch already merged) has
#   no spine, so those raw ops hit the classifier's local-state prompt every time the discipline
#   recurs (dialectic/substrate-access.md §Discipline-based permissioning, "d-land SPINE — queued
#   fix-on-bite" 2026-07-05). This bundles the MECHANICAL half of `d-land` into one grantable unit
#   — Bash(bin/land.sh:*) — same shape as standup.sh/standdown.sh.
#
# CROSS-DYAD REFERENCE (D1 triangulation, this session): dyad-cairn (github.com/pltrinh1122/dyad-cairn)
#   independently converged on "one committed script per discipline" as the granted unit (bin/pr,
#   bin/commission, bin/audit, bin/retro, bin/d-start/d-land/d-reflect...) — confirms the shape here.
#   NOT adopted from cairn: its `bin/gh`+FSM `trail_dispose()` auto-executes `gh pr merge` with no
#   human confirmation, and `bin/agy` unconditionally strips the harness's own permission gate
#   (`--dangerously-skip-permissions`) to unblock headless merges. Cairn owns that as a considered
#   trade-off (their SPAO/FSM test-gates stand in for HITL); bond's `bond:C1` makes the human merge
#   THE load-bearing act, not a redundant check a test suite could subsume — so this script commits
#   and pushes, same as cairn's mechanical scripts, but never merges. Merge stays the Operator's,
#   full stop. → dialectic/substrate-access.md §Discipline-based permissioning for the full triangulation.
#
# SCOPE (the landing-discipline checklist's own boundary — dialectic/relationship-craft.md
#   §The landing-discipline):
#   - DOES:    detect an already-landed branch (tip is an ancestor of origin/<default>) and re-branch
#              fresh off it; stage+commit if a message is given and the tree is dirty; push via
#              bin/git.sh (reuses ITS ALLOWED_OPS/PROTECTED_BRANCHES gate — single-home, not
#              re-policed here).
#   - NEVER:   opens a PR, merges, or resolves judgment calls (DAG review, PR body) — those stay the
#              Agent's live judgment (`bond:no-self-act`) or the Operator's gate (`bond:no-self-ratify`).
#
# COVALENT GATE: same as git.sh/standup.sh — the Operator performs the permission grant
#   (Bash(bin/land.sh:*)); this script is unaffected either way, runnable by hand meanwhile.
#
# Usage:  bin/land.sh                    # sync/re-branch check + push only (tree already clean/committed)
#         bin/land.sh "commit message"   # stage-all + commit with this message, then sync/re-branch + push
#         LAND_SH_DEFAULT_BRANCH=main bin/land.sh   # override default-branch name (default: main)

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DEFAULT_BRANCH="${LAND_SH_DEFAULT_BRANCH:-main}"

git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
  || { echo "land.sh: REFUSED — not inside a git work tree" >&2; exit 1; }

branch="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$branch" == "$DEFAULT_BRANCH" ]]; then
  echo "land.sh: REFUSED — on '$DEFAULT_BRANCH' itself; d-land operates from a feature branch." >&2
  exit 1
fi

# ── sync ────────────────────────────────────────────────────────────────────────────────────────
echo "land.sh: → git fetch origin $DEFAULT_BRANCH" >&2
git fetch origin "$DEFAULT_BRANCH"

# ── re-branch (only if THIS branch's tip already landed in origin/<default>, e.g. its PR merged) ──
# Guarded by "HEAD != origin/<default>" too: a FRESH branch cut off the default branch is trivially
# its own ancestor (every commit is an ancestor of itself) — that must fall through to commit/push,
# not be mistaken for "already landed, reset it." Only a branch that is BEHIND origin/<default> and
# wholly contained in it is the landed case.
head_sha="$(git rev-parse HEAD)"
default_sha="$(git rev-parse "origin/$DEFAULT_BRANCH")"
if [[ "$head_sha" != "$default_sha" ]] \
   && git merge-base --is-ancestor "$branch" "origin/$DEFAULT_BRANCH" 2>/dev/null; then
  echo "land.sh: '$branch' is already an ancestor of origin/$DEFAULT_BRANCH — treating as a landed arc." >&2
  echo "land.sh: → git checkout -B $branch origin/$DEFAULT_BRANCH" >&2
  git checkout -B "$branch" "origin/$DEFAULT_BRANCH"
  echo "land.sh: restarted '$branch' fresh off origin/$DEFAULT_BRANCH — nothing to commit/push this run." >&2
  exit 0
fi
# NOTE (fail-loud, not silent-clean — bond:substrate-agnostic clause-2): this ancestor-check misses a
# SQUASH-merged PR (the merged commit on main isn't byte-identical to the branch tip). A squash-merged
# branch just looks unlanded here and gets committed/pushed onto its own now-orphaned history; the next
# d-start's ROM/durability checks still surface a stale branch, so this fails loud, not clean — a known
# gap, not assumed-covered.

# ── commit (only if a message was given AND the tree is dirty) ────────────────────────────────────
if [[ $# -ge 1 ]]; then
  msg="$1"
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "land.sh: → git add -A && git commit -m <msg>" >&2
    git add -A
    git commit -m "$msg"
  else
    echo "land.sh: tree already clean — nothing to commit (message ignored)." >&2
  fi
elif [[ -n "$(git status --porcelain)" ]]; then
  echo "land.sh: REFUSED — tree is dirty and no commit message was given (usage: bin/land.sh \"<message>\")." >&2
  exit 1
fi

# ── push (delegates to bin/git.sh — single-home for push policy, not re-implemented here) ─────────
exec "$ROOT/bin/git.sh" push
