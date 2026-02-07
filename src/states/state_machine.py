"""
Verwaltet den aktuellen Spielzustand (z.B. Menü oder Spiel).
"""
class StateMachine:
    def __init__(self):
        self.current_state = None

    def change_state(self, new_state):
        # Wir rufen exit() beim alten State auf, falls es existiert
        if self.current_state and hasattr(self.current_state, 'exit'):
            self.current_state.exit()
        
        self.current_state = new_state
        
        # Wir rufen enter() beim neuen State auf, falls es existiert
        if self.current_state and hasattr(self.current_state, 'enter'):
            self.current_state.enter()

    def handle_input(self, event):
        if self.current_state:
            self.current_state.handle_input(event)

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)