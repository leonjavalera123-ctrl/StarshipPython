"""
level13_datavault.py  --  LEVEL 13: The Data Vault
==================================================

Concept taught: COMBINING loops and logic -- an if INSIDE a for loop,
plus the two patterns that fall out of it: COUNTERS and FILTERS.

This is a CONSOLIDATION level. Nothing brand new -- instead we bolt
together the pieces you already own (for, if, lists, .append, counters)
into the single most common shape in all of programming: walk a list,
test each item, react. Once this clicks, you can write real programs.

HOW A LEVEL IS SHAPED
---------------------
Every level file gives the game ONE dictionary called LEVEL. main.py reads
it and runs the five-step lesson flow:

    1. brief    -> PYX explains the story + what you'll learn
    2. example  -> a working snippet of code is shown FIRST
    3. explain  -> each important piece of that snippet, in plain English
    4. practice -> YOU type real Python; stuck? a hint ladder helps
    5. repair   -> your success brings the ship's system back online

Multi-line blocks (for / if) are finished by pressing Enter on a BLANK line.
Keep all in-game text plain ASCII (the terminal font can't draw emoji).
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 13,
    "system": "DATA VAULT",
    "concept": "combining loops and logic",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Data Vault is sealed, Cadet. Inside: the ship's records.",
        "Its lock won't take a password. It takes WORKING CODE.",
        "",
        "Here every tool you own comes together at once:",
        "loops to walk the data, if to test each piece,",
        "lists and counters to keep score of what you find.",
        "",
        "This is where the pieces click. Let's crack it.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'total = 0\n'
            'for n in [4, 9, 2]:\n'
            '    if n > 3:\n'
            '        total = total + 1'
        ),
        "caption": "Walk the list, test each number, and ADD ONE every time "
                   "it passes. Here 4 and 9 are above 3 (2 is not), so total "
                   "ends at 2. We just COUNTED how many numbers beat 3.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "for n in [4, 9, 2]:\n    if n > 3:",
            "note": "An if can live INSIDE a for. The loop hands you one item "
                    "at a time; the if checks THAT item. So the test runs once "
                    "for every value in the list -- 4, then 9, then 2.",
        },
        {
            "code": "total = 0\n...\n    total = total + 1",
            "note": "The COUNTER pattern. Start a count at 0 BEFORE the loop. "
                    "Each time the if is true, add 1. When the loop ends, the "
                    "counter holds HOW MANY items passed the test.",
        },
        {
            "code": "big = []\n...\n    big.append(n)",
            "note": "The FILTER pattern. Start an EMPTY list [] before the loop. "
                    "Each time the if is true, .append() that item. When the "
                    "loop ends, the list holds only the items that matched.",
        },
        {
            "code": "for ...:\n    if ...:\n        do_this",
            "note": "INDENTATION shows the levels. The loop body is indented "
                    "ONCE. The if's body is indented TWICE -- it's inside the "
                    "loop AND inside the if. Each step in is one more 4-space tab.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Count the alarms. readings is a list of sensor values. Count how many are above 50:\nalerts = 0\nfor r in readings:\n    if r > 50:\n        alerts = alerts + 1",
            "intro": ["readings = [12, 80, 45, 99, 30] is loaded.",
                      "Put an if INSIDE a for to test every item.",
                      "Blank line runs the block."],
            "seed": {"readings": [12, 80, 45, 99, 30]},
            "hints": [
                "Start a counter:  alerts = 0",
                "Loop, and inside, if r > 50: add one to alerts.",
                "alerts = 0\nfor r in readings:\n    if r > 50:\n        alerts = alerts + 1",
            ],
            "solution": "alerts = 0\nfor r in readings:\n    if r > 50:\n        alerts = alerts + 1",
            "check": lambda term: term.ns.get("alerts") == 2,
            "success": "2 readings over 50. Loop + if + counter -- the workhorse pattern of code.",
        },
        {
            "instruction": "Collect the big ones. Build a new list named high holding only the readings above 50:\nhigh = []\nfor r in readings:\n    if r > 50:\n        high.append(r)",
            "intro": ["readings = [12, 80, 45, 99, 30] is loaded.",
                      "Start with an empty list and append the matches.",
                      "Blank line runs the block."],
            "seed": {"readings": [12, 80, 45, 99, 30]},
            "hints": [
                "Empty list:  high = []",
                "Loop, and if r > 50: high.append(r)",
                "high = []\nfor r in readings:\n    if r > 50:\n        high.append(r)",
            ],
            "solution": "high = []\nfor r in readings:\n    if r > 50:\n        high.append(r)",
            "check": lambda term: term.ns.get("high") == [80, 99],
            "success": "high = [80, 99]. You filtered a list -- a skill you'll use constantly.",
        },
        {
            "instruction": "Decode the signal. codes is a list of 1s and 0s. For each, print \"OK\" if it's 1, else \"FAIL\":\nfor c in codes:\n    if c == 1:\n        print(\"OK\")\n    else:\n        print(\"FAIL\")",
            "intro": ["codes = [1, 0, 1, 1] is loaded.",
                      "if/else inside the loop reacts to each item.",
                      "Blank line runs the block."],
            "seed": {"codes": [1, 0, 1, 1]},
            "hints": [
                "Loop each item:  for c in codes:",
                "Inside:  if c == 1: print(\"OK\")  else: print(\"FAIL\")",
                'for c in codes:\n    if c == 1:\n        print("OK")\n    else:\n        print("FAIL")',
            ],
            "solution": 'for c in codes:\n    if c == 1:\n        print("OK")\n    else:\n        print("FAIL")',
            "check": lambda term: term.last_run.lower().count("ok") == 3,
            "success": "OK, FAIL, OK, OK -- signal decoded. The vault springs open!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The Data Vault unlocks with a deep, satisfying clunk. Records restored.",
        "",
        "You combined it all: a for to walk the data, an if to judge it,",
        "and counters and lists to remember what you found.",
        "",
        "Core systems are restored, Cadet -- but the Wormhole Drive needs MORE.",
        "Before we can jump home, you must master the ADVANCED systems.",
        "First up: the NAV BEACONS, and a new kind of data called a tuple.",
    ],
}
