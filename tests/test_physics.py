"""
Unit Tests für die Physik-Engine.
"""
import unittest
import pygame
from src.components.physics import PlatformerPhysics

class TestPhysics(unittest.TestCase):
    def setUp(self) -> None:
        self.physics = PlatformerPhysics()
        self.rect = pygame.Rect(0, 0, 40, 60)
        self.vel = pygame.Vector2(0, 0)

    def test_gravity(self) -> None:
        """Testet, ob Schwerkraft angewendet wird."""
        self.physics.update(self.rect, self.vel, 0, [])
        self.assertGreater(self.vel.y, 0, "Schwerkraft sollte Velocity Y erhöhen")

    def test_movement(self) -> None:
        """Testet horizontale Bewegung."""
        # Input nach rechts (1.0)
        self.physics.update(self.rect, self.vel, 1.0, [])
        self.assertGreater(self.vel.x, 0, "Input rechts sollte positive Velocity erzeugen")

    def test_collision_floor(self) -> None:
        """Testet Bodenkollision."""
        # Spieler in der Luft, fällt schnell
        self.rect.y = 100
        self.vel.y = 10
        
        # Boden bei 110
        floor = pygame.Rect(0, 110, 200, 20)
        
        new_rect, new_vel, on_ground = self.physics.update(self.rect, self.vel, 0, [floor])
        
        self.assertTrue(on_ground, "Sollte den Boden berühren")
        self.assertEqual(new_vel.y, 0, "Vertikale Geschwindigkeit sollte 0 sein")
        self.assertEqual(new_rect.bottom, floor.top, "Sollte auf dem Boden stehen")

if __name__ == "__main__":
    unittest.main()
