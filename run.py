"""
Starte das Spiel mit diesem Skript.
"""
import sys
import os

# Sicherstellen, dass das 'src' Verzeichnis im Pfad ist
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from src.main import main

if __name__ == "__main__":
    main()