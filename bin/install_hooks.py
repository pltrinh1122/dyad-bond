#!/usr/bin/env python3
"""Install dyad-bond's stand-up / stand-down hooks in a Claude Code settings file.

Wires two hooks (Item-K6):
  - SessionStart (startup/resume/clear/compact) -> `bin/standup.sh --hook`  (mechanical resume checks,
    injected as additionalContext so the resume routine loads without a per-session trigger). All four
    sources per dialectic/standdown-automation.md's own table — `clear` was a gap vs that table until
    2026-07-04 (Operator-caught: does /clear re-load the anchor the way /compact is documented to?
    Unconfirmed either way, but the check is cheap + idempotent + non-judgmental, so include it).
  - SessionEnd                            -> `bin/standdown.sh --log`  (mechanical durability line;
    SessionEnd is teardown-only, so this is logging — the JUDGMENT write stays the agent's act).

Properties (mirrors bin/grant_push.py):
  - idempotent      — re-running makes no further change once present
  - safe            — refuses on invalid/non-object JSON; never clobbers; atomic write
  - non-destructive — preserves existing keys, including other hooks/permissions

NOTE: executing this against the real settings file IS the install. By the covalent gate
(K6 constraint a / S2 — substrate-access.md) that is the OPERATOR's act, never the Agent's
self-grant: an Agent installing automated self-behavior is exactly the boundary S2 guards.
Design + rationale: dialectic/standdown-automation.md. Default target is the checked-in tier.
"""
import argparse
import json
import os
import pathlib
import sys
import tempfile

# $CLAUDE_PROJECT_DIR is expanded by Claude Code at hook-run time to the project root.
DIR = "$CLAUDE_PROJECT_DIR"
HOOKS = {
    "SessionStart": [{
        "matcher": "startup|resume|clear|compact",
        "hooks": [{"type": "command", "command": f"{DIR}/bin/standup.sh --hook"}],
    }],
    "SessionEnd": [{
        "hooks": [{"type": "command", "command": f"{DIR}/bin/standdown.sh --log"}],
    }],
}


def install(path):
    p = pathlib.Path(path)
    raw = p.read_text() if p.exists() else ""
    try:
        cfg = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as e:
        sys.exit(f"REFUSED: {p} is not valid JSON ({e}); leaving it untouched.")
    if not isinstance(cfg, dict):
        sys.exit(f"REFUSED: top-level of {p} is not a JSON object; leaving it untouched.")

    hooks = cfg.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        sys.exit(f"REFUSED: hooks in {p} is not a JSON object; leaving it untouched.")

    added = []
    for event, groups in HOOKS.items():
        existing = hooks.setdefault(event, [])
        if not isinstance(existing, list):
            sys.exit(f"REFUSED: hooks.{event} in {p} is not a list; leaving it untouched.")
        for g in groups:
            cmd = g["hooks"][0]["command"]
            already = any(
                isinstance(eg, dict)
                and any(isinstance(h, dict) and h.get("command") == cmd
                        for h in eg.get("hooks", []))
                for eg in existing
            )
            if not already:
                existing.append(g)
                added.append((event, cmd))

    # atomic write: tmp in same dir + os.replace
    p.parent.mkdir(parents=True, exist_ok=True)
    out = json.dumps(cfg, indent=2) + "\n"
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), prefix=".settings-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(out)
        os.replace(tmp, p)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    if added:
        print(f"✓ {p}: wired {len(added)} hook(s):")
        for event, cmd in added:
            print(f"    +{event}: {cmd}")
    else:
        print(f"✓ {p}: hooks already wired — no change (idempotent).")
    print("\n--- resulting file ---")
    print(p.read_text(), end="")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--path", default=".claude/settings.json",
                    help="settings file to update (default: .claude/settings.json)")
    install(ap.parse_args().path)


if __name__ == "__main__":
    main()
