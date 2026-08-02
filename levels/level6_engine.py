"""
level6_engine.py  --  LEVEL 6: The Engine Room
==============================================

Concept taught: for loops and range().

HOW A LEVEL IS SHAPED
---------------------
Every level file gives the game ONE dictionary called LEVEL. main.py reads it
and runs the five-step lesson flow:

    1. brief    -> PYX explains the story + what you'll learn
    2. example  -> a working snippet of code is shown FIRST
    3. explain  -> each important piece of that snippet, in plain English
    4. practice -> YOU type real Python; stuck? a hint ladder helps
    5. repair   -> your success brings the ship's system back online

This level uses MULTI-LINE BLOCKS. In the terminal you type the first line
(it ends with a colon), press Tab to indent the body, then press Enter on a
BLANK line to run the whole block at once. You never touch main.py to make a
level -- you only fill in this data. Keep all in-game text plain ASCII.
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 6,
    "system": "ENGINE ROOM",
    "concept": "for loops and range()",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Welcome to the Engine Room, Cadet. This is where Pyxis gets her push.",
        "The engines start with ignition pulses -- the same spark, fired again",
        "and again. Doing that by hand would mean typing the same line over and",
        "over. We have a better way.",
        "",
        "Today you learn the FOR LOOP. You write the work ONCE, and the computer",
        "repeats it for you. Type the loop line ending in ':', indent the body",
        "with Tab, then press Enter on a BLANK line to run the whole block.",
        "Let's look at a working example first.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'for step in range(3):\n'
            '    print("Step", step)'
        ),
        "caption": "A for loop repeats its indented line once for each number "
                   "range(3) gives: 0, 1, 2. So this prints  Step 0,  then "
                   "Step 1,  then  Step 2 -- three times, from one loop.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "for step in range(3):\n    print(\"Step\", step)",
            "note": "A FOR LOOP repeats its indented body once per item. The "
                    "indented line (4 spaces, from Tab) runs again and again. "
                    "Type the body, then press Enter on a BLANK line to run it.",
        },
        {
            "code": "range(3)",
            "note": "range(3) produces the numbers 0, 1, 2. It STARTS AT 0 and "
                    "STOPS BEFORE 3 -- so 3 itself is never included. That is "
                    "three numbers, which is why the loop runs three times.",
        },
        {
            "code": "range(1, 5)",
            "note": "Give range TWO numbers and it counts from the first up to "
                    "(but not including) the second. range(1, 5) produces 1, 2, "
                    "3, 4. The second number is the stop line, never reached.",
        },
        {
            "code": "for c in cylinders:\n    print(\"Firing\", c)",
            "note": "A for loop can also walk through a LIST, item by item. Each "
                    "time around, c becomes the next item. Same rule: indent the "
                    "body with Tab, then a blank line runs the block.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Fire the ignition 3 times. Write a for loop:\nfor i in range(3):  then an indented  print(\"Ignition\", i)\nPress Enter on a blank line to run it.",
            "intro": ["range(3) gives the numbers 0, 1, 2.",
                      "Indent the loop body with Tab.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "First line:  for i in range(3):",
                "Indented body:  print(\"Ignition\", i)",
                'for i in range(3):\n    print("Ignition", i)',
            ],
            "solution": 'for i in range(3):\n    print("Ignition", i)',
            "check": lambda term: "ignition" in term.last_run.lower() and "2" in term.last_run,
            "success": "Ignition 0, 1, 2 -- three pulses fired. The loop did the repeating for you.",
        },
        {
            "instruction": "Test each cylinder. Loop over the cylinders list and print \"Firing\" with each one:\nfor c in cylinders:  then  print(\"Firing\", c)",
            "intro": ["cylinders = [\"A\", \"B\", \"C\"] is loaded.",
                      "A for loop can walk through a list, item by item.",
                      "Blank line runs the block."],
            "seed": {"cylinders": ["A", "B", "C"]},
            "hints": [
                "for <name> in <list>:  picks each item in turn.",
                "Name the item c and print it.",
                'for c in cylinders:\n    print("Firing", c)',
            ],
            "solution": 'for c in cylinders:\n    print("Firing", c)',
            "check": lambda term: "firing a" in term.last_run.lower() and "firing c" in term.last_run.lower(),
            "success": "Cylinders A, B, C all firing. One loop, every item handled.",
        },
        {
            "instruction": "Add up the thrust. Start total = 0, then loop the numbers 1 to 4 and add each to total:\ntotal = 0\nfor n in range(1, 5):\n    total = total + n",
            "intro": ["range(1, 5) gives 1, 2, 3, 4 (the second number is not included).",
                      "Building up total a bit at a time is called accumulating.",
                      "Blank line runs the loop block."],
            "seed": {},
            "hints": [
                "Set total = 0 first, on its own line.",
                "Loop with  for n in range(1, 5):  and add:  total = total + n",
                "total = 0\nfor n in range(1, 5):\n    total = total + n",
            ],
            "solution": "total = 0\nfor n in range(1, 5):\n    total = total + n",
            "check": lambda term: term.ns.get("total") == 10,
            "success": "Thrust total: 10. You just summed numbers with a loop. Engines roaring!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The engines catch -- a deep, steady roar rolls through the deck plates.",
        "ENGINE ROOM: ONLINE. Pyxis can move under her own power again.",
        "",
        "You learned the FOR LOOP: write the work once, and let it repeat over a",
        "range of numbers or every item in a list. No more copy-paste.",
        "",
        "Next stop: the Shield Generator. Its power pulses until the shield is full",
        "-- so there you'll learn the WHILE LOOP. Onward, Cadet.",
    ],
}
