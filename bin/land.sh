#!/usr/bin/env bash
# bin/land.sh — dyad-bond d-land spine (discipline-scoped landing mechanics)
#
# WHY: d-land had no spine, so its local-nav (post-merge sync / re-branch / reset) PROMPTED every
#   session (deferrals.md 2026-07-05 "d-land requires permission"; the strand-recovery hit again
#   2026-07-06 — a reused branch stranded two commits off main). This encapsulates the MECHANICAL
#   half of the landing-discipline (relationship-craft.md §The landing-discipline) as ONE granted
#   unit — granted like standup.sh / standdown.sh, NOT a universal git.sh/allowlist widen
#   (substrate-access.md §Tier-2: the fix for local-nav recurring INSIDE a discipline is that
#   discipline's own spine, not a wider wrapper). Symmetry: d-start:standup.sh :: d-reflect:standdown.sh
#   :: d-land:land.sh.
#
# WHAT IT DOES NOT DO (by design — the JUDGMENT half stays the agent's covalent act, K6-b):
#   - It does NOT open, merge, or auto-merge the PR. The agent writes the PR body (judgment) and opens
#     via bin/gh.sh under the d-land signal (bond:no-self-act); the Operator merges (bond:no-self-ratify).
#   - It does NOT commit (a commit needs a message = judgment). It reports uncommitted/unpushed state;
#     the agent commits/pushes via bin/git.sh.
#   It stops at: "everything mechanical is verified, here is the scoped arc + the judgment template."
#
# Usage:  bin/land.sh            # mechanical landing checks + judgment template (agent runs on d-land)
#         bin/land.sh --sync     # pre-landing sync: SAFE re-branch when the branch's PR already merged
#                                 #   and nothing is ahead (the strand-remover). Never discards
#                                 #   ahead-commits; reports the recovery if diverged; refuses on main.
#         LAND_SH_DRY_RUN=1 bin/land.sh --sync   # print the reset it would run, do not execute

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PROTECTED_BRANCHES=(main)          # never reset/re-branch these under --sync
BOOT_SET=(DYAD.md CLAUDE.md GEMINI.md GLOSSARY.md)   # touching any = RESTART-PENDING implication

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
contains() { local x="$1"; shift; for e in "$@"; do [[ "$e" == "$x" ]] && return 0; done; return 1; }

# ─────────────────────────────────────────────────────────────────────────────────────────────
# --sync : encapsulate the post-merge local-nav that otherwise prompts (fetch + safe re-branch)
# ─────────────────────────────────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--sync" ]]; then
  contains "$branch" "${PROTECTED_BRANCHES[@]}" \
    && { echo "land.sh --sync: REFUSED — on protected branch '$branch' (re-branch a feature branch, not main)." >&2; exit 2; }
  git fetch origin main >/dev/null 2>&1 || { echo "land.sh --sync: fetch origin main FAILED — resolve network/remote, retry." >&2; exit 1; }
  ahead="$(git rev-list --count origin/main..HEAD 2>/dev/null || echo '?')"
  behind="$(git rev-list --count HEAD..origin/main 2>/dev/null || echo '?')"
  target="$(git rev-parse --short origin/main 2>/dev/null || echo '?')"
  if [[ "$ahead" == "0" && "$behind" == "0" ]]; then
    echo "land.sh --sync: NOOP — \`$branch\` already at origin/main ($target). Nothing to sync."
    exit 0
  elif [[ "$ahead" == "0" && "$behind" != "0" ]]; then
    # SAFE: nothing ahead → reset --hard loses no work. This is the strand-remover.
    if [[ "${LAND_SH_DRY_RUN:-}" == "1" ]]; then
      echo "land.sh --sync: DRY-RUN — would run: git reset --hard origin/main  ($branch 0-ahead, $behind-behind → $target)"
      exit 0
    fi
    git reset --hard origin/main >/dev/null
    echo "land.sh --sync: OK — \`$branch\` re-based to origin/main ($target); was 0-ahead/$behind-behind. Clean slate for the next arc."
    exit 0
  else
    # ahead>0 : do NOT auto-reset (would discard commits). Report the recovery, let the agent decide.
    echo "land.sh --sync: HELD — \`$branch\` is $ahead-ahead / $behind-behind of origin/main ($target)." >&2
    if [[ "$behind" == "0" ]]; then
      echo "  Normal in-flight arc ($ahead unmerged commit(s), main unchanged) — no sync needed; commit/push and land." >&2
    else
      echo "  DIVERGED (strand: this branch's prior PR merged, then it was reused). Auto-reset would LOSE the $ahead ahead-commit(s)." >&2
      echo "  Recover by hand (cherry-pick the strand onto fresh main):" >&2
      echo "    git checkout -B $branch origin/main && git cherry-pick $(git rev-list --reverse origin/main..HEAD | tr '\n' ' ')" >&2
    fi
    exit 3
  fi
fi

# ─────────────────────────────────────────────────────────────────────────────────────────────
# default : mechanical landing checks + judgment template (agent runs on d-land)
# ─────────────────────────────────────────────────────────────────────────────────────────────
lines=(); add() { lines+=("$1"); }

