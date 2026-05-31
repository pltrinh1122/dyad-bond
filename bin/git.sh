#!/usr/bin/env bash
# bin/git.sh — dyad-bond substrate-access wrapper for git (v0.1)
#
# WHY (ours — see dialectic/substrate-access.md for the full reason + lineage):
#   push-to-main is recurring per-session friction; the harness auto-mode classifier blocks
#   BOTH a direct push and an Agent self-grant of `git push` (Self-Modification). For dyad-bond
#   the stake is MEMORY DURABILITY: the disk-ledger is the dyad's cross-/exit memory and the
#   remote is its only off-disk backup, so unpushed history = an ungrounded memory — a standing
#   threat to the research substrate our method reads ("the record we are already writing").
#
# STRUCTURE (invariant — triangulated from dyad-healer@bin/git.sh, which falsified 3 designs;
#   we INHERIT it, not re-derive): declared-policy single-file wrapper, permission-gated,
#   fail-closed. The harness grants the NARROW permission Bash(bin/git.sh:*) — never broad git.
#
# COVALENT GATE: boundary integrity rests on Operator-ratified edits to the POLICY block below
#   (chat-as-gate) + the Operator-performed permission grant — NOT an Agent self-grant. The Agent
#   gets the choke-point; widening it stays the Operator's act. Distinct, never merged.
#
# Usage:  bin/git.sh <op> [args...]
#         GIT_SH_DRY_RUN=1 bin/git.sh push     # print the resolved command, do not execute
#
# ── DECLARED ACCESS POLICY (Operator-governed; edit THIS block to widen/narrow) ───────────
ALLOWED_OPS=(push)                              # ops the Agent may invoke; all else refused
PROTECTED_BRANCHES=(main)                       # branches on which rewriting flags are refused
FORCE_FLAGS=(--force -f --force-with-lease)     # flags treated as history-rewriting
# ──────────────────────────────────────────────────────────────────────────────────────────

set -euo pipefail

die() { printf 'git.sh: REFUSED — %s\n' "$1" >&2; exit 1; }

contains() { local needle="$1"; shift; local x; for x in "$@"; do [[ "$x" == "$needle" ]] && return 0; done; return 1; }

run() {
  printf 'git.sh: → git %s\n' "$*" >&2
  if [[ "${GIT_SH_DRY_RUN:-0}" == "1" ]]; then
    printf 'git.sh: (dry-run; not executed)\n' >&2
    return 0
  fi
  command git "$@"
}

[[ $# -ge 1 ]] || die "no op given (usage: git.sh <op> [args])"
op="$1"; shift

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || die "not inside a git work tree"
contains "$op" "${ALLOWED_OPS[@]}" || die "op '$op' is not in declared ALLOWED_OPS (fail-closed)"

case "$op" in
  push)
    branch="$(git rev-parse --abbrev-ref HEAD)"
    if contains "$branch" "${PROTECTED_BRANCHES[@]}"; then
      for arg in "$@"; do
        contains "$arg" "${FORCE_FLAGS[@]}" \
          && die "history-rewriting flag '$arg' refused on protected branch '$branch'"
      done
    fi
    run push origin "$branch" "$@"
    ;;
  *)
    die "no handler for op '$op' (unreachable; ALLOWED_OPS gate)"
    ;;
esac
