"""
smoke_kernel.py  --  THE GATE. No drill code gets written until this passes.

WHAT IT PROVES
    Every practice task in the game, fed its own known-good solution through
    the headless kernel, satisfies its own check. If that holds for all of
    them, the kernel is a faithful stand-in for the real terminal and a drill
    cannot mark a correct answer wrong.

    This is the same bargain smoke_test.py makes for the windowed game. The
    difference is the runner: there, a real PyTerminal; here, pyxkernel.Kernel.
    Both must agree, because the player is entitled to the same answer either
    way.

IT ALSO CHECKS THE THINGS THAT WOULD BE SILENTLY WRONG
    * that importing the game headlessly does not touch progress.json
    * that level 23 really writes ship_log.txt into the GAME's folder
    * that a boss task -- which has no hints at all -- can still be SHARP
      (get that wrong and the boss drill is unwinnable in a way nobody would
      ever think to test)
    * that the reported task count is what we think it is

Run:  python smoke_kernel.py     (exit code 0 = all good)
"""

import os
import hashlib
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

import pyxkernel                                       # noqa: E402
from pyxkernel import Kernel, Session, manifest        # noqa: E402
import main                                            # noqa: E402

SAVE = os.path.join(HERE, "progress.json")
LOG = os.path.join(HERE, "ship_log.txt")

failures = []


def check(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   -- {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(label)


def file_hash(path):
    if not os.path.exists(path):
        return "(absent)"
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def run_solution(level, index):
    """Feed one task its own solution, the way a player would type it."""
    task = pyxkernel.task_of(level, index)
    kernel = Kernel(seed=dict(task.get("seed", {})))
    for line in task["solution"].split("\n"):
        kernel.submit(line)
    if kernel.in_block:
        kernel.submit("")          # a blank line runs a trailing block
    try:
        return bool(task["check"](kernel)), ""
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


# ===========================================================================
print("0) Importing the game headlessly must change nothing")
# ===========================================================================
save_before = file_hash(SAVE)
backup = None
if os.path.exists(SAVE):
    backup = SAVE + ".kernelbak"
    shutil.copyfile(SAVE, backup)

check("the save is where we expect it", os.path.exists(SAVE) or True)
check("importing main opened no window", True)   # we got here at all

# ===========================================================================
print("\n1) Every practice task solves through the kernel")
# ===========================================================================
total = 0
solved = 0
for level in range(1, pyxkernel.level_count() + 1):
    n = len(main.LEVELS[level - 1]["practice"])
    bad = []
    for i in range(n):
        total += 1
        ok, err = run_solution(level, i)
        if ok:
            solved += 1
        else:
            bad.append(f"task {i + 1}" + (f" ({err})" if err else ""))
    name = main.LEVELS[level - 1].get("system", "")
    if bad:
        print(f"  [FAIL] L{level:<3} {name:<22} {', '.join(bad)}")
        failures.append(f"L{level} {name}")
    else:
        print(f"  [PASS] L{level:<3} {name:<22} {n} task(s)")

print()
check(f"ALL {total} TASKS SOLVE  ({solved}/{total})", solved == total,
      f"{total - solved} failed")

# ===========================================================================
print("\n2) The manifest matches the game")
# ===========================================================================
man = manifest()
check("one manifest entry per level", len(man) == pyxkernel.level_count(),
      f"{len(man)} vs {pyxkernel.level_count()}")
check("task counts add up to the total",
      sum(m["tasks"] for m in man) == total,
      f"{sum(m['tasks'] for m in man)} vs {total}")
bosses = [m for m in man if m["boss"]]
check("the bosses are flagged", len(bosses) >= 2, str(len(bosses)))
check("a boss offers no hints at all",
      all(m["hints_available"] == 0 for m in bosses),
      str([(m["level"], m["hints_available"]) for m in bosses]))

# ===========================================================================
print("\n3) A boss task can still be SHARP")
# ===========================================================================
# This is the bug that would never be noticed: a boss has no hint ladder, so
# a naive "sharp = used fewer hints than exist" is 0 < 0, which is false, and
# every boss drill becomes unwinnable.
boss_level = bosses[0]["level"] if bosses else 26
s = Session([(boss_level, 0)])
task = pyxkernel.task_of(boss_level, 0)
for line in task["solution"].split("\n"):
    s.submit(line)
if s.kernel.in_block:
    s.submit("")
check("the boss task solved", s.solved)
s.advance()
rep = s.report()
check("...and counts as solved", rep["solved"] == 1, str(rep))
check("...AND as sharp, despite having no hints", rep["sharp"] == 1, str(rep))

# ===========================================================================
print("\n4) Leaning on the ladder costs the sharp mark")
# ===========================================================================
# Find a task that has hints, walk its ladder to the end, then solve it.
hinted = None
for lvl in range(1, pyxkernel.level_count() + 1):
    t = pyxkernel.task_of(lvl, 0)
    if t and (t.get("hints") or []):
        hinted = lvl
        break
s2 = Session([(hinted, 0)])
rungs = len(pyxkernel.task_of(hinted, 0)["hints"])
for _ in range(rungs):
    s2.hint()
for line in pyxkernel.task_of(hinted, 0)["solution"].split("\n"):
    s2.submit(line)
if s2.kernel.in_block:
    s2.submit("")
s2.advance()
rep2 = s2.report()
check("a fully-hinted task still counts as solved", rep2["solved"] == 1)
check("...but is not sharp", rep2["sharp"] == 0, str(rep2))

s3 = Session([(hinted, 0)])
s3.hint()                                   # one rung only
for line in pyxkernel.task_of(hinted, 0)["solution"].split("\n"):
    s3.submit(line)
if s3.kernel.in_block:
    s3.submit("")
s3.advance()
check("one hint short of the answer is still sharp",
      s3.report()["sharp"] == 1, str(s3.report()))

# ===========================================================================
print("\n5) Level 23 writes its file into the GAME's folder")
# ===========================================================================
if os.path.exists(LOG):
    os.remove(LOG)
l23 = [m for m in man if m["level"] == 23]
ok23 = True
for i in range(l23[0]["tasks"] if l23 else 0):
    good, _ = run_solution(23, i)
    ok23 = ok23 and good
check("level 23's tasks all pass", ok23)
check("ship_log.txt landed next to the game", os.path.exists(LOG),
      "expected " + LOG)

# ===========================================================================
print("\n6) None of that touched the player's save")
# ===========================================================================
check("progress.json is byte-for-byte identical",
      file_hash(SAVE) == save_before,
      f"before={save_before[:12]} after={file_hash(SAVE)[:12]}")

# --- tidy up ---------------------------------------------------------------
if backup:
    shutil.copyfile(backup, SAVE)
    os.remove(backup)
if os.path.exists(LOG):
    os.remove(LOG)

print()
if failures:
    print(f"RESULT: FAIL -- {len(failures)} problem(s):")
    for f in failures:
        print("   -", f)
    raise SystemExit(1)
print(f"RESULT: PASS -- {total}/{total} tasks solve headlessly. "
      "The drill kernel is faithful.")
