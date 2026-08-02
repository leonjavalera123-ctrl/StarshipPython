@echo off
REM Launcher for Starship Pyxis. Double-click this (or the desktop shortcut)
REM to play. It moves into the game's folder, then starts main.py with Python.
cd /d "%~dp0"
python main.py
REM If the game closed because of an error, this pause lets you read it.
if errorlevel 1 pause
