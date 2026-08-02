"""
level11_drones.py  --  LEVEL 11: The Repair Drones
==================================================

Concept taught: CLASSES and OBJECTS -- a gentle first taste of OOP.

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

A NOTE ON THE Drone CLASS BELOW
-------------------------------
Practice task 2 hands the cadet a ready-made blueprint to build from. So we
define a real module-level Drone class here and feed it into that task's seed
(seed={"Drone": Drone}). The terminal pre-loads it into its namespace, so the
cadet can type  d = Drone("Rusty")  and it just works.
"""


# ---------------------------------------------------------------------------
# A module-level blueprint, used by practice task 2's seed.
# A class is a BLUEPRINT: from it we can stamp out many drone objects.
# ---------------------------------------------------------------------------
class Drone:
    def __init__(self, name):
        self.name = name


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 11,
    "system": "REPAIR DRONES",
    "concept": "classes and objects",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Good work so far, Cadet. The hull has a hundred small breaches.",
        "I can't send you crawling through every one. We need a fleet.",
        "",
        "A fleet of repair DRONES -- and they all share the same design.",
        "For that, you'll learn a new idea: the CLASS.",
        "",
        "A class is a BLUEPRINT. Build it once, stamp out many objects from it.",
        "Each object is its own drone, with its own name. Let's see one.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'class Ship:\n'
            '    def __init__(self, name):\n'
            '        self.name = name\n'
            'pyxis = Ship("Pyxis")\n'
            'print(pyxis.name)'
        ),
        "caption": "class Ship is a BLUEPRINT. From it we BUILD one object, "
                   "pyxis, by calling Ship(\"Pyxis\"). Then we read pyxis.name "
                   "-- the name stored on that object. Running this prints:  Pyxis",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "class Ship:",
            "note": "This starts a CLASS -- a blueprint for making objects. "
                    "'Ship' is a name you invent (classes usually start with a "
                    "capital letter). Everything indented under the header is "
                    "part of the blueprint.",
        },
        {
            "code": "def __init__(self, name):",
            "note": "__init__ is a special setup method. It runs AUTOMATICALLY "
                    "every time you build a new object. Whatever you pass in -- "
                    "here a name -- arrives as its parameters so the object can "
                    "remember it.",
        },
        {
            "code": "self.name = name",
            "note": "'self' means 'THIS particular object' -- the one being "
                    "built right now. self.name = name STORES the name onto that "
                    "object, so each drone keeps its own. Later you read it back "
                    "with  pyxis.name.",
        },
        {
            "code": 'pyxis = Ship("Pyxis")',
            "note": "A METHOD is a function defined inside a class; its first "
                    "parameter is always self. You build an object by calling the "
                    "class like a function: Ship(\"Pyxis\"). You call a method on "
                    "an object the same way:  obj.method().",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Design a drone blueprint. Define a class named Drone whose __init__ stores a name:\nclass Drone:\n    def __init__(self, name):\n        self.name = name\nPress Enter on a blank line to finish the class.",
            "intro": ["A class is a blueprint for making objects.",
                      "__init__ runs when you create one; self is the new object.",
                      "Blank line finishes the class."],
            "seed": {},
            "hints": [
                "First line:  class Drone:",
                "Inside, an __init__ that saves the name:  self.name = name",
                'class Drone:\n    def __init__(self, name):\n        self.name = name',
            ],
            "solution": 'class Drone:\n    def __init__(self, name):\n        self.name = name',
            "check": lambda term: term.ns.get("Drone") is not None and getattr(term.ns["Drone"]("Sparky"), "name", None) == "Sparky",
            "success": "Blueprint complete. From this one class you can build many drones.",
        },
        {
            "instruction": "Build one. The Drone blueprint is loaded -- create a drone named \"Rusty\" and store it in d:\nd = Drone(\"Rusty\")",
            "intro": ["Drone is already defined for you.",
                      "Call the class like a function to make an object."],
            "seed": {"Drone": Drone},
            "hints": [
                "Use the class name with the drone's name in brackets.",
                "Store it in a variable named d.",
                'd = Drone("Rusty")',
            ],
            "solution": 'd = Drone("Rusty")',
            "check": lambda term: getattr(term.ns.get("d"), "name", None) == "Rusty",
            "success": "Drone 'Rusty' assembled and online. That's your first object!",
        },
        {
            "instruction": "Teach it a trick. Define a class Bot with a method beep that returns \"beep\":\nclass Bot:\n    def beep(self):\n        return \"beep\"",
            "intro": ["A method is a function that lives inside a class.",
                      "Methods always take self as their first parameter.",
                      "Blank line finishes the class."],
            "seed": {},
            "hints": [
                "Header:  class Bot:",
                "A method inside:  def beep(self):  then  return \"beep\"",
                'class Bot:\n    def beep(self):\n        return "beep"',
            ],
            "solution": 'class Bot:\n    def beep(self):\n        return "beep"',
            "check": lambda term: term.ns.get("Bot") is not None and term.ns["Bot"]().beep() == "beep",
            "success": "Bot().beep() -> 'beep'. Your drones can act on their own now.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Drones stream out of the bay, each one running your blueprint.",
        "The breaches seal one by one. REPAIR DRONES: ONLINE.",
        "",
        "You learned CLASSES today: a blueprint you stamp objects from, with",
        "__init__ to set them up, self to mean 'this object', and methods to act.",
        "",
        "But the air is getting thin. Next: LIFE SUPPORT -- where you learn ERROR",
        "HANDLING with try/except, so a single fault can't crash the whole ship.",
    ],
}
