"""
Zentrale Konstanten für das Spiel.
"""
from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    PAUSE = auto()
    SETTINGS = auto()
    GAME_OVER = auto()

# Bildschirm
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "Pixel Hero: The Great Escape"

# Farben (Cooles Farbschema)
COLOR_BG = (30, 30, 45)       # Dunkelblau
COLOR_TEXT = (240, 240, 240)  # Weißlich
COLOR_ACCENT = (255, 100, 0)   # Orange
COLOR_PLAYER = (0, 200, 255)   # Hellblau
COLOR_PLATFORM = (100, 100, 120) # Grau
COLOR_GOAL = (50, 255, 150)    # Neongrün

# Physik
GRAVITY = 0.9
PLAYER_SPEED = 8
PLAYER_JUMP_FORCE = -18
# SCROLL_THRESHOLD wird nicht mehr direkt benötigt dank Lerp-Kamera
