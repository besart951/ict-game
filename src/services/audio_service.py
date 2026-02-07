"""
Audio-Dienste für das neue Asset-Paket.
"""
import pygame
from src import assets

class AudioService:
    """Verwaltet die neuen Kenney SFX Sounds."""
    
    def __init__(self) -> None:
        self.enabled = True
        try:
            pygame.mixer.init()
            # Wir laden die neuen OGG Sounds
            self.sounds = {
                "jump": pygame.mixer.Sound(assets.get_sound_path("jump")),
                "win": pygame.mixer.Sound(assets.get_sound_path("magic")), # Magic klingt wie Sieg
                "coin": pygame.mixer.Sound(assets.get_sound_path("coin")),
                "select": pygame.mixer.Sound(assets.get_sound_path("select")),
                "hurt": pygame.mixer.Sound(assets.get_sound_path("hurt"))
            }
        except Exception as e:
            print(f"Audio konnte nicht vollständig initialisiert werden: {e}")
            self.enabled = False

    def play(self, name: str) -> None:
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def play_jump(self) -> None:
        self.play("jump")

    def play_win(self) -> None:
        self.play("win")
        
    def play_select(self) -> None:
        self.play("select")