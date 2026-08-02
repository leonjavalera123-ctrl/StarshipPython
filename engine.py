"""
engine.py  --  The reusable "toolkit" for the whole game.
=========================================================

Welcome, cadet! This file is the BOX OF TOOLS that every screen in the game
shares. It does NOT contain any level or story -- just helpers so we never have
to copy-paste the same code over and over.

A 30-second crash course on how a game draws things (pygame):
    * The window is a giant grid of colored dots called pixels.
    * pygame calls that grid a "surface". The main one is the window itself
      (we always call it `screen`).
    * To show anything you (1) draw onto the surface, then (2) "flip" the screen
      so the new picture appears. A game repeats this ~60 times a second inside
      a loop. That loop lives in main.py.

What's in this toolbox:
    - COLORS       : a palette of named colors so we never juggle raw numbers
    - font()       : loads text fonts once and reuses them
    - draw_text()  : puts (word-wrapped) text on the screen
    - draw_panel() : draws a rounded box (our windows/cards)
    - Starfield    : the twinkling stars in the background
    - Button       : a clickable button
    - Scene        : the "blueprint" every screen inherits from

Read this file first. Once these tools make sense, every level reads like
plain English.
"""

import random
import pygame  # the game library, installed with:  pip install pygame


# ---------------------------------------------------------------------------
# 1) THE WINDOW SIZE
# ---------------------------------------------------------------------------
# These are plain numbers stored in variables. We use ALL-CAPS names by
# convention to say "this is a constant -- a setting we don't change while
# the game is running."
WIDTH = 1000   # how many pixels wide the window is
HEIGHT = 700   # how many pixels tall the window is
FPS = 60       # "frames per second" -- how many times we redraw each second


# ---------------------------------------------------------------------------
# 2) THE COLOR PALETTE  (a deep-space look)
# ---------------------------------------------------------------------------
# A color in pygame is a tuple of 3 numbers: (Red, Green, Blue), each 0-255.
# (0, 0, 0) is black; (255, 255, 255) is white.
# We keep them in a dictionary so we can ask for a color BY NAME, like
# COLORS["cyan"]. A dictionary maps a "key" (the name) to a "value" (the color).
COLORS = {
    "space":  (8, 10, 26),      # deep-space background (almost black blue)
    "panel":  (18, 22, 46),     # window/card background
    "panel2": (28, 34, 64),     # a lighter inner box
    "star":   (235, 240, 255),  # bright near-white -- our normal text
    "cyan":   (90, 200, 255),   # PYX's voice + highlights
    "green":  (80, 230, 150),   # success / "system online"
    "amber":  (255, 200, 90),   # hints and warnings
    "red":    (255, 100, 110),  # errors / danger
    "gray":   (130, 140, 170),  # dim, secondary text
    "purple": (175, 135, 255),  # accents / nebula
    "code":   (150, 230, 255),  # the color we print example code in
}


# ---------------------------------------------------------------------------
# 3) FONTS
# ---------------------------------------------------------------------------
# A "font" is a typeface at a chosen size. Building a font is a touch slow, so
# we build each one ONCE and keep it in a dictionary to reuse. The leading
# underscore in `_FONT_CACHE` is a gentle hint: "internal -- don't poke at this".
_FONT_CACHE = {}

def font(size, mono=True):
    """Return a font of the given pixel size, building it once then reusing it.

    mono=True gives a monospace (typewriter) font -- every letter the same
    width -- which is what makes code line up neatly like a real terminal.
    """
    key = (size, mono)               # the cache key: this exact size + style
    if key not in _FONT_CACHE:       # have we built this font already?
        if mono:
            # SysFont looks for a font already installed on your computer.
            # "consolas" ships with Windows; the others are backups.
            f = pygame.font.SysFont("consolas,couriernew,monospace", size)
        else:
            f = pygame.font.SysFont("segoeui,arial", size)
        _FONT_CACHE[key] = f         # remember it so next time is instant
    return _FONT_CACHE[key]


# ---------------------------------------------------------------------------
# 4) DRAWING TEXT  (with automatic word-wrapping)
# ---------------------------------------------------------------------------
def draw_text(surface, text, x, y, size=22, color="star",
              mono=True, max_width=None, line_gap=6, center=False):
    """Draw `text` onto `surface` starting at the point (x, y).

    Pixels are counted from the TOP-LEFT corner of the window:
        x grows to the RIGHT, y grows DOWNWARD.

    If `max_width` is given, long lines wrap onto more lines automatically.
    Returns the y just BELOW what we drew, so the caller can keep stacking text.
    """
    f = font(size, mono)
    # Allow either a color NAME ("cyan") or a raw (r, g, b) tuple.
    rgb = COLORS[color] if isinstance(color, str) else color

    # Step 1: split the text into lines that fit inside max_width.
    if max_width is None:
        lines = text.split("\n")          # only break on real newlines
    else:
        lines = []
        for paragraph in text.split("\n"):        # respect explicit newlines too
            words = paragraph.split(" ")
            current = ""
            for word in words:
                trial = word if current == "" else current + " " + word
                # f.size(...) tells us how wide a string would be, in pixels.
                if f.size(trial)[0] <= max_width:
                    current = trial               # still fits -- add the word
                else:
                    lines.append(current)         # full -- start a new line
                    current = word
            lines.append(current)

    # Step 2: actually render each line, moving down by one line each time.
    line_height = f.get_height() + line_gap
    for i, line in enumerate(lines):
        img = f.render(line, True, rgb)           # turn the string into a picture
        rect = img.get_rect()                     # a rectangle that size
        if center:
            rect.midtop = (x, y + i * line_height)    # x is the CENTER
        else:
            rect.topleft = (x, y + i * line_height)   # x is the LEFT edge
        surface.blit(img, rect)                   # "blit" = paste the picture on
    return y + len(lines) * line_height           # bottom edge, for stacking


