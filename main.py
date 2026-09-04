"""
main.py  --  Starship Pyxis: the game loop and the lesson flow.
==============================================================

Run the game with:   python main.py

This file is the DIRECTOR. It:
    * opens the window and runs the ~60-times-a-second game loop
    * shows the Title screen
    * runs each LEVEL through the five-step flow:
          brief -> example -> explain -> practice -> repair
    * shows the "chapter complete" screen at the end

The actual lesson CONTENT lives in the levels/ folder, not here. This file
just knows how to PRESENT any level's data. So to add Level 2 later, we write
levels/level2_oxygen.py and add it to the LEVELS list below -- nothing else.
"""

import os
import sys
import json
import math
import time
import pygame

from engine import (WIDTH, HEIGHT, FPS, COLORS, font, draw_text, draw_panel,
                    text_height, Button, Starfield, Scene)
from pyterminal import PyTerminal
import sfx                      # tiny sound-effects helper (safe if no audio)
import handoff                  # lets the 3D ship game ask us to run one level

# Import each level's data. To add a level, import it and add it to LEVELS.
from levels import (level1_power, level2_oxygen, level3_comms, level4_navigation,
                    level5_cargo, level6_engine, level7_shield, level8_charts,
                    level9_airlock, level10_sensors, level11_drones,
                    level12_lifesupport, level13_datavault, level14_beacons,
                    level15_roster, level16_fabricator, level17_modulebay,
                    level18_logic, level19_mainframe, level20_docking,
                    level21_textlab, level22_database, level23_blackbox,
                    level24_reactor, level25_hyperdrive, level26_gauntlet,
                    level27_kraken, level28_wormhole, level29_architect)

LEVELS = [
    level1_power.LEVEL,        # print() + variables
    level2_oxygen.LEVEL,       # numbers & math
    level3_comms.LEVEL,        # strings, f-strings, methods
    level4_navigation.LEVEL,   # if / elif / else
    level5_cargo.LEVEL,        # lists
    level6_engine.LEVEL,       # for loops + range
    level7_shield.LEVEL,       # while loops
    level8_charts.LEVEL,       # dictionaries
    level9_airlock.LEVEL,      # functions
    level10_sensors.LEVEL,     # functions: params, defaults, logic
    level11_drones.LEVEL,      # classes & objects
    level12_lifesupport.LEVEL, # try / except
    level13_datavault.LEVEL,   # combining loops + logic
    level14_beacons.LEVEL,     # tuples
    level15_roster.LEVEL,      # sets
    level16_fabricator.LEVEL,  # list comprehensions
    level17_modulebay.LEVEL,   # importing modules
    level18_logic.LEVEL,       # boolean logic (and/or/not)
    level19_mainframe.LEVEL,   # nested data (lists of dicts)
    level20_docking.LEVEL,     # enumerate() + zip()
    level21_textlab.LEVEL,     # string slicing + methods
    level22_database.LEVEL,    # looping dictionaries
    level23_blackbox.LEVEL,    # reading + writing files
    level24_reactor.LEVEL,     # loop else (while/else, for/else)
    level25_hyperdrive.LEVEL,  # recursion
    level26_gauntlet.LEVEL,    # BOSS: combine everything
    level27_kraken.LEVEL,      # FINAL BOSS: classes + everything
    level28_wormhole.LEVEL,    # capstone (last of the main campaign)
    level29_architect.LEVEL,   # SECRET boss (post-game, hidden until you win)
]

# Adjustable settings (changed on the Settings screen, saved to disk).
# type_speed = characters/second for PYX's typewriter.
CONFIG = {"type_speed": 48}
TYPE_SPEEDS = [22, 48, 110]            # Slow / Normal / Fast  (Settings cycles these)
MUSIC_LEVELS = [0.0, 0.15, 0.35, 0.6]  # Off / Low / Medium / High


def main_count():
    """How many levels are in the normal campaign (everything not secret)."""
    return sum(1 for lvl in LEVELS if not lvl.get("secret"))


# ---------------------------------------------------------------------------
# HANDOFF MODE  (only ever switched on by the 3D ship game)
# ---------------------------------------------------------------------------
# Normally both of these stay exactly as they are below and the game behaves
# the way it always has. They only change when we were started with
# "--level N" on the command line -- see the bottom of this file.
#
#   REQUEST      what the ship asked for, or None for a normal double-click.
#   SAVE_LOCKED  True means "do not touch progress.json". The ship is borrowing
#                the game to run one level; the cadet's own campaign save must
#                come out of that completely untouched.
REQUEST = None
SAVE_LOCKED = False


# ---------------------------------------------------------------------------
# SAVING YOUR PROGRESS
# ---------------------------------------------------------------------------
# We remember the highest level you've unlocked in a tiny file next to this one
# (progress.json). "unlocked" is a number: how many levels you've finished, which
# is also the index of the next level you can start. 0 = only Level 1 is open.
SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "progress.json")

def load_state():
    """Read the saved progress + settings dict. Returns {} if there's no save."""
    try:
        with open(SAVE_PATH) as f:
            return json.load(f)
    except Exception:
        return {}           # no save file (or unreadable) -> defaults

def save_game(game):
    """Write progress AND settings to disk. getattr keeps tests/headless safe.

    'unlocked' = how many levels are finished (gating + progress count).
    'level'/'task' = the EXACT spot to resume -- the level you're on and which
    practice task -- so closing mid-level still continues right where you were.

    In handoff mode this does nothing at all: the 3D ship keeps its own save,
    and a level played from the ship must never move the cadet's own bookmark.
    """
    if SAVE_LOCKED:
        return
    try:
        with open(SAVE_PATH, "w") as f:
            json.dump({
                "unlocked": getattr(game, "unlocked", 0),
                "level": getattr(game, "resume_level", 0),
                "task": getattr(game, "resume_task", 0),
                "music": getattr(game, "music_idx", 2),
                "fx": getattr(game, "fx_on", True),
                "type": getattr(game, "type_idx", 1),
            }, f)
    except Exception:
        pass                # if we can't save, the game still plays fine

