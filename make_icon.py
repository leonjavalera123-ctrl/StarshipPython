"""
make_icon.py  --  generates assets/icon.ico (a little rocket) for the game.

Run once with:  python make_icon.py
It draws the icon with pygame, saves a PNG, then wraps that PNG into a Windows
.ico file by hand (no extra libraries needed). Safe to delete after running.
"""
import os, struct
os.environ["SDL_VIDEODRIVER"] = "dummy"      # render without opening a window
import pygame

pygame.init()
SIZE = 256
surf = pygame.Surface((SIZE, SIZE), pygame.SRCALPHA)   # SRCALPHA = transparency

SPACE = (8, 10, 26)
CYAN  = (90, 200, 255)
WHITE = (235, 240, 255)
AMBER = (255, 200, 90)
DARK  = (18, 22, 46)

# Rounded deep-space tile background.
pygame.draw.rect(surf, SPACE, (0, 0, SIZE, SIZE), border_radius=48)

# A few background stars.
for (sx, sy, r) in [(40, 50, 3), (210, 70, 4), (60, 200, 3),
                    (200, 200, 3), (180, 40, 2), (50, 120, 2)]:
    pygame.draw.circle(surf, WHITE, (sx, sy), r)

# Exhaust flame (drawn first so the rocket sits on top of it).
pygame.draw.polygon(surf, AMBER, [(112, 184), (144, 184), (128, 232)])
pygame.draw.polygon(surf, WHITE, [(120, 184), (136, 184), (128, 210)])

# Fins (two triangles at the base).
pygame.draw.polygon(surf, CYAN, [(108, 150), (84, 192), (108, 186)])
pygame.draw.polygon(surf, CYAN, [(148, 150), (172, 192), (148, 186)])

# Rocket body (a rounded vertical capsule).
pygame.draw.rect(surf, WHITE, (106, 78, 44, 110), border_radius=22)
# Nose cone.
pygame.draw.polygon(surf, CYAN, [(128, 40), (106, 86), (150, 86)])
# Porthole window.
pygame.draw.circle(surf, DARK, (128, 110), 15)
pygame.draw.circle(surf, CYAN, (128, 110), 15, width=4)

os.makedirs("assets", exist_ok=True)
png_path = "assets/icon.png"
pygame.image.save(surf, png_path)                      # pygame writes PNG natively
pygame.quit()

# --- wrap the PNG bytes into a minimal .ico container (Vista+ supports PNG) ---
with open(png_path, "rb") as fh:
    png = fh.read()

header = struct.pack("<HHH", 0, 1, 1)                  # reserved, type=icon, count=1
entry = struct.pack("<BBBBHHII",
                    0, 0,        # width, height (0 means 256)
                    0, 0,        # palette count, reserved
                    1, 32,       # color planes, bits-per-pixel
                    len(png),    # size of the image data
                    6 + 16)      # offset to the image data
with open("assets/icon.ico", "wb") as fh:
    fh.write(header + entry + png)

print("Wrote assets/icon.ico  (", len(png), "bytes of PNG inside )")
