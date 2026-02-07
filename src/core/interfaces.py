"""
Kern-Schnittstellen (Interfaces) für die Spiel-Architektur.
Hier definieren wir die Verträge (Protocols), die unsere Klassen erfüllen müssen.
Dies unterstützt das Dependency Inversion Principle (DIP).
"""
from typing import Protocol, runtime_checkable
import pygame

@runtime_checkable
class IInputHandler(Protocol):
    """
    Schnittstelle für Eingabe-Verarbeitung.
    ISP: Nur Methoden, die für Input relevant sind.
    """
    def get_x_axis(self) -> float:
        """Gibt die horizontale Eingabe zurück (-1.0 bis 1.0)."""
        ...
    
    def is_jump_pressed(self) -> bool:
        """Gibt True zurück, wenn die Sprung-Taste gedrückt wurde."""
        ...
    
    def is_pause_pressed(self) -> bool:
        """Gibt True zurück, wenn die Pause-Taste gedrückt wurde."""
        ...

@runtime_checkable
class IPhysicsComponent(Protocol):
    """
    Schnittstelle für Physik-Berechnungen.
    SRP: Trennt Physik von der Entity-Logik.
    """
    def update(self, rect: pygame.Rect, velocity: pygame.Vector2, input_x: float, platforms: list[pygame.Rect]) -> tuple[pygame.Rect, pygame.Vector2, bool]:
        """
        Berechnet die neue Position und Geschwindigkeit.
        Gibt (neues_rect, neue_velocity, on_ground) zurück.
        """
        ...

@runtime_checkable
class IRenderer(Protocol):
    """
    Schnittstelle für das Zeichnen auf den Bildschirm.
    DIP: Das Spiel hängt nicht direkt von pygame.draw ab.
    """
    def render(self, surface: pygame.Surface, camera_x: int) -> None:
        """Zeichnet das Objekt relativ zur Kamera."""
        ...

@runtime_checkable
class IGameState(Protocol):
    """
    Schnittstelle für einen Spielzustand (State Pattern).
    OCP: Neue Zustände können hinzugefügt werden, ohne den Manager zu ändern.
    """
    def handle_input(self, event: pygame.event.Event) -> None:
        """Verarbeitet Events."""
        ...

    def update(self, dt: float) -> None:
        """Aktualisiert die Logik des Zustands."""
        ...

    def draw(self, screen: pygame.Surface) -> None:
        """Zeichnet den Zustand."""
        ...
    
    def enter(self) -> None:
        """Wird aufgerufen, wenn der Zustand aktiv wird."""
        ...
    
    def exit(self) -> None:
        """Wird aufgerufen, wenn der Zustand verlassen wird."""
        ...
