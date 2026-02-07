"""
Eingabe-Komponenten.
"""
import pygame
from src.core.interfaces import IInputHandler

class KeyboardInputHandler:
    """
    Implementierung von IInputHandler für Tastatur-Steuerung.
    """
    def get_x_axis(self) -> float:
        keys = pygame.key.get_pressed()
        val = 0.0
        if keys[pygame.K_LEFT]:
            val -= 1.0
        if keys[pygame.K_RIGHT]:
            val += 1.0
        return val

    def is_jump_pressed(self) -> bool:
        # Hinweis: Dies prüft den aktuellen Status, für One-Shot Events
        # sollte man Event-Loop nutzen. Hier vereinfacht für Movement-Logik.
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE] or keys[pygame.K_UP]

    def is_pause_pressed(self) -> bool:
        keys = pygame.key.get_pressed()
        return keys[pygame.K_ESCAPE]
