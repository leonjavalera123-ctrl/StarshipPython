"""
level1_power.py  --  LEVEL 1: The Power Core
============================================

Concept taught: print() and your very first VARIABLE.

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
    "number": 1,
    "system": "POWER CORE",
    "concept": "print() and your first variable",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    # A list of lines PYX "says". Short lines read better on screen.
    "brief": [
        "Cadet... you're awake. Good. I am PYX, the ship's computer.",
        "We struck an asteroid field. Every system is offline. Even me, mostly.",
        "",
        "The Power Core is dark. To restart it, you must speak to me in CODE.",
        "Don't worry -- I'll show you exactly how, one piece at a time.",
        "",
        "Today's two tools: the print command, and the variable.",
        "print shows a message. A variable remembers a value for later.",
        "Let's look at an example before you try anything.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'power = 100\n'
            'print("Power level:", power)'
        ),
        "caption": "Two lines of Python. The first REMEMBERS a number. "
                   "The second SHOWS it. Running this prints:  Power level: 100",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    # A list of {code, note} cards. main.py shows the code fragment, then the
    # note under it, so you learn the syntax bit by bit.
    "explain": [
        {
            "code": "power = 100",
            "note": "This makes a VARIABLE. 'power' is a name you invented; the "
                    "= sign STORES the value 100 into that name. Read = as "
                    "'gets', not 'equals'. From now on, 'power' means 100.",
        },
        {
            "code": 'print("Power level:", power)',
            "note": "print(...) shows things on the screen. The two round "
                    "brackets () hold what to show. Here we give it two items, "
                    "separated by a comma -- print puts a space between them.",
        },
        {
            "code": '"Power level:"',
            "note": "Quotes make a STRING -- plain text. Anything inside quotes "
                    "is shown EXACTLY as written, letter for letter.",
        },
        {
            "code": "power",
            "note": "No quotes! So Python does NOT print the letters p-o-w-e-r. "
                    "It looks up the variable and prints what's inside it: 100.",
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
            "instruction": "Use print to send the message:  Power core online\n"
                           "Type it after the >>> and press Enter.",
            "intro": ["Power Core terminal ready.",
                      "Try:  print(\"your message here\")"],
            "seed": {},
            "hints": [
                "The print command needs round brackets: print(...)",
                "Your message is text, so it goes in quotes: \"Power core online\"",
                "Put it together: print(\"Power core online\")",
            ],
            "solution": 'print("Power core online")',
            # check(): we look at term.last_run -- the text the last command made.
            "check": lambda term: "power core online" in term.last_run.lower(),
            "success": "I hear you, Cadet. The console lights flicker on. Nice.",
        },
        {
            "instruction": "Now MAKE A VARIABLE. Create one named  power  and "
                           "store the number  100  in it.",
            "intro": ["The core needs a target charge level to aim for.",
                      "Store it in a variable named power."],
            "seed": {},
            "hints": [
                "A variable is:  name = value",
                "The name is power, the value is 100 (a number, so NO quotes).",
                "Type exactly:  power = 100",
            ],
            "solution": "power = 100",
            # This time we inspect term.ns -- the terminal's memory of variables.
            "check": lambda term: term.ns.get("power") == 100,
            "success": "Charge target set to 100. PYX logs it. Good work.",
        },
        {
            "instruction": "Finish it: print the message  Charging core to: 100\n"
                           "but use your power variable for the number, like the "
                           "example did.",
            "intro": ["Your power variable still holds 100.",
                      "Combine text and the variable in one print."],
            "seed": {"power": 100},
            "hints": [
                "Give print two items separated by a comma.",
                "First the text in quotes, then the variable with no quotes.",
                'Type:  print("Charging core to:", power)',
            ],
            "solution": 'print("Charging core to:", power)',
            "check": lambda term: ("charging core to" in term.last_run.lower()
                                   and "100" in term.last_run),
            "success": "POWER CORE: ONLINE. The ship hums back to life around you.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Lights blaze on across the deck. The hum of the core fills the ship.",
        "",
        "You just used the two most common tools in all of Python:",
        "  * print  -- to show information",
        "  * a variable  -- to remember a value and reuse it",
        "",
        "Power restored, Cadet. But Oxygen is running low...",
        "Next, you'll learn to do MATH with code. Breathe easy -- I'll guide you.",
    ],
}
