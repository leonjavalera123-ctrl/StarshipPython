"""
level5_cargo.py  --  LEVEL 5: The Cargo Bay
============================================

Concept taught: LISTS -- holding many values in order.

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
    "number": 5,
    "system": "CARGO BAY",
    "concept": "lists",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Into the Cargo Bay, Cadet. Crates are floating everywhere.",
        "The manifest -- our list of what's aboard -- is scrambled.",
        "",
        "One variable holds ONE value. But cargo is MANY things.",
        "For that, Python gives us the LIST.",
        "",
        "A list keeps many values in order, lined up in a row.",
        "Learn lists, and we can take inventory and set this bay right.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'crew = ["Ada", "Grace", "Alan"]\n'
            'print(crew[0])\n'
            'print(len(crew))'
        ),
        "caption": "A list of three names. crew[0] grabs the FIRST one, so "
                   "this prints:  Ada  then  3  -- because len() counts the items.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": 'crew = ["Ada", "Grace", "Alan"]',
            "note": "A LIST holds many values in ORDER, inside square brackets "
                    "[ ]. Each item is separated by a comma. This one list "
                    "remembers all three names at once, in the order you wrote them.",
        },
        {
            "code": "crew[0]",
            "note": "Square brackets with a number pick ONE item out. But lists "
                    "COUNT FROM 0, not 1 -- so [0] is the FIRST item, [1] the "
                    "second, [2] the third. crew[0] is 'Ada'.",
        },
        {
            "code": 'crew.append("Mae")',
            "note": ".append(x) ADDS x to the END of the list. The list grows by "
                    "one. After this, crew is four names long, with 'Mae' last.",
        },
        {
            "code": "len(crew)",
            "note": "len(mylist) tells you HOW MANY items the list has. With "
                    "three names inside, len(crew) is 3. Add one, and it becomes 4.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Take inventory. Make a list named supplies holding three texts: \"water\", \"food\", \"tools\".",
            "intro": ["A list holds many values in order, inside square brackets [ ].",
                      "Separate items with commas."],
            "seed": {},
            "hints": [
                "Square brackets make a list:  [ ]",
                "Put three quoted texts inside, comma-separated.",
                'supplies = ["water", "food", "tools"]',
            ],
            "solution": 'supplies = ["water", "food", "tools"]',
            "check": lambda term: term.ns.get("supplies") == ["water", "food", "tools"],
            "success": "Three crates logged. The cargo manifest updates.",
        },
        {
            "instruction": "Grab the FIRST item. Print supplies[0].\n(Lists count from 0, so [0] is the first item.)",
            "intro": ["supplies = [\"water\", \"food\", \"tools\"] is loaded.",
                      "Index 0 is the first item, 1 the second, and so on."],
            "seed": {"supplies": ["water", "food", "tools"]},
            "hints": [
                "Use square brackets with a number to pick an item.",
                "The first item is at index 0.",
                "print(supplies[0])",
            ],
            "solution": "print(supplies[0])",
            "check": lambda term: "water" in term.last_run.lower(),
            "success": "Water crate retrieved. Position 0 -- the first slot.",
        },
        {
            "instruction": "A medkit arrived. Add \"medkit\" to the end of supplies using supplies.append(\"medkit\").",
            "intro": ["supplies has 3 items right now.",
                      ".append(x) adds x to the end of a list."],
            "seed": {"supplies": ["water", "food", "tools"]},
            "hints": [
                "Lists have an .append() tool.",
                "Put the new item in quotes inside the brackets.",
                'supplies.append("medkit")',
            ],
            "solution": 'supplies.append("medkit")',
            "check": lambda term: "medkit" in term.ns.get("supplies", []),
            "success": "Medkit stowed. The list grew from 3 items to 4.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Crates settle into their racks. The manifest glows green: CARGO BAY ONLINE.",
        "",
        "You learned the LIST -- many values in order, inside [ ], counted from 0,",
        "grown with .append(), and measured with len(). Inventory is yours now.",
        "",
        "Next, the Engine Room, Cadet. Rows of pistons, all needing the same command.",
        "There you'll learn the FOR LOOP -- how to repeat work without retyping it.",
    ],
}
