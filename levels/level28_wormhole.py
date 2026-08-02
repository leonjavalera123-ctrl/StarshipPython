"""
level28_wormhole.py  --  LEVEL 28: The Wormhole Drive
=====================================================

Concept taught: putting it all together (functions + loops + logic).

This is the CAPSTONE -- the final level. Everything you have practiced comes
together here: print, variables, math, strings, if/else, lists, loops, dicts,
functions, classes, error handling, tuples, sets, comprehensions, modules,
boolean logic, nested data, enumerate/zip, slicing, and dict looping. The
Wormhole Drive is the last system, and powering it sends the cadet HOME.

HOW A LEVEL IS SHAPED
---------------------
Every level file gives the game ONE dictionary called LEVEL. main.py reads it
and runs the five-step lesson flow:

    1. brief    -> PYX explains the story + what you'll learn
    2. example  -> a working snippet of code is shown FIRST
    3. explain  -> each important piece of that snippet, in plain English
    4. practice -> YOU type real Python; stuck? a hint ladder helps
    5. repair   -> your success brings the ship's system back online

You never have to touch main.py to make a level. You only fill in this data.
Keep all in-game text plain ASCII (the terminal font can't draw emoji).
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 28,
    "system": "WORMHOLE DRIVE",
    "concept": "putting it all together (functions + loops + logic)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Cadet... look at the board. Every system reads green.",
        "Core systems, advanced systems, even the Kraken -- all behind you now.",
        "",
        "One system remains: the Wormhole Drive. The way HOME.",
        "To power it, you'll write functions that combine EVERYTHING you know.",
        "Loops inside functions. Logic inside functions. Lists built and returned.",
        "",
        "This is the last challenge, Cadet. Power the drive, and you fly home.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'def add_all(nums):\n'
            '    total = 0\n'
            '    for n in nums:\n'
            '        total = total + n\n'
            '    return total\n'
            'print(add_all([1, 2, 3]))'
        ),
        "caption": "A function with a LOOP inside it. add_all walks through the "
                   "list, adds every number into total, then RETURNS the answer. "
                   "Calling it on [1, 2, 3] prints:  6",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "def add_all(nums):\n    total = 0\n    for n in nums:\n        total = total + n",
            "note": "A function can hold a LOOP. Everything indented under def is "
                    "the function's body -- including the for loop. Each time you "
                    "call add_all, that loop runs fresh on whatever list you pass.",
        },
        {
            "code": "def check(level):\n    if level < 50:\n        return \"LOW\"\n    return \"OK\"",
            "note": "A function can hold an IF. The function looks at its input, "
                    "makes a decision, and returns a different answer for each "
                    "case. You wrap a choice in a name and reuse it anywhere.",
        },
        {
            "code": "def doubles(nums):\n    out = []\n    for n in nums:\n        out.append(n * 2)\n    return out",
            "note": "Build a RESULT LIST inside a function, then return it. Start "
                    "with an empty list, append to it as the loop runs, and hand "
                    "back the finished list. doubles([1, 2]) returns [2, 4].",
        },
        {
            "code": "# print, math, strings, if, lists, loops, dicts, functions...",
            "note": "The big picture: functions PACKAGE logic so you can reuse and "
                    "combine it. Print, math, strings, if/else, lists, loops, "
                    "dicts -- every tool you learned now snaps together inside "
                    "functions. That is how real programs are built. Look how far "
                    "you've come, Cadet.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Build a countdown function. Define countdown(n) that returns a list from n down to 1:\ndef countdown(n):\n    result = []\n    while n > 0:\n        result.append(n)\n        n = n - 1\n    return result",
            "intro": ["This combines a function, a while loop, and a list.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [
                "Header:  def countdown(n):  then start  result = []",
                "Loop while n > 0, appending n and lowering n, then return result.",
                "def countdown(n):\n    result = []\n    while n > 0:\n        result.append(n)\n        n = n - 1\n    return result",
            ],
            "solution": "def countdown(n):\n    result = []\n    while n > 0:\n        result.append(n)\n        n = n - 1\n    return result",
            "check": lambda term: callable(term.ns.get("countdown")) and term.ns["countdown"](3) == [3, 2, 1],
            "success": "countdown(3) -> [3, 2, 1]. Function + loop + list, all at once.",
        },
        {
            "instruction": "Run a safety check. Define safe_levels(values) that returns how many values are below 100:\ndef safe_levels(values):\n    count = 0\n    for v in values:\n        if v < 100:\n            count = count + 1\n    return count",
            "intro": ["This combines a function, a for loop, and an if.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [
                "Header:  def safe_levels(values):  then  count = 0",
                "Loop, if v < 100: count = count + 1, then return count.",
                "def safe_levels(values):\n    count = 0\n    for v in values:\n        if v < 100:\n            count = count + 1\n    return count",
            ],
            "solution": "def safe_levels(values):\n    count = 0\n    for v in values:\n        if v < 100:\n            count = count + 1\n    return count",
            "check": lambda term: callable(term.ns.get("safe_levels")) and term.ns["safe_levels"]([50, 200, 30]) == 2,
            "success": "safe_levels([50, 200, 30]) -> 2. Every system reads green.",
        },
        {
            "instruction": "Fire the jump drive. Define launch(name) that returns an f-string \"<name>, jump to lightspeed!\":\ndef launch(name):\n    return f\"{name}, jump to lightspeed!\"",
            "intro": ["One last function to take you home.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [
                "Header:  def launch(name):",
                "Return:  return f\"{name}, jump to lightspeed!\"",
                'def launch(name):\n    return f"{name}, jump to lightspeed!"',
            ],
            "solution": 'def launch(name):\n    return f"{name}, jump to lightspeed!"',
            "check": lambda term: callable(term.ns.get("launch")) and term.ns["launch"]("Pyxis") == "Pyxis, jump to lightspeed!",
            "success": "Pyxis, jump to lightspeed! The wormhole opens. You're going HOME, Cadet.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Space tears open ahead -- a wormhole, blue and bright. The Pyxis leaps,",
        "and the stars stretch into lines. You're going home.",
        "",
        "Look at all you can do now: print and variables, math and strings,",
        "if/else and lists, loops and dicts, functions, classes, error handling,",
        "tuples, sets, comprehensions, modules, logic, nested data, and more.",
        "You started speaking to me one line at a time. Now you build whole programs.",
        "You're not just a cadet anymore, Cadet -- you're a Python programmer.",
    ],
}
