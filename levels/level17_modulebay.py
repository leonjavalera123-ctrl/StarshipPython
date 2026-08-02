"""
level17_modulebay.py  --  LEVEL 17: The Module Bay
==================================================

Concept taught: importing modules -- using ready-made toolboxes.

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
    "number": 17,
    "system": "MODULE BAY",
    "concept": "importing modules",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Module Bay is sealed, Cadet. This is where the ship keeps its TOOLS.",
        "",
        "Here's a secret real coders learn: you don't have to build everything",
        "yourself. Python comes with ready-made toolboxes called MODULES.",
        "",
        "Need square roots? There's a toolbox for that: math.",
        "Need a dice roll or a surprise? There's one for that too: random.",
        "",
        "You just IMPORT a toolbox, then reach in and grab the tool you need.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'import math\n'
            'print(math.sqrt(25))'
        ),
        "caption": "import opens a toolbox; here the built-in math toolbox. "
                   "Then we use its sqrt tool. Running this prints:  5.0",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "import math",
            "note": "import brings in a MODULE -- a collection of ready-made "
                    "tools someone already wrote and tested for you. After this "
                    "line, the whole math toolbox is open and ready to use.",
        },
        {
            "code": "math.sqrt(25)",
            "note": "To use a tool, write the module name, a dot, then the tool: "
                    "module.function(). Read the dot as 'inside'. So this means "
                    "'the sqrt tool inside math', given the number 25.",
        },
        {
            "code": "math.sqrt, math.floor, math.pi",
            "note": "The math toolbox is packed: sqrt (square root), floor "
                    "(round down to a whole number), pi (the number 3.14159...), "
                    "and many more. One import, lots of handy tools.",
        },
        {
            "code": "import random  ->  random.randint(1, 6)",
            "note": "The random toolbox makes random numbers -- perfect for "
                    "games! random.randint(1, 6) picks a whole number from 1 to "
                    "6, just like rolling a die. Surprise on demand.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Load the math toolbox and use it. Import math, then print the square root of 16:\nimport math\nprint(math.sqrt(16))",
            "intro": ["import brings in a module -- a toolbox of ready-made functions.",
                      "Use a tool with  module.function()."],
            "seed": {},
            "hints": [
                "First line:  import math",
                "Then:  print(math.sqrt(16))",
                "import math\nprint(math.sqrt(16))",
            ],
            "solution": "import math\nprint(math.sqrt(16))",
            "check": lambda term: "4.0" in term.last_run,
            "success": "4.0 -- math.sqrt did the work for you. No need to reinvent it.",
        },
        {
            "instruction": "Round down. Import math and print math.floor(9.9) (which chops off the decimal):\nimport math\nprint(math.floor(9.9))",
            "intro": ["A module can hold many tools.",
                      "math.floor rounds a number DOWN to a whole number."],
            "seed": {},
            "hints": [
                "Import math first.",
                "Use math.floor(9.9).",
                "import math\nprint(math.floor(9.9))",
            ],
            "solution": "import math\nprint(math.floor(9.9))",
            "check": lambda term: term.last_run.strip().endswith("9"),
            "success": "9 -- floored down from 9.9. Modules are full of handy tools like this.",
        },
        {
            "instruction": "Roll a die. Import random and print a random number from 1 to 6:\nimport random\nprint(random.randint(1, 6))",
            "intro": ["The random module makes games fun -- it produces random numbers.",
                      "random.randint(1, 6) is like rolling a six-sided die."],
            "seed": {},
            "hints": [
                "First line:  import random",
                "Then:  print(random.randint(1, 6))",
                "import random\nprint(random.randint(1, 6))",
            ],
            "solution": "import random\nprint(random.randint(1, 6))",
            "check": lambda term: term.last_run.strip() in {"1", "2", "3", "4", "5", "6"},
            "success": "You rolled a die with code! random is how games add surprise.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The Module Bay hums to life, shelves of tools sliding into reach.",
        "",
        "MODULE BAY: ONLINE.",
        "",
        "Recap: import opens a toolbox, and module.function() uses a tool inside it.",
        "Next up: the Logic Gates, where you learn BOOLEAN LOGIC -- and, or, not.",
    ],
}
