"""
Das Hauptmenü des Spiels.
"""
import sys
import pygame
from src import settings
from src.ui import Button

class MenuState:
    def __init__(self, context):
        self.context = context
        # Buttons erstellen
        self.buttons = [
            Button(settings.SCREEN_WIDTH//2 - 100, 250, 200, 60, "START", (255, 100, 0)),
            Button(settings.SCREEN_WIDTH//2 - 100, 350, 200, 60, "BEENDEN", (200, 50, 50))
        ]
        self.font = pygame.font.SysFont("arial", 64, bold=True)

    def enter(self):
        pygame.mouse.set_visible(True)

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.buttons:
                if btn.is_clicked(event):
                    self.context.audio_service.play_select()
                    
                    if btn.text == "START":
                        from src.states.play_state import PlayState
                        self.context.change_state(PlayState(self.context))
                    elif btn.text == "BEENDEN":
                        pygame.quit()
                        sys.exit()

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons:
            btn.check_hover(mouse_pos)

    def draw(self, screen):
        screen.fill(settings.COLOR_BG)
        
        # Titel zeichnen
        title_surf = self.font.render(settings.TITLE, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(settings.SCREEN_WIDTH//2, 150))
        screen.blit(title_surf, title_rect)
        
        # Buttons zeichnen
        for btn in self.buttons:
            btn.draw(screen)