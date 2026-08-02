"""
level24_reactor.py  --  LEVEL 24: The Reactor Loop
==================================================

Concept taught: loop else (while/else and for/else).

An advanced, slightly unusual feature the cadet masters before the boss
challenges: a loop can carry its OWN else branch. The else runs only when the
loop finished on its own -- it was NOT cut short by a break. This is the classic
tool for search loops: break when you find it, and the else answers the question
"did we never find it?".

HOW A LEVEL IS SHAPED
---------------------
Every level file gives the game ONE dictionary called LEVEL. main.py reads it
and runs the five-step lesson flow:

    1. brief    -> PYX explains the story + what you'll learn
    2. example  -> a working snippet of code is shown FIRST
    3. explain  -> each important piece of that snippet, in plain English
    4. practice -> YOU type real Python; stuck? a hint ladder helps
    5. repair   -> your success brings the ship's system back online

A while/else or for/else is ONE compound block -- the else is part of the loop.
In the terminal you type the whole thing, then press Enter on a BLANK line to
run it all together. Keep all in-game text plain ASCII (no emoji).
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 24,
    "system": "REACTOR LOOP",
    "concept": "loop else (while/else and for/else)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Reactor Loop, Cadet. It cycles until the core reads STABLE,",
        "then it must CONFIRM that it settled on its own.",
        "",
        "Today's tool is rare but handy: the LOOP-ELSE.",
        "Yes -- a loop can have an else attached to it.",
        "It runs ONLY if the loop finished WITHOUT a break.",
        "",
        "It is perfect for searches: did we find it, or not?",
        "Let's look before you touch the reactor.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'for x in [1, 2]:\n'
            '    print(x)\n'
            'else:\n'
            '    print("loop finished")'
        ),
        "caption": "The else is attached to the LOOP, not to an if. It runs once, "
                   "AFTER the loop completes normally. This prints:  1  then  2  "
                   'then  loop finished',
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "for x in [1, 2]:\n    ...\nelse:\n    ...",
            "note": "A loop can carry an else: written at the SAME indent as the "
                    "loop word (for or while). It is not a separate statement -- "
                    "it belongs to the loop. Yes, this is an unusual feature; most "
                    "people meet else only with if. Loops can have one too.",
        },
        {
            "code": "else:  # runs if the loop finished normally",
            "note": "The else block runs ONLY when the loop ran all the way to its "
                    "natural end -- the for ran out of items, or the while "
                    "condition became False. Reached the end on its own? The else "
                    "fires.",
        },
        {
            "code": "break  # stops the loop AND skips the else",
            "note": "If a break stops the loop early, the loop is over AND the else "
                    "is SKIPPED entirely. That is the whole point: break means "
                    "'I got what I came for', so the 'finished without finding "
                    "anything' else does not run.",
        },
        {
            "code": "for x in data:\n    if match: break\nelse:\n    not_found()",
            "note": "This is the classic search pattern. Loop through the data; the "
                    "moment you find a match, break. If you never break, the loop "
                    "ends normally and the else handles the 'not found' case. Works "
                    "exactly the same on both for and while loops.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Run the reactor to 3, then confirm. Write a while loop with an else that prints \"Stable\" when it finishes:\nn = 0\nwhile n < 3:\n    print(n)\n    n = n + 1\nelse:\n    print(\"Stable\")",
            "intro": ["A loop's else runs when the loop finishes NORMALLY.",
                      "Type n = 0 first, then the while/else block.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Start  n = 0  on its own line.",
                "while n < 3:  print(n) and n = n + 1; then  else:  print(\"Stable\")",
                'n = 0\nwhile n < 3:\n    print(n)\n    n = n + 1\nelse:\n    print("Stable")',
            ],
            "solution": 'n = 0\nwhile n < 3:\n    print(n)\n    n = n + 1\nelse:\n    print("Stable")',
            "check": lambda term: "stable" in term.last_run.lower() and "2" in term.last_run,
            "success": "0, 1, 2, then Stable. The else fired because the loop finished on its own.",
        },
        {
            "instruction": "Now break out early. Search for 7; when found, print \"Found\" and break (the else must NOT run):\nn = 0\nwhile n < 10:\n    if n == 7:\n        print(\"Found\")\n        break\n    n = n + 1\nelse:\n    print(\"Never\")",
            "intro": ["break stops the loop -- and SKIPS the else.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Inside the loop:  if n == 7: print(\"Found\"); break",
                "The else only runs if the loop was NOT broken.",
                'n = 0\nwhile n < 10:\n    if n == 7:\n        print("Found")\n        break\n    n = n + 1\nelse:\n    print("Never")',
            ],
            "solution": 'n = 0\nwhile n < 10:\n    if n == 7:\n        print("Found")\n        break\n    n = n + 1\nelse:\n    print("Never")',
            "check": lambda term: "found" in term.last_run.lower() and "never" not in term.last_run.lower(),
            "success": "Found -- and 'Never' never printed. break skipped the else. That's the whole trick.",
        },
        {
            "instruction": "Use for/else to report a miss. Search the list for 99; if the loop ends without finding it, the else reports it:\nfor x in [1, 2, 3]:\n    if x == 99:\n        print(\"Hit\")\n        break\nelse:\n    print(\"No target\")",
            "intro": ["for loops can have an else too.",
                      "99 isn't in the list, so the loop finishes and else runs.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Loop the list; if x == 99: print(\"Hit\"); break.",
                "After the loop, else: print(\"No target\").",
                'for x in [1, 2, 3]:\n    if x == 99:\n        print("Hit")\n        break\nelse:\n    print("No target")',
            ],
            "solution": 'for x in [1, 2, 3]:\n    if x == 99:\n        print("Hit")\n        break\nelse:\n    print("No target")',
            "check": lambda term: "no target" in term.last_run.lower(),
            "success": "No target -- the else fired because nothing matched. Perfect for searches!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "REACTOR LOOP: ONLINE. The core cycles, settles, and confirms STABLE.",
        "",
        "You learned the rare LOOP-ELSE: an else on a loop that runs only when",
        "the loop finishes without a break -- the perfect 'found it or not?' tool.",
        "",
        "Next is the Hyperdrive Core, where functions learn to call THEMSELVES.",
        "They call it RECURSION. Steady, Cadet -- I'll guide you through it.",
    ],
}
