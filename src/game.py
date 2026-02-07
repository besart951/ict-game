"""
Die Haupt-Klasse (Game Loop).
"""
import pygame
import sys
from src import constants
from src.states.state_machine import StateMachine
from src.states.menu_state import MenuState
from src.services.audio_service import AudioService

class Game:
    """
    Der Einstiegspunkt des Spiels. Verwaltet Fenster und Game Loop.
    """
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()
        
        self.audio_service = AudioService()
        self.state_machine = StateMachine()
        # Start State setzen
        self.state_machine.change_state(MenuState(self))

    def change_state(self, new_state) -> None:
        """Delegiert State-Wechsel an die StateMachine."""
        self.state_machine.change_state(new_state)

    def run(self) -> None:
        """Der Game Loop."""
        while True:
            dt = self.clock.tick(constants.FPS) / 1000.0 # Delta Time in Sekunden
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.state_machine.handle_input(event)
            
            self.state_machine.update(dt)
            self.state_machine.draw(self.screen)
            
            pygame.display.flip()
