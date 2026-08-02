"""
level8_charts.py  --  LEVEL 8: The Star Charts
==============================================

Concept taught: DICTIONARIES -- storing labelled values (key -> value).

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
    "number": 8,
    "system": "STAR CHARTS",
    "concept": "dictionaries",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Good to see you again, Cadet. The Star Charts are a mess.",
        "Every star and planet is still here -- but the LABELS fell off.",
        "",
        "I have a name, a type, a moon count... but nothing says which is which.",
        "To fix this, you need a new kind of container: the DICTIONARY.",
        "",
        "A dictionary stores labelled values: each value gets a KEY.",
        "Look something up by its label, not by counting positions.",
        "Let's chart an example before you take the helm.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'star = {"name": "Sol", "type": "yellow"}\n'
            'print(star["type"])'
        ),
        "caption": "A dictionary with two labelled entries. We look up the value "
                   "filed under \"type\". Running this prints:  yellow",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": 'star = {"name": "Sol", "type": "yellow"}',
            "note": "A DICTIONARY stores key: value pairs inside curly braces "
                    "{ }. Here \"name\" -> \"Sol\" and \"type\" -> \"yellow\". "
                    "Each pair is  key: value, and pairs are separated by commas.",
        },
        {
            "code": 'star["name"]',
            "note": "To read a value, write the dictionary's name then the KEY in "
                    "square brackets [ ]. This hands you \"Sol\". A LIST uses a "
                    "number position like star[0]; a dict uses a NAMED key instead.",
        },
        {
            "code": '"name"   "type"',
            "note": "Keys are usually text (strings), so they go in quotes. The "
                    "VALUES can be anything: text, a number, True/False, even "
                    "another list or dictionary. Keys label; values hold the data.",
        },
        {
            "code": 'star["visited"] = True',
            "note": "Assigning to a key that isn't there yet ADDS it. Now the "
                    "dictionary has a third entry, \"visited\" -> True. Same syntax "
                    "with an existing key would just change that value.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python (VERBATIM per spec) ------
    "practice": [
        {
            "instruction": "Log a planet. Make a dictionary named planet with two entries: \"name\" set to \"Mars\" and \"moons\" set to 2.",
            "intro": ["A dictionary stores labelled values inside curly braces { }.",
                      "Each entry is  key: value, separated by commas."],
            "seed": {},
            "hints": [
                "Curly braces make a dict:  { }",
                "Entries look like  \"name\": \"Mars\"",
                'planet = {"name": "Mars", "moons": 2}',
            ],
            "solution": 'planet = {"name": "Mars", "moons": 2}',
            "check": lambda term: isinstance(term.ns.get("planet"), dict) and term.ns["planet"].get("name") == "Mars",
            "success": "Mars logged with 2 moons. The star chart lights up.",
        },
        {
            "instruction": "Read the planet's name. Print planet[\"name\"].",
            "intro": ["planet = {\"name\": \"Mars\", \"moons\": 2} is loaded.",
                      "Look up a value by its key in square brackets."],
            "seed": {"planet": {"name": "Mars", "moons": 2}},
            "hints": [
                "Use square brackets with the KEY (text in quotes).",
                "The key you want is \"name\".",
                'print(planet["name"])',
            ],
            "solution": 'print(planet["name"])',
            "check": lambda term: "mars" in term.last_run.lower(),
            "success": "Mars -- pulled straight from the dictionary by its label.",
        },
        {
            "instruction": "Mark it explored. Add a new entry: set planet[\"visited\"] to True.",
            "intro": ["planet already has name and moons.",
                      "Assigning a new key adds it to the dictionary."],
            "seed": {"planet": {"name": "Mars", "moons": 2}},
            "hints": [
                "Use the key in brackets on the left of an = sign.",
                "True is a special value (no quotes).",
                'planet["visited"] = True',
            ],
            "solution": 'planet["visited"] = True',
            "check": lambda term: term.ns.get("planet", {}).get("visited") is True,
            "success": "Mars marked as visited. Your dictionary just grew a new entry.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Labels snap back onto every star. The Star Charts blaze to life.",
        "",
        "You learned DICTIONARIES: labelled values, looked up by KEY,",
        "not by counting positions like a list does.",
        "",
        "STAR CHARTS: ONLINE. But the Airlock Controls are jammed shut...",
        "Next you'll learn FUNCTIONS -- reusable commands you build yourself.",
    ],
}
