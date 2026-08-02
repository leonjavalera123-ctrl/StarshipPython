"""
level19_mainframe.py  --  LEVEL 19: The Mainframe
=================================================

Concept taught: nested data (lists of dictionaries).

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
    "number": 19,
    "system": "MAINFRAME",
    "concept": "nested data (lists of dictionaries)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Mainframe wakes, Cadet. It stores the whole fleet's records.",
        "And those records are data INSIDE data -- the shape of the real world.",
        "",
        "You already know lists (ordered rows) and dictionaries (labelled facts).",
        "Today we combine them: a LIST OF DICTIONARIES.",
        "Each dictionary is one ship's record; the list holds them all.",
        "",
        "Master this and you can read any real data. It is the last advanced",
        "system before the jump home. Let's bring the Mainframe online.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'ships = [{"name": "Pyxis", "fuel": 80}]\n'
            'print(ships[0]["name"])'
        ),
        "caption": "A LIST holding one DICTIONARY. ships[0] grabs the first "
                   "record (a dict); then [\"name\"] reads its value. Running "
                   "this prints:  Pyxis",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": 'ships = [{"name": "Pyxis", "fuel": 80}]',
            "note": "Data can NEST. A list can hold dictionaries -- the square "
                    "brackets [ ] make the list, and inside it sits a { } dict. "
                    "Each dictionary is one RECORD: a little bundle of facts.",
        },
        {
            "code": 'fleet[1]["name"]',
            "note": "Chain the brackets to reach inside. First [1] picks the "
                    "item by POSITION (the 2nd record). That gives you a dict, "
                    "and [\"name\"] then reads its value by KEY. Position, then key.",
        },
        {
            "code": 'for ship in fleet:\n    print(ship["name"])',
            "note": "Loop over the list to process EVERY record. Each turn, "
                    "'ship' is one dictionary. Inside the loop you read its keys "
                    "like ship[\"name\"] or ship[\"fuel\"] -- one record at a time.",
        },
        {
            "code": '[{"name": ..., "fuel": ...}, {...}, {...}]',
            "note": "This shape is EVERYWHERE in real data: a list of users, of "
                    "products, of ships -- each one a dict of details. Learn it "
                    "once and you can read almost any data you'll ever meet.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Log the fleet. Make a list named fleet containing two dictionaries:\nfleet = [{\"name\": \"Pyxis\", \"fuel\": 80}, {\"name\": \"Vela\", \"fuel\": 30}]",
            "intro": ["Data can nest: here, a LIST that holds DICTIONARIES.",
                      "Each dict is one ship's record."],
            "seed": {},
            "hints": [
                "Outer square brackets for the list.",
                "Inside, two dicts separated by a comma, each with name and fuel.",
                'fleet = [{"name": "Pyxis", "fuel": 80}, {"name": "Vela", "fuel": 30}]',
            ],
            "solution": 'fleet = [{"name": "Pyxis", "fuel": 80}, {"name": "Vela", "fuel": 30}]',
            "check": lambda term: isinstance(term.ns.get("fleet"), list) and len(term.ns["fleet"]) == 2 and term.ns["fleet"][0].get("name") == "Pyxis",
            "success": "Two ship records logged. A list of dictionaries -- real-world data shape.",
        },
        {
            "instruction": "Read a nested value. Print the name of the SECOND ship:\nprint(fleet[1][\"name\"])",
            "intro": ["fleet is loaded with two ship dicts.",
                      "Chain the brackets: [1] picks the 2nd ship, then [\"name\"] its name."],
            "seed": {"fleet": [{"name": "Pyxis", "fuel": 80}, {"name": "Vela", "fuel": 30}]},
            "hints": [
                "First pick the ship by position:  fleet[1]",
                "Then its name by key:  [\"name\"]",
                'print(fleet[1]["name"])',
            ],
            "solution": 'print(fleet[1]["name"])',
            "check": lambda term: "vela" in term.last_run.lower(),
            "success": "Vela -- reached by [1] then [\"name\"]. Chaining brackets digs into nested data.",
        },
        {
            "instruction": "Find the low-fuel ships. Loop the fleet and collect the NAME of any ship with fuel < 50:\nlow = []\nfor ship in fleet:\n    if ship[\"fuel\"] < 50:\n        low.append(ship[\"name\"])",
            "intro": ["fleet is loaded with two ship dicts.",
                      "Loop the list, read each dict, and append matches.",
                      "Blank line runs the block."],
            "seed": {"fleet": [{"name": "Pyxis", "fuel": 80}, {"name": "Vela", "fuel": 30}]},
            "hints": [
                "Start  low = []  then loop  for ship in fleet:",
                "Inside:  if ship[\"fuel\"] < 50: low.append(ship[\"name\"])",
                'low = []\nfor ship in fleet:\n    if ship["fuel"] < 50:\n        low.append(ship["name"])',
            ],
            "solution": 'low = []\nfor ship in fleet:\n    if ship["fuel"] < 50:\n        low.append(ship["name"])',
            "check": lambda term: term.ns.get("low") == ["Vela"],
            "success": "['Vela'] -- you searched a list of records. This is what real data work looks like.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Records stream up the screen -- the MAINFRAME is online, Cadet.",
        "",
        "You worked a LIST OF DICTIONARIES: chained brackets to reach inside,",
        "and looped the records to search them. That's real data, handled.",
        "",
        "More systems still flicker, Cadet -- and tougher trials lie ahead.",
        "Next: DOCKING SYNC, where you learn to number and pair your data.",
    ],
}
