"""
Entitäten für Dekorationen.
"""
import pygame
import random
from src import assets

class Decoration(pygame.sprite.Sprite):
    """Einfache Dekoration wie Wolken oder Gras."""
    def __init__(self, x: int, y: int, name: str, scale: tuple[int, int]) -> None:
        super().__init__()
        self.image = assets.load_image(assets.get_tile_path(name), scale)
        self.rect = self.image.get_rect(topleft=(x, y))

class DecorationService:
    """Hilft beim Erstellen von Dekorationen."""
    @staticmethod
    def create_random_clouds(group: pygame.sprite.Group, count: int, world_width: int) -> None:
        for _ in range(count):
            x = random.randint(0, world_width)
            y = random.randint(50, 200)
            cloud = Decoration(x, y, "terrain_stone_cloud", (80, 40))
            group.add(cloud)

    @staticmethod
    def create_grass_tufts(group: pygame.sprite.Group, platforms: pygame.sprite.Group) -> None:
        for plat in platforms:
            # Nur auf horizontalen Flächen
            if plat.rect.width > 40:
                for x in range(plat.rect.left, plat.rect.right, 100):
                    if random.random() > 0.5:
                        tuft = Decoration(x, plat.rect.top - 20, "grass", (20, 20))
                        group.add(tuft)
