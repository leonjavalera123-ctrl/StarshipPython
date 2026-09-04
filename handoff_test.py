"""
handoff_test.py  --  proves the 3D ship can borrow this game safely.

This is the gate for Phase 1 of the Starship Pyxis: Shakedown build. It runs
with NO real window (the 'dummy' video driver), so it works headless and fast.

WHAT IT PROVES
    1. Reading the request off the command line works (and no request at all
       still means "just start normally").
    2. `is_clean` grades the way the design says: hints are FREE, only reading
       the full answer or not finishing costs you the label.
    3. A whole level can be played to the end in handoff mode, and the ship gets
       a correct report back.
    4. Closing the window mid-level reports "not certified" instead of nothing.
    5. A finished level's report can never be overwritten by a later bail.
    6. THE BIG ONE: progress.json comes out byte-for-byte identical. The cadet's
       own campaign save is not the ship's to touch.
    7. ...but with handoff mode OFF, saving still works exactly as it always did.

Run:  python handoff_test.py     (exit code 0 = all good)
"""
import os
import json
import shutil
import hashlib

os.environ["SDL_VIDEODRIVER"] = "dummy"   # no real window needed
os.environ["SDL_AUDIODRIVER"] = "dummy"

# Always work from the game's own folder. Level 23 writes ship_log.txt to the
# CURRENT folder, so running this from somewhere else would grade the wrong file.
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

import pygame
pygame.init()
pygame.display.set_mode((1000, 700))

import handoff
import main
from main import Game, LevelScene

REPORT_PATH = os.path.join(HERE, "_test_report.json")
failures = []


def check(label, condition, detail=""):
    """Record one pass/fail line."""
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}"
          + (f"  -- {detail}" if detail and not condition else ""))
    if not condition:
        failures.append(label)


def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def fake_game():
    """A Game object with no real window, enough for a LevelScene to run."""
    game = Game.__new__(Game)
    game.screen = pygame.display.get_surface()
    game.unlocked = 0
    game.resume_level = 0
    game.resume_task = 0
    game.confirm_quit = False
    return game


def play_level(scene, use_hints_on_first_task=False, walk_ladder_to_end=False):
    """Drive a LevelScene from brief all the way to the end of repair.

    Feeds each practice task its own known-good solution, exactly like
    smoke_test.py does. Optionally presses the hint button first, so we can test
    that hints are free and that the last rung is what actually costs you.
    """
    guard = 0
    while guard < 80:
        guard += 1
        if scene.phase == "brief":
            scene.set_phase("example")
        elif scene.phase == "example":
            scene.explain_i = 0
            scene.set_phase("explain")
        elif scene.phase == "explain":
            if scene.explain_i < len(scene.level["explain"]) - 1:
                scene.explain_i += 1
            else:
                scene.set_phase("practice")
        elif scene.phase == "practice":
            task = scene.level["practice"][scene.task_i]
            hints = task.get("hints") or []
            if scene.task_i == 0 and hints:
                # Press the hint button the way the real game does.
                rungs = len(hints) if walk_ladder_to_end else 1
                if use_hints_on_first_task or walk_ladder_to_end:
                    for _ in range(rungs):
                        if scene.hints_shown < len(hints):
                            scene.hints_shown += 1
                            scene.hints_used += 1
                        if scene.hints_shown >= len(hints) and scene.hint_btn.enabled:
                            scene.full_answers += 1
                            scene.hint_btn.enabled = False
            for line in task["solution"].split("\n"):
                scene.terminal.input = line
                scene.terminal.submit_line()
            if scene.terminal.in_block:
                scene.terminal.input = ""
                scene.terminal.submit_line()
            if not task["check"](scene.terminal):
                return False
            if scene.task_i < len(scene.level["practice"]) - 1:
                scene._load_task(scene.task_i + 1)
            else:
                scene.set_phase("repair")
        elif scene.phase == "repair":
            scene._go_next_level()
            return True
    return False


def run_handoff_level(level_number, **kwargs):
    """Play one level start to finish in handoff mode; return the ship's report."""
    if os.path.exists(REPORT_PATH):
        os.remove(REPORT_PATH)
    main.REQUEST = {"level": level_number, "session": "sess-123",
                    "report": REPORT_PATH}
    main.SAVE_LOCKED = True
    try:
        game = fake_game()
        scene = LevelScene(game, main.LEVELS[level_number - 1], level_number - 1)
        ok = play_level(scene, **kwargs)
        if not ok:
            return None
        with open(REPORT_PATH) as f:
            return json.load(f)
    finally:
        main.REQUEST = None
        main.SAVE_LOCKED = False


# ===========================================================================
print("1) Reading the request off the command line")
# ===========================================================================
check("no arguments means normal startup",
      handoff.read_request([]) is None)
check("a full request parses",
      handoff.read_request(["--level", "7", "--session", "abc",
                            "--report", "r.json"])
      == {"level": 7, "session": "abc", "report": "r.json"})
check("a non-numeric level is ignored",
      handoff.read_request(["--level", "banana"]) is None)
check("unknown flags are skipped",
      handoff.read_request(["--wat", "--level", "2"])["level"] == 2)

# ===========================================================================
print("\n2) Grading: hints are free, the full answer is not")
# ===========================================================================
base = {"cleared": True, "tasks": 3, "hints_used": 0, "full_answer_reveals": 0}
check("a finished level is clean", handoff.is_clean(base))
check("leaning on hints is still clean",
      handoff.is_clean(dict(base, hints_used=9)))
check("reading the full answer is not clean",
      not handoff.is_clean(dict(base, full_answer_reveals=1)))
check("an unfinished level is not clean",
      not handoff.is_clean(dict(base, cleared=False)))
check("a level with no task data is not clean",
      not handoff.is_clean(dict(base, tasks=0)))
check("garbage is not clean", not handoff.is_clean(None))

# ===========================================================================
print("\n3) A full level played through the ship")
# ===========================================================================
save_before = file_hash(main.SAVE_PATH)
save_text_before = open(main.SAVE_PATH).read()

rep = run_handoff_level(1)
check("level 1 produced a report", rep is not None)
if rep:
    check("session id echoed back", rep["session"] == "sess-123", rep.get("session"))
    check("reported as certified", rep["cleared"] is True)
    check("level number is 1-based", rep["level"] == 1, rep.get("level"))
    check("task count matches the level",
          rep["tasks"] == len(main.LEVELS[0]["practice"]), rep.get("tasks"))
    check("a clean run reveals no answers", rep["full_answer_reveals"] == 0)
    check("the report grades as clean", handoff.is_clean(rep))
    check("duration was measured", isinstance(rep["duration"], (int, float)))

print("\n   ...the same level, leaning on one hint")
rep = run_handoff_level(1, use_hints_on_first_task=True)
if rep:
    check("hints were counted", rep["hints_used"] >= 1, rep.get("hints_used"))
    check("using a hint is STILL clean", handoff.is_clean(rep))

print("\n   ...the same level, walking the ladder to the answer")
rep = run_handoff_level(1, walk_ladder_to_end=True)
if rep:
    check("the full answer was noticed", rep["full_answer_reveals"] == 1,
          rep.get("full_answer_reveals"))
    check("reading the answer is not clean", not handoff.is_clean(rep))
    check("but it still CERTIFIES the system", rep["cleared"] is True)

# ===========================================================================
print("\n4) Level 23 -- the one that writes a file to the current folder")
# ===========================================================================
rep = run_handoff_level(23)
check("level 23 round-trips", rep is not None and rep["cleared"] is True)
check("ship_log.txt landed in the game folder",
      os.path.exists(os.path.join(HERE, "ship_log.txt")))

# ===========================================================================
print("\n5) A boss level (no hints at all)")
# ===========================================================================
rep = run_handoff_level(26)
if rep:
    check("boss level round-trips", rep["cleared"] is True)
    check("a boss offers no hint rungs", rep["hints_available"] == 0,
          rep.get("hints_available"))
    check("a boss can never look like it revealed an answer",
          rep["full_answer_reveals"] == 0)
    check("so a boss run grades clean", handoff.is_clean(rep))

# ===========================================================================
print("\n6) Leaving early")
# ===========================================================================
if os.path.exists(REPORT_PATH):
    os.remove(REPORT_PATH)
main.REQUEST = {"level": 2, "session": "bail-1", "report": REPORT_PATH}
main.SAVE_LOCKED = True
try:
    game = fake_game()
    game.scene = LevelScene(game, main.LEVELS[1], 1)
    game.handoff_bail()                      # like clicking the window's X
    with open(REPORT_PATH) as f:
        rep = json.load(f)
    check("closing mid-level still reports", rep["session"] == "bail-1")
    check("...and reports NOT certified", rep["cleared"] is False)
    check("...which never grades clean", not handoff.is_clean(rep))
finally:
    main.REQUEST = None
    main.SAVE_LOCKED = False

print("\n   ...and a finished level cannot be downgraded afterwards")
if os.path.exists(REPORT_PATH):
    os.remove(REPORT_PATH)
main.REQUEST = {"level": 1, "session": "once", "report": REPORT_PATH}
main.SAVE_LOCKED = True
try:
    game = fake_game()
    scene = LevelScene(game, main.LEVELS[0], 0)
    game.scene = scene
    play_level(scene)                        # finishes -> reports cleared=True
    game.handoff_bail()                      # then the window closes anyway
    with open(REPORT_PATH) as f:
        rep = json.load(f)
    check("the good report survives the window closing", rep["cleared"] is True)
finally:
    main.REQUEST = None
    main.SAVE_LOCKED = False

# ===========================================================================
print("\n7) THE BIG ONE -- the cadet's own save is untouched")
# ===========================================================================
check("progress.json is byte-for-byte identical",
      file_hash(main.SAVE_PATH) == save_before,
      f"before={save_before[:12]} after={file_hash(main.SAVE_PATH)[:12]}")
check("...and still says what it said before",
      open(main.SAVE_PATH).read() == save_text_before)

# ===========================================================================
print("\n8) With handoff mode OFF, saving still works normally")
# ===========================================================================
backup = main.SAVE_PATH + ".testbak"
shutil.copyfile(main.SAVE_PATH, backup)
try:
    main.REQUEST = None
    main.SAVE_LOCKED = False
    game = fake_game()
    game.unlocked = 4
    game.resume_level = 3
    game.resume_task = 2
    game.music_idx, game.fx_on, game.type_idx = 2, True, 1
    main.save_game(game)
    st = main.load_state()
    check("normal play still writes progress", st["unlocked"] == 4, st)
    check("...including the exact resume spot",
          st["level"] == 3 and st["task"] == 2, st)
finally:
    shutil.copyfile(backup, main.SAVE_PATH)   # put the real save straight back
    os.remove(backup)

check("the real save was restored", file_hash(main.SAVE_PATH) == save_before)

# ---------------------------------------------------------------------------
# Tidy up anything the test made.
for junk in (REPORT_PATH, os.path.join(HERE, "ship_log.txt")):
    if os.path.exists(junk):
        os.remove(junk)

print()
if failures:
    print(f"RESULT: FAIL -- {len(failures)} problem(s):")
    for f in failures:
        print("   -", f)
    raise SystemExit(1)
print("RESULT: PASS -- the ship can borrow this game safely.")
