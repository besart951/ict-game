"""
Die Haupt-Klasse des Spiels.
Hier wird Pygame initialisiert und der Game-Loop gestartet.
"""
import pygame
import sys
from src import settings
from src.states.state_machine import StateMachine
from src.states.menu_state import MenuState
from src.audio import AudioService

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        
        self.audio_service = AudioService()
        self.state_machine = StateMachine()
        
        # Startzustand: Hauptmenü
        self.state_machine.change_state(MenuState(self))

    def change_state(self, new_state):
        self.state_machine.change_state(new_state)

    def run(self):
        """Der Game Loop läuft 60 mal pro Sekunde."""
        while True:
            # Delta Time (Zeit seit dem letzten Frame)
            dt = self.clock.tick(settings.FPS) / 1000.0
            
            # Events abarbeiten (Tastatur, Maus, Beenden)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.state_machine.handle_input(event)
            
            # Spiel-Logik aktualisieren
            self.state_machine.update(dt)
            
            # Alles zeichnen
            self.state_machine.draw(self.screen)
            
            # Bildschirm aktualisieren
            pygame.display.flip()