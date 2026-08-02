"""
level21_textlab.py  --  LEVEL 21: The Text Lab
==============================================

Concept taught: string slicing and methods.

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
    "number": 21,
    "system": "TEXT LAB",
    "concept": "string slicing and methods",

    # --- STEP 1: BRIEF -- PYX sets the scene -------------------------------
    "brief": [
        "We're close to home now, Cadet. But the incoming signals are GARBLED.",
        "Letters jumbled, fields stuck together, words running backwards.",
        "",
        "The Text Lab can fix all of it -- if you learn to reshape text.",
        "You'll SLICE a string to grab just the part you want.",
        "You'll REVERSE it to undo a backwards transmission.",
        "And you'll SPLIT messy text apart, then JOIN it back together.",
        "Watch one example, then we clean up these signals together.",
    ],

    # --- STEP 2: EXAMPLE -- show working code first ------------------------
    "example": {
        "code": (
            's = "Nebula"\n'
            'print(s[0:3])\n'
            'print(s[::-1])'
        ),
        "caption": "s[0:3] grabs the first three letters, so it prints  Neb. "
                   "s[::-1] walks the string backwards, so it prints  alubeN.",
    },

    # --- STEP 3: EXPLAIN -- each important piece, in plain English ---------
    "explain": [
        {
            "code": "s[0:3]",
            "note": "This is SLICING. The square brackets with start:end grab "
                    "PART of a string. 0 is where to start; 3 is where to stop. "
                    "Important: the end index is NOT included -- you get letters "
                    "0, 1, and 2, but not 3.",
        },
        {
            "code": "s[::-1]",
            "note": "This special slice REVERSES a string. The -1 tells Python "
                    "to step backwards through every letter, so \"Nebula\" "
                    "becomes \"alubeN\".",
        },
        {
            "code": '"a,b,c".split(",")',
            "note": ".split breaks text into a LIST. It cuts wherever it finds "
                    "the separator you give it. Here the separator is a comma, so "
                    "\"a,b,c\" becomes the list ['a', 'b', 'c'].",
        },
        {
            "code": '"-".join(["a", "b", "c"])',
            "note": ".join is the opposite of split: it GLUES a list back into "
                    "one string, putting the joiner text between each item -- so "
                    "this gives \"a-b-c\". And .replace(old, new) swaps text, like "
                    "\"cat\".replace(\"c\", \"b\") giving \"bat\".",
        },
    ],

    # --- STEP 4: PRACTICE -- you type real Python -------------------------
    "practice": [
        {
            "instruction": "Grab the first three letters. The string word is loaded -- print word[0:3]:\nprint(word[0:3])",
            "intro": ["word = \"Galaxy\" is loaded.",
                      "Slicing  [start:end]  takes part of a string (end not included)."],
            "seed": {"word": "Galaxy"},
            "hints": [
                "Use square brackets with a start and end:  word[0:3]",
                "0 is the start, 3 is just past the last letter you want.",
                "print(word[0:3])",
            ],
            "solution": "print(word[0:3])",
            "check": lambda term: "Gal" in term.last_run,
            "success": "Gal -- the first three letters, sliced clean off the front.",
        },
        {
            "instruction": "Reverse the signal. Print word backwards using the [::-1] slice:\nprint(word[::-1])",
            "intro": ["word = \"Galaxy\" is loaded.",
                      "The slice [::-1] walks the string backwards."],
            "seed": {"word": "Galaxy"},
            "hints": [
                "Use the special reversing slice  [::-1].",
                "Attach it to word.",
                "print(word[::-1])",
            ],
            "solution": "print(word[::-1])",
            "check": lambda term: "yxalaG" in term.last_run,
            "success": "yxalaG -- reversed. Signal decoded backwards.",
        },
        {
            "instruction": "Split a record. Turn the text \"a,b,c\" into a list by splitting on commas:\nparts = \"a,b,c\".split(\",\")",
            "intro": [".split(\",\") breaks text wherever a comma appears.",
                      "It hands you back a list."],
            "seed": {},
            "hints": [
                "Call .split on the text, with the separator in quotes.",
                "\"a,b,c\".split(\",\")",
                'parts = "a,b,c".split(",")',
            ],
            "solution": 'parts = "a,b,c".split(",")',
            "check": lambda term: term.ns.get("parts") == ["a", "b", "c"],
            "success": "['a', 'b', 'c'] -- one string split into a tidy list.",
        },
    ],

    # --- STEP 5: REPAIR -- the payoff -------------------------------------
    "repair": [
        "The garble clears. Clean text streams across the Lab screen.",
        "TEXT LAB: ONLINE. Every signal readable again.",
        "",
        "You can now slice strings, reverse them, and split and join text at will.",
        "",
        "One system left before home: the Crew Database.",
        "Next you'll learn to LOOP THROUGH DICTIONARIES -- reading every crew "
        "record, key and value, one by one. Almost there, Cadet.",
    ],
}
