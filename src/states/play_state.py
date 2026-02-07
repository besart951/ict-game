"""
Spiel-Zustand mit Hintergrundgrafik.
"""
import pygame
from src import constants, assets
from src.core.interfaces import IGameState
from src.entities.player import Player, Platform, Goal
from src.entities.decorations import DecorationService
from src.services.audio_service import AudioService

class PlayState:
    def __init__(self, context) -> None:
        self.context = context
        self.audio_service = context.audio_service
        
        # Hintergrund laden
        self.bg_image = assets.load_image(assets.get_background_path("background_clouds"), 
                                         (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        
        self._create_level()
        
        self.player = Player(self.audio_service)
        self.all_sprites.add(self.player)
        self.camera_x = 0.0

    def _create_level(self) -> None:
        # Boden
        p1 = Platform(0, constants.SCREEN_HEIGHT - 80, 5000, 80)
        self.platforms.add(p1)
        self.all_sprites.add(p1)
        
        level_data = [
            (400, 400, 160, 40),
            (700, 300, 120, 40),
            (1000, 200, 200, 40),
            (1350, 350, 160, 40),
            (1700, 450, 200, 40),
            (2000, 300, 80, 40),
            (2300, 200, 40, 40),
        ]
        
        for plat in level_data:
            p = Platform(*plat)
            self.platforms.add(p)
            self.all_sprites.add(p)
            
        self.goal = Goal(2300, 160)
        self.goals.add(self.goal)
        self.all_sprites.add(self.goal)

        # Dekorationen hinzufügen
        DecorationService.create_random_clouds(self.decorations, 20, 5000)
        DecorationService.create_grass_tufts(self.decorations, self.platforms)
        # Dekorationen zur all_sprites hinzufügen (damit sie gezeichnet werden)
        # Aber wir zeichnen sie separat für Layering
        self.all_sprites.add(self.decorations)

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_input(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.states.menu_state import MenuState
                self.context.change_state(MenuState(self.context))

    def update(self, dt: float) -> None:
        platform_rects = [p.rect for p in self.platforms]
        self.player.update(platform_rects)
        
        # Kamera
        target_cam_x = self.player.rect.centerx - constants.SCREEN_WIDTH // 2
        target_cam_x = max(0, target_cam_x)
        self.camera_x += (target_cam_x - self.camera_x) * 0.1
        
        # Win
        if pygame.sprite.spritecollide(self.player, self.goals, False):
            self.audio_service.play_win()
            from src.states.menu_state import MenuState
            self.context.change_state(MenuState(self.context))

    def draw(self, screen: pygame.Surface) -> None:
        # Parallax Hintergrund (bewegt sich langsamer)
        bg_x = -(int(self.camera_x) // 3) % constants.SCREEN_WIDTH
        screen.blit(self.bg_image, (bg_x, 0))
        screen.blit(self.bg_image, (bg_x - constants.SCREEN_WIDTH, 0))
        screen.blit(self.bg_image, (bg_x + constants.SCREEN_WIDTH, 0))
        
        cam_int = int(self.camera_x)
        for sprite in self.all_sprites:
            r = sprite.visual_rect if hasattr(sprite, 'visual_rect') else sprite.rect
            screen.blit(sprite.image, (r.x - cam_int, r.y))