# Starship Pyxis: Shakedown 🚀

A beginner Python course disguised as a starship voyage, built with **pygame**.
You are a cadet on a shakedown cruise. Systems keep failing, and the only way to
fix them is to write the code yourself.

It teaches Python from absolute zero — the first level assumes you have never
written a line — and your guide, **PYX**, walks you through every step.

---

## ▶️ How to run it

You need Python 3 and pygame:

```
pip install pygame
```

Then, from inside this folder:

```
python main.py
```

**Windows:** you can also double-click `Play Starship Pyxis.bat`.

Your progress saves automatically, so closing mid-level picks up where you left
off.

---

## 🗺️ Every level runs the same five steps

Each of the ship's systems is one lesson, and each lesson walks the same path:

1. **Brief** — what has broken, and what you will need to fix it
2. **Example** — the new idea, shown working in a few lines
3. **Explain** — why it works, in plain language
4. **Practice** — short tasks you type yourself, checked as you go
5. **Repair** — use what you just learned to actually fix the system

The point of the shape is that you never meet a puzzle before you have met the
idea behind it.

---

## 🛰️ The voyage

**29 levels**, one per ship system, from the power core outward:

power → oxygen → comms → navigation → cargo → engine → shields → charts →
airlock → sensors → drones → life support → data vault → beacons → roster →
fabricator → module bay → logic → mainframe → docking → text lab → database →
black box → reactor → hyperdrive → gauntlet → kraken → wormhole

The twenty-ninth is a post-game secret, hidden until you finish the campaign.

Along the way you cover variables, types, conditionals, loops, lists,
dictionaries, functions, strings, and file-shaped data — each introduced because
a system needs it, not because a syllabus said so.

---

## 📂 Repository map

```
main.py           the director: window, game loop, level flow
engine.py         core game objects and state
pyterminal.py     the in-game code terminal you type into
levels/           one file per system, each holding its own lesson and tasks
sfx.py            sound effects
assets/           art and audio
make_icon.py      generates the window icon
make_sounds.py    generates the sound effects

pyxkernel.py      runs practice tasks with no window at all
kernel_server.py  serves that kernel on a local port
handoff.py        lets another program request a single level
smoke_kernel.py   the gate: every task, fed its own solution, must still pass
```

The last four files exist so the 3D version of this game — a Godot starship you
walk around — can hand a level to this one and get the result back. `smoke_kernel.py`
is what keeps that honest: it feeds every practice task its own known-good
solution through the headless kernel and checks each one still passes, proving
the kernel is a faithful stand-in for the real terminal.

---

## 🛠️ How this was built

A personal project, built to learn Python. Written with heavy help from Claude
Code. The teaching structure — five phases per level, no puzzle before the idea
— was the part that got designed carefully; the code follows from it.
