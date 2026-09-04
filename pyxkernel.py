"""
pyxkernel.py  --  runs the practice tasks with no window at all.

WHAT THIS IS FOR
    Playing a level normally opens the game in its own window, and that is
    right: the five-phase lesson is the game. But for DRILLS -- short sets of
    practice tasks you run to stay sharp -- opening a second window to type
    four lines is heavy. This module runs the same tasks, with the same
    checkers, inside a headless Python process that the 3D ship talks to over
    a socket. Same code, same answers, no window.

WHY IT WORKS AT ALL
    Every one of the game's practice checks only ever looks at two things:
    `term.ns` (the variables you have made) and `term.last_run` (the text your
    last command produced). Nothing looks at pygame, at the screen, or at
    anything else. So a class that provides exactly those two attributes can
    run all 92 checkers untouched -- which is the whole reason this is a
    couple of hundred lines rather than a rewrite.

    smoke_kernel.py proves it: every task's own known-good solution, fed
    through this kernel, must satisfy that task's own check.

WHY GODOT SENDS ONLY (level, task) NUMBERS
    A task's `seed` holds LIVE PYTHON OBJECTS -- a tuple, a set, a class
    definition the task then asks you to instantiate. None of that survives a
    trip through JSON. So the 3D side never sends task content; it names a task
    by its level and index, and this side looks it up in the real level files.
    One source of truth, and it is the game's own.

THERE IS NO "SHOW ME THE ANSWER" COMMAND
    Starship Pyxis does not have one -- the last rung of a task's hint ladder
    IS the answer, reached by asking for hints one at a time. Adding a reveal
    here would quietly invent a shortcut the game deliberately does not have.
"""

import io
import os
import sys
import contextlib

# The lesson content lives in a pygame game. Tell SDL to use its do-nothing
# drivers BEFORE importing it, so no window and no audio device are ever
# opened -- this has to run on a machine with neither.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

# Level 23 teaches file handling by really writing ship_log.txt, and it uses a
# RELATIVE path. Without this line the file lands wherever the 3D game happened
# to be started from and the task grades against the wrong thing.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import main  # noqa: E402  (must come after the SDL environment is set)


# ---------------------------------------------------------------------------
# THE TERMINAL, WITHOUT THE TERMINAL
# ---------------------------------------------------------------------------

class Kernel:
    """Everything PyTerminal does with your code, and nothing it does on screen.

    `run_source` and `submit` are deliberate line-for-line copies of the real
    terminal's logic rather than a tidier rewrite. If the two ever disagree,
    a task could pass in one and fail in the other, and the player would be
    right and the game would be wrong.
    """

    def __init__(self, seed=None):
        self.ns = {}
        if seed:
            self.ns.update(seed)
        self.last_run = ""
        self.block = []           # collected lines of a multi-line block
        self.out = []             # [(text, colour)] produced since last drained

    @property
    def in_block(self):
        return len(self.block) > 0

    def echo(self, text, colour="star"):
        for line in str(text).split("\n"):
            self.out.append((line, colour))

    def run_source(self, source):
        """Compile and run one complete piece of code, capturing its output."""
        self.last_run = ""
        buffer = io.StringIO()
        try:
            # An EXPRESSION first (it has a value), else STATEMENTS.
            try:
                code = compile(source, "<drill>", "eval")
                is_expr = True
            except SyntaxError:
                code = compile(source, "<drill>", "exec")
                is_expr = False

            with contextlib.redirect_stdout(buffer):
                if is_expr:
                    result = eval(code, self.ns)
                else:
                    exec(code, self.ns)
                    result = None

            printed = buffer.getvalue()
            if printed:
                self.echo(printed.rstrip("\n"), "star")
            if is_expr and result is not None:
                self.echo(repr(result), "cyan")
            self.last_run = printed + ("" if result is None else repr(result))

        except Exception as e:
            self.echo(f"{type(e).__name__}: {e}", "red")
            self.last_run = f"{type(e).__name__}: {e}"

    def submit(self, line):
        """One line typed and Enter pressed. Run it, or keep collecting a block.

        The block rule is the game's: a line ending in ':' starts one, and a
        BLANK line runs it. Solutions in the level files are written expecting
        exactly that.
        """
        prompt = "... " if self.in_block else ">>> "
        self.echo(prompt + line, "green")

        if self.in_block:
            if line.strip() == "":
                source = "\n".join(self.block)
                self.block = []
                self.run_source(source)
            else:
                self.block.append(line)
        else:
            if line.strip() == "":
                pass
            elif line.rstrip().endswith(":"):
                self.block.append(line)
            else:
                self.run_source(line)

    def drain(self):
        """Take everything printed since last time, for sending to the ship."""
        lines, self.out = self.out, []
        return lines


# ---------------------------------------------------------------------------
# LOOKING UP THE REAL TASKS
# ---------------------------------------------------------------------------

def level_count():
    return len(main.LEVELS)


