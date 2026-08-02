"""
make_sounds.py  --  generates the game's sound effects as .wav files.

Run once with:  python make_sounds.py
It synthesizes a few short tones using only Python's built-in `wave`, `struct`,
and `math` modules (no extra libraries) and writes them into assets/.
Safe to delete after running. Re-run any time to regenerate.

The sounds:
    blip.wav    -- a tiny tick, played as PYX's text types out
    solved.wav  -- a happy two-note chime when you solve a task
    online.wav  -- a rising arpeggio when a whole system comes online
"""
import os, wave, struct, math

SR = 22050  # samples per second (audio "frame rate")


def tone(freq, dur, vol=0.4, shape="sine"):
    """Build a list of samples for one note. A short fade in/out avoids clicks."""
    n = int(SR * dur)
    out = []
    attack = max(1, int(0.005 * SR))     # 5ms fade-in
    release = max(1, int(0.010 * SR))    # 10ms fade-out
    for i in range(n):
        t = i / SR
        if shape == "sine":
            s = math.sin(2 * math.pi * freq * t)
        else:  # a softer square, for a more "digital" beep
            s = 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0
        env = min(1.0, i / attack, (n - i) / release)   # volume envelope
        out.append(s * vol * env)
    return out


def save(name, samples):
    """Write a list of -1..1 samples to a 16-bit mono WAV file in assets/."""
    path = os.path.join(BASE, name + ".wav")
    with wave.open(path, "w") as w:
        w.setnchannels(1)        # mono
        w.setsampwidth(2)        # 2 bytes = 16-bit
        w.setframerate(SR)
        frames = b"".join(
            struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767)) for s in samples
        )
        w.writeframes(frames)
    print("wrote", path)


BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(BASE, exist_ok=True)

# A tiny tick for the typing animation (quiet and very short).
save("blip", tone(1500, 0.022, vol=0.18))

# A cheerful two-note "ding" for solving a task.
save("solved", tone(660, 0.09, vol=0.35) + tone(990, 0.13, vol=0.35))

# A rising four-note arpeggio for a whole system coming online.
save("online", tone(523, 0.08, vol=0.33) + tone(659, 0.08, vol=0.33)
              + tone(784, 0.08, vol=0.33) + tone(1046, 0.18, vol=0.4))


def ambient_pad(dur, freqs, vol=0.12):
    """A soft, SEAMLESSLY-LOOPING chord pad for background music.

    Trick for a clickless loop: every frequency (and the slow volume swell) is
    an exact multiple of 1/dur, so each wave completes whole cycles over the
    loop -- the end lines up perfectly with the start.
    """
    n = int(SR * dur)
    out = []
    for i in range(n):
        t = i / SR
        s = 0.0
        for f in freqs:
            s += math.sin(2 * math.pi * f * t)
        swell = 0.7 + 0.3 * math.sin(2 * math.pi * (1.0 / dur) * t)   # 1 cycle/loop
        out.append(s * vol * swell / len(freqs))
    return out


# An 8-second spacey drone (stacked fifths: A2, E3, A3, E4) for under the game.
save("music", ambient_pad(8.0, [110.0, 165.0, 220.0, 330.0]))

print("Done. Sound + music written to assets/.")
