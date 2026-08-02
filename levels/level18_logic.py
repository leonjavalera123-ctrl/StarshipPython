"""
level18_logic.py  --  LEVEL 18: The Logic Gates
================================================

Concept taught: boolean logic -- combining True/False with  and, or, not.

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
    "number": 18,
    "system": "LOGIC GATES",
    "concept": "boolean logic: and, or, not",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Logic Gates, Cadet. An advanced system -- but you're ready.",
        "These gates route power based on COMBINED conditions.",
        "",
        "One True/False check is rarely enough out here.",
        "Sometimes BOTH things must be true. Sometimes just ONE.",
        "Sometimes you need the OPPOSITE of a check.",
        "",
        "Three little words do all of it:  and, or, not.",
        "Learn them, and you can ask the ship anything.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'age = 20\n'
            'print(age > 18 and age < 65)'
        ),
        "caption": "We check TWO things at once and join them with  and. "
                   "This prints True because both sides are True: "
                   "20 is greater than 18 AND less than 65.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "True and False",
            "note": "and is True only when BOTH sides are True. If even one "
                    "side is False, the whole thing is False. Think of two "
                    "switches in a row: power flows only if both are ON.",
        },
        {
            "code": "True or False",
            "note": "or is True when AT LEAST ONE side is True. It only "
                    "becomes False if BOTH sides are False. Two switches "
                    "side by side: power flows if either one is ON.",
        },
        {
            "code": "not True",
            "note": "not flips a value to its opposite. not True is False, "
                    "and not False is True. It simply reverses the answer "
                    "of whatever True/False check you put after it.",
        },
        {
            "code": "temp < 50 and pressure < 10",
            "note": "The real power: join actual comparisons. Each side is "
                    "its own True/False check, and  and  combines them. This "
                    "is how programs make complex decisions from many facts.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Test an AND gate. Print the result of  True and False:\nprint(True and False)",
            "intro": ["and is True only when BOTH sides are True.",
                      "Try it directly."],
            "seed": {},
            "hints": [
                "Just print the expression.",
                "True and False",
                "print(True and False)",
            ],
            "solution": "print(True and False)",
            "check": lambda term: "false" in term.last_run.lower(),
            "success": "False -- because AND needs BOTH sides True, and one was False.",
        },
        {
            "instruction": "Combine two checks. temp is 30 and pressure is 5. Make safe True only if temp < 50 AND pressure < 10:\nsafe = temp < 50 and pressure < 10\nprint(safe)",
            "intro": ["temp = 30 and pressure = 5 are loaded.",
                      "You can join two comparisons with  and."],
            "seed": {"temp": 30, "pressure": 5},
            "hints": [
                "Each side is a comparison:  temp < 50  and  pressure < 10",
                "Join them with the word  and.",
                "safe = temp < 50 and pressure < 10\nprint(safe)",
            ],
            "solution": "safe = temp < 50 and pressure < 10\nprint(safe)",
            "check": lambda term: "true" in term.last_run.lower(),
            "success": "True -- both conditions held, so the system is safe.",
        },
        {
            "instruction": "Flip a value with NOT. Print the opposite of  5 > 10:\nprint(not (5 > 10))",
            "intro": ["not flips True to False and False to True.",
                      "5 > 10 is False, so  not (5 > 10)  is True."],
            "seed": {},
            "hints": [
                "Wrap the comparison and put  not  in front.",
                "not (5 > 10)",
                "print(not (5 > 10))",
            ],
            "solution": "print(not (5 > 10))",
            "check": lambda term: "true" in term.last_run.lower(),
            "success": "True -- not flipped the False around. AND, OR, NOT: the logic gates.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The Logic Gates light up in sequence -- power routing itself,",
        "switching paths based on the conditions you taught it to read.",
        "LOGIC GATES: ONLINE.",
        "",
        "You learned the three combiners:  and (both true), or (at least",
        "one true), not (flip it). That's how code makes real decisions.",
        "",
        "Next: the Mainframe -- where data gets DEEP. Lists of dictionaries,",
        "nested together. Almost home now, Cadet. I'll be right here.",
    ],
}
