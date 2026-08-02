"""
level9_airlock.py  --  LEVEL 9: The Airlock Controls
====================================================

Concept taught: FUNCTIONS -- def, parameters, and return.

HOW A LEVEL IS SHAPED
---------------------
Every level file gives the game ONE dictionary called LEVEL. main.py reads it
and runs the five-step lesson flow:

    1. brief    -> PYX explains the story + what you'll learn
    2. example  -> a working snippet of code is shown FIRST
    3. explain  -> each important piece of that snippet, in plain English
    4. practice -> YOU type real Python; stuck? a hint ladder helps
    5. repair   -> your success brings the ship's system back online

A FUNCTION is a multi-line block, like if and for. You type the header (which
ends in a colon), indent the body with Tab, then press Enter on a BLANK line
to FINISH the definition. Keep all in-game text plain ASCII.
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 9,
    "system": "AIRLOCK CONTROLS",
    "concept": "functions (def, parameters, return)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Airlock Controls are jammed, Cadet. We cycle them constantly --",
        "open, seal, check pressure, report status -- the same steps, over and over.",
        "",
        "Copying those steps everywhere is how mistakes creep in.",
        "What we need is a reusable COMMAND we can write once and call any time.",
        "",
        "That command is a FUNCTION. You define it with the word def.",
        "Package the code once, give it a name, then call it whenever you like.",
        "Let's look at one before you build your own.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'def greet(name):\n'
            '    return "Hello, " + name\n'
            '\n'
            'print(greet("Cadet"))'
        ),
        "caption": "def greet(name): makes a reusable command called greet. "
                   "Its body builds a message and RETURNS it. Later we CALL it "
                   'with greet("Cadet"), and print shows the result:  Hello, Cadet',
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "def greet(name):",
            "note": "def names a reusable block of code -- here it's called "
                    "greet. The header ENDS IN A COLON, and the lines under it "
                    "(the body) must be INDENTED. After the body, press Enter on "
                    "a BLANK line to finish the definition.",
        },
        {
            "code": "(name)",
            "note": "The words inside the round brackets are PARAMETERS -- the "
                    "inputs the function expects. Inside the body, 'name' stands "
                    "for whatever value you hand in when you call it.",
        },
        {
            "code": 'return "Hello, " + name',
            "note": "return hands a value back to whoever CALLED the function. "
                    "It's the function's answer. Without return, calling it gives "
                    "you nothing useful back.",
        },
        {
            "code": 'print(greet("Cadet"))',
            "note": "You CALL a function by writing its name with arguments in "
                    'brackets: greet("Cadet"). That runs the body with name set '
                    'to "Cadet", returns "Hello, Cadet", and print shows it.',
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Build a reusable command. Define a function named open_airlock that returns the text \"Airlock open\":\ndef open_airlock():\n    return \"Airlock open\"\nPress Enter on a blank line to finish the function.",
            "intro": ["def names a reusable block of code.",
                      "return hands a value back to whoever calls it.",
                      "Blank line finishes the definition."],
            "seed": {},
            "hints": [
                "Start with:  def open_airlock():",
                "Indented body:  return \"Airlock open\"",
                'def open_airlock():\n    return "Airlock open"',
            ],
            "solution": 'def open_airlock():\n    return "Airlock open"',
            "check": lambda term: callable(term.ns.get("open_airlock")) and term.ns["open_airlock"]() == "Airlock open",
            "success": "Function ready. Now you can open the airlock any time by calling it.",
        },
        {
            "instruction": "Make a function that does math. Define add_air(amount) that returns amount + 5:\ndef add_air(amount):\n    return amount + 5",
            "intro": ["Words inside the ( ) are parameters -- inputs to the function.",
                      "Blank line finishes the definition."],
            "seed": {},
            "hints": [
                "Put the input name in the brackets:  def add_air(amount):",
                "Return the result:  return amount + 5",
                "def add_air(amount):\n    return amount + 5",
            ],
            "solution": "def add_air(amount):\n    return amount + 5",
            "check": lambda term: callable(term.ns.get("add_air")) and term.ns["add_air"](10) == 15,
            "success": "Give it 10, it returns 15. One function, endless reuse.",
        },
        {
            "instruction": "Report a status. Define status(name) that returns an f-string \"<name> ready\":\ndef status(name):\n    return f\"{name} ready\"",
            "intro": ["A function can build and return an f-string.",
                      "Blank line finishes the definition."],
            "seed": {},
            "hints": [
                "Header:  def status(name):",
                "Return an f-string with the parameter inside:  return f\"{name} ready\"",
                'def status(name):\n    return f"{name} ready"',
            ],
            "solution": 'def status(name):\n    return f"{name} ready"',
            "check": lambda term: callable(term.ns.get("status")) and term.ns["status"]("Drone") == "Drone ready",
            "success": "status(\"Drone\") -> \"Drone ready\". The airlock obeys your commands now.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The airlock seals hiss, then cycle smoothly. AIRLOCK: ONLINE.",
        "",
        "You learned to write FUNCTIONS: def names a reusable block, parameters",
        "feed it inputs, and return hands an answer back when you CALL it.",
        "",
        "Next stop: the Sensor Array. There we'll teach functions a few new tricks",
        "-- default values and logic -- so they can think for themselves. Onward, Cadet.",
    ],
}
