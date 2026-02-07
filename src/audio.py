"""
Audio-Verwaltung für das Spiel.
"""
import pygame
from src import assets

class AudioService:
    """Verwaltet Musik und Soundeffekte."""
    
    def __init__(self):
        self.enabled = True
        try:
            pygame.mixer.init()
            self.sounds = {
                "jump": pygame.mixer.Sound(assets.get_sound_path("jump")),
                "win": pygame.mixer.Sound(assets.get_sound_path("magic")),
                "coin": pygame.mixer.Sound(assets.get_sound_path("coin")),
                "select": pygame.mixer.Sound(assets.get_sound_path("select")),
                "hurt": pygame.mixer.Sound(assets.get_sound_path("hurt"))
            }
        except Exception as e:
            print(f"Audio Fehler: {e}")
            self.enabled = False

    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def play_jump(self):
        self.play("jump")

    def play_win(self):
        self.play("win")
        
    def play_select(self):
        self.play("select")
