"""
level4_navigation.py  --  LEVEL 4: Navigation
=============================================

Concept taught: comparisons and if / elif / else -- making DECISIONS in code.

This is the first level where you write a MULTI-LINE BLOCK. In the terminal you
type each line of the block, indent the inside lines with the Tab key (Tab gives
you 4 spaces), and then press Enter on a BLANK line to run the whole thing.

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
    "number": 4,
    "system": "NAVIGATION",
    "concept": "comparisons and if / elif / else",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Navigation is offline, Cadet. We are drifting blind.",
        "To steer, the ship must make DECISIONS: turn or hold, slow or go.",
        "",
        "Today you teach the computer to CHOOSE -- with if and else.",
        "First it asks a yes/no question, then it acts on the answer.",
        "",
        "These lessons span several lines, so we type a BLOCK.",
        "Type each line, use Tab to indent the inside lines,",
        "then press Enter on an EMPTY line to run the whole block.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'temperature = 30\n'
            'if temperature > 25:\n'
            '    print("Cooling system on")'
        ),
        "caption": "The computer asks: is temperature greater than 25? It is "
                   "(30 > 25), so the indented line runs and prints:  "
                   "Cooling system on",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "temperature > 25",
            "note": "A COMPARISON. The operators  >  <  ==  >=  ask a question "
                    "and answer with True or False. Watch out: == (TWO equals "
                    "signs) means 'is equal to'. One = stores a value; two == "
                    "checks if two things are equal.",
        },
        {
            "code": "if temperature > 25:\n    print(\"Cooling system on\")",
            "note": "The if structure: the word if, a condition, then a colon : "
                    "at the end. The next line is INDENTED (4 spaces -- press "
                    "Tab). That indented line runs ONLY when the condition is "
                    "True. Press Enter on a blank line to run the block.",
        },
        {
            "code": "if fuel < 50:\n    print(\"Refuel\")\nelse:\n    print(\"OK\")",
            "note": "else: is the 'otherwise' branch. When the if condition is "
                    "False, Python skips the if line and runs the indented line "
                    "under else instead. One of the two always runs.",
        },
        {
            "code": ("if speed == 0:\n    print(\"Stopped\")\n"
                     "elif speed < 10:\n    print(\"Cruising\")\n"
                     "else:\n    print(\"Too fast\")"),
            "note": "elif means 'else, if...' -- extra branches. Python checks "
                    "them IN ORDER, top to bottom, and runs the first one that "
                    "is True. Keep every inside line indented, then a blank line "
                    "to run.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Ask the computer a question. Print whether 8 is greater than 3 with:  print(8 > 3)",
            "intro": ["A comparison answers True or False.", "Try:  print(8 > 3)"],
            "seed": {},
            "hints": [
                "The > symbol means 'greater than'.",
                "Wrap the comparison in print(...).",
                "Type:  print(8 > 3)",
            ],
            "solution": "print(8 > 3)",
            "check": lambda term: "true" in term.last_run.lower(),
            "success": "True! 8 really is greater than 3. Comparisons are how code decides.",
        },
        {
            "instruction": "Fuel is at 20. Write an if/else: if fuel < 50 print \"Refuel needed\", otherwise print \"Fuel OK\".\nTIP: type each line, indent with Tab, then press Enter on an EMPTY line to run it.",
            "intro": ["fuel is already set to 20.",
                      "Indent the lines under if/else with the Tab key.",
                      "Press Enter on a blank line to run the block."],
            "seed": {"fuel": 20},
            "hints": [
                "First line:  if fuel < 50:",
                "Indented under it:  print(\"Refuel needed\"); then a line  else:  then indented  print(\"Fuel OK\")",
                'if fuel < 50:\n    print("Refuel needed")\nelse:\n    print("Fuel OK")',
            ],
            "solution": 'if fuel < 50:\n    print("Refuel needed")\nelse:\n    print("Fuel OK")',
            "check": lambda term: "refuel needed" in term.last_run.lower(),
            "success": "Refuel needed -- correct! The computer chose the right branch.",
        },
        {
            "instruction": "Speed is 8. Use if / elif / else: print \"Stopped\" if speed == 0, \"Cruising\" if speed < 10, else \"Too fast\".",
            "intro": ["speed is already set to 8.",
                      "elif means 'else, if...' -- extra branches.",
                      "Press Enter on a blank line to run the block."],
            "seed": {"speed": 8},
            "hints": [
                "Check exact equality with two equals signs:  speed == 0",
                "Order: if (== 0), elif (< 10), else.",
                'if speed == 0:\n    print("Stopped")\nelif speed < 10:\n    print("Cruising")\nelse:\n    print("Too fast")',
            ],
            "solution": 'if speed == 0:\n    print("Stopped")\nelif speed < 10:\n    print("Cruising")\nelse:\n    print("Too fast")',
            "check": lambda term: "cruising" in term.last_run.lower(),
            "success": "Cruising speed confirmed. You can steer the ship now, Cadet.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The star charts flare to life. NAVIGATION: ONLINE. We can steer again.",
        "",
        "You taught the computer to DECIDE: if asks a question, elif adds more",
        "branches, and else handles everything left over -- one always runs.",
        "",
        "Next stop: the Cargo Bay, where supplies float loose in the dark.",
        "There you'll learn LISTS -- holding many values in one tidy place.",
    ],
}
