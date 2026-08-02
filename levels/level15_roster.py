"""
level15_roster.py  --  LEVEL 15: The Crew Roster
================================================

Concept taught: sets -- collections that keep only UNIQUE values.

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
    "number": 15,
    "system": "CREW ROSTER",
    "concept": "sets (unique values)",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "Crew Roster online, Cadet -- but something is wrong with it.",
        "Every time a name is logged, it gets logged AGAIN. And again.",
        "The roster is full of duplicates: 'Ada, Ada, Ada, Grace, Grace'.",
        "",
        "We need a smarter container -- one that refuses repeats.",
        "That tool is the SET. A set keeps only UNIQUE values.",
        "Add the same name twice? The set quietly keeps just one.",
        "Let's look at an example before you try it.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            "ids = {1, 2, 2, 3}\n"
            "print(len(ids))"
        ),
        "caption": "Prints 3, not 4. The duplicate 2 is dropped automatically, "
                   "so the set holds just {1, 2, 3}.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "ids = {1, 2, 2, 3}",
            "note": "A SET uses curly braces { } with plain values inside. Unlike "
                    "a dictionary, there is NO key: value pairing -- just lone "
                    "values separated by commas.",
        },
        {
            "code": "{1, 2, 2, 3}  ->  {1, 2, 3}",
            "note": "A set removes duplicates automatically. It also has NO order, "
                    "so don't count on the items lining up the way you typed them.",
        },
        {
            "code": "ids.add(5)",
            "note": ".add(x) inserts a value into the set. If x is already there, "
                    "nothing changes -- the set simply stays unique.",
        },
        {
            "code": "set([1, 1, 2])   #  x in myset",
            "note": "set(a_list) converts a list into a set, wiping out duplicates. "
                    "And  x in myset  quickly tests membership (True/False). Note: "
                    "an empty set is written set(), because {} makes an empty dict.",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Build the crew set. Make a set named crew with these names, including a duplicate:\ncrew = {\"Ada\", \"Grace\", \"Ada\"}\nA set automatically drops the repeat.",
            "intro": ["A set holds UNIQUE values inside curly braces { }.",
                      "Duplicates are removed automatically."],
            "seed": {},
            "hints": [
                "Curly braces with plain values (no key: value) make a set.",
                "Include \"Ada\" twice on purpose.",
                'crew = {"Ada", "Grace", "Ada"}',
            ],
            "solution": 'crew = {"Ada", "Grace", "Ada"}',
            "check": lambda term: term.ns.get("crew") == {"Ada", "Grace"},
            "success": "Two crew members -- the duplicate Ada was dropped. Sets keep things unique.",
        },
        {
            "instruction": "A new recruit boards. Add \"Alan\" to the crew set with crew.add(\"Alan\").",
            "intro": ["crew = {\"Ada\", \"Grace\"} is loaded.",
                      ".add(x) puts x into a set (if not already there)."],
            "seed": {"crew": {"Ada", "Grace"}},
            "hints": [
                "Sets have an .add() tool.",
                "Put the new name in quotes.",
                'crew.add("Alan")',
            ],
            "solution": 'crew.add("Alan")',
            "check": lambda term: "Alan" in term.ns.get("crew", set()),
            "success": "Alan added. The roster now holds three unique names.",
        },
        {
            "instruction": "Clean a messy list. Turn the list [1, 1, 2, 3] into a set of unique values:\nunique = set([1, 1, 2, 3])",
            "intro": ["set(...) can convert a list into a set, removing duplicates.",
                      "Great for finding the distinct values."],
            "seed": {},
            "hints": [
                "Wrap the list in  set( ... )",
                "set([1, 1, 2, 3])",
                "unique = set([1, 1, 2, 3])",
            ],
            "solution": "unique = set([1, 1, 2, 3])",
            "check": lambda term: term.ns.get("unique") == {1, 2, 3},
            "success": "unique = {1, 2, 3}. The repeats vanished. Sets are your dedup tool.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "CREW ROSTER: ONLINE. The duplicate names melt away -- one entry each.",
        "",
        "You learned the SET: curly braces holding UNIQUE values, no repeats,",
        "with .add() to insert and set(list) to scrub duplicates in one move.",
        "",
        "Next stop: the Fabricator, where you'll learn LIST COMPREHENSIONS --",
        "a slick way to build whole lists in a single line. Onward, Cadet.",
    ],
}
