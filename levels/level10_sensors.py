"""
level10_sensors.py  --  LEVEL 10: The Sensor Array
==================================================

Concept taught: functions with multiple parameters, default values, and
                using if to decide what to return.

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

A function definition is a multi-line BLOCK. In the practice terminal you type
the header line ending in ':', then the indented body, then press Enter on a
BLANK line to finish and run the whole definition.
"""


# ---------------------------------------------------------------------------
# The five-step lesson, as plain data.
# ---------------------------------------------------------------------------
LEVEL = {
    "number": 10,
    "system": "SENSOR ARRAY",
    "concept": "functions with multiple parameters, defaults, and logic",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Sensor Array is awake, Cadet, but its functions are too simple.",
        "Each one takes a single input. The array needs to think harder.",
        "",
        "Today we make functions SMARTER in three ways:",
        "  * give a function several inputs, separated by commas",
        "  * give an input a DEFAULT, used when the caller skips it",
        "  * use if INSIDE a function to decide what to return",
        "",
        "Same blank-line-finishes-the-block rule as before. Let's look.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'def power(base, boost=10):\n'
            '    return base + boost\n'
            'print(power(5))\n'
            'print(power(5, 50))'
        ),
        "caption": "power takes two inputs. The second, boost, has a DEFAULT of "
                   "10. So power(5) uses boost=10 and gives 15. power(5, 50) "
                   "overrides it and gives 55.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "def area(w, h):",
            "note": "A function can take SEVERAL parameters -- just list them "
                    "inside the brackets, separated by commas. Here area expects "
                    "two values: w and h. The caller must give one for each.",
        },
        {
            "code": 'def scan(target, unit="km"):',
            "note": "Putting = after a parameter gives it a DEFAULT value. If the "
                    "caller leaves unit out, Python fills in \"km\" for you. "
                    "Defaults always come AFTER the plain parameters.",
        },
        {
            "code": "scan(5)   ...or...   scan(5, \"ly\")",
            "note": "Because unit has a default, you can call with OR without it. "
                    "scan(5) uses \"km\". scan(5, \"ly\") replaces the default "
                    "with \"ly\". The optional argument is yours to skip.",
        },
        {
            "code": "if level > 80:\n    return \"Critical\"\nreturn \"Normal\"",
            "note": "A function can use if to CHOOSE what to return. return hands "
                    "back a value AND immediately ends the function -- so if the "
                    "if is true, \"Normal\" below is never reached.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Two inputs. Define area(w, h) that returns w * h:\ndef area(w, h):\n    return w * h",
            "intro": ["A function can take more than one parameter, separated by commas.",
                      "Blank line finishes the definition."],
            "seed": {},
            "hints": [
                "Header with two inputs:  def area(w, h):",
                "Return their product:  return w * h",
                "def area(w, h):\n    return w * h",
            ],
            "solution": "def area(w, h):\n    return w * h",
            "check": lambda term: callable(term.ns.get("area")) and term.ns["area"](2, 3) == 6,
            "success": "area(2, 3) -> 6. Two inputs, one answer. Sensors aligning.",
        },
        {
            "instruction": "Give a default. Define scan(target, unit=\"km\") that returns an f-string \"<target> <unit>\":\ndef scan(target, unit=\"km\"):\n    return f\"{target} {unit}\"",
            "intro": ["unit=\"km\" is a DEFAULT -- used when the caller doesn't give one.",
                      "Blank line finishes the definition."],
            "seed": {},
            "hints": [
                "Give the second parameter a default with = :  unit=\"km\"",
                "Return:  return f\"{target} {unit}\"",
                'def scan(target, unit="km"):\n    return f"{target} {unit}"',
            ],
            "solution": 'def scan(target, unit="km"):\n    return f"{target} {unit}"',
            "check": lambda term: callable(term.ns.get("scan")) and term.ns["scan"](5) == "5 km" and term.ns["scan"](5, "ly") == "5 ly",
            "success": "scan(5) -> '5 km', scan(5, 'ly') -> '5 ly'. Defaults save you typing.",
        },
        {
            "instruction": "Decide inside a function. Define alert(level) that returns \"Critical\" if level > 80, otherwise \"Normal\":\ndef alert(level):\n    if level > 80:\n        return \"Critical\"\n    return \"Normal\"",
            "intro": ["A function can use if to choose what to return.",
                      "return immediately ends the function.",
                      "Blank line finishes the definition."],
            "seed": {},
            "hints": [
                "Header:  def alert(level):",
                "Inside:  if level > 80:  return \"Critical\"  then  return \"Normal\"",
                'def alert(level):\n    if level > 80:\n        return "Critical"\n    return "Normal"',
            ],
            "solution": 'def alert(level):\n    if level > 80:\n        return "Critical"\n    return "Normal"',
            "check": lambda term: callable(term.ns.get("alert")) and term.ns["alert"](90) == "Critical" and term.ns["alert"](10) == "Normal",
            "success": "alert(90)='Critical', alert(10)='Normal'. Smart sensors online!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "SENSOR ARRAY: ONLINE. Sweeps of light fan out into the dark.",
        "",
        "Your functions can think now: many inputs, sensible defaults, and an",
        "if to choose what to return. That is real, practical Python.",
        "",
        "Next, the Repair Drones stir in the hold. To command them you'll learn",
        "CLASSES and OBJECTS -- blueprints for building your own kinds of things.",
    ],
}