# 1. Durability (uncommitted / un-backed = ungrounded memory) — agent commits/pushes via git.sh.
# "unbacked" = commits reachable from HEAD but not from ANY remote ref (refs/remotes/*) — the true
# off-disk-durability test. Robust to all three traps hit building this: bin/git.sh pushes without -u
# (so @{u} is unreliable); auto-delete-on-merge leaves a STALE origin/<branch> ref; and a fresh
# re-branch sits on origin/main (backed up there, not on a branch of its own name). A single command
# → no pipefail double-emit.
dirty="$(git status --porcelain 2>/dev/null || true)"
unbacked="$(git rev-list --count HEAD --not --remotes 2>/dev/null || echo '?')"
if [[ -n "$dirty" ]]; then
  add "Durability: ⚠ DIRTY on \`$branch\` ($(printf '%s\n' "$dirty" | wc -l | tr -d ' ') paths) — commit via bin/git.sh before landing (a landing off an uncommitted tree drops work)."
elif [[ "$unbacked" != "0" ]]; then
  add "Durability: ⚠ $unbacked commit(s) not backed up on any remote — push via bin/git.sh."
else
  add "Durability: ✓ clean + backed up on \`$branch\`."
fi

# 2. Green-gate (verify before asserting green — item 2). invariant-eval always; linters if touched.
changed="$(git diff --name-only origin/main...HEAD 2>/dev/null; git diff --name-only 2>/dev/null; git diff --cached --name-only 2>/dev/null)"
gate_fail=0
run_gate() { # <label> <cmd...>
  local label="$1"; shift
  if "$@" >/tmp/land-gate.out 2>&1; then add "Green-gate: ✓ $label"; else
    add "Green-gate: ✗ $label FAILED — landing BLOCKED (fix before opening):"; add "  $(tail -3 /tmp/land-gate.out | tr '\n' '§' | sed 's/§/ | /g')"; gate_fail=1; fi
}
run_gate "invariant-eval.py" python3 bin/invariant-eval.py dialectic/invariant-schema.yaml dialectic/invariants-bond.yaml
grep -q 'invariants-bond\.yaml' <<<"$changed" && run_gate "validate-g0-genes.py" python3 bin/validate-g0-genes.py dialectic/invariants-bond.yaml
grep -q '^commissions/' <<<"$changed" && run_gate "commission-lint.py (touched commissions)" bash -c 'python3 bin/commission-lint.py commissions/*.md'
grep -q '^kb/.*\.md$' <<<"$changed" && run_gate "discipline-lint.py (touched kb/)" python3 bin/discipline-lint.py

# 3. Scope-to-arc by execution (item 3) — bundle everything ahead of main, not just the last commit.
mapfile -t arc < <(git log --oneline origin/main..HEAD 2>/dev/null || true)
if ((${#arc[@]})); then
  add "Arc scope (origin/main..HEAD → the PR bundle): ${#arc[@]} commit(s)"
  for c in "${arc[@]}"; do add "  $c"; done
else
  add "Arc scope: 0 commits ahead of main — nothing to land (already merged, or --sync needed for a strand)."
fi

# 4. Open-PR state → routes commit-push-done vs open-a-new-PR.
pr_json="$(bin/gh.sh pr list --head "$branch" --state open --json number,title 2>/dev/null | grep -oE '"number":[0-9]+' | head -1 || true)"
if [[ -n "$pr_json" ]]; then
  add "PR state: an OPEN PR exists for \`$branch\` (${pr_json}) → route = commit + push, done. Do NOT open a second."
else
  add "PR state: NO open PR for \`$branch\` → route = if the arc reads complete, open ONE (agent writes body + opens via bin/gh.sh)."
fi

# 8. RESTART-PENDING implication (item 8) — did the arc touch the boot-set?
touched_boot=()
for f in "${BOOT_SET[@]}"; do grep -qx "$f" <<<"$changed" && touched_boot+=("$f"); done
if ((${#touched_boot[@]})); then
  add "RESTART-PENDING: ⚠ boot-set touched (${touched_boot[*]}) → set RESTART-PENDING + refresh the per-file inv:rom-currency line in carry-forward.md (bond:rom-ui)."
else
  add "RESTART-PENDING: none — no boot-set file (${BOOT_SET[*]}) in the arc."
fi

# 9. PR-template presence (item 9 — re-check each landing, not once per session).
tmpl="$(find .github -iname '*template*' 2>/dev/null | head -1 || true)"
add "PR template: ${tmpl:-none found under .github}"

printf '%s\n' \
  "dyad-bond d-land (bin/land.sh) — mechanical landing checks. Green-gate must pass before opening."
printf '  %s\n' "${lines[@]}"

cat <<'TEMPLATE'

d-land — JUDGMENT (the agent fills; auto-check ≠ auto-act, K6-b / bond:no-self-act):
  1. Execution DAG — resolve remaining deps (doc drift, open dispositions) autonomously before opening.
  4/5. If opening: write a real body (Summary + Test plan), open MECHANICALLY off the d-land signal
       (no second CTA — SG-4), via bin/gh.sh. Do NOT merge / auto-merge / request reviewers.
  7. Surface it back explicitly — in chat AND logged in carry-forward.md ("PR #N is up for your gate").
TEMPLATE

[[ "$gate_fail" == "0" ]] || exit 1
