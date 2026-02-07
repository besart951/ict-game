"""Sprite-Klassen für das Spiel."""

from __future__ import annotations

import random
import pygame

from . import settings


class Player(pygame.sprite.Sprite):
    """Der Spieler-Sprite, steuerbar mit den Pfeiltasten."""

    def __init__(self, start_pos: tuple[int, int]) -> None:
        """Initialisiert den Spieler.

        Wichtige Punkte:
        - Wir erstellen ein einfaches farbiges Surface als Platzhalter-Grafik.
        - Mit `get_rect()` erzeugen wir ein Rechteck (rect), das Position
          und Kollisionen beschreibt.
        - Das rect ist die wichtigste Anlaufstelle für Positionen im Spiel.
        """
        super().__init__()

        # Platzhalter-Grafik: ein blaues Quadrat
        self.image = pygame.Surface((settings.PLAYER_SIZE, settings.PLAYER_SIZE))
        self.image.fill(settings.BLUE)

        # Das rect speichert Position und Größe. Startposition per center setzen.
        self.rect = self.image.get_rect(center=start_pos)

        # Bewegungsgeschwindigkeit in Pixel pro Update-Schritt
        self.speed = settings.PLAYER_SPEED

    def update(self, screen_rect: pygame.Rect) -> None:
        """Aktualisiert die Spielerposition pro Frame.

        - Wir lesen die Tastatur mit `pygame.key.get_pressed()`.
        - Die Bewegung wird über das rect gesteuert (rect.x / rect.y).
        - Danach halten wir den Spieler im Bildschirmrahmen.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Spieler innerhalb des sichtbaren Bereichs halten
        self.rect.clamp_ip(screen_rect)


class Enemy(pygame.sprite.Sprite):
    """Ein einfacher Gegner, der von oben nach unten fliegt."""

    def __init__(self, start_pos: tuple[int, int]) -> None:
        """Initialisiert den Gegner.

        - Auch hier nutzen wir ein farbiges Surface als Platzhalter.
        - Das rect bestimmt Position und Größe.
        """
        super().__init__()

        self.image = pygame.Surface((settings.ENEMY_SIZE, settings.ENEMY_SIZE))
        self.image.fill(settings.RED)

        self.rect = self.image.get_rect(center=start_pos)
        self.speed = settings.ENEMY_SPEED

    def update(self, screen_rect: pygame.Rect) -> None:
        """Bewegt den Gegner nach unten.

        - Wenn der Gegner den unteren Bildschirmrand verlässt,
          setzen wir ihn wieder nach oben.
        - Die neue X-Position wird zufällig gewählt.
        """
        self.rect.y += self.speed

        if self.rect.top > screen_rect.bottom:
            new_x = random.randint(
                screen_rect.left + settings.ENEMY_SPAWN_MARGIN,
                screen_rect.right - settings.ENEMY_SPAWN_MARGIN,
            )
            self.rect.midbottom = (new_x, screen_rect.top)
