"""
State Machine Implementierung.
"""
import pygame
from src.core.interfaces import IGameState

class StateMachine:
    """
    Verwaltet den aktuellen Spielzustand.
    """
    def __init__(self) -> None:
        self.current_state: IGameState | None = None

    def change_state(self, new_state: IGameState) -> None:
        """Wechselt zu einem neuen Zustand."""
        if self.current_state:
            self.current_state.exit()
        
        self.current_state = new_state
        self.current_state.enter()

    def update(self, dt: float) -> None:
        if self.current_state:
            self.current_state.update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        if self.current_state:
            self.current_state.draw(screen)
            
    def handle_input(self, event: pygame.event.Event) -> None:
        if self.current_state:
            self.current_state.handle_input(event)
