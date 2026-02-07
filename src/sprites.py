"""
Spiel-Objekte (Sprites).
Hier definieren wir die Klassen für den Spieler und die Gegner.
"""
import random
import pygame
from src import settings  # Import aus dem src-Paket

class Player(pygame.sprite.Sprite):
    """
    Der Spieler-Charakter.
    Kann mit den Pfeiltasten nach links und rechts bewegt werden.
    """
    def __init__(self) -> None:
        super().__init__()
        # 1. Aussehen erstellen (Ein blaues Quadrat)
        self.image = pygame.Surface((settings.PLAYER_SIZE, settings.PLAYER_SIZE))
        self.image.fill(settings.BLUE)
        
        # 2. Position festlegen (Rechteck / Hitbox)
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.PLAYER_START_X
        self.rect.bottom = settings.PLAYER_START_Y
        
        # Geschwindigkeit
        self.speed: int = settings.PLAYER_SPEED

    def update(self) -> None:
        """Wird jeden Frame aufgerufen, um die Position zu aktualisieren."""
        keys = pygame.key.get_pressed()
        
        # Bewegung nach links
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        # Bewegung nach rechts
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Bildschirm-Grenzen prüfen (damit der Spieler nicht rausläuft)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    """
    Ein Gegner, der von oben nach unten fällt.
    """
    def __init__(self) -> None:
        super().__init__()
        # Rotes Quadrat als Gegner
        self.image = pygame.Surface((settings.ENEMY_SIZE, settings.ENEMY_SIZE))
        self.image.fill(settings.RED)
        
        # Start-Position: Zufällig oben
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.SCREEN_WIDTH - settings.ENEMY_SIZE)
        self.rect.y = -settings.ENEMY_SIZE  # Startet außerhalb des Bildschirms (oben)
        
        # Zufällige Geschwindigkeit
        self.speed: int = random.randint(settings.ENEMY_SPEED_MIN, settings.ENEMY_SPEED_MAX)

    def update(self) -> None:
        """Bewegt den Gegner nach unten."""
        self.rect.y += self.speed
        
        # Wenn der Gegner unten rausfliegt, löschen wir ihn (um Speicher zu sparen)
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()  # Entfernt das Sprite aus allen Gruppen