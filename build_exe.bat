@echo off
pip install pyinstaller
pyinstaller --onefile --name nexus_terminal app.py
pause