def text_height(text, size=22, mono=True, max_width=None, line_gap=6):
    """Measure how TALL `text` would be (in pixels) if drawn with draw_text.

    It wraps exactly the same way draw_text does, then returns
    number_of_lines * line_height. We use this to know when a block of text is
    taller than its panel, so we can offer scrolling.
    """
    f = font(size, mono)
    if max_width is None:
        lines = text.split("\n")
    else:
        lines = []
        for paragraph in text.split("\n"):
            words = paragraph.split(" ")
            current = ""
            for word in words:
                trial = word if current == "" else current + " " + word
                if f.size(trial)[0] <= max_width:
                    current = trial
                else:
                    lines.append(current)
                    current = word
            lines.append(current)
    return len(lines) * (f.get_height() + line_gap)


# ---------------------------------------------------------------------------
# 5) DRAWING A PANEL  (a rounded box -- our windows and cards)
# ---------------------------------------------------------------------------
def draw_panel(surface, rect, fill="panel", border="cyan", width=2, radius=12):
    """Draw a filled rounded rectangle with a colored outline.

    `rect` is a pygame.Rect (it bundles x, y, width, height together).
    Pass border=None to draw no outline.
    """
    fill_rgb = COLORS[fill] if isinstance(fill, str) else fill
    pygame.draw.rect(surface, fill_rgb, rect, border_radius=radius)
    if border is not None:
        border_rgb = COLORS[border] if isinstance(border, str) else border
        pygame.draw.rect(surface, border_rgb, rect, width=width, border_radius=radius)


# ---------------------------------------------------------------------------
# 6) THE STARFIELD  (twinkling background)
# ---------------------------------------------------------------------------
class Starfield:
    """A field of little stars that drift and twinkle behind everything.

    A "class" is a blueprint. We make one Starfield object and it remembers
    where all its stars are. `self` means "this particular starfield".
    """

    def __init__(self, count=90):
        # Build a list of stars. Each star is a small dictionary holding its
        # position, brightness, and how fast it twinkles.
        self.stars = []
        for _ in range(count):                # `_` = "a number we don't need"
            self.stars.append({
                "x": random.randint(0, WIDTH),
                "y": random.randint(0, HEIGHT),
                "base": random.randint(60, 180),   # base brightness
                "speed": random.uniform(0.5, 2.0), # twinkle speed
                "phase": random.uniform(0, 6.28),  # where in the twinkle it starts
            })
        self.t = 0.0                          # a clock that keeps ticking up

    def update(self, dt):
        # dt = seconds since the last frame. We add it to our clock.
        self.t += dt

    def draw(self, surface):
        import math
        for s in self.stars:
            # A sine wave gently raises and lowers the brightness -> twinkle.
            twinkle = math.sin(self.t * s["speed"] + s["phase"]) * 50
            b = max(0, min(255, int(s["base"] + twinkle)))
            surface.set_at((s["x"], s["y"]), (b, b, min(255, b + 30)))


# ---------------------------------------------------------------------------
# 7) A CLICKABLE BUTTON
# ---------------------------------------------------------------------------
class Button:
    """A rectangle with a label that knows when it has been clicked.

    From this one blueprint we make many button objects, each remembering its
    own position, label, and color.
    """

    def __init__(self, x, y, w, h, label, color="cyan"):
        # __init__ runs once, when we create the button. It stores the settings.
        self.rect = pygame.Rect(x, y, w, h)   # bundles x, y, width, height
        self.label = label
        self.color = color
        self.hover = False                    # is the mouse over it right now?
        self.enabled = True                   # a disabled button can't be clicked

    def handle_event(self, event):
        """Look at one input event. Return True only if THIS button was clicked."""
        if event.type == pygame.MOUSEMOTION:
            # event.pos is the mouse (x, y). collidepoint asks "is it inside me?"
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.enabled and self.rect.collidepoint(event.pos):
                return True                   # yes -- a left-click landed on us
        return False                          # otherwise, not clicked

    def draw(self, surface):
        base = COLORS[self.color] if isinstance(self.color, str) else self.color
        if not self.enabled:
            base = COLORS["gray"]             # show disabled buttons as gray
        # When hovered, fill solid; otherwise show an outline only.
        if self.hover and self.enabled:
            pygame.draw.rect(surface, base, self.rect, border_radius=8)
            txt_color = COLORS["space"]       # dark text on the bright fill
        else:
            pygame.draw.rect(surface, COLORS["panel2"], self.rect, border_radius=8)
            pygame.draw.rect(surface, base, self.rect, width=2, border_radius=8)
            txt_color = base
        # Center the label inside the button.
        f = font(22)
        img = f.render(self.label, True, txt_color)
        surface.blit(img, img.get_rect(center=self.rect.center))


# ---------------------------------------------------------------------------
# 8) THE SCENE "BLUEPRINT"
# ---------------------------------------------------------------------------
class Scene:
    """Every screen in the game (title, each level, the win screen) is a Scene.

    A Scene promises three abilities, and the game loop in main.py calls them
    every frame: handle_event (react to input), update (advance time), and
    draw (paint the screen). Real screens INHERIT from this and fill them in.

    To move to another screen, a scene sets `self.next_scene = "some_name"`;
    main.py notices and swaps scenes for us.
    """

    def __init__(self, game):
        self.game = game            # a link back to the main Game object
        self.next_scene = None      # stays None until we want to switch screens

    def handle_event(self, event):
        """React to one input event (key press, mouse click). Override me."""
        pass

    def update(self, dt):
        """Advance animations. dt = seconds since the last frame. Override me."""
        pass

    def draw(self, surface):
        """Paint everything for this frame. Override me."""
        pass
