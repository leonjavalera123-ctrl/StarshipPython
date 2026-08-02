"""
level20_docking.py  --  LEVEL 20: The Docking Sync
==================================================

Concept taught: enumerate() and zip().

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
    "number": 20,
    "system": "DOCKING SYNC",
    "concept": "enumerate() and zip()",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "We're nearly home, Cadet. Now the Docking Sync must come online.",
        "The docking computer numbers each clamp and pairs ships to bays.",
        "",
        "Two new tools do exactly that work for us.",
        "enumerate() NUMBERS your items as you loop -- 0, 1, 2...",
        "zip() PAIRS two lists, walking them side by side.",
        "",
        "Both live in a for-loop. Finish a block with a BLANK line.",
        "Watch the example, then you'll align the clamps yourself.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'for i, color in enumerate(["red", "blue"]):\n'
            '    print(i, color)'
        ),
        "caption": "enumerate hands the loop a NUMBER and an ITEM each time. "
                   "This prints:  0 red  then  1 blue. Press Enter on a BLANK "
                   "line to run the block.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "for i, item in enumerate(list):",
            "note": "enumerate(list) hands back PAIRS: a position and the item "
                    "at that position. You catch both with two names, here i and "
                    "item, so every loop you know WHERE you are and WHAT you got.",
        },
        {
            "code": "i  ->  0, 1, 2, ...",
            "note": "The index starts at 0, not 1. The first item is number 0, "
                    "the second is number 1, and so on. Computers love counting "
                    "from zero -- it's the same as list positions like list[0].",
        },
        {
            "code": "for x, y in zip(a, b):",
            "note": "zip(a, b) pairs two lists item-by-item: a[0] with b[0], then "
                    "a[1] with b[1]. It's like a zipper joining two rows of teeth "
                    "into one. Great for matching ships to bays.",
        },
        {
            "code": "x, y  =  one pair",
            "note": "The two names in the for line do the catching. enumerate and "
                    "zip each hand you a PAIR every loop; unpacking it into two "
                    "names splits that pair so you can use each half on its own.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Number the crew. Loop with enumerate to print each index and name:\nfor i, name in enumerate(crew):\n    print(i, name)",
            "intro": ["crew = [\"Ada\", \"Grace\"] is loaded.",
                      "enumerate gives you the position AND the item.",
                      "Blank line runs the block."],
            "seed": {"crew": ["Ada", "Grace"]},
            "hints": [
                "Use  for i, name in enumerate(crew):",
                "Inside, print both:  print(i, name)",
                "for i, name in enumerate(crew):\n    print(i, name)",
            ],
            "solution": "for i, name in enumerate(crew):\n    print(i, name)",
            "check": lambda term: "0 ada" in term.last_run.lower() and "1 grace" in term.last_run.lower(),
            "success": "0 Ada, 1 Grace -- every crew member numbered. That's enumerate.",
        },
        {
            "instruction": "Pair ships to jobs. Use zip to print each name with its job:\nfor name, job in zip(names, jobs):\n    print(name, job)",
            "intro": ["names = [\"Ada\", \"Grace\"] and jobs = [\"pilot\", \"engineer\"] are loaded.",
                      "zip walks two lists together.",
                      "Blank line runs the block."],
            "seed": {"names": ["Ada", "Grace"], "jobs": ["pilot", "engineer"]},
            "hints": [
                "Use  for name, job in zip(names, jobs):",
                "Inside:  print(name, job)",
                "for name, job in zip(names, jobs):\n    print(name, job)",
            ],
            "solution": "for name, job in zip(names, jobs):\n    print(name, job)",
            "check": lambda term: "ada pilot" in term.last_run.lower() and "grace engineer" in term.last_run.lower(),
            "success": "Ada pilot, Grace engineer -- two lists, zipped into pairs.",
        },
        {
            "instruction": "Build a labeled list. Pair each index with its code into a list of tuples:\nlabeled = []\nfor i, c in enumerate(codes):\n    labeled.append((i, c))",
            "intro": ["codes = [\"x\", \"y\"] is loaded.",
                      "(i, c) makes a tuple of the position and the item.",
                      "Blank line runs the block."],
            "seed": {"codes": ["x", "y"]},
            "hints": [
                "Start  labeled = []  then loop with enumerate.",
                "Append a tuple each time:  labeled.append((i, c))",
                'labeled = []\nfor i, c in enumerate(codes):\n    labeled.append((i, c))',
            ],
            "solution": "labeled = []\nfor i, c in enumerate(codes):\n    labeled.append((i, c))",
            "check": lambda term: term.ns.get("labeled") == [(0, "x"), (1, "y")],
            "success": "[(0, 'x'), (1, 'y')] -- numbered and paired. Docking clamps aligned!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Clamps swing into line and the bays light up green. DOCKING SYNC: ONLINE.",
        "",
        "You numbered items with enumerate() and paired lists with zip() --",
        "two tools every real Python loop reaches for.",
        "",
        "Next stop: the Text Lab, where you'll learn STRING SLICING --",
        "carving out just the piece of text you need. Almost home, Cadet.",
    ],
}
