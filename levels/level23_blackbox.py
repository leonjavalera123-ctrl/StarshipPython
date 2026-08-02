"""
level23_blackbox.py  --  LEVEL 23: The Black Box Recorder
=========================================================

Concept taught: reading and writing FILES (open / write / close / read / with).

This one is special: the code you type REALLY creates a small file on disk
(ship_log.txt, in the game's folder). That's the honest way to learn files --
you can even open ship_log.txt yourself afterwards and see what you wrote.

Because a check has to look at the file (not just the namespace), we define a
tiny module-level helper `_log_has(text)` and call it from the check lambdas
(a lambda can't hold a try/except).

The three tasks run in order, so task 1 creates the file before tasks 2-3 read
it. Keep all in-game text plain ASCII. Multi-line blocks finish on a blank line.
"""

LOG_FILE = "ship_log.txt"


def _log_has(text):
    """True if the log file exists and contains `text`. Safe if it's missing."""
    try:
        with open(LOG_FILE) as fh:
            return text in fh.read()
    except Exception:
        return False


LEVEL = {
    "number": 23,
    "system": "BLACK BOX RECORDER",
    "concept": "reading and writing files",

    "brief": [
        "Every starship needs a black box, Cadet -- a recorder that survives.",
        "Ours is wiped. We must teach it to SAVE data to disk, and read it back.",
        "",
        "Today: real FILES. You'll open a file, write to it, and read it again.",
        "Heads up -- this actually makes a file (ship_log.txt) in the game folder.",
        "You can open it yourself later and see your own words. Spooky, right?",
        "",
        "Let's get the recorder logging again.",
    ],

    "example": {
        "code": (
            'f = open("log.txt", "w")\n'
            'f.write("Launch OK")\n'
            'f.close()\n'
            'print(open("log.txt").read())'
        ),
        "caption": "Open a file for writing, write a line, close it -- then open it "
                   "again and read it back. This prints:  Launch OK",
    },

    "explain": [
        {
            "code": 'f = open("log.txt", "w")',
            "note": "open(name, \"w\") opens a file for WRITING. The \"w\" means "
                    "write -- it creates the file (and erases anything already in "
                    "it). It hands back a file object we store in f.",
        },
        {
            "code": 'f.write("Launch OK")\nf.close()',
            "note": ".write(text) puts text into the file. .close() saves it and "
                    "lets go of the file. Always close what you open -- or use "
                    "'with' below, which closes it for you.",
        },
        {
            "code": 'open("log.txt").read()',
            "note": "open(name) with no mode opens it for READING. .read() returns "
                    "the WHOLE file as one string. That's how you load data back.",
        },
        {
            "code": 'with open("log.txt") as f:\n    data = f.read()',
            "note": "The 'with' form is the safe, preferred way: it opens the file, "
                    "gives it to you as f, and AUTO-CLOSES it when the indented "
                    "block ends -- even if something goes wrong.",
        },
    ],

    "practice": [
        {
            "instruction": "Start the recorder. Open \"ship_log.txt\" for writing, write \"Day 1: launched\", then close it:\nf = open(\"ship_log.txt\", \"w\")\nf.write(\"Day 1: launched\")\nf.close()",
            "intro": ["This really creates a file in the game folder.",
                      "Three lines: open, write, close."],
            "seed": {},
            "hints": [
                "Open for writing with the \"w\" mode:  open(\"ship_log.txt\", \"w\")",
                "Then  f.write(\"Day 1: launched\")  and  f.close()",
                'f = open("ship_log.txt", "w")\nf.write("Day 1: launched")\nf.close()',
            ],
            "solution": 'f = open("ship_log.txt", "w")\nf.write("Day 1: launched")\nf.close()',
            "check": lambda term: _log_has("Day 1: launched"),
            "success": "Entry saved to disk. The black box is recording again.",
        },
        {
            "instruction": "Play it back. Read the whole file into a variable named log:\nlog = open(\"ship_log.txt\").read()",
            "intro": ["The file you just wrote is still on disk.",
                      "open(...).read() returns the whole file as text."],
            "seed": {},
            "hints": [
                "Open the file (no mode = read) and call .read() on it.",
                "Store the result in log.",
                'log = open("ship_log.txt").read()',
            ],
            "solution": 'log = open("ship_log.txt").read()',
            "check": lambda term: isinstance(term.ns.get("log"), str) and "Day 1: launched" in term.ns.get("log", ""),
            "success": "log now holds 'Day 1: launched' -- read straight off the disk.",
        },
        {
            "instruction": "Do it the safe way. Read the file inside a with-block, into a variable named data:\nwith open(\"ship_log.txt\") as f:\n    data = f.read()",
            "intro": ["'with' auto-closes the file when the block ends.",
                      "Blank line runs the block."],
            "seed": {},
            "hints": [
                "Start:  with open(\"ship_log.txt\") as f:",
                "Indented body:  data = f.read()",
                'with open("ship_log.txt") as f:\n    data = f.read()',
            ],
            "solution": 'with open("ship_log.txt") as f:\n    data = f.read()',
            "check": lambda term: isinstance(term.ns.get("data"), str) and "Day 1" in term.ns.get("data", ""),
            "success": "Read safely, file auto-closed. BLACK BOX RECORDER online!",
        },
    ],

    "repair": [
        "The recorder hums, etching your words into protected memory.",
        "",
        "You wrote to a FILE and read it back -- open, write, close, and the",
        "safe 'with' form. That's how programs remember things between runs.",
        "",
        "Two systems still flicker before the trials ahead, Cadet.",
        "Next: the REACTOR LOOP, and a clever trick called loop-else.",
    ],
}
