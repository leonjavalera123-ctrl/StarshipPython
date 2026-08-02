"""
level29_architect.py  --  LEVEL 29: The Architect  (SECRET BOSS)
===============================================================

A hidden post-game boss. It does NOT appear in the normal level chain -- it is
flagged  "secret": True  and only unlocks AFTER the player beats the game (the
Wormhole Drive). main.py shows it as "??? CLASSIFIED" in Level Select until then,
and offers it from the victory screen.

Like the other bosses it has  "boss": True  and empty "hints" lists. Two checks
build an object, so a couple of module-level helpers sit above LEVEL.

Keep all in-game text plain ASCII. Multi-line blocks finish on a blank line.
"""


def _vault_ok(ns):
    Vault = ns.get("Vault")
    if Vault is None:
        return False
    try:
        v = Vault()
        v.store("a")
        return v.store("b") == 2 and v.items == ["a", "b"]
    except Exception:
        return False


LEVEL = {
    "number": 29,
    "system": "THE ARCHITECT",
    "concept": "SECRET BOSS -- recursion + classes + everything",
    "boss": True,
    "secret": True,

    "brief": [
        "...Cadet. You're home. You should be resting. But a signal found you.",
        "It's old. Older than me. It calls itself THE ARCHITECT --",
        "the intelligence that designed my very first line of code.",
        "",
        "It wants to test the student who surpassed its student: you.",
        "Five trials. No hints. Recursion, classes, data, text -- all of it.",
        "",
        "You don't have to do this. But I think you're ready. Let's answer it.",
    ],

    "example": {
        "code": (
            'def deep(n):\n'
            '    if n == 0:\n'
            '        return "core"\n'
            '    return deep(n - 1)\n'
            'print(deep(3))'
        ),
        "caption": "The Architect speaks in recursion -- functions that call "
                   "themselves down to a base case. deep(3) calls down to deep(0) "
                   "and returns 'core'. Match its patterns to prevail.",
    },

    "explain": [
        {
            "code": "# Secret boss rules",
            "note": "No hints. Each task gives a function/class name and one example "
                    "of what it must do. This is everything you've learned, at once.",
        },
        {
            "code": "def f(n):\n    if base_case:\n        return ...\n    return f(smaller)",
            "note": "Expect recursion and classes. Finish each block with a blank "
                    "line; the Architect then calls your code to judge it. Breathe. "
                    "You have beaten harder than this.",
        },
    ],

    "practice": [
        {
            "instruction": "Define power(base, exp) RECURSIVELY. Base case: if exp == 0 return 1; else return base * power(base, exp - 1).\nExample: power(2, 3) -> 8",
            "intro": ["SECRET BOSS -- no hints.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": "def power(base, exp):\n    if exp == 0:\n        return 1\n    return base * power(base, exp - 1)",
            "check": lambda term: callable(term.ns.get("power")) and term.ns["power"](2, 3) == 8 and term.ns["power"](5, 0) == 1,
            "success": "power(2, 3) -> 8. The recursion folded perfectly. The Architect stirs.",
        },
        {
            "instruction": "Define a class Vault: __init__ sets self.items = [], and store(self, x) appends x and RETURNS the new length.\nExample: v = Vault(); v.store(\"a\"); v.store(\"b\") -> 2",
            "intro": ["No hints. A class with state and a method.",
                      "Blank line finishes the class."],
            "seed": {},
            "hints": [],
            "solution": "class Vault:\n    def __init__(self):\n        self.items = []\n    def store(self, x):\n        self.items.append(x)\n        return len(self.items)",
            "check": lambda term: _vault_ok(term.ns),
            "success": "Vault holds and counts. Object mastery confirmed.",
        },
        {
            "instruction": "Define grand_total(records) returning the SUM of every record's \"amount\".\nExample: grand_total([{\"amount\": 3}, {\"amount\": 4}]) -> 7",
            "intro": ["No hints. Loop the records and total their amounts.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": 'def grand_total(records):\n    total = 0\n    for r in records:\n        total = total + r["amount"]\n    return total',
            "check": lambda term: callable(term.ns.get("grand_total")) and term.ns["grand_total"]([{"amount": 3}, {"amount": 4}]) == 7 and term.ns["grand_total"]([]) == 0,
            "success": "Records summed. Nested data bends to your will.",
        },
        {
            "instruction": "Define is_palindrome(word) returning True if the word reads the same backwards.\nExample: is_palindrome(\"level\") -> True ;  is_palindrome(\"nova\") -> False",
            "intro": ["No hints. Compare the word to its reverse.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": "def is_palindrome(word):\n    return word == word[::-1]",
            "check": lambda term: callable(term.ns.get("is_palindrome")) and term.ns["is_palindrome"]("level") is True and term.ns["is_palindrome"]("nova") is False,
            "success": "Symmetry detected. The Architect's defenses crack.",
        },
        {
            "instruction": "FINAL TRIAL. Define ascend(name) returning the f-string \"<name> ascends beyond the stars.\".\nExample: ascend(\"Pyxis\") -> \"Pyxis ascends beyond the stars.\"",
            "intro": ["The last line of code. Make it count.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": 'def ascend(name):\n    return f"{name} ascends beyond the stars."',
            "check": lambda term: callable(term.ns.get("ascend")) and term.ns["ascend"]("Pyxis") == "Pyxis ascends beyond the stars.",
            "success": "Pyxis ascends beyond the stars. The Architect goes quiet -- at peace.",
        },
    ],

    "repair": [
        "The ancient signal softens. 'You have surpassed all I designed,' it says.",
        "'Carry the craft forward.' And then it is gone, back into the deep.",
        "",
        "There is nothing left to fix, Cadet. You have done it all.",
        "From a single print() to recursion, classes, and a secret undone.",
        "",
        "Whatever you build next out there -- I know it will be remarkable.",
        "  -- PYX, signing off, proud.",
    ],
}
