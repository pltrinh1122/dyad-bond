#!/usr/bin/env bash
# bin/scratch.sh — dyad-bond minimal-save scratch tier (s-local7, 2026-06-22; v2 after adversarial verify)
#
# ⚠ RETIRED 2026-06-27 (Operator fold+land) — DORMANT, do not wire into resume/standup/standdown.
#   Store was mount-coupled (cloud-dark) + the use-case (un-landed raw crossing /exit) is dissolved by the
#   thread-until-land discipline. Durability-of-record = Agent-owned WIP auto-save (commit+push at pauses),
#   Stop-hook-enforced. Single-home: dialectic/substrate-access.md §Scratch RETIRED. Kept for git history.
#
# WHY (ours — s-local7, Operator-initiated initiative-test): the Agent races to *consolidate / land*
#   (synthesize prose into the corpus) mid-descent. Diagnosed root = the served-helpfulness prior; the
#   excuse it wore = inv:durability conflating SAVE with LAND (the only durable state was committed-to-
#   corpus). FIX = decouple: SAVE = raw capture, durable, judgment-free (this tool); LAND = synthesis
#   into dialectic/, single-homed, IFF-gated, deferred until the thread settles.
#
# WHAT THIS TOOL IS / IS NOT (honest after adversarial verify — see dialectic/scratch-tier.md):
#   - It removes the durability ALIBI for racing. It does NOT bind the impulse. Necessary, not sufficient.
#   - The binding mechanism is the OPERATOR as external separator + the lagged `--rate` trend.
#     `--catch` only MEASURES; it does not prevent. Self-logged catches are a FLOOR, not a count
#     (F2-K1: the Agent can't reliably self-detect its own reflex) — tag Operator-detected ones `-o`.
#   - SCRATCH IS A TRANSIENT CAPTURE BUFFER, NOT a content-home. dialectic/ is always canonical. So an
#     un-`--done` entry that has already landed is STALENESS to clear, not a rival home (no single-home breach).
#
# DURABILITY (precise, not oversold): the store is on the persistent local mount — durable against
#   `/exit`, `git clean`, repo re-clone (the dir can be wiped, the mount remains). It is NOT backed up
#   off-machine (single local disk, no remote) — a mount loss loses un-landed notes. So: land/discard
#   promptly; don't treat the tank as an archive. (Unlike .falsify-seen/.msg-tracker, which are
#   reconstructable cursors backed by gh — scratch holds ORIGINAL content with no upstream.)
#
# CONCURRENCY (bond is multi-writer — parallel sessions): the store is APPEND-ONLY. Saves, catches, and
#   `--done` all append; reviewed-state is folded at read time. No read-modify-rewrite → no lost-update.
#   ids are random tokens (no max+1 race). The ONLY rewrite is `--gc` (explicit maintenance, run quiescent).
#
# Usage:
#   scratch.sh "note"               save a raw note (triage item)
#   scratch.sh -t <thread> "note"   save with a reload-pointer thread tag
#   scratch.sh -- "note"            save a literal note that begins with dashes
#   scratch.sh --catch <stop> "n"   log a self-detected reflex catch (measurement; source=self)
#   scratch.sh --catch <stop> -o "n"  log an OPERATOR-detected catch (source=operator — the real signal)
#   scratch.sh --list               list unreviewed NOTES (triage; catches are not triage items)
#   scratch.sh --done <id>...        mark notes reviewed (landed / discarded) — append-only, multi-writer-safe
#   scratch.sh --rate [<stop>]      catch counts by stop, split self vs operator
#   scratch.sh --count              # unreviewed notes (standup surfacing)
#   scratch.sh --gc                 compact: drop reviewed notes + done-records (run when no parallel writer)
set -euo pipefail
exec python3 - "$@" <<'PY'
import sys, os, json, secrets
from collections import Counter
from datetime import datetime, timezone

STORE = "/mnt/shared_data/dzw/.dyad-bond-state/scratch.jsonl"
KNOWN = {"--list", "--count", "--rate", "--done", "--catch", "--gc", "-t", "--"}

def now():    return datetime.now(timezone.utc).isoformat(timespec="seconds")
def new_id(): return secrets.token_hex(3)            # 6 hex chars — unique without coordination, typeable

def load():
    if not os.path.exists(STORE): return []
    out = []
    with open(STORE) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try: out.append(json.loads(line))
            except json.JSONDecodeError: pass        # tolerate a torn line; never lose the rest
    return out

