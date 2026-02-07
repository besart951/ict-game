"""Startpunkt des Spiels (Game Loop)."""

from __future__ import annotations

import sys
import pygame

from . import settings
from .sprites import Player, Enemy


def main() -> None:
    """Startet das Spiel.

    Ablauf:
    1) Pygame initialisieren
    2) Fenster und Clock erstellen
    3) Sprites erzeugen
    4) Game Loop starten
    """
    pygame.init()

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Mein super Spiel")
    clock = pygame.time.Clock()

    screen_rect = screen.get_rect()

    player = Player(start_pos=screen_rect.center)
    enemies = pygame.sprite.Group()

    # Mehrere Gegner erzeugen, verteilt über die obere Bildschirmhälfte
    for i in range(5):
        enemy_x = 100 + i * 120
        enemy_y = -50 - i * 80
        enemies.add(Enemy(start_pos=(enemy_x, enemy_y)))

    all_sprites = pygame.sprite.Group(player, *enemies)

    running = True
    while running:
        # Ereignisse (Events) verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update der Sprites (Bewegung, Logik)
        all_sprites.update(screen_rect)

        # Bildschirm zeichnen
        screen.fill(settings.WHITE)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(settings.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
