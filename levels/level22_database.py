"""
level22_database.py  --  LEVEL 22: The Crew Database
====================================================

Concept taught: looping through dictionaries with .items(), .keys(), .values().

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
    "number": 22,
    "system": "CREW DATABASE",
    "concept": "looping through dictionaries",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "The Crew Database is our last advanced system, Cadet.",
        "It holds a record for every soul aboard -- names and their data.",
        "",
        "A dictionary stores those records as name -> value pairs.",
        "To bring it online, we must read it record by record.",
        "",
        "Today you'll LOOP THROUGH DICTIONARIES three ways:",
        "  .items() for pairs, .keys() for names, .values() for the data.",
        "Watch the example, then you'll read the crew yourself.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            'ages = {"Ada": 36, "Grace": 85}\n'
            'for name, age in ages.items():\n'
            '    print(name, age)'
        ),
        "caption": "A for-loop walks the dictionary. .items() hands you each "
                   "name and age together, so this prints each name with its "
                   "age:  Ada 36  then  Grace 85.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "for name in scores:",
            "note": "Looping a dictionary DIRECTLY gives you its KEYS -- the "
                    "names you stored. Each time around, 'name' is one key. The "
                    "values are not handed to you here, just the names.",
        },
        {
            "code": "for k, v in scores.items():",
            "note": ".items() gives you key,value PAIRS. Two names after 'for' "
                    "UNPACK each pair: 'k' becomes the key, 'v' becomes the "
                    "value. Now you have both halves of the record at once.",
        },
        {
            "code": "for v in scores.values():",
            "note": ".values() gives you JUST the values -- the data, no names. "
                    "Its partner .keys() gives just the keys. Pick the one that "
                    "matches what you actually need from the record.",
        },
        {
            "code": "for ... in scores.items():",
            "note": "Together these let you PROCESS EVERY RECORD in a dictionary "
                    "-- print them, total them, search them. One loop visits the "
                    "whole database, one record at a time.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "List the crew. Loop the scores dict to print each name (looping a dict gives its keys):\nfor name in scores:\n    print(name)",
            "intro": ["scores = {\"Ada\": 90, \"Grace\": 85} is loaded.",
                      "Looping a dictionary directly gives you its keys.",
                      "Blank line runs the block."],
            "seed": {"scores": {"Ada": 90, "Grace": 85}},
            "hints": [
                "Loop the dict directly:  for name in scores:",
                "Print the key:  print(name)",
                "for name in scores:\n    print(name)",
            ],
            "solution": "for name in scores:\n    print(name)",
            "check": lambda term: "ada" in term.last_run.lower() and "grace" in term.last_run.lower(),
            "success": "Ada, Grace -- every key listed. That's the simplest dict loop.",
        },
        {
            "instruction": "Show names AND scores. Use .items() to print each name with its score:\nfor name, score in scores.items():\n    print(name, score)",
            "intro": ["scores = {\"Ada\": 90, \"Grace\": 85} is loaded.",
                      ".items() gives key and value together.",
                      "Blank line runs the block."],
            "seed": {"scores": {"Ada": 90, "Grace": 85}},
            "hints": [
                "Loop with two names:  for name, score in scores.items():",
                "Print both:  print(name, score)",
                "for name, score in scores.items():\n    print(name, score)",
            ],
            "solution": "for name, score in scores.items():\n    print(name, score)",
            "check": lambda term: "ada 90" in term.last_run.lower() and "grace 85" in term.last_run.lower(),
            "success": "Ada 90, Grace 85 -- keys and values together with .items().",
        },
        {
            "instruction": "Total the scores. Add up every value using .values():\ntotal = 0\nfor v in scores.values():\n    total = total + v",
            "intro": ["scores = {\"Ada\": 90, \"Grace\": 85} is loaded.",
                      ".values() gives just the numbers.",
                      "Blank line runs the block."],
            "seed": {"scores": {"Ada": 90, "Grace": 85}},
            "hints": [
                "Start  total = 0  then loop  for v in scores.values():",
                "Add each value:  total = total + v",
                "total = 0\nfor v in scores.values():\n    total = total + v",
            ],
            "solution": "total = 0\nfor v in scores.values():\n    total = total + v",
            "check": lambda term: term.ns.get("total") == 175,
            "success": "175 -- summed straight from the dictionary's values. Database online!",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "Records scroll up the screen -- the CREW DATABASE is ONLINE.",
        "",
        "You can now read any dictionary: .items() for pairs, .keys() for",
        "names, .values() for the data -- every record, one at a time.",
        "",
        "Strong work, Cadet. But one recorder is still dark.",
        "Next: the BLACK BOX, where you learn to save and read real FILES.",
        "After that... the boss challenges await. Steady now.",
    ],
}