def apply_settings(game):
    """Push the game's current settings into CONFIG and the audio system."""
    CONFIG["type_speed"] = TYPE_SPEEDS[getattr(game, "type_idx", 1)]
    sfx.set_music_volume(MUSIC_LEVELS[getattr(game, "music_idx", 2)])
    sfx.set_fx(getattr(game, "fx_on", True))


# ---------------------------------------------------------------------------
# A shared header bar, used by every screen so they look consistent.
# ---------------------------------------------------------------------------
def draw_header(surface, title, subtitle=""):
    draw_panel(surface, pygame.Rect(0, 0, WIDTH, 72), fill="panel", border=None)
    pygame.draw.line(surface, COLORS["cyan"], (0, 72), (WIDTH, 72), 2)
    draw_text(surface, title, 24, 16, size=30, color="cyan")
    if subtitle:
        draw_text(surface, subtitle, 24, 48, size=18, color="gray")


# ===========================================================================
#  TITLE SCREEN
# ===========================================================================
class TitleScene(Scene):
    def __init__(self, game):
        super().__init__(game)   # run Scene.__init__ to set up self.game etc.
        # How far has the player gotten? This decides which buttons we show.
        self.unlocked = game.unlocked
        # Where to resume: the exact level + task they left off on.
        self.resume_level = getattr(game, "resume_level", 0)
        self.resume_task = getattr(game, "resume_task", 0)
        started = (self.unlocked > 0 or self.resume_level > 0
                   or self.resume_task > 0)   # have they played before?
        # The main button: "Continue (Level N)" if they have progress, else start.
        label = (f"Continue  (Level {self.resume_level + 1})" if started
                 else "Begin Mission")
        self.begin = Button(WIDTH // 2 - 130, 364, 260, 52, label)
        self.select = Button(WIDTH // 2 - 130, 424, 260, 44, "Level Select")
        self.settings = Button(WIDTH // 2 - 130, 476, 260, 44, "Settings")
        # New Game only matters once there's progress to reset.
        self.newgame = (Button(WIDTH // 2 - 130, 528, 260, 42, "New Game", color="gray")
                        if started else None)
        self.quit = Button(WIDTH // 2 - 130, 528 + (52 if started else 0), 260, 42,
                           "Quit", color="gray")

    def handle_event(self, event):
        if self.begin.handle_event(event):
            # Resume at the EXACT level + task we saved (capture before creating
            # the scene, since LevelScene.__init__ resets the saved task to 0).
            i = min(self.resume_level, len(LEVELS) - 1)
            t = min(self.resume_task, len(LEVELS[i]["practice"]) - 1)
            sc = LevelScene(self.game, LEVELS[i], i)
            if t > 0:                        # were we mid-level? jump to that task
                sc.set_phase("practice")
                sc._load_task(t)
            self.next_scene = sc
        if self.select.handle_event(event):
            self.next_scene = LevelSelectScene(self.game)
        if self.newgame and self.newgame.handle_event(event):
            self.game.unlocked = 0           # wipe progress and start over
            self.game.resume_level = 0
            self.game.resume_task = 0
            save_game(self.game)
            self.next_scene = LevelScene(self.game, LEVELS[0], 0)
        if self.settings.handle_event(event):
            self.next_scene = SettingsScene(self.game)
        if self.quit.handle_event(event):
            self.next_scene = "quit"

    def draw(self, surface):
        draw_text(surface, "STARSHIP  PYXIS", WIDTH // 2, 150, size=64,
                  color="cyan", center=True)
        draw_text(surface, "Learn Python. Repair the ship. Get home.",
                  WIDTH // 2, 232, size=24, color="star", center=True)
        draw_text(surface, "A 20-level coding adventure for brand-new programmers",
                  WIDTH // 2, 272, size=18, color="gray", center=True)
        if self.unlocked > 0:
            done = min(self.unlocked, len(LEVELS))
            draw_text(surface, f"Progress: {done} / {len(LEVELS)} systems online",
                      WIDTH // 2, 332, size=18, color="green", center=True)
        self.begin.draw(surface)
        self.select.draw(surface)
        self.settings.draw(surface)
        if self.newgame:
            self.newgame.draw(surface)
        self.quit.draw(surface)
        draw_text(surface, "ESC = menu (or quit).    F11 = fullscreen.    "
                           "M = mute.", WIDTH // 2, 642, size=16,
                  color="gray", center=True)
        draw_text(surface, "In long messages, scroll with the mouse wheel or "
                           "arrow keys.", WIDTH // 2, 666, size=15,
                  color="gray", center=True)


# ===========================================================================
#  LEVEL SELECT  --  a map of all systems; replay any you've unlocked
# ===========================================================================
class LevelSelectScene(Scene):
    """A grid of every level. Unlocked ones are clickable; locked ones are grey.

    You unlock the next level by finishing the current one. This screen lets you
    replay anything you've reached -- handy for practising a tricky concept.
    """

    def __init__(self, game):
        super().__init__(game)
        self.buttons = []           # list of (Button, level_index)
        cols, x0, y0, gap_x, gap_y, bw, bh = 3, 40, 92, 14, 10, 304, 44
        for i, lvl in enumerate(LEVELS):
            x = x0 + (i % cols) * (bw + gap_x)
            y = y0 + (i // cols) * (bh + gap_y)
            unlocked = i <= game.unlocked        # finished-or-next levels are open
            if lvl.get("secret"):
                # A secret level stays "classified" until you've beaten the game.
                label = (f"{lvl['number']}.  {lvl['system']}" if unlocked
                         else "29.  ? ? ?   CLASSIFIED")
                color = "purple" if unlocked else "gray"
            elif unlocked:
                label, color = f"{lvl['number']}.  {lvl['system']}", "cyan"
            else:
                label, color = f"{lvl['number']}.  LOCKED", "gray"
            b = Button(x, y, bw, bh, label, color=color)
            b.enabled = unlocked
            self.buttons.append((b, i))
        self.back = Button(WIDTH // 2 - 90, 648, 180, 42, "Back", color="gray")

    def handle_event(self, event):
        for b, i in self.buttons:
            if b.handle_event(event):
                self.next_scene = LevelScene(self.game, LEVELS[i], i)
        if self.back.handle_event(event):
            self.next_scene = TitleScene(self.game)

    def draw(self, surface):
        draw_header(surface, "SELECT A SYSTEM",
                    f"{min(self.game.unlocked, len(LEVELS))} of {len(LEVELS)} unlocked "
                    f"-- click any unlocked system to play or replay it")
        for b, i in self.buttons:
            b.draw(surface)
        self.back.draw(surface)


# ===========================================================================
#  SETTINGS  --  music volume, sound effects, text speed (all saved)
# ===========================================================================
class SettingsScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        x = WIDTH // 2 - 150
        self.music = Button(x, 190, 300, 52, "")
        self.fx = Button(x, 270, 300, 52, "")
        self.text = Button(x, 350, 300, 52, "")
        self.back = Button(WIDTH // 2 - 90, 470, 180, 46, "Back", color="gray")
        self._refresh()

    def _refresh(self):
        vol = ["Off", "Low", "Medium", "High"][self.game.music_idx]
        spd = ["Slow", "Normal", "Fast"][self.game.type_idx]
        self.music.label = f"Music:  {vol}"
        self.fx.label = f"Sound FX:  {'On' if self.game.fx_on else 'Off'}"
        self.text.label = f"Text speed:  {spd}"

    def handle_event(self, event):
        changed = False
        if self.music.handle_event(event):
            self.game.music_idx = (self.game.music_idx + 1) % len(MUSIC_LEVELS)
            changed = True
        if self.fx.handle_event(event):
            self.game.fx_on = not self.game.fx_on
            changed = True
        if self.text.handle_event(event):
            self.game.type_idx = (self.game.type_idx + 1) % len(TYPE_SPEEDS)
            changed = True
        if changed:
            apply_settings(self.game)       # apply live
            save_game(self.game)            # and remember it
            self._refresh()
            sfx.play("blip")                # tiny audible confirmation
        if self.back.handle_event(event):
            self.next_scene = TitleScene(self.game)

    def draw(self, surface):
        draw_header(surface, "SETTINGS",
                    "click an option to change it -- saved automatically")
        draw_text(surface, "M = mute (except while typing code).    "
                           "F11 = fullscreen.", WIDTH // 2, 140, size=17,
                  color="gray", center=True)
        self.music.draw(surface)
        self.fx.draw(surface)
        self.text.draw(surface)
        self.back.draw(surface)


# ===========================================================================
#  THE LEVEL SCREEN  --  runs one level through all five steps
# ===========================================================================
class LevelScene(Scene):
    """One level, shown as a little state machine.

    self.phase is one of: "brief", "example", "explain", "practice", "repair".
    A "Continue" button walks you forward through the phases. The practice
    phase is special: it holds the typing terminal and the hint ladder.
    """

    def __init__(self, game, level, index):
        super().__init__(game)
        self.level = level          # the LEVEL dict from the level file
        self.index = index          # which level number we are (0-based)
        # Remember -- immediately -- that this is where the player now is, so
        # closing the game on this level resumes here next time.
        self.game.resume_level = index
        self.game.resume_task = 0
        save_game(self.game)

        # One reusable Continue button, bottom-right.
        self.cont = Button(WIDTH - 208, 628, 184, 48, "Continue")

        # State used by the practice phase:
        self.task_i = 0             # which practice task we're on
        self.terminal = None        # the PyTerminal (built when practice starts)
        self.hints_shown = 0        # how many hint-ladder steps are revealed
        self.solved = False         # has the current task been solved?
        self.hint_btn = Button(672, 232, 304, 44, "I'm stuck (show a hint)",
                               color="amber")
        # Wipe the code box back to a clean slate for the current task.
        self.reset_btn = Button(24, 620, 168, 34, "Reset code", color="amber")

        # State used by the explain phase:
        self.explain_i = 0          # which explain card we're showing

        # State for PYX's typewriter animation (used in brief + repair).
        self.type_t = 0.0           # seconds elapsed since the text started
        self.type_done = False      # has the whole message finished typing?
        self._typed_count = 0       # how many characters are visible right now
        self.anim_t = 0.0           # a free-running clock for PYX's blinking
        self.scroll = 0             # pixels scrolled down in long text panels

        # Scorekeeping for the 3D ship. These four tick along quietly during
        # normal play too -- nothing reads them unless we're in handoff mode.
        self.resets = 0             # times "Reset code" was pressed
        self.hints_used = 0         # hint rungs revealed across the whole level
        self.full_answers = 0       # tasks where the LAST rung (the answer) showed
        self.started_at = time.monotonic()   # a stopwatch for this session
        self.reported = False       # have we already answered the ship?

        self.set_phase("brief")

    def report(self, cleared):
        """Tell the 3D ship how this session went. Does nothing in normal play.

        Only ever answers ONCE per session: whoever gets here first wins, so a
        finished level can't later be overwritten by the window closing.
        """
        if REQUEST is None or self.reported:
            return
        self.reported = True
        # How many hint rungs this level offers in total. Boss levels have NO
        # hints at all, so this is 0 for them -- which is how the ship knows not
        # to grade a boss as "used no hints, therefore easy".
        hints_available = sum(len(t.get("hints") or [])
                              for t in self.level["practice"])
        handoff.write_report(REQUEST["report"], {
            "session": REQUEST["session"],
            "level": self.index + 1,          # 1-based, matching --level
            "cleared": bool(cleared),
            "tasks": len(self.level["practice"]),
            "hints_used": self.hints_used,
            "hints_available": hints_available,
            "full_answer_reveals": self.full_answers,
            "resets": self.resets,
            "duration": round(time.monotonic() - self.started_at, 1),
        })

    # -- switch to a new phase and prepare anything it needs ----------------
    def set_phase(self, phase):
        self.phase = phase
        self.scroll = 0             # start each screen scrolled to the top
        if phase == "practice":
            self._load_task(0)
        if phase in ("brief", "repair"):
            # Restart PYX's typewriter for this dialogue.
            self.type_t = 0.0
            self.type_done = False
            self._typed_count = 0
            if phase == "repair":
                sfx.play("online")          # the "system online" jingle

    def _dialogue_text(self):
        """The full text PYX is currently 'speaking' (brief or repair), joined."""
        lines = self.level["brief"] if self.phase == "brief" else self.level["repair"]
        return "\n".join(lines)

    def _scrolled_text(self, surface, text, rect, size, color, line_gap,
                       auto_bottom=False):
        """Draw `text` inside `rect`, clipped, offset by self.scroll so the
        player can scroll long passages. Shows a hint when there's more to see.
        `auto_bottom` keeps the view pinned to the newest text while typing."""
        height = text_height(text, size=size, max_width=rect.width, line_gap=line_gap)
        max_scroll = max(0, height - rect.height)
        if auto_bottom:
            self.scroll = max_scroll                 # follow the typewriter down
        self.scroll = max(0, min(self.scroll, max_scroll))   # clamp
        old_clip = surface.get_clip()
        surface.set_clip(rect)                       # don't spill past the panel
        draw_text(surface, text, rect.x, rect.y - self.scroll, size=size,
                  color=color, max_width=rect.width, line_gap=line_gap)
        surface.set_clip(old_clip)
        # Little hints so the player knows scrolling is possible.
        if self.scroll > 0:
            draw_text(surface, "^ scroll up", rect.right - 8, rect.y - 20,
                      size=14, color="amber")
        if self.scroll < max_scroll:
            draw_text(surface, "more below -- scroll down (mouse wheel / arrows) v",
                      rect.centerx, rect.bottom + 4, size=14, color="amber",
                      center=True)
        return max_scroll

    def _scroll_event(self, event):
        """Mouse wheel and Up/Down/PageUp/PageDown scroll the long-text panels."""
        if event.type == pygame.MOUSEWHEEL:
            self.scroll -= event.y * 40              # wheel up = view up
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_PAGEDOWN):
                self.scroll += 50
            elif event.key in (pygame.K_UP, pygame.K_PAGEUP):
                self.scroll -= 50
        self.scroll = max(0, self.scroll)            # (upper clamp happens in draw)

    def _draw_pyx_avatar(self, surface, x, y, size, talking):
        """Draw PYX as a little AI face that blinks, and 'talks' while typing."""
        box = pygame.Rect(x, y, size, size)
        draw_panel(surface, box, fill=(6, 10, 22), border="cyan", radius=14)
        cx = x + size // 2
        # A little antenna on top.
        pygame.draw.line(surface, COLORS["cyan"], (cx, y), (cx, y - 10), 2)
        pygame.draw.circle(surface, COLORS["cyan"], (cx, y - 12), 3)
        # Eyes -- they blink shut briefly every few seconds.
        blinking = (self.anim_t % 3.2) < 0.12
        eye_y = y + int(size * 0.34)
        ew, eh = int(size * 0.12), int(size * 0.17)
        for ex in (x + int(size * 0.24), x + int(size * 0.64)):
            if blinking:
                pygame.draw.line(surface, COLORS["cyan"],
                                 (ex, eye_y + eh // 2), (ex + ew, eye_y + eh // 2), 3)
            else:
                pygame.draw.rect(surface, COLORS["cyan"],
                                 pygame.Rect(ex, eye_y, ew, eh), border_radius=3)
        # Mouth -- an equalizer that wiggles while PYX is speaking, else a line.
        mx, my = x + int(size * 0.27), y + int(size * 0.74)
        if talking:
            for k in range(5):
                h = 4 + int(8 * (0.5 + 0.5 * math.sin(self.anim_t * 12 + k)))
                pygame.draw.rect(surface, COLORS["green"],
                                 pygame.Rect(mx + k * 8, my - h // 2, 4, h),
                                 border_radius=2)
        else:
            pygame.draw.line(surface, COLORS["gray"], (mx, my), (mx + 36, my), 2)

    # -- build a fresh terminal for practice task number i ------------------
    def _load_task(self, i):
        self.task_i = i
        task = self.level["practice"][i]
        rect = pygame.Rect(24, 184, 632, 430)
        # Each task gets its own clean terminal, pre-loaded with its seed data.
        self.terminal = PyTerminal(rect, seed=dict(task.get("seed", {})),
                                   intro=task.get("intro"))
        self.hints_shown = 0
        self.solved = False
        self.hint_btn.enabled = True
        self.hint_btn.label = "I'm stuck (show a hint)"
        # Remember which task we're on, so we resume right here next time.
        self.game.resume_level = self.index
        self.game.resume_task = i
        save_game(self.game)

    def _reset_terminal(self):
        """Wipe the code box back to a clean slate for the CURRENT task --
        clears the scrollback, any half-typed line, and all the variables you
        made -- but keeps any hints you've already revealed."""
        task = self.level["practice"][self.task_i]
        rect = pygame.Rect(24, 184, 632, 430)
        self.terminal = PyTerminal(rect, seed=dict(task.get("seed", {})),
                                   intro=task.get("intro"))
        self.resets += 1            # the ship counts these (cosmetic only)
        sfx.play("blip")

    # ----------------------------------------------------------------- input
    def handle_event(self, event):
        if self.phase == "practice":
            self._practice_event(event)
        else:
            self._scroll_event(event)       # let long passages scroll
            self._linear_event(event)

    def typing_in_terminal(self):
        """True while you're typing code, so letter keys (like 'm') aren't
        stolen by global shortcuts such as the M mute toggle."""
        return self.phase == "practice" and not self.solved

    def _linear_event(self, event):
        # brief / example / explain / repair all just wait for "Continue".
        if self.cont.handle_event(event):
            # If PYX is still typing, the first click just reveals it all.
            if self.phase in ("brief", "repair") and not self.type_done:
                self.type_done = True
                return
            if self.phase == "brief":
                self.set_phase("example")
            elif self.phase == "example":
                self.explain_i = 0
                self.set_phase("explain")
            elif self.phase == "explain":
                # Step through the explain cards one at a time.
                if self.explain_i < len(self.level["explain"]) - 1:
                    self.explain_i += 1
                    self.scroll = 0          # new card -> back to the top
                else:
                    self.set_phase("practice")
            elif self.phase == "repair":
                self._go_next_level()

    def _practice_event(self, event):
        task = self.level["practice"][self.task_i]
        if not self.solved:
            # Let the player type into the terminal.
            self.terminal.handle_event(event)
            # After every keystroke, ask the task's check() if it's solved now.
            try:
                if task["check"](self.terminal):
                    self.solved = True
                    sfx.play("solved")          # happy chime on success
            except Exception:
                pass    # a half-typed command may error mid-check; ignore it
            # The hint button reveals the next rung of the hint ladder.
            # (Boss levels have NO hints, so we skip this entirely.)
            if task.get("hints") and self.hint_btn.handle_event(event):
                if self.hints_shown < len(task["hints"]):
                    self.hints_shown += 1
                    self.hints_used += 1        # hints are FREE -- just counted
                if self.hints_shown >= len(task["hints"]):
                    if self.hint_btn.enabled:
                        # The last rung IS the answer, so note it once per task.
                        # (A boss task has no hints, so it can never land here.)
                        self.full_answers += 1
                    self.hint_btn.enabled = False
                    self.hint_btn.label = "(that's the full answer)"
            # "Reset code" wipes the box clean if your attempts got messy.
            if self.reset_btn.handle_event(event):
                self._reset_terminal()
        else:
            # Solved! The Continue button moves to the next task or to repair.
            if self.cont.handle_event(event):
                if self.task_i < len(self.level["practice"]) - 1:
                    self._load_task(self.task_i + 1)
                else:
                    self.set_phase("repair")

    def _go_next_level(self):
        # HANDOFF MODE: the ship asked for THIS level only. Report the good news
        # and close, so the 3D game gets control back instead of us rolling on
        # into the next level.
        if REQUEST is not None:
            self.report(cleared=True)
            self.next_scene = "quit"
            return
        # Finishing this level unlocks the next one. Remember it on disk.
        self.game.unlocked = max(self.game.unlocked, self.index + 1)
        save_game(self.game)
        nxt = self.index + 1
        # The campaign ends before any SECRET level -> go to the finale screen.
        # (Secret levels are reached from the victory screen / Level Select.)
        if nxt < len(LEVELS) and not LEVELS[nxt].get("secret"):
            self.next_scene = LevelScene(self.game, LEVELS[nxt], nxt)
        else:
            self.next_scene = CompleteScene(self.game)

    # ---------------------------------------------------------------- update
    def update(self, dt):
        self.anim_t += dt           # keeps PYX's eyes blinking on a steady beat
        if self.terminal:
            self.terminal.update(dt)
        # Advance PYX's typewriter during brief/repair, ticking a soft blip.
        if self.phase in ("brief", "repair") and not self.type_done:
            self.type_t += dt
            shown = int(self.type_t * CONFIG["type_speed"])
            full = len(self._dialogue_text())
            if shown >= full:
                self.type_done = True
                shown = full
            elif shown // 3 != self._typed_count // 3:
                sfx.play("blip", 0.45)          # a tick every few characters
            self._typed_count = min(shown, full)

    # ------------------------------------------------------------------ draw
    def draw(self, surface):
        title = f"LEVEL {self.level['number']}:  {self.level['system']}"
        draw_header(surface, title, self.level["concept"])
        self._draw_progress(surface)
        if self.phase == "brief":
            self._draw_brief(surface)
        elif self.phase == "example":
            self._draw_example(surface)
        elif self.phase == "explain":
            self._draw_explain(surface)
        elif self.phase == "practice":
            self._draw_practice(surface)
        elif self.phase == "repair":
            self._draw_repair(surface)

    def _draw_progress(self, surface):
        # A small "how far am I" readout on the right of the header bar.
        n, tot = self.level["number"], len(LEVELS)
        draw_text(surface, f"SYSTEM {n} / {tot}", WIDTH - 190, 14, size=17,
                  color="gray")
        track = pygame.Rect(WIDTH - 190, 44, 166, 9)
        pygame.draw.rect(surface, COLORS["panel2"], track, border_radius=4)
        fill = pygame.Rect(WIDTH - 190, 44, max(4, int(166 * n / tot)), 9)
        pygame.draw.rect(surface, COLORS["green"], fill, border_radius=4)

    def _draw_brief(self, surface):
        panel = pygame.Rect(24, 96, WIDTH - 48, 480)
        draw_panel(surface, panel, border="cyan")
        draw_text(surface, "PYX  //  incoming transmission", 44, 116,
                  size=20, color="cyan")
        self._draw_pyx_avatar(surface, WIDTH - 138, 120, 88,
                              talking=not self.type_done)
        # PYX's words type out one character at a time (with a blinking cursor),
        # and scroll if the message is taller than the panel.
        full = self._dialogue_text()
        shown = full if self.type_done else full[:self._typed_count] + "_"
        text_rect = pygame.Rect(44, 156, WIDTH - 210, 410)
        self._scrolled_text(surface, shown if shown else " ", text_rect, 22,
                            "star", 8, auto_bottom=not self.type_done)
        self.cont.label = "Continue" if self.type_done else "Skip"
        self.cont.draw(surface)

    def _draw_example(self, surface):
        draw_text(surface, "Watch first -- here's working code:", 24, 92,
                  size=22, color="amber")
        # The code box.
        box = pygame.Rect(24, 130, WIDTH - 48, 200)
        draw_panel(surface, box, fill=(4, 6, 14), border="cyan")
        y = 156
        for line in self.level["example"]["code"].split("\n"):
            draw_text(surface, ">>> " + line, 48, y, size=26, color="code")
            y += 40
        # The caption underneath.
        cap = pygame.Rect(24, 350, WIDTH - 48, 200)
        draw_panel(surface, cap, fill="panel", border=None)
        draw_text(surface, self.level["example"]["caption"], 44, 372, size=22,
                  color="star", max_width=WIDTH - 90, line_gap=8)
        draw_text(surface, "Don't memorize it -- I'll explain every piece next.",
                  44, 470, size=18, color="gray")
        self.cont.draw(surface)

    def _draw_explain(self, surface):
        cards = self.level["explain"]
        card = cards[self.explain_i]
        draw_text(surface, f"How it works  --  piece {self.explain_i + 1} "
                           f"of {len(cards)}", 24, 92, size=22, color="amber")
        # The code fragment in its own box -- sized to the snippet so multi-line
        # examples fit (and clipped if it is unusually tall).
        code = card["code"]
        nlines = code.count("\n") + 1
        box = pygame.Rect(24, 122, WIDTH - 48, min(36 + nlines * 28, 200))
        draw_panel(surface, box, fill=(4, 6, 14), border="cyan")
        old_clip = surface.get_clip()
        surface.set_clip(box)
        draw_text(surface, code, 44, box.y + 14, size=22, color="code", line_gap=6)
        surface.set_clip(old_clip)
        # The explanation below, scrollable if it runs long.
        note_top = box.bottom + 14
        note = pygame.Rect(24, note_top, WIDTH - 48, 574 - note_top)
        draw_panel(surface, note, fill="panel", border=None)
        text_rect = pygame.Rect(44, note_top + 18, WIDTH - 90, note.height - 34)
        self._scrolled_text(surface, card["note"], text_rect, 22, "star", 8)
        # Change the button label on the last card.
        self.cont.label = ("Start practising" if self.explain_i == len(cards) - 1
                           else "Continue")
        self.cont.draw(surface)

    def _draw_practice(self, surface):
        task = self.level["practice"][self.task_i]
        total = len(self.level["practice"])
        is_boss = self.level.get("boss")
        # Instruction panel along the top (red trim for boss challenges).
        instr = pygame.Rect(24, 84, WIDTH - 48, 90)
        draw_panel(surface, instr, border=("red" if is_boss else "amber"))
        draw_text(surface, f"TASK {self.task_i + 1} of {total}", 40, 92,
                  size=16, color=("red" if is_boss else "amber"))
        if is_boss:
            draw_text(surface, "BOSS CHALLENGE -- NO HINTS", WIDTH - 320, 92,
                      size=16, color="red")
        draw_text(surface, task["instruction"], 40, 112, size=21, color="star",
                  max_width=WIDTH - 90, line_gap=6)

        # The terminal (left), with a "Reset code" button while you're working.
        self.terminal.draw(surface)
        if not self.solved:
            self.reset_btn.draw(surface)
        draw_text(surface, "Enter runs.  Up/Down = history.  Tab = indent.",
                  204, 628, size=15, color="gray")

        # The right-hand column: hints (or the boss "no hints" note), or success.
        if not self.solved:
            if task.get("hints"):
                self.hint_btn.draw(surface)
                hpanel = pygame.Rect(672, 288, 304, 326)
                draw_panel(surface, hpanel, fill="panel", border=None)
                if self.hints_shown == 0:
                    draw_text(surface, "Stuck? Press the button above for a nudge. "
                                       "Each press reveals a little more.", 688, 306,
                              size=17, color="gray", max_width=272, line_gap=6)
                else:
                    y = 304
                    for h in range(self.hints_shown):
                        last = (h == self.hints_shown - 1
                                and self.hints_shown == len(task["hints"]))
                        color = "green" if last else "amber"
                        y = draw_text(surface, f"{h + 1}. {task['hints'][h]}",
                                      688, y, size=18, color=color,
                                      max_width=272, line_gap=6)
                        y += 10
            else:
                # Boss challenge: no hint ladder, just a steady word of confidence.
                bpanel = pygame.Rect(672, 232, 304, 382)
                draw_panel(surface, bpanel, border="red")
                draw_text(surface, "BOSS CHALLENGE", 688, 252, size=22, color="red")
                draw_text(surface, "No hints this time, Cadet.\n\nRead the function "
                                   "name and the example, then write it.\n\nYou have "
                                   "every tool you need. Go.", 688, 296, size=18,
                          color="star", max_width=272, line_gap=8)
        else:
            spanel = pygame.Rect(672, 232, 304, 382)
            draw_panel(surface, spanel, border="green")
            draw_text(surface, "SOLVED!", 688, 252, size=24, color="green")
            draw_text(surface, task["success"], 688, 292, size=19, color="star",
                      max_width=272, line_gap=8)
            self.cont.label = ("Next task" if self.task_i < total - 1
                               else "Restore the system")
            self.cont.draw(surface)

    def _draw_repair(self, surface):
        panel = pygame.Rect(24, 96, WIDTH - 48, 356)
        draw_panel(surface, panel, border="green")
        draw_text(surface, f"{self.level['system']}: ONLINE", 44, 116,
                  size=26, color="green")
        self._draw_pyx_avatar(surface, WIDTH - 138, 110, 80,
                              talking=not self.type_done)
        # PYX's debrief types out, same as the brief -- and scrolls if long.
        full = self._dialogue_text()
        shown = full if self.type_done else full[:self._typed_count] + "_"
        text_rect = pygame.Rect(44, 158, WIDTH - 210, 286)
        self._scrolled_text(surface, shown if shown else " ", text_rect, 22,
                            "star", 8, auto_bottom=not self.type_done)
        # The ship-systems map lights up another block.
        self._draw_system_map(surface, pygame.Rect(24, 470, WIDTH - 48, 152))
        self.cont.label = "Continue" if self.type_done else "Skip"
        self.cont.draw(surface)

    def _draw_system_map(self, surface, rect):
        """A row of little blocks -- one per level -- that light up as you go."""
        draw_panel(surface, rect, fill="panel", border=None)
        n = len(LEVELS)
        online = self.level["number"]          # systems online = up to here
        draw_text(surface, f"SHIP SYSTEMS ONLINE:  {online} / {n}",
                  rect.x + 16, rect.y + 12, size=18, color="green")
        cell = 22
        step = (rect.width - 32) / n
        cy = rect.y + 50
        for i, lvl in enumerate(LEVELS):
            cx = int(rect.x + 16 + i * step)
            cellrect = pygame.Rect(cx, cy, cell, cell)
            num = lvl["number"]
            if num < online:
                color = COLORS["green"]                  # already online
            elif num == online:
                color = COLORS["cyan"]                   # the one you just fixed
            else:
                color = COLORS["panel2"]                 # still offline
            pygame.draw.rect(surface, color, cellrect, border_radius=4)
            if lvl.get("boss"):                          # mark bosses in red
                pygame.draw.rect(surface, COLORS["red"], cellrect, width=2,
                                 border_radius=4)
        draw_text(surface, "Each block is a system you've brought back online.",
                  rect.x + 16, cy + cell + 12, size=15, color="gray")


# ===========================================================================
#  CHAPTER COMPLETE  (shown after the last built level)
# ===========================================================================
class CompleteScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        secret_idx = len(LEVELS) - 1                 # the secret level's index
        self.secret_done = game.unlocked > secret_idx
        # If the campaign is beaten but the secret boss isn't, tease it.
        self.secret_btn = None
        if game.unlocked >= secret_idx and not self.secret_done:
            self.secret_btn = Button(WIDTH // 2 - 170, 436, 340, 50,
                                     "??? ANSWER THE SIGNAL", color="purple")
        row_y = 506 if self.secret_btn else 470
        self.select = Button(WIDTH // 2 - 230, row_y, 220, 50, "Level Select")
        self.menu = Button(WIDTH // 2 + 10, row_y, 220, 50, "Back to title")

    def handle_event(self, event):
        if self.secret_btn and self.secret_btn.handle_event(event):
            i = len(LEVELS) - 1
            self.next_scene = LevelScene(self.game, LEVELS[i], i)
        if self.select.handle_event(event):
            self.next_scene = LevelSelectScene(self.game)
        if self.menu.handle_event(event):
            self.next_scene = TitleScene(self.game)

    def draw(self, surface):
        title = "TRUE ENDING" if self.secret_done else "YOU MADE IT HOME"
        draw_text(surface, title, WIDTH // 2, 150, size=52,
                  color="green", center=True)
        draw_text(surface, "Every system restored. The Pyxis is whole again --",
                  WIDTH // 2, 232, size=22, color="star", center=True)
        draw_text(surface, "and you wrote real Python to do it.",
                  WIDTH // 2, 264, size=22, color="star", center=True)
        draw_text(surface, "You now know: print & variables, math, strings, if/else, "
                           "lists, loops, dictionaries, functions, classes, error "
                           "handling, tuples, sets, comprehensions, modules, logic, "
                           "nested data, enumerate/zip, slicing, and reading & "
                           "writing files.", WIDTH // 2, 312,
                  size=18, color="gray", center=True, max_width=880)
        draw_text(surface, "That's the real foundation of programming. You're a "
                           "Python programmer now, Cadet.", WIDTH // 2, 392,
                  size=20, color="cyan", center=True, max_width=820)
        if self.secret_done:
            draw_text(surface, "You answered the Architect. Nothing remains unsolved.",
                      WIDTH // 2, 430, size=19, color="purple", center=True)
        elif self.secret_btn:
            draw_text(surface, "...but a strange signal pulses from deep space.",
                      WIDTH // 2, 414, size=18, color="purple", center=True)
            self.secret_btn.draw(surface)
        self.select.draw(surface)
        self.menu.draw(surface)


# ===========================================================================
#  THE GAME OBJECT + MAIN LOOP
# ===========================================================================
class Game:
    def __init__(self):
        pygame.init()
        sfx.init()                        # start audio (silently no-ops if none)
        # SCALED lets the fixed 1000x700 game scale cleanly to any window or
        # fullscreen size. Fall back to a plain window if SCALED isn't available.
        try:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
        except Exception:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fullscreen = False
        pygame.display.set_caption("Starship Pyxis -- Learn Python")
        self.clock = pygame.time.Clock()
        self.stars = Starfield()
        # Load progress + settings from disk (with sensible defaults).
        st = load_state()
        self.unlocked = max(0, min(len(LEVELS), int(st.get("unlocked", 0))))
        # The exact resume spot: which level, and which task within it. For OLD
        # saves that only stored "unlocked", default the resume level to that
        # (the furthest reached) so upgrading never bumps anyone back to Level 1.
        self.resume_level = max(0, min(len(LEVELS) - 1,
                                       int(st.get("level", self.unlocked))))
        self.resume_task = max(0, int(st.get("task", 0)))
        self.music_idx = int(st.get("music", 2))   # 0..3 (Off/Low/Med/High)
        self.fx_on = bool(st.get("fx", True))       # sound effects on/off
        self.type_idx = int(st.get("type", 1))      # 0..2 (Slow/Normal/Fast)
        apply_settings(self)
        # In handoff mode, ESC asks "leave session?" first. This is that question
        # being on screen. It stays False for the whole of normal play.
        self.confirm_quit = False
        self.scene = TitleScene(self)     # the first screen

    def handoff_bail(self):
        """Leaving early: tell the ship the system was NOT certified.

        Called when the window is closed or the cadet answers Y to the "leave
        session?" question. If the level was already finished, `report` has
        happened once already and quietly ignores us.
        """
        reporter = getattr(self.scene, "report", None)
        if REQUEST is not None and callable(reporter):
            reporter(cleared=False)

    def toggle_fullscreen(self):
        """Switch between a window and fullscreen (the game scales to fit)."""
        try:
            pygame.display.toggle_fullscreen()
            self.fullscreen = not self.fullscreen
        except Exception:
            pass                          # some setups can't -- just stay windowed

    def run(self):
        running = True
        while running:
            # dt = seconds since the last frame (clock.tick caps us at FPS).
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                # While the "leave session?" question is up it owns the keyboard,
                # so a stray keypress can't reach the code terminal behind it.
                if self.confirm_quit and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.handoff_bail()
                        running = False
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        self.confirm_quit = False
                    continue

                if event.type == pygame.QUIT:
                    self.handoff_bail()     # closing the window = not certified
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # In handoff mode the ship is waiting on us, and the title
                    # screen isn't ours to go to -- so ESC asks first instead.
                    if REQUEST is not None:
                        self.confirm_quit = True
                    # ESC quits from the title, but elsewhere just bails to the
                    # title (so you never lose the whole game by mistake).
                    elif isinstance(self.scene, TitleScene):
                        running = False
                    else:
                        self.scene = TitleScene(self)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.toggle_fullscreen()    # F11 = windowed <-> fullscreen
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_m
                      and not getattr(self.scene, "typing_in_terminal",
                                      lambda: False)()):
                    # M mutes/unmutes -- but NOT while you're typing code, so you
                    # can still type the letter 'm' in the terminal.
                    sfx.toggle_mute()
                else:
                    self.scene.handle_event(event)

            # If the scene asked to switch, do it now.
            if self.scene.next_scene is not None:
                if self.scene.next_scene == "quit":
                    running = False
                else:
                    self.scene = self.scene.next_scene   # a new Scene object

            self.stars.update(dt)
            self.scene.update(dt)

            # Draw order: space, stars, then the scene on top.
            self.screen.fill(COLORS["space"])
            self.stars.draw(self.screen)
            self.scene.draw(self.screen)
            if sfx.is_muted():              # a quiet reminder that audio is off
                draw_text(self.screen, "MUTED (M)", 16, HEIGHT - 26, size=14,
                          color="gray")
            if self.confirm_quit:
                self._draw_confirm(self.screen)
            pygame.display.flip()           # show the freshly drawn frame

        pygame.quit()
        sys.exit()

    def _draw_confirm(self, surface):
        """The one-line "are you sure?" asked when ESC is pressed on the ship."""
        box = pygame.Rect(140, 296, WIDTH - 280, 108)
        draw_panel(surface, box, fill="panel", border="amber")
        draw_text(surface, "Leave session? Progress on this task is kept "
                  "next time.", WIDTH // 2, box.y + 24, size=20, color="star",
                  center=True)
        draw_text(surface, "Y = leave    N = keep going", WIDTH // 2,
                  box.y + 62, size=20, color="amber", center=True)


if __name__ == "__main__":
    # Did the 3D ship game start us with "--level N"? If it didn't, REQUEST is
    # None, nothing below changes, and the game opens on its title screen
    # exactly as it always has.
    REQUEST = handoff.read_request()
    if REQUEST is not None:
        SAVE_LOCKED = True          # hands off the cadet's own progress.json
    game = Game()
    if REQUEST is not None:
        # Jump straight into the level the ship asked for. --level is 1-based
        # (level 1 is the first one), and we clamp it so a silly number can
        # never crash us.
        i = max(0, min(len(LEVELS) - 1, REQUEST["level"] - 1))
        game.scene = LevelScene(game, LEVELS[i], i)
    game.run()
