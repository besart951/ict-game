"""
Spiel-Entitäten mit echten Sprites.
"""
import pygame
from src import constants, assets
from src.components.input import KeyboardInputHandler
from src.components.physics import PlatformerPhysics
from src.services.audio_service import AudioService

class Player(pygame.sprite.Sprite):
    """
    Der Spieler mit Animationen aus den neuen Assets.
    """
    def __init__(self, audio_service: AudioService) -> None:
        super().__init__()
        self.audio_service = audio_service
        
        # 1. Sprites laden
        self.images = {
            "idle": assets.load_image(assets.get_character_path("idle"), (48, 48)),
            "jump": assets.load_image(assets.get_character_path("jump"), (48, 48)),
            "walk_a": assets.load_image(assets.get_character_path("walk_a"), (48, 48)),
            "walk_b": assets.load_image(assets.get_character_path("walk_b"), (48, 48))
        }
        
        # 2. Komponenten
        self.physics = PlatformerPhysics()
        self.input_handler = KeyboardInputHandler()
        
        # 3. State
        self.image = self.images["idle"]
        self.rect = pygame.Rect(0, 0, 32, 44) # Physics Hitbox etwas kleiner als Sprite
        self.visual_rect = self.image.get_rect()
        
        self.pos = pygame.Vector2(100, 400)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        
        # Animations-Timer
        self.anim_timer = 0.0
        self.facing_right = True

    def update(self, platforms: list[pygame.Rect]) -> None:
        # Input
        x_input = self.input_handler.get_x_axis()
        wants_jump = self.input_handler.is_jump_pressed()
        
        if x_input > 0: self.facing_right = True
        elif x_input < 0: self.facing_right = False

        # Springen
        if wants_jump and self.on_ground:
            self.vel = self.physics.jump(self.vel, self.on_ground)
            self.audio_service.play_jump()
            self.on_ground = False

        # Physik
        self.rect, self.vel, self.on_ground = self.physics.update(
            self.rect, self.vel, x_input, platforms
        )
        
        # Animation wählen
        self._animate(x_input)

    def _animate(self, x_input: float) -> None:
        self.anim_timer += 0.15 # Geschwindigkeit der Animation
        
        if not self.on_ground:
            img = self.images["jump"]
        elif abs(self.vel.x) > 0.5:
            # Wechsel zwischen walk_a und walk_b
            frame = int(self.anim_timer) % 2
            img = self.images["walk_a"] if frame == 0 else self.images["walk_b"]
        else:
            img = self.images["idle"]
            
        # Spiegeln falls nötig
        if not self.facing_right:
            img = pygame.transform.flip(img, True, False)
            
        self.image = img
        self.visual_rect = self.image.get_rect(midbottom=self.rect.midbottom)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        super().__init__()
        # Wir laden einen Gras-Tile
        tile = assets.load_image(assets.get_tile_path("terrain_grass_block_top"), (40, 40))
        
        # Wir füllen die Fläche mit dem Tile
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        for ix in range(0, w, 40):
            for iy in range(0, h, 40):
                self.image.blit(tile, (ix, iy))
        
        self.rect = self.image.get_rect(topleft=(x, y))

class Goal(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        # Flagge oder Exit-Schild als Ziel
        self.image = assets.load_image(assets.get_tile_path("sign_exit"), (40, 40))
        self.rect = self.image.get_rect(topleft=(x, y))