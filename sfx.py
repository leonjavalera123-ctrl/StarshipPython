"""
sfx.py  --  tiny, safe sound + music helper.

The game calls sfx.init() once at startup, then:
    sfx.play("solved")          -- play a one-shot effect
    sfx.set_music_volume(0.35)  -- set the background-music loudness (0..1)
    sfx.set_fx(False)           -- turn sound effects off/on
    sfx.toggle_mute()           -- silence / restore EVERYTHING (the M key)

Everything is wrapped so the game NEVER crashes over audio: if there's no sound
card, no mixer, or the files are missing, sound simply does nothing and the game
plays on silently. (This also keeps the headless tests happy.)
"""
import os
import pygame

_sounds = {}            # name -> pygame Sound (one-shot effects)
_enabled = False        # did the mixer start successfully?
_music_ok = False       # did the background music load?
_muted = False          # has the player pressed M to silence things?
_fx_on = True           # are sound effects enabled (Settings)?
_music_vol = 0.35       # desired music loudness when not muted (Settings)


def init():
    """Start the mixer, load the effect .wav files, and begin the music loop."""
    global _enabled, _music_ok
    try:
        pygame.mixer.init()
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
        for name in ("blip", "solved", "online"):
            path = os.path.join(base, name + ".wav")
            if os.path.exists(path):
                _sounds[name] = pygame.mixer.Sound(path)
        _enabled = True
        music_path = os.path.join(base, "music.wav")
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.0 if _muted else _music_vol)
            pygame.mixer.music.play(-1)         # loop forever
            _music_ok = True
    except Exception:
        _enabled = False    # no audio device, etc. -> stay silent


def play(name, volume=1.0):
    """Play a one-shot effect. Silent if muted, effects-off, or no audio."""
    if not _enabled or _muted or not _fx_on:
        return
    snd = _sounds.get(name)
    if snd is None:
        return
    try:
        snd.set_volume(volume)
        snd.play()
    except Exception:
        pass


def set_music_volume(vol):
    """Set the background-music loudness (0..1). Applies live unless muted."""
    global _music_vol
    _music_vol = vol
    try:
        if _music_ok and not _muted:
            pygame.mixer.music.set_volume(vol)
    except Exception:
        pass


def set_fx(on):
    """Enable or disable one-shot sound effects."""
    global _fx_on
    _fx_on = bool(on)


def toggle_mute():
    """Flip ALL audio on/off. Returns the new muted state (True = silent)."""
    global _muted
    _muted = not _muted
    try:
        if _music_ok:
            pygame.mixer.music.set_volume(0.0 if _muted else _music_vol)
    except Exception:
        pass
    return _muted


def is_muted():
    return _muted
