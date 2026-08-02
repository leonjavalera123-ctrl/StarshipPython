"""
level27_kraken.py  --  LEVEL 27: The Kraken Protocol  (FINAL BOSS)
=================================================================

The hardest challenge in the game: a five-task boss that pulls together
classes, methods, loops, logic, and strings -- with NO hints.

Two checks need to create an object and call methods on it, which is more than
a one-line lambda can do, so we define small helper functions ABOVE the LEVEL
dict and call them from the check lambdas. (Each helper returns True/False and
swallows errors, so a half-typed answer never breaks the game.)

Marked with  "boss": True. Every task's "hints" list is empty on purpose.
Keep all in-game text plain ASCII. Multi-line blocks finish on a blank line.
"""


# --- helpers for the class-based checks (a lambda can't hold statements) -----
def _ship_ok(ns):
    Ship = ns.get("Ship")
    if Ship is None:
        return False
    try:
        s = Ship("Pyxis", 50)
        return s.name == "Pyxis" and s.fuel == 50
    except Exception:
        return False


def _reactor_ok(ns):
    Reactor = ns.get("Reactor")
    if Reactor is None:
        return False
    try:
        r = Reactor()
        r.charge(5)
        return r.charge(5) == 10 and r.power == 10
    except Exception:
        return False


LEVEL = {
    "number": 27,
    "system": "KRAKEN PROTOCOL",
    "concept": "FINAL BOSS -- classes + everything (no hints)",
    "boss": True,

    "brief": [
        "There it is. The Kraken -- a rogue AI the size of a moon.",
        "It hijacked a war fleet, and it stands between you and home.",
        "",
        "This is the FINAL BOSS, Cadet. Five tasks. No hints. No net.",
        "You'll build classes, charge a reactor, run safety logic, decode orders.",
        "Everything I taught you, everything you became -- it all comes down to this.",
        "",
        "Take a breath. Then let's end this.",
    ],

    "example": {
        "code": (
            'class Probe:\n'
            '    def __init__(self, name):\n'
            '        self.name = name\n'
            'p = Probe("Scout")\n'
            'print(p.name)'
        ),
        "caption": "Your final weapon is the class: a blueprint with __init__ and "
                   "self. This builds a Probe object and reads its name (Scout). "
                   "The boss tasks build on this -- no hints, just you.",
    },

    "explain": [
        {
            "code": "# Final boss rules",
            "note": "No hints. Each task gives the name and an example of what it "
                    "must do. Read the example like a target: match its result and "
                    "the protocol breaks.",
        },
        {
            "code": "class Name:\n    def __init__(self, ...):\n        self.x = ...",
            "note": "You'll define classes (remember __init__ and self) and plain "
                    "functions. Finish each block with a blank line; the protocol "
                    "then creates objects and calls your code to test it.",
        },
    ],

    "practice": [
        {
            "instruction": "Define a class Ship whose __init__(self, name, fuel) stores BOTH as self.name and self.fuel.\nExample: Ship(\"Pyxis\", 50).fuel -> 50",
            "intro": ["FINAL BOSS -- no hints.",
                      "Blank line finishes the class."],
            "seed": {},
            "hints": [],
            "solution": "class Ship:\n    def __init__(self, name, fuel):\n        self.name = name\n        self.fuel = fuel",
            "check": lambda term: _ship_ok(term.ns),
            "success": "Hull blueprint forged. The Pyxis answers your command.",
        },
        {
            "instruction": "Define a class Reactor: __init__ sets self.power = 0, and a method charge(self, amount) that ADDS amount to self.power and RETURNS the new power.\nExample: r = Reactor(); r.charge(5); r.charge(5) -> 10",
            "intro": ["No hints. A method lives inside the class and takes self.",
                      "Blank line finishes the class."],
            "seed": {},
            "hints": [],
            "solution": "class Reactor:\n    def __init__(self):\n        self.power = 0\n    def charge(self, amount):\n        self.power = self.power + amount\n        return self.power",
            "check": lambda term: _reactor_ok(term.ns),
            "success": "Reactor spun up to full power. Weapons hot.",
        },
        {
            "instruction": "Define all_safe(readings) that returns True only if EVERY reading is below 100, else False.\nExample: all_safe([10, 50, 99]) -> True ;  all_safe([10, 200]) -> False",
            "intro": ["No hints. Loop the readings; one bad value means False.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": "def all_safe(readings):\n    for r in readings:\n        if r >= 100:\n            return False\n    return True",
            "check": lambda term: callable(term.ns.get("all_safe")) and term.ns["all_safe"]([10, 50, 99]) is True and term.ns["all_safe"]([10, 200]) is False and term.ns["all_safe"]([]) is True,
            "success": "Shields verified across every sector. Holding.",
        },
        {
            "instruction": "Define decode(message) that returns the message in CAPITALS with spaces replaced by dashes.\nExample: decode(\"all clear\") -> \"ALL-CLEAR\"   (use .upper() and .replace(\" \", \"-\"))",
            "intro": ["No hints. Chain two string tools together.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": 'def decode(message):\n    return message.upper().replace(" ", "-")',
            "check": lambda term: callable(term.ns.get("decode")) and term.ns["decode"]("all clear") == "ALL-CLEAR" and term.ns["decode"]("go now") == "GO-NOW",
            "success": "Kraken's orders decoded and jammed. It's faltering!",
        },
        {
            "instruction": "FINAL STRIKE. Define victory(name) that returns the f-string \"<name> defeats the Kraken!\".\nExample: victory(\"Pyxis\") -> \"Pyxis defeats the Kraken!\"",
            "intro": ["The last line of code you need to win.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": 'def victory(name):\n    return f"{name} defeats the Kraken!"',
            "check": lambda term: callable(term.ns.get("victory")) and term.ns["victory"]("Pyxis") == "Pyxis defeats the Kraken!",
            "success": "Pyxis defeats the Kraken! Its lights go dark, one by one.",
        },
    ],

    "repair": [
        "The Kraken shudders, its stolen fleet drifting loose, and goes still.",
        "You beat it -- not with weapons, but with clean, careful code.",
        "",
        "The path home is clear at last. One jump remains, Cadet.",
        "",
        "I've watched you grow from one nervous print() into THIS.",
        "Power up the Wormhole Drive. Let's go home.",
    ],
}
