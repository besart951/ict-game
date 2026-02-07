"""
Menü-Zustand.
"""
import sys
import pygame
from src import constants
from src.ui import Button
from src.core.interfaces import IGameState

class MenuState:
    """Zeigt das Hauptmenü an."""
    
    def __init__(self, context) -> None:
        self.context = context
        self.buttons = [
            Button(400, 250, 200, 60, "START", constants.COLOR_ACCENT),
            Button(400, 410, 200, 60, "QUIT", (200, 50, 50))
        ]
        self.font = pygame.font.SysFont("arial", 64, bold=True)

    def enter(self) -> None:
        pygame.mouse.set_visible(True)

    def exit(self) -> None:
        pass

    def handle_input(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.buttons:
                if btn.is_clicked(event):
                    self.context.audio_service.play_select()
                    
                    if btn.text == "START":
                        from src.states.play_state import PlayState
                        self.context.change_state(PlayState(self.context))
                    elif btn.text == "QUIT":
                        pygame.quit()
                        sys.exit()

    def update(self, dt: float) -> None:
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons:
            btn.check_hover(mouse_pos)

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(constants.COLOR_BG)
        title_surf = self.font.render(constants.TITLE, True, constants.COLOR_ACCENT)
        title_rect = title_surf.get_rect(center=(constants.SCREEN_WIDTH//2, 150))
        screen.blit(title_surf, title_rect)
        
        for btn in self.buttons:
            btn.draw(screen)
