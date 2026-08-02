"""
level3_comms.py  --  LEVEL 3: The Comms Antenna
===============================================

Concept taught: strings, f-strings, and text methods.

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
    "number": 3,
    "system": "COMMS ANTENNA",
    "concept": "strings, f-strings, and text methods",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    # A list of lines PYX "says". Short lines read better on screen.
    "brief": [
        "Power hums, air flows. Now we are alone and unheard, Cadet.",
        "The Comms Antenna is dead. No signal goes out, no help comes in.",
        "",
        "To call for rescue we must build a message in CODE.",
        "Messages are made of STRINGS -- that is just a word for TEXT.",
        "",
        "Today you learn to write text, slot variables into it, and shape it.",
        "Get this right and a distress call leaves the ship. Let's begin.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'name = "Cadet"\n'
            'print(f"Welcome aboard, {name}!")'
        ),
        "caption": "The first line stores the text Cadet. The second prints:  "
                   "Welcome aboard, Cadet!  The {name} part got swapped for its value.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    # A list of {code, note} cards. main.py shows the code fragment, then the
    # note under it, so you learn the syntax bit by bit.
    "explain": [
        {
            "code": '"Cadet"',
            "note": "Quotes make a STRING -- plain text. Anything between the "
                    "quotes is kept EXACTLY as written, letter for letter. You "
                    "can use double quotes or single quotes; just match them.",
        },
        {
            "code": 'f"Welcome aboard, {name}!"',
            "note": "Put an f right before the opening quote and it becomes an "
                    "f-string. Inside it, { } is a window: Python looks up the "
                    "variable named in the braces and drops its VALUE into the text.",
        },
        {
            "code": '"hi".upper()',
            "note": "Text comes with built-in tools called METHODS. You attach "
                    "one with a dot. .upper() hands back a SHOUTING copy: "
                    '"hi".upper() gives "HI". The original text is left unchanged.',
        },
        {
            "code": 'len("word")',
            "note": "len(...) counts how many characters are in a string. "
                    'len("word") is 4. Handy for checking a message is not empty '
                    "before you transmit it.",
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
            "instruction": "Set your call sign. Make a variable named callsign and store the text \"Pyxis\" in it.",
            "intro": ["Comms console ready.", "Remember: text goes in quotes."],
            "seed": {},
            "hints": [
                "A variable is:  name = value",
                "The value is text, so it needs quotes: \"Pyxis\"",
                "Type:  callsign = \"Pyxis\"",
            ],
            "solution": 'callsign = "Pyxis"',
            "check": lambda term: term.ns.get("callsign") == "Pyxis",
            "success": "Call sign locked in: Pyxis. The antenna swivels toward Earth.",
        },
        {
            "instruction": "Build the distress call. Make message = f\"Calling Earth from {callsign}\" then print(message).",
            "intro": ["callsign is already set to \"Pyxis\".",
                      "An f-string lets you drop a variable inside text with { }."],
            "seed": {"callsign": "Pyxis"},
            "hints": [
                "Start the text with an f and quotes:  f\"...\"",
                "Put the variable in curly braces:  {callsign}",
                'Type:  message = f"Calling Earth from {callsign}"  then  print(message)',
            ],
            "solution": 'message = f"Calling Earth from {callsign}"\nprint(message)',
            "check": lambda term: "calling earth from pyxis" in term.last_run.lower(),
            "success": "Signal away! 'Calling Earth from Pyxis' beams into the dark.",
        },
        {
            "instruction": "Make it LOUD. Print the word mayday in capital letters using .upper().",
            "intro": ["Text has built-in tools called methods.",
                      "\"hello\".upper() gives \"HELLO\"."],
            "seed": {},
            "hints": [
                "Start with the text in quotes:  \"mayday\"",
                "Attach .upper() to it:  \"mayday\".upper()",
                'Type:  print("mayday".upper())',
            ],
            "solution": 'print("mayday".upper())',
            "check": lambda term: "MAYDAY" in term.last_run,
            "success": "MAYDAY broadcast on all channels. Someone will hear us.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The antenna locks on and a green TRANSMITTING light blinks steadily.",
        "Far away, a station answers: they heard us. Help is coming, Cadet.",
        "",
        "You can now work with STRINGS: write text in quotes, slot variables in",
        "with an f-string, and reshape it with methods like .upper().",
        "",
        "But a rescue ship needs a course. Next: the Navigation system,",
        "where you teach the ship to make DECISIONS with if and else.",
    ],
}
