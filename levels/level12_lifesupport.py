"""
level12_lifesupport.py  --  LEVEL 12: Life Support
==================================================

Concept taught: ERROR HANDLING with try / except.

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

A note on try / except: it is a MULTI-LINE BLOCK, just like if and for. The
try: line opens it, the except line continues it, and a BLANK line tells the
terminal you are done and runs the whole thing.
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 12,
    "system": "LIFE SUPPORT",
    "concept": "error handling with try / except",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Life Support is online, Cadet, but it keeps CRASHING.",
        "Every time a sensor sends bad data, the whole program stops cold.",
        "",
        "One bad number, and the air recyclers go dark. That cannot happen.",
        "We need code that SURVIVES a mistake instead of falling over.",
        "",
        "The tool for this is try / except. You wrap risky code in try,",
        "and if it goes wrong, except catches the error and we keep going.",
        "Let's look at an example before you try it.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'try:\n'
            '    print(int("42"))\n'
            'except ValueError:\n'
            '    print("That was not a number")'
        ),
        "caption": "The try block runs the risky code -- here, turning text into "
                   "a number. If that works, you see 42. If it fails, except "
                   "catches the error and prints the backup message INSTEAD of "
                   "crashing the ship.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "try:",
            "note": "try: wraps code that MIGHT fail. Indent the risky lines "
                    "underneath it. Python attempts them, but stays ready in "
                    "case something goes wrong. Think of it as 'attempt this'.",
        },
        {
            "code": 'except ValueError:',
            "note": "except runs ONLY if the try code hit that kind of error. "
                    "It catches the problem, runs its own lines instead, and the "
                    "program KEEPS GOING -- no crash. Think of it as 'if it "
                    "breaks, do this'.",
        },
        {
            "code": "ZeroDivisionError / ValueError",
            "note": "Errors have names. ZeroDivisionError happens when you "
                    "divide by zero, like 10 / 0. ValueError happens when a "
                    "value is the wrong kind, like int(\"oops\"). You name the "
                    "error you expect after the word except.",
        },
        {
            "code": "try: ... (no error)",
            "note": "Good news: if the try code works fine, the except part is "
                    "SKIPPED entirely. except is a safety net, not a second step "
                    "-- it only catches you when you actually fall.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Catch a crash. Wrap a divide-by-zero in try/except so it prints \"Cannot divide by zero\" instead of crashing:\ntry:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")",
            "intro": ["try runs risky code; except catches the error if it happens.",
                      "Dividing by zero normally crashes a program.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Put the risky line under  try:",
                "Catch it with  except ZeroDivisionError:  then print a message.",
                'try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',
            ],
            "solution": 'try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',
            "check": lambda term: "cannot divide by zero" in term.last_run.lower(),
            "success": "Caught it! The ship kept running instead of crashing. That's resilience.",
        },
        {
            "instruction": "Bad input. Try to turn \"oops\" into a number, and catch the error with \"Not a number\":\ntry:\n    number = int(\"oops\")\nexcept ValueError:\n    print(\"Not a number\")",
            "intro": ["int(\"oops\") fails because that text isn't a number.",
                      "That kind of error is called a ValueError.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Risky line under try:  number = int(\"oops\")",
                "Catch with  except ValueError:",
                'try:\n    number = int("oops")\nexcept ValueError:\n    print("Not a number")',
            ],
            "solution": 'try:\n    number = int("oops")\nexcept ValueError:\n    print("Not a number")',
            "check": lambda term: "not a number" in term.last_run.lower(),
            "success": "Handled gracefully. Bad data no longer takes down life support.",
        },
        {
            "instruction": "When nothing goes wrong. Run a safe try where the code works fine and prints \"Reading sensor\":\ntry:\n    print(\"Reading sensor\")\n    value = 100\nexcept Exception:\n    print(\"Sensor failed\")",
            "intro": ["If the try code works, the except part is skipped entirely.",
                      "Exception catches any kind of error.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Put two safe lines under try (a print and an assignment).",
                "Add  except Exception:  with a backup message.",
                'try:\n    print("Reading sensor")\n    value = 100\nexcept Exception:\n    print("Sensor failed")',
            ],
            "solution": 'try:\n    print("Reading sensor")\n    value = 100\nexcept Exception:\n    print("Sensor failed")',
            "check": lambda term: "reading sensor" in term.last_run.lower(),
            "success": "No error, so except was skipped. Life support: stable and self-healing.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The air recyclers steady. Life Support holds firm -- no more crashes.",
        "",
        "You learned try / except: wrap risky code in try, and except catches",
        "the error so the program survives instead of falling over.",
        "",
        "Next stop: the Data Vault. There you'll COMBINE loops and logic,",
        "weaving everything you know into code that thinks for itself. Onward.",
    ],
}
