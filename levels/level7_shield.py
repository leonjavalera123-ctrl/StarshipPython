"""
level7_shield.py  --  LEVEL 7: The Shield Generator
===================================================

Concept taught: while loops -- code that REPEATS until a condition is met.

HOW A LEVEL IS SHAPED
---------------------
Every level file gives the game ONE dictionary called LEVEL. main.py reads it
and runs the five-step lesson flow:

    1. brief    -> PYX explains the story + what you'll learn
    2. example  -> a working snippet of code is shown FIRST
    3. explain  -> each important piece of that snippet, in plain English
    4. practice -> YOU type real Python; stuck? a hint ladder helps
    5. repair   -> your success brings the ship's system back online

This level uses MULTI-LINE BLOCKS. Type the first line ending in a colon, then
press Enter. Indent the body with Tab. When the block is done, press Enter on
an EMPTY line to run it all. Keep all in-game text plain ASCII.
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 7,
    "system": "SHIELD GENERATOR",
    "concept": "while loops",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Good work, Cadet. The Shield Generator is next -- and we need it.",
        "Debris is still drifting toward the hull out there.",
        "",
        "A shield doesn't snap on. It must CHARGE UP, a little at a time,",
        "and keep charging UNTIL it reaches full strength.",
        "",
        "For that you need a new tool: the WHILE LOOP.",
        "A while loop repeats the same lines over and over, as long as a",
        "condition stays true. Let's watch one count before you try it.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'countdown = 3\n'
            'while countdown > 0:\n'
            '    print(countdown)\n'
            '    countdown = countdown - 1'
        ),
        "caption": "A while loop. As long as countdown > 0 is true, it prints "
                   "the number, then makes it smaller. It prints  3, 2, 1  "
                   "and then stops -- because 0 > 0 is false.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "while countdown > 0:",
            "note": "A WHILE LOOP repeats its indented lines AS LONG AS the "
                    "condition (countdown > 0) is true. The line ends in a "
                    "colon : -- that starts a block. Press Enter, then indent "
                    "the body with Tab. Press Enter on a BLANK line to run it.",
        },
        {
            "code": "countdown > 0",
            "note": "This condition is checked BEFORE each pass. If it's true, "
                    "the loop runs the body once more, then checks again. The "
                    "moment it's false, the loop stops and skips the body.",
        },
        {
            "code": "countdown = countdown - 1",
            "note": "This is the most important line! You MUST change the "
                    "variable inside the loop. If countdown never shrinks, the "
                    "condition stays true forever -- an INFINITE LOOP that "
                    "never stops. Always move the loop toward its end.",
        },
        {
            "code": "total = total + 1",
            "note": "Each pass can BUILD UP a value -- adding to a number, or "
                    "joining onto a string ( word = word + \"!\" ). The "
                    "variable grows a little every pass. That is how a shield "
                    "charges from 0 up to full, one step at a time.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Charge the shield to 3. Start charge = 0, then while charge < 3 add 1 and print it:\ncharge = 0\nwhile charge < 3:\n    charge = charge + 1\n    print(\"Charging\", charge)",
            "intro": ["A while loop repeats AS LONG AS its condition is True.",
                      "You must change charge inside, or it loops forever.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Set charge = 0 first.",
                "while charge < 3:  then indented:  charge = charge + 1",
                'charge = 0\nwhile charge < 3:\n    charge = charge + 1\n    print("Charging", charge)',
            ],
            "solution": 'charge = 0\nwhile charge < 3:\n    charge = charge + 1\n    print("Charging", charge)',
            "check": lambda term: term.ns.get("charge") == 3,
            "success": "Shield at full charge: 3. The loop stopped the moment the condition failed.",
        },
        {
            "instruction": "Drain the reserves. power is 10. While power > 0, subtract 5 each time:\nwhile power > 0:\n    power = power - 5",
            "intro": ["power is already set to 10.",
                      "Each pass lowers power until the condition is False.",
                      "Blank line runs the block."],
            "seed": {"power": 10},
            "hints": [
                "Condition:  while power > 0:",
                "Indented body lowers it:  power = power - 5",
                "while power > 0:\n    power = power - 5",
            ],
            "solution": "while power > 0:\n    power = power - 5",
            "check": lambda term: term.ns.get("power") == 0,
            "success": "Reserves drained to 0. 10 -> 5 -> 0, then the loop ended.",
        },
        {
            "instruction": "Send 4 pings. Start beeps = \"\" and count = 0, then while count < 4 add \"beep \" and count up:\nbeeps = \"\"\ncount = 0\nwhile count < 4:\n    beeps = beeps + \"beep \"\n    count = count + 1",
            "intro": ["You can build a string a piece at a time, just like a number.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Two starters:  beeps = \"\"  and  count = 0",
                "Loop while count < 4, adding to beeps and to count.",
                'beeps = ""\ncount = 0\nwhile count < 4:\n    beeps = beeps + "beep "\n    count = count + 1',
            ],
            "solution": 'beeps = ""\ncount = 0\nwhile count < 4:\n    beeps = beeps + "beep "\n    count = count + 1',
            "check": lambda term: term.ns.get("beeps", "").count("beep") == 4,
            "success": "beep beep beep beep -- four pings sent. Shields holding, Cadet!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "A deep hum rises through the deck -- SHIELDS ONLINE. The debris glances off.",
        "",
        "You learned the WHILE LOOP: it repeats its block as long as a condition",
        "is true, and stops the moment that condition turns false -- so long as",
        "you change the variable inside to get there.",
        "",
        "Next: the Star Charts are scrambled. To map the stars you'll learn",
        "DICTIONARIES -- pairing each name with its value. Onward, Cadet.",
    ],
}
