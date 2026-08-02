"""
level26_gauntlet.py  --  LEVEL 26: The Asteroid Gauntlet  (BOSS CHALLENGE)
=========================================================================

This is a BOSS level. The rules change:
    * NO hint ladder. You get the task and a worked EXAMPLE of the input/output,
      and that's it. You combine the skills you already have.
    * The tasks are a little harder and lean on several ideas at once
      (functions + loops + conditionals + comprehensions + nested data).

A boss level is marked with  "boss": True  so main.py styles it and hides the
hint button. Every task's "hints" list is empty on purpose.

Keep all in-game text plain ASCII. Multi-line blocks finish on a blank line.
"""


LEVEL = {
    "number": 26,
    "system": "ASTEROID GAUNTLET",
    "concept": "BOSS CHALLENGE -- combine everything (no hints)",
    "boss": True,

    "brief": [
        "Alarms, Cadet. An asteroid field dead ahead -- dense, fast, deadly.",
        "Autopilot can't thread this. Only your code can.",
        "",
        "This is a BOSS challenge. No hints this time. You're ready.",
        "I'll give you each function's name and one example of what it should do.",
        "Use everything: functions, loops, ifs, comprehensions, lists of records.",
        "",
        "Steady hands. Let's fly through the rocks.",
    ],

    "example": {
        "code": (
            'def big_ones(nums):\n'
            '    return [n for n in nums if n > 10]\n'
            'print(big_ones([5, 20, 8, 30]))'
        ),
        "caption": "A reminder of your tools: a function that filters a list with "
                   "a comprehension. big_ones([5, 20, 8, 30]) returns [20, 30]. "
                   "The boss tasks look like this -- name, example, go.",
    },

    "explain": [
        {
            "code": "# Boss rules",
            "note": "No hint ladder here. Each task gives you the function name and "
                    "ONE example of input -> output. Read the example carefully: it "
                    "tells you exactly what your function must return.",
        },
        {
            "code": "def name(inputs):\n    ...\n    return answer",
            "note": "Every task asks for a FUNCTION that returns a value (no need to "
                    "print). Define it, press Enter on a blank line to finish, and "
                    "the gauntlet checks it by calling it with test values.",
        },
    ],

    "practice": [
        {
            "instruction": "Define count_hits(grid) that returns HOW MANY numbers in the list are greater than 0.\nExample: count_hits([0, 3, 0, 5]) -> 2",
            "intro": ["Boss challenge -- no hints. You've got this.",
                      "Define the function; blank line finishes it."],
            "seed": {},
            "hints": [],
            "solution": "def count_hits(grid):\n    count = 0\n    for n in grid:\n        if n > 0:\n            count = count + 1\n    return count",
            "check": lambda term: callable(term.ns.get("count_hits")) and term.ns["count_hits"]([0, 3, 0, 5]) == 2 and term.ns["count_hits"]([0, 0]) == 0,
            "success": "Hits counted. Two rocks tagged. Keep moving.",
        },
        {
            "instruction": "Define evens_only(nums) that returns a NEW list with only the even numbers.\nExample: evens_only([1, 2, 3, 4, 6]) -> [2, 4, 6]",
            "intro": ["No hints. Remember: even means  n % 2 == 0.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": "def evens_only(nums):\n    return [n for n in nums if n % 2 == 0]",
            "check": lambda term: callable(term.ns.get("evens_only")) and term.ns["evens_only"]([1, 2, 3, 4, 6]) == [2, 4, 6] and term.ns["evens_only"]([1, 3]) == [],
            "success": "Even thrusters firing. Clean filter.",
        },
        {
            "instruction": "Define reverse_caps(word) that returns the word REVERSED and in CAPITALS.\nExample: reverse_caps(\"nova\") -> \"AVON\"",
            "intro": ["No hints. Think: reverse with a slice, then .upper().",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": "def reverse_caps(word):\n    return word[::-1].upper()",
            "check": lambda term: callable(term.ns.get("reverse_caps")) and term.ns["reverse_caps"]("nova") == "AVON" and term.ns["reverse_caps"]("hi") == "IH",
            "success": "Signal flipped and amplified. Sharp work.",
        },
        {
            "instruction": "Define total_fuel(fleet), where fleet is a LIST OF DICTS each with a \"fuel\" key. Return the total fuel.\nExample: total_fuel([{\"fuel\": 10}, {\"fuel\": 5}]) -> 15",
            "intro": ["Last one. Loop the records and add up each ship's fuel.",
                      "Blank line finishes the function."],
            "seed": {},
            "hints": [],
            "solution": 'def total_fuel(fleet):\n    total = 0\n    for ship in fleet:\n        total = total + ship["fuel"]\n    return total',
            "check": lambda term: callable(term.ns.get("total_fuel")) and term.ns["total_fuel"]([{"fuel": 10}, {"fuel": 5}]) == 15 and term.ns["total_fuel"]([]) == 0,
            "success": "Fuel tallied across the whole fleet. ASTEROID FIELD CLEARED!",
        },
    ],

    "repair": [
        "The last rock tumbles past the viewport and the field falls behind you.",
        "Silence. Stars. You flew the gauntlet on nothing but your own code.",
        "",
        "You combined it ALL: functions, loops, ifs, comprehensions, records.",
        "",
        "But sensors catch something vast moving in the dark ahead, Cadet...",
        "Something with the call sign KRAKEN. Steel yourself. The final boss waits.",
    ],
}
