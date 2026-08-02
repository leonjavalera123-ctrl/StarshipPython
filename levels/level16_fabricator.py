"""
level16_fabricator.py  --  LEVEL 16: The Fabricator
===================================================

Concept taught: list comprehensions -- a compact, one-line way to build a list.

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
    "number": 16,
    "system": "FABRICATOR",
    "concept": "list comprehensions",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Fabricator is humming, Cadet. This is the machine that builds",
        "parts in bulk -- a whole row of bolts, panels, or fuel cells at once.",
        "",
        "To run it, you'll learn a LIST COMPREHENSION.",
        "It is a compact, one-line way to BUILD A LIST.",
        "",
        "Give it a rule and a sequence, and it makes the whole list for you.",
        "One tidy line instead of a long loop. Let me show you.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'doubles = [x * 2 for x in [1, 2, 3]]\n'
            'print(doubles)'
        ),
        "caption": "One line builds the whole list. It doubles each number in "
                   "[1, 2, 3], so this prints:  [2, 4, 6]",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "doubles = [x * 2 for x in [1, 2, 3]]",
            "note": "A list comprehension builds a list in ONE line. Its shape "
                    "is:  [expression for item in sequence]. It walks the "
                    "sequence and runs the expression on each item.",
        },
        {
            "code": "for x in [1, 2, 3]:  doubles.append(x * 2)",
            "note": "It is a shortcut for a for-loop that APPENDS. The long way "
                    "starts an empty list and appends each result. The "
                    "comprehension does the same work in a single neat line.",
        },
        {
            "code": "[x for x in [1, 2, 3, 4] if x > 2]",
            "note": "Add  if condition  at the END to keep only SOME items. "
                    "Only items where the condition is True go into the new "
                    "list. This one keeps [3, 4].",
        },
        {
            "code": "n % 2 == 0",
            "note": "The % (modulo) operator gives the REMAINDER of a division. "
                    "6 % 2 is 0; 7 % 2 is 1. So  n % 2 == 0  is True for EVEN "
                    "numbers (they divide by 2 with nothing left over).",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Fabricate squares. Build a list of the squares of 1 to 4 in ONE line:\nsquares = [n * n for n in range(1, 5)]",
            "intro": ["A list comprehension builds a list compactly.",
                      "Shape:  [expression for item in sequence]"],
            "seed": {},
            "hints": [
                "range(1, 5) gives 1, 2, 3, 4.",
                "The expression is  n * n.",
                "squares = [n * n for n in range(1, 5)]",
            ],
            "solution": "squares = [n * n for n in range(1, 5)]",
            "check": lambda term: term.ns.get("squares") == [1, 4, 9, 16],
            "success": "[1, 4, 9, 16] in one line. That's the power of a comprehension.",
        },
        {
            "instruction": "Keep only the evens. Build a list of even numbers from 0 to 9 using a condition:\nevens = [n for n in range(10) if n % 2 == 0]",
            "intro": ["Add  if condition  to a comprehension to filter items.",
                      "n % 2 == 0 is True when n is even (no remainder)."],
            "seed": {},
            "hints": [
                "The % operator gives the remainder; even means  n % 2 == 0.",
                "Add the if at the end of the comprehension.",
                "evens = [n for n in range(10) if n % 2 == 0]",
            ],
            "solution": "evens = [n for n in range(10) if n % 2 == 0]",
            "check": lambda term: term.ns.get("evens") == [0, 2, 4, 6, 8],
            "success": "[0, 2, 4, 6, 8]. Build and filter, all in one neat line.",
        },
        {
            "instruction": "Shout the names. The list names is loaded -- build a new list with each name in CAPITALS:\nloud = [name.upper() for name in names]",
            "intro": ["names = [\"ada\", \"grace\"] is loaded.",
                      "You can call a method inside a comprehension."],
            "seed": {"names": ["ada", "grace"]},
            "hints": [
                "The expression is  name.upper().",
                "Loop with  for name in names.",
                "loud = [name.upper() for name in names]",
            ],
            "solution": "loud = [name.upper() for name in names]",
            "check": lambda term: term.ns.get("loud") == ["ADA", "GRACE"],
            "success": "['ADA', 'GRACE']. You transformed a whole list in one line.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "FABRICATOR: ONLINE. The machine roars and stamps out a fresh row of",
        "parts, gleaming and ready. The bulk assembly line is yours, Cadet.",
        "",
        "Recap: a list comprehension --  [expression for item in sequence]  --",
        "builds a whole list in one compact line, and an  if  can filter it.",
        "",
        "Next: the Module Bay, where you'll learn to IMPORT MODULES -- ready-made",
        "toolboxes of code you can pull in and use. I'll meet you there.",
    ],
}
