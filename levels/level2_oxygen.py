"""
level2_oxygen.py  --  LEVEL 2: The Oxygen Recycler
==================================================

Concept taught: numbers and math (+, -, *, /).

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
    "number": 2,
    "system": "OXYGEN RECYCLER",
    "concept": "numbers and math (+, -, *, /)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    # A list of lines PYX "says". Short lines read better on screen.
    "brief": [
        "Power's back, Cadet. I can think clearly again. Well done.",
        "But the air is getting thin. The Oxygen Recycler is down.",
        "",
        "To fix it, we must do MATH -- count tanks, total the air, share it out.",
        "Good news: Python is a brilliant calculator. It loves numbers.",
        "",
        "You'll use four signs:  +  to add,  -  to subtract,",
        "  *  to multiply, and  /  to divide. No quotes -- numbers are not text.",
        "Let's look at an example before you try anything.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'tanks = 4\n'
            'oxygen = tanks * 250\n'
            'print("Oxygen units:", oxygen)'
        ),
        "caption": "Three lines. We store 4 tanks, MULTIPLY by 250 units each "
                   "with the * sign, then show the total. Running this prints:  "
                   "Oxygen units: 1000",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    # A list of {code, note} cards. main.py shows the code fragment, then the
    # note under it, so you learn the syntax bit by bit.
    "explain": [
        {
            "code": "3 + 5    and    9 - 2",
            "note": "The + sign ADDS numbers (3 + 5 is 8). The - sign SUBTRACTS "
                    "(9 - 2 is 7). These two work just like they do on paper.",
        },
        {
            "code": "tanks * 250",
            "note": "The * sign (the star) means MULTIPLY. There is no x key for "
                    "this in code, so we use *. So 4 * 250 is 1000.",
        },
        {
            "code": "750 / 2",
            "note": "The / sign (the slash) means DIVIDE. 750 / 2 splits 750 into "
                    "2 equal parts, giving 375. It shares a number out evenly.",
        },
        {
            "code": "5 / 2   ->   2.5",
            "note": "Division always gives a DECIMAL -- a number with a dot. "
                    "5 / 2 is 2.5. And even 750 / 2 comes out as 375.0, with a "
                    ".0 on the end. That dot is normal; it just means 'decimal'.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    # A list of tasks. Each task has:
    #   instruction : what to do (PyX-style, clear and small)
    #   intro       : grey welcome lines shown in the terminal
    #   seed        : variables pre-loaded into the terminal (often empty)
    #   hints       : the HINT LADDER -- revealed one click at a time
    #   solution    : a known-good answer (used by the final hint + tests)
    #   check       : a function given the terminal; returns True when solved
    #   success     : PYX's cheer when you pass
    "practice": [
        {
            "instruction": "The recycler needs a quick test. Print the answer to 18 + 24.\nType it after the >>> and press Enter.",
            "intro": ["Recycler math console online.", "Try:  print(18 + 24)"],
            "seed": {},
            "hints": [
                "print needs round brackets: print(...)",
                "Put the sum inside, with no quotes (it's math, not text).",
                "Type:  print(18 + 24)",
            ],
            "solution": "print(18 + 24)",
            "check": lambda term: "42" in term.last_run,
            "success": "42 units. The recycler hums as it calibrates. Nice math.",
        },
        {
            "instruction": "Each tank holds 250 units of air. Make three variables, one per line:\ntanks = 3, then per_tank = 250, then total = tanks * per_tank.",
            "intro": ["Type one line at a time, pressing Enter after each.",
                      "The * symbol means multiply."],
            "seed": {},
            "hints": [
                "Start simple:  tanks = 3",
                "Then:  per_tank = 250",
                "Multiply with the * symbol:  total = tanks * per_tank",
            ],
            "solution": "tanks = 3\nper_tank = 250\ntotal = tanks * per_tank",
            "check": lambda term: term.ns.get("total") == 750,
            "success": "750 units of breathable air. The crew can rest easy.",
        },
        {
            "instruction": "Split the air evenly between 2 decks. Your total (750) is ready.\nMake half = total / 2, then on the next line print(half).",
            "intro": ["total is already set to 750.", "The / symbol means divide."],
            "seed": {"total": 750},
            "hints": [
                "Divide with the / symbol.",
                "half = total / 2",
                "Then on the next line:  print(half)",
            ],
            "solution": "half = total / 2\nprint(half)",
            "check": lambda term: "375" in term.last_run,
            "success": "375.0 per deck. Notice the .0 -- division always gives a decimal!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Vents hiss open. Clean air floods the deck. The recycler is ONLINE.",
        "",
        "Breathe it in, Cadet. You earned that.",
        "Today you taught Python to do math: + add, - subtract, * multiply, / divide.",
        "",
        "Oxygen restored. But we're still alone out here, with no way to call home.",
        "Next: the Comms Antenna -- where you'll learn STRINGS, the way code holds TEXT.",
    ],
}
