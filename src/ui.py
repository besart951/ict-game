"""
UI-Elemente wie Buttons.
"""
import pygame

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("arial", 32, bold=True)
        self.is_hovered = False

    def draw(self, screen):
        # Farbe heller machen wenn Maus drüber ist
        draw_color = [min(c + 30, 255) for c in self.color] if self.is_hovered else self.color
        
        # Kleiner Schatten für 3D Effekt
        pygame.draw.rect(screen, (20, 20, 20), (self.rect.x + 4, self.rect.y + 4, self.rect.width, self.rect.height))
        # Der eigentliche Button
        pygame.draw.rect(screen, draw_color, self.rect)
        # Weißer Rahmen
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        # Text in die Mitte setzen
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False