def task_of(level, index):
    """The task dict for a 1-based level and 0-based task index, or None."""
    if level < 1 or level > len(main.LEVELS):
        return None
    practice = main.LEVELS[level - 1]["practice"]
    if index < 0 or index >= len(practice):
        return None
    return practice[index]


def manifest():
    """Everything the ship needs to build a drill picker, derived live.

    Nothing about the curriculum is duplicated on the Godot side: task counts,
    level names and which levels have hints all come from here, so editing a
    level file can never leave the two out of step.
    """
    out = []
    for i, level in enumerate(main.LEVELS, start=1):
        practice = level["practice"]
        out.append({
            "level": i,
            "system": level.get("system", ""),
            "concept": level.get("concept", ""),
            "tasks": len(practice),
            "boss": bool(level.get("boss")),
            "secret": bool(level.get("secret")),
            # 0 means "this level offers no hints at all", which is how the
            # ship knows not to grade a boss as suspiciously hint-free.
            "hints_available": sum(len(t.get("hints") or []) for t in practice),
        })
    return out


# ---------------------------------------------------------------------------
# A DRILL
# ---------------------------------------------------------------------------

class Session:
    """A list of practice tasks, played one after another.

    Scoring mirrors the launcher's report exactly:
        solved  -- the check passed
        sharp   -- solved without walking the hint ladder to its last rung
    A task with NO hints (every boss task) is sharp on solving, because there
    is no ladder to walk. Getting that wrong makes bosses permanently
    un-sharp, which would quietly make the BOSS REFRESH drill unwinnable.
    """

    def __init__(self, pairs):
        self.pairs = [(int(a), int(b)) for a, b in pairs]
        self.index = -1
        self.kernel = None
        self.task = None
        self.hints_shown = 0
        self.solved = False
        self.results = []          # one dict per finished task
        self.done = False
        self.advance()

    # -- moving between tasks ------------------------------------------------

    def _record(self, skipped=False):
        if self.task is None:
            return
        hints = self.task.get("hints") or []
        has_hints = len(hints) > 0
        self.results.append({
            "level": self.pairs[self.index][0],
            "task": self.pairs[self.index][1],
            "solved": bool(self.solved),
            "skipped": bool(skipped),
            "hints_used": self.hints_shown,
            "hints_available": len(hints),
            # See the class note: no ladder means nothing to walk.
            "sharp": bool(self.solved) and (
                not has_hints or self.hints_shown < len(hints)),
        })

    def advance(self, skipped=False):
        if self.index >= 0:
            self._record(skipped)
        self.index += 1
        if self.index >= len(self.pairs):
            self.task = None
            self.kernel = None
            self.done = True
            return
        level, ti = self.pairs[self.index]
        self.task = task_of(level, ti)
        if self.task is None:                 # bad pair: skip it rather than die
            self.advance()
            return
        # A FRESH NAMESPACE PER TASK, seeded from the task's own live objects.
        self.kernel = Kernel(seed=dict(self.task.get("seed", {})))
        self.hints_shown = 0
        self.solved = False

    # -- playing -------------------------------------------------------------

    def submit(self, line):
        """Type one line. Returns the output it produced."""
        if self.kernel is None:
            return []
        self.kernel.submit(line)
        # Check after every line, exactly as the real game does: no check can
        # flip without a line having been executed.
        if not self.solved:
            try:
                if self.task["check"](self.kernel):
                    self.solved = True
            except Exception:
                pass          # a half-typed command may error mid-check
        return self.kernel.drain()

    def hint(self):
        """Reveal the next rung. The LAST rung is the answer -- that is the
        only place an answer is ever shown, and it costs the sharp mark."""
        hints = self.task.get("hints") or [] if self.task else []
        if self.hints_shown < len(hints):
            self.hints_shown += 1
            return hints[self.hints_shown - 1]
        return ""

    def state(self):
        if self.done or self.task is None:
            return {"done": True, "report": self.report()}
        hints = self.task.get("hints") or []
        return {
            "done": False,
            "n": self.index + 1,
            "of": len(self.pairs),
            "level": self.pairs[self.index][0],
            "instruction": str(self.task.get("instruction", "")),
            "intro": [str(x) for x in (self.task.get("intro") or [])],
            "solved": self.solved,
            "hints_available": len(hints),
            "hints_used": self.hints_shown,
            # The hints ALREADY revealed, so re-opening a panel does not lose
            # them -- but never the ones that have not been asked for.
            "hints": [str(h) for h in hints[:self.hints_shown]],
        }

    def report(self):
        solved = sum(1 for r in self.results if r["solved"])
        sharp = sum(1 for r in self.results if r["sharp"])
        return {
            "total": len(self.pairs),
            "attempted": len(self.results),
            "solved": solved,
            "sharp": sharp,
            "skipped": sum(1 for r in self.results if r["skipped"]),
            "hints_used": sum(r["hints_used"] for r in self.results),
            "tasks": self.results,
        }
