"""
level25_hyperdrive.py  --  LEVEL 25: The Hyperdrive Core
=======================================================

Concept taught: recursion (functions that call themselves).

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
    "number": 25,
    "system": "HYPERDRIVE CORE",
    "concept": "recursion (functions that call themselves)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Hyperdrive Core, Cadet. The last great system on this ship.",
        "It folds space by repeating a single pattern WITHIN itself.",
        "",
        "To wake it, you must learn the strangest tool in Python: RECURSION.",
        "Recursion is a function that calls ITSELF.",
        "",
        "It always needs a BASE CASE -- a stopping point -- or it never ends.",
        "Each call handles a smaller piece, then the answers fold together.",
        "Look at the example. It feels odd at first. That is normal.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'def factorial(n):\n'
            '    if n <= 1:\n'
            '        return 1\n'
            '    return n * factorial(n - 1)\n'
            'print(factorial(4))'
        ),
        "caption": "This prints 24. The function calls ITSELF with a smaller n "
                   "(4, then 3, then 2, then 1). When n reaches 1 the base case "
                   "stops it, and the answers multiply back up: 4*3*2*1 = 24.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "return n * factorial(n - 1)",
            "note": "Recursion = a function that CALLS ITSELF. See how factorial "
                    "uses its own name inside its own body? That is the whole "
                    "idea: the function solves part of the problem, then asks "
                    "ITSELF to solve the rest.",
        },
        {
            "code": "if n <= 1:\n    return 1",
            "note": "This is the BASE CASE -- the stopping condition. Without it "
                    "the function would call itself forever and crash. EVERY "
                    "recursive function MUST have a base case. Always write it "
                    "first.",
        },
        {
            "code": "factorial(n - 1)",
            "note": "Each call works on a SMALLER version of the problem: n - 1. "
                    "Step by step it shrinks toward the base case. That steady "
                    "shrinking is what guarantees the recursion eventually stops.",
        },
        {
            "code": "4 * (3 * (2 * (1)))",
            "note": "The calls STACK UP -- factorial(4) waits on factorial(3), "
                    "which waits on factorial(2), and so on. At the base case they "
                    "UNWIND, each returning its answer up the chain, combining "
                    "into 24. If this feels strange, you are not alone -- recursion "
                    "is famously mind-bending at first. It clicks with practice.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Define factorial(n) recursively. Base case: if n <= 1 return 1; otherwise return n * factorial(n - 1):\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)",
            "intro": ["Recursion = a function that calls ITSELF.",
                      "The base case (n <= 1) stops it.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [
                "Base case first:  if n <= 1: return 1",
                "Then the recursive step:  return n * factorial(n - 1)",
                "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)",
            ],
            "solution": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)",
            "check": lambda term: callable(term.ns.get("factorial")) and term.ns["factorial"](5) == 120 and term.ns["factorial"](1) == 1,
            "success": "factorial(5) -> 120. The function called itself all the way down to 1.",
        },
        {
            "instruction": "Define sum_to(n) recursively. Base case: if n == 0 return 0; otherwise return n + sum_to(n - 1):\ndef sum_to(n):\n    if n == 0:\n        return 0\n    return n + sum_to(n - 1)",
            "intro": ["Same shape: a base case, then a smaller call.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [
                "Base case:  if n == 0: return 0",
                "Recursive step:  return n + sum_to(n - 1)",
                "def sum_to(n):\n    if n == 0:\n        return 0\n    return n + sum_to(n - 1)",
            ],
            "solution": "def sum_to(n):\n    if n == 0:\n        return 0\n    return n + sum_to(n - 1)",
            "check": lambda term: callable(term.ns.get("sum_to")) and term.ns["sum_to"](5) == 15 and term.ns["sum_to"](0) == 0,
            "success": "sum_to(5) -> 15. 5 + 4 + 3 + 2 + 1, built by the function calling itself.",
        },
        {
            "instruction": "Build a list with recursion. Define countdown(n): if n == 0 return the empty list []; otherwise return [n] + countdown(n - 1):\ndef countdown(n):\n    if n == 0:\n        return []\n    return [n] + countdown(n - 1)",
            "intro": ["Recursion can build lists too.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [
                "Base case:  if n == 0: return []",
                "Recursive step:  return [n] + countdown(n - 1)",
                "def countdown(n):\n    if n == 0:\n        return []\n    return [n] + countdown(n - 1)",
            ],
            "solution": "def countdown(n):\n    if n == 0:\n        return []\n    return [n] + countdown(n - 1)",
            "check": lambda term: callable(term.ns.get("countdown")) and term.ns["countdown"](3) == [3, 2, 1] and term.ns["countdown"](0) == [],
            "success": "countdown(3) -> [3, 2, 1]. Recursion assembled the whole list. Hyperdrive online!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Space folds. The Hyperdrive Core blazes to life, humming with power.",
        "",
        "You taught a function to call ITSELF -- recursion -- always with a",
        "base case to stop it, each call a smaller step toward that finish.",
        "",
        "Every system aboard is online now, Cadet. But you are not done.",
        "The BOSS CHALLENGES begin next: the Asteroid Gauntlet. No hints. Just you.",
    ],
}
