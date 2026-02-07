"""
Asset-Verwaltung für das Spiel.
Lädt Grafiken und Sounds aus dem src/assets Verzeichnis.
Verwendet absolute Pfade relativ zur Datei, um Working-Directory-Fehler zu vermeiden.
"""
import os
import sys
import pygame

# Basis-Pfad: Das Verzeichnis, in dem diese Datei liegt
# Falls als EXE ausgeführt, nutzt PyInstaller den temporären Pfad _MEIPASS
if hasattr(sys, '_MEIPASS'):
    BASE_PATH = os.path.join(sys._MEIPASS, "src")
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSET_DIR = os.path.join(BASE_PATH, "assets")
SPRITE_DIR = os.path.join(ASSET_DIR, "Sprites")
SOUND_DIR = os.path.join(ASSET_DIR, "Sounds")

def get_character_path(name: str, color: str = "yellow") -> str:
    return os.path.join(SPRITE_DIR, "Characters", "Default", f"character_{color}_{name}.png")

def get_tile_path(name: str) -> str:
    return os.path.join(SPRITE_DIR, "Tiles", "Default", f"{name}.png")

def get_enemy_path(name: str) -> str:
    return os.path.join(SPRITE_DIR, "Enemies", "Default", f"{name}.png")

def get_background_path(name: str) -> str:
    return os.path.join(SPRITE_DIR, "Backgrounds", "Default", f"{name}.png")

def get_sound_path(name: str) -> str:
    return os.path.join(SOUND_DIR, f"sfx_{name}.ogg")

def load_image(path: str, scale: tuple[int, int] | None = None) -> pygame.Surface:
    """Lädt ein Bild und skaliert es optional."""
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except Exception as e:
        print(f"Fehler beim Laden von {path}: {e}")
        # Rückfall: Ein Platzhalter
        fallback = pygame.Surface(scale if scale else (32, 32))
        fallback.fill((255, 0, 255)) 
        return fallback

def ensure_assets() -> None:
    """Prüft, ob der Asset-Ordner existiert."""
    if not os.path.exists(ASSET_DIR):
        print(f"WARNUNG: Asset-Verzeichnis {ASSET_DIR} nicht gefunden!")
