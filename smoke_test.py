"""
smoke_test.py  --  a quick automated check that the game is wired up right.

It runs with NO real window (the 'dummy' video driver) so it works headless.
It checks two things:
    1. Every practice task's known 'solution' actually makes its 'check' pass.
    2. The lesson flow advances brief -> example -> explain -> practice -> repair
       and finishes the level without crashing.

Run:  python smoke_test.py    (exit code 0 = all good)
"""
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"   # no real window needed
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1000, 700))

from pyterminal import PyTerminal
import main
from main import Game, LevelScene


def check_solutions():
    failures = []
    for level in main.LEVELS:
        for i, task in enumerate(level["practice"]):
            term = PyTerminal(pygame.Rect(0, 0, 600, 400),
                              seed=dict(task.get("seed", {})))
            # Run each line of the known-good solution through the terminal.
            for line in task["solution"].split("\n"):
                term.input = line
                term.submit_line()
            # If the solution ends a block, an extra blank line runs it.
            if term.in_block:
                term.input = ""
                term.submit_line()
            ok = task["check"](term)
            tag = f"L{level['number']} task {i + 1}"
            print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {task['solution']!r}")
            if not ok:
                failures.append(tag)
    return failures


def walk_flow():
    """Drive one level through every phase, feeding solutions at practice time."""
    game = Game.__new__(Game)        # make a Game without opening a real window
    game.screen = pygame.display.get_surface()
    scene = LevelScene(game, main.LEVELS[0], 0)

    seen = []
    guard = 0
    while True:
        guard += 1
        if guard > 50:
            raise RuntimeError("flow did not finish -- possible loop")
        seen.append(scene.phase)
        if scene.phase == "practice":
            task = scene.level["practice"][scene.task_i]
            for line in task["solution"].split("\n"):
                scene.terminal.input = line
                scene.terminal.submit_line()
            scene.solved = scene.solved or task["check"](scene.terminal)
            assert scene.solved, f"task {scene.task_i} not solved by its solution"
            # Advance past the solved task.
            if scene.task_i < len(scene.level["practice"]) - 1:
                scene._load_task(scene.task_i + 1)
            else:
                scene.set_phase("repair")
        elif scene.phase == "brief":
            scene.set_phase("example")
        elif scene.phase == "example":
            scene.explain_i = 0
            scene.set_phase("explain")
        elif scene.phase == "explain":
            if scene.explain_i < len(scene.level["explain"]) - 1:
                scene.explain_i += 1
            else:
                scene.set_phase("practice")
        elif scene.phase == "repair":
            break
    return seen


if __name__ == "__main__":
    print("Checking that each task's solution passes its check():")
    fails = check_solutions()
    print("\nWalking the full lesson flow:")
    phases = walk_flow()
    print("  phases visited:", " -> ".join(dict.fromkeys(phases)))

    print()
    if fails:
        print("RESULT: FAIL --", ", ".join(fails))
        raise SystemExit(1)
    print("RESULT: PASS -- everything checks out.")