def append(rec):                                     # the ONLY write path (besides --gc) — O_APPEND atomic
    os.makedirs(os.path.dirname(STORE), exist_ok=True)
    with open(STORE, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def done_ids(recs):                                  # fold reviewed-state from append-only tombstones
    s = set()
    for r in recs:
        if r.get("kind") == "_done":
            s.update(r.get("ids", []))
    return s

def notes(recs):   return [r for r in recs if r.get("kind") == "note"]
def catches(recs): return [r for r in recs if r.get("kind") == "catch"]

def die(msg, code=2):
    print(msg, file=sys.stderr); sys.exit(code)

args = sys.argv[1:]
USAGE = ('usage: scratch.sh "note" | -t <thread> "note" | -- "note" | --catch <stop> [-o] "note" '
         '| --list | --done <id>... | --rate [stop] | --count | --gc')
if not args: die(USAGE)
cmd = args[0]
session = os.environ.get("DYAD_SESSION", "")         # optional session stamp (else bucket by ts/date)

# ── read ops ──────────────────────────────────────────────────────────────────
if cmd == "--list":
    recs = load(); dn = done_ids(recs)
    es = [e for e in notes(recs) if e.get("id") not in dn]
    if not es: print("scratch: 0 unreviewed notes — tank clean."); sys.exit(0)
    for e in es:
        thr = f" ({e['thread']})" if e.get("thread") else ""
        print(f"#{e.get('id','?')}  {e.get('ts','?')}  note{thr}  {e.get('note','')}")
    print(f"\n{len(es)} unreviewed — land what's settled into dialectic/, then `scratch.sh --done <id>...`")
    sys.exit(0)

if cmd == "--count":
    recs = load(); dn = done_ids(recs)
    print(sum(1 for e in notes(recs) if e.get("id") not in dn)); sys.exit(0)

if cmd == "--rate":
    stop = args[1] if len(args) > 1 else None
    cs = [c for c in catches(load()) if stop is None or c.get("stop") == stop]
    if not cs: print("no catches logged."); sys.exit(0)
    by = {}
    for c in cs:
        by.setdefault(c.get("stop", "?"), Counter())[c.get("source", "self")] += 1
    for k in sorted(by, key=lambda k: -sum(by[k].values())):
        op, self_ = by[k].get("operator", 0), by[k].get("self", 0)
        print(f"{op+self_:>3}  {k}   (operator:{op}  self:{self_}←floor)")
    print("\nsignal = the operator:N trend (self:N is a floor — under-counts; F2-K1).")
    sys.exit(0)

# ── --done (append-only tombstone — multi-writer-safe, no rewrite) ──────────────
if cmd == "--done":
    recs = load(); valid_note_ids = {e.get("id") for e in notes(recs)}
    want, bad = [], []
    for a in args[1:]:
        a = a.lstrip("#")
        (want if a in valid_note_ids else bad).append(a)
    if bad: print(f"⚠ ignored (no such note id): {' '.join(bad)}", file=sys.stderr)
    if not want: die("nothing to mark — no valid note id given.", 1 if args[1:] else 2)
    already = done_ids(recs)
    fresh = [i for i in want if i not in already]
    if fresh: append({"kind": "_done", "ids": fresh, "ts": now()})
    print(f"marked {len(fresh)} reviewed" + (f" ({len(want)-len(fresh)} already)" if len(want) != len(fresh) else "") + ".")
    sys.exit(0)

# ── --gc (the ONLY rewrite — explicit maintenance; run with no parallel writer) ─
if cmd == "--gc":
    recs = load(); dn = done_ids(recs)
    keep = [r for r in recs if r.get("kind") == "catch"
            or (r.get("kind") == "note" and r.get("id") not in dn)]
    dropped = len(recs) - len(keep)
    tmp = STORE + ".tmp"
    os.makedirs(os.path.dirname(STORE), exist_ok=True)
    with open(tmp, "w") as f:
        for r in keep: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, STORE)
    print(f"gc: dropped {dropped} reviewed-note/tombstone record(s); kept {len(keep)} (catches + unreviewed notes)."); sys.exit(0)

# ── save / catch (append-only) ──────────────────────────────────────────────────
if cmd == "--catch":
    if len(args) < 3: die('usage: scratch.sh --catch <stop> [-o] "note"')
    stop = args[1]; rest = args[2:]
    source = "self"
    if rest and rest[0] == "-o": source, rest = "operator", rest[1:]
    note = " ".join(rest).strip()
    if not note: die("empty catch note.")
    e = {"id": new_id(), "ts": now(), "kind": "catch", "stop": stop, "source": source, "note": note}
    if session: e["session"] = session
    append(e); print(f"caught {e['id']}: [{stop}/{source}] {note}"); sys.exit(0)

thread = None
if cmd == "-t":
    if len(args) < 3: die('usage: scratch.sh -t <thread> "note"')
    thread, note = args[1], " ".join(args[2:]).strip()
elif cmd == "--":
    note = " ".join(args[1:]).strip()                # explicit literal save (note may start with dashes)
elif cmd.startswith("-") and cmd not in KNOWN:
    die(f"unknown option '{cmd}'. To save a literal note that begins with dashes, use:  scratch.sh -- \"{cmd} ...\"")
else:
    note = " ".join(args).strip()
    if note.startswith("--"):
        die(f"refusing to save a note that begins with '--' (likely a mis-quoted command). Use `scratch.sh -- \"...\"` to force.")

if not note: die("empty note — nothing to save.")
e = {"id": new_id(), "ts": now(), "kind": "note", "note": note}
if thread:  e["thread"] = thread
if session: e["session"] = session
append(e); print(f"saved {e['id']}: {note}")
PY
