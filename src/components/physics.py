"""
Physik-Logik.
"""
import pygame
from src import constants

class PlatformerPhysics:
    """
    Kapselt die Physik-Logik für einen Platformer.
    """
    def __init__(self) -> None:
        self.gravity = constants.GRAVITY
        self.friction = 0.1 # Lerp Faktor
        self.speed = constants.PLAYER_SPEED
        self.jump_force = constants.PLAYER_JUMP_FORCE

    def update(self, rect: pygame.Rect, velocity: pygame.Vector2, input_x: float, platforms: list[pygame.Rect]) -> tuple[pygame.Rect, pygame.Vector2, bool]:
        """
        Führt einen Physik-Schritt durch.
        """
        # 1. Horizontale Geschwindigkeit (Lerp)
        target_vel_x = input_x * self.speed
        velocity.x += (target_vel_x - velocity.x) * self.friction
        
        # 2. Vertikale Geschwindigkeit (Schwerkraft)
        velocity.y += self.gravity
        
        # 3. Position X aktualisieren & Kollision
        rect_x = rect.copy()
        rect_x.x += int(velocity.x)
        
        for plat in platforms:
            if rect_x.colliderect(plat):
                if velocity.x > 0:
                    rect_x.right = plat.left
                    velocity.x = 0
                elif velocity.x < 0:
                    rect_x.left = plat.right
                    velocity.x = 0
        
        # 4. Position Y aktualisieren & Kollision
        rect_y = rect_x # Startet von der neuen X-Pos
        rect_y.y += int(velocity.y)
        on_ground = False
        
        for plat in platforms:
            if rect_y.colliderect(plat):
                if velocity.y > 0:
                    rect_y.bottom = plat.top
                    velocity.y = 0
                    on_ground = True
                elif velocity.y < 0:
                    rect_y.top = plat.bottom
                    velocity.y = 0
        
        return rect_y, velocity, on_ground

    def jump(self, velocity: pygame.Vector2, on_ground: bool) -> pygame.Vector2:
        """Versucht zu springen."""
        if on_ground:
            velocity.y = self.jump_force
        return velocity
