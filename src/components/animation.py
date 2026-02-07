"""
Animations-Komponenten.
"""
import pygame

class SquashStretchAnimator:
    """
    Verwaltet die Squash & Stretch Animation.
    """
    def __init__(self, original_image: pygame.Surface) -> None:
        self.base_image = original_image
        self.current_image = original_image
        self.stretch_factor = 1.0
        self.base_width = original_image.get_width()
        self.base_height = original_image.get_height()

    def update(self, velocity: pygame.Vector2, on_ground: bool) -> None:
        """Berechnet den neuen Stretch-Faktor."""
        # Rückkehr zur Normalform
        self.stretch_factor += (1.0 - self.stretch_factor) * 0.1
        
        target_stretch = 1.0
        
        if not on_ground:
            # Stretch beim Fallen/Springen
            target_stretch = 1.0 + abs(velocity.y) * 0.02
        else:
            # Squash beim Laufen
            squash = 1.0 + abs(velocity.x) * 0.02
            # Squash bedeutet Breite > Höhe, also Stretch Faktor < 1
            target_stretch = 1.0 / squash
            
        # Wir kombinieren den Target-Stretch mit dem Impuls-Stretch
        # Hier vereinfacht: Wir wenden den Target-Stretch direkt an die Visuals an,
        # behalten aber self.stretch_factor für Impulse (z.B. Landung) bei.
        
        final_w = int(self.base_width / (target_stretch * self.stretch_factor))
        final_h = int(self.base_height * (target_stretch * self.stretch_factor))
        
        self.current_image = pygame.transform.scale(self.base_image, (final_w, final_h))

    def trigger_jump(self) -> None:
        """Setzt einen Impuls für Stretch beim Absprung."""
        self.stretch_factor = 1.3

    def get_image(self) -> pygame.Surface:
        return self.current_image
