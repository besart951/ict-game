"""
UI-Komponenten für Menüs.
"""
import pygame
from src import constants

class Button:
    """Ein klickbarer Button für Menüs."""
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int]) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("arial", 32, bold=True)
        self.is_hovered = False

    def draw(self, screen: pygame.Surface) -> None:
        # Hover-Effekt: Farbe etwas heller machen
        draw_color = [min(c + 30, 255) for c in self.color] if self.is_hovered else self.color
        
        # Schatten
        pygame.draw.rect(screen, (20, 20, 20), (self.rect.x + 5, self.rect.y + 5, self.rect.width, self.rect.height))
        # Button
        pygame.draw.rect(screen, draw_color, self.rect)
        pygame.draw.rect(screen, constants.COLOR_TEXT, self.rect, 2) # Rahmen

        # Text zentrieren
        text_surf = self.font.render(self.text, True, constants.COLOR_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos: tuple[int, int]) -> None:
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False
