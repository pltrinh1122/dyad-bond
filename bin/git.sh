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
#         bin/git.sh pull                        # ff-only refresh of current branch + submodules
#
# ── DECLARED ACCESS POLICY (Operator-governed; edit THIS block to widen/narrow) ───────────
ALLOWED_OPS=(push pull)                         # ops the Agent may invoke; all else refused
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
  pull)
    # "refresh" — fast-forward ONLY, with submodule trees synced to the pulled pointers.
    # Refuses (never merges/rebases) if local has diverged, so it cannot create a merge commit
    # or rewrite history on a protected branch. Arg-pinned: no passthrough, so --rebase / --no-ff
    # / arbitrary <refspec> cannot be injected.
    #
    # Emits a tagged verdict so the caller can tell FULLY-applied from PARTIAL (super advanced,
    # submodule stale) from REFUSED (nothing applied). A blocked submodule checkout exits non-zero
    # AFTER the superproject has already fast-forwarded — so non-zero alone cannot tell "retry-safe"
    # (diverged: nothing applied) from "do NOT re-pull" (partial: super already moved). Verified
    # empirically: partial submodule checkout exits 1 with super HEAD advanced.
    # Exit: 0 = OK/NOOP (intent met) · 1 = REFUSED (nothing applied) · 2 = PARTIAL (half-applied).
    branch="$(git rev-parse --abbrev-ref HEAD)"
    [[ $# -eq 0 ]] || die "pull takes no args (pinned to --ff-only --recurse-submodules origin '$branch'); got: $*"
    before="$(git rev-parse HEAD)"
    rc=0; run pull --ff-only --recurse-submodules origin "$branch" || rc=$?
    [[ "${GIT_SH_DRY_RUN:-0}" == "1" ]] && exit 0
    after="$(git rev-parse HEAD)"
    subs_out="$(git submodule status | grep -vE '^ ' || true)"   # nonempty = a submodule off-pointer
    if [[ $rc -eq 0 && -z "$subs_out" ]]; then
      if [[ "$before" == "$after" ]]; then
        printf 'git.sh: NOOP pull — %s already at %s (submodules in sync)\n' "$branch" "${after:0:7}" >&2
      else
        printf 'git.sh: OK pull — %s %s→%s, submodules synced\n' "$branch" "${before:0:7}" "${after:0:7}" >&2
      fi
      exit 0
    fi
    if [[ "$before" == "$after" ]]; then
      printf 'git.sh: REFUSED — pull NOT applied: %s unchanged at %s (ff refused: local diverged, or fetch failed). Resolve & retry.\n' "$branch" "${before:0:7}" >&2
      exit 1
    fi
    printf 'git.sh: PARTIAL — %s advanced %s→%s but submodules NOT synced:\n%s\n  → clean the submodule work tree, then: git submodule update --init  (do NOT re-pull; super already moved)\n' "$branch" "${before:0:7}" "${after:0:7}" "$subs_out" >&2
    exit 2
    ;;
  *)
    die "no handler for op '$op' (unreachable; ALLOWED_OPS gate)"
    ;;
esac
