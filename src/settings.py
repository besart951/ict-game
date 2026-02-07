"""
Einstellungen für das Spiel.
Hier werden Konstanten wie Bildschirmgröße, Farben und Geschwindigkeit definiert.
"""

# Bildschirm-Einstellungen
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60
TITLE: str = "Mein Super OOP Spiel"

# Farben (R, G, B)
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
BLUE: tuple[int, int, int] = (50, 150, 255)
RED: tuple[int, int, int] = (220, 50, 50)
GREEN: tuple[int, int, int] = (50, 200, 50)

# Spieler-Einstellungen
PLAYER_SIZE: int = 50
PLAYER_SPEED: int = 5
PLAYER_START_X: int = SCREEN_WIDTH // 2
PLAYER_START_Y: int = SCREEN_HEIGHT - 100

# Gegner-Einstellungen
ENEMY_SIZE: int = 40
ENEMY_SPEED_MIN: int = 3
ENEMY_SPEED_MAX: int = 6
ENEMY_SPAWN_RATE: int = 60  # Alle 60 Frames (ca. 1 Sekunde) ein neuer Gegner