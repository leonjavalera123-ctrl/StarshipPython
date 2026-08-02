"""
level14_beacons.py  --  LEVEL 14: The Nav Beacons
=================================================

Concept taught: tuples (fixed sequences).

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
    "number": 14,
    "system": "NAV BEACONS",
    "concept": "tuples (fixed sequences)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Core systems are steady, Cadet. We're pointed home.",
        "But the wormhole drive won't fire until the advanced systems wake up.",
        "",
        "First: the Nav Beacons. They store FIXED coordinates --",
        "anchor points in space that must NEVER change, or we drift off course.",
        "",
        "For data that must stay locked, Python uses a TUPLE.",
        "A tuple is like a list, but unchangeable. Let me show you.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            "point = (3, 7)\n"
            "print(point[0])"
        ),
        "caption": "This prints:  3. 'point' is a TUPLE -- two values locked "
                   "together. We read item 0 with point[0]. A tuple is fixed: "
                   "once made, its values cannot be changed.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "point = (3, 7)",
            "note": "A tuple uses ROUND brackets ( ) and holds values in order. "
                    "Here point holds two numbers: 3 first, then 7. The comma "
                    "separates them, just like items in a list.",
        },
        {
            "code": "point[0] = 99   # ERROR!",
            "note": "A tuple is IMMUTABLE -- once made, you CANNOT change it. "
                    "Trying to overwrite an item raises an error. That's perfect "
                    "for fixed data like beacon coordinates that must stay put. "
                    "(A list CAN change; a tuple cannot.)",
        },
        {
            "code": "point[0]",
            "note": "Index a tuple just like a list, starting at 0. So point[0] "
                    "is 3 (the first item) and point[1] is 7 (the second). The "
                    "square brackets READ a value -- they don't change anything.",
        },
        {
            "code": "x, y = point",
            "note": "UNPACKING copies each item into its own variable. After this, "
                    "x is 3 and y is 7 -- in one neat line. It's a tidy way to "
                    "pull the pieces of a tuple out into named values.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Mark a beacon's position. Make a tuple named position holding two numbers: 10 and 20.\nTuples use round brackets:  (10, 20)",
            "intro": ["A tuple is like a list, but it CANNOT be changed once made.",
                      "It uses round brackets ( )."],
            "seed": {},
            "hints": [
                "Round brackets make a tuple:  ( )",
                "Put the two numbers inside, comma-separated.",
                "position = (10, 20)",
            ],
            "solution": "position = (10, 20)",
            "check": lambda term: term.ns.get("position") == (10, 20),
            "success": "Beacon fixed at (10, 20). A tuple locks those coordinates in place.",
        },
        {
            "instruction": "Read the first coordinate. Print position[0].",
            "intro": ["position = (10, 20) is loaded.",
                      "Index a tuple just like a list, starting at 0."],
            "seed": {"position": (10, 20)},
            "hints": [
                "Use square brackets with the index.",
                "The first item is at index 0.",
                "print(position[0])",
            ],
            "solution": "print(position[0])",
            "check": lambda term: "10" in term.last_run,
            "success": "10 -- the x coordinate, pulled from slot 0.",
        },
        {
            "instruction": "Unpack both at once. Split position into two variables:  x, y = position",
            "intro": ["position = (10, 20) is loaded.",
                      "Unpacking copies each item into its own variable."],
            "seed": {"position": (10, 20)},
            "hints": [
                "Put two names on the left of the = sign.",
                "x, y = position",
                "x, y = position",
            ],
            "solution": "x, y = position",
            "check": lambda term: term.ns.get("x") == 10 and term.ns.get("y") == 20,
            "success": "x = 10, y = 20. Unpacking is a clean way to read a tuple.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "NAV BEACONS: ONLINE. Anchor points snap into place across the star map.",
        "",
        "You learned the TUPLE: like a list, but locked -- round brackets ( ),",
        "indexed from 0, and unpackable with  x, y = point. Perfect for fixed data.",
        "",
        "Next system: the Crew Roster, where you'll learn SETS -- collections that",
        "keep only UNIQUE values. No duplicate cadets allowed. Lead on.",
    ],
}
