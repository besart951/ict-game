"""
Haupteinstiegspunkt für das Pixel Hero Spiel.
"""
import sys
import os

# Pfad anpassen, damit src gefunden wird
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game import Game

def main() -> None:
    # Spielinstanz erstellen und starten
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
