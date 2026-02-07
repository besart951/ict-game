"""
Der Spiel-Zustand (Das eigentliche Level).
Hier wird das Level aufgebaut und aktualisiert.
"""
import pygame
import random
from src import settings, assets, sprites

class PlayState:
    def __init__(self, context):
        self.context = context
        self.audio_service = context.audio_service
        
        # Hintergrund
        self.bg_image = assets.load_image(assets.get_background_path("background_clouds"), 
                                         (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        
        # Gruppen
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        
        # Level bauen
        self._setup_level()
        
        # Spieler erstellen
        self.player = sprites.Player(self.audio_service)
        self.all_sprites.add(self.player)
        
        self.camera_x = 0

    def _setup_level(self):
        """
        Hier können Kinder ganz einfach neue Plattformen und Gegner hinzufügen!
        """
        # 1. Bodenplatten (x, y, breite, höhe)
        level_platforms = [
            (0, 520, 3000, 80),    # Langer Boden
            (400, 400, 160, 40),   # Kleine Plattform
            (700, 300, 200, 40),
            (1100, 350, 120, 40),
            (1400, 250, 160, 40),
            (1800, 400, 200, 40),
            (2200, 300, 80, 40),
            (2500, 200, 400, 40),
        ]
        
        for p_data in level_platforms:
            p = sprites.Platform(*p_data)
            self.platforms.add(p)
            self.all_sprites.add(p)

        # 2. Gegner (x, y, laufweite)
        level_enemies = [
            (500, 480, 200),
            (1200, 480, 300),
            (1800, 360, 150),
        ]
        
        for e_data in level_enemies:
            e = sprites.Enemy(*e_data)
            self.enemies.add(e)
            self.all_sprites.add(e)

        # 3. Ziel
        self.goal = sprites.Goal(2700, 160)
        self.goals.add(self.goal)
        self.all_sprites.add(self.goal)

        # 4. Ein paar Wolken zufällig verteilen
        for _ in range(15):
            cloud = sprites.Decoration(random.randint(0, 3000), random.randint(50, 200), "terrain_stone_cloud")
            self.decorations.add(cloud)
            self.all_sprites.add(cloud)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.states.menu_state import MenuState
                self.context.change_state(MenuState(self.context))

    def update(self, dt):
        # Update alle Sprites
        self.player.update(self.platforms)
        self.enemies.update(self.platforms)
        
        # Kamera folgt dem Spieler
        target_cam_x = self.player.rect.centerx - settings.SCREEN_WIDTH // 2
        target_cam_x = max(0, target_cam_x)
        self.camera_x += (target_cam_x - self.camera_x) * 0.1
        
        # Kollision: Spieler <-> Gegner
        enemy_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for enemy in enemy_hits:
            if not enemy.is_dead:
                # Prüfen, ob der Spieler von oben kommt (Kopf-Sprung)
                # Die Unterkante des Spielers muss über der Mitte des Gegners sein UND er muss fallen
                if self.player.vel.y > 0 and self.player.rect.bottom < enemy.rect.centery + 10:
                    enemy.defeat()
                    self.player.vel.y = -12 # Kleiner Sprung nach oben
                    self.audio_service.play("coin") # Benutze Coin-Sound für Sieg
                else:
                    self.audio_service.play("hurt")
                    self._restart_level()

        # Kollision: Spieler <-> Ziel
        if pygame.sprite.spritecollide(self.player, self.goals, False):
            self.audio_service.play_win()
            from src.states.menu_state import MenuState
            self.context.change_state(MenuState(self.context))

    def _restart_level(self):
        self.player.pos = pygame.Vector2(100, 400)
        self.player.vel = pygame.Vector2(0, 0)

    def draw(self, screen):
        bg_x = -(int(self.camera_x) // 3) % settings.SCREEN_WIDTH
        screen.blit(self.bg_image, (bg_x, 0))
        screen.blit(self.bg_image, (bg_x - settings.SCREEN_WIDTH, 0))
        screen.blit(self.bg_image, (bg_x + settings.SCREEN_WIDTH, 0))
        
        cam_offset = int(self.camera_x)
        for sprite in self.all_sprites:
            screen.blit(sprite.image, (sprite.rect.x - cam_offset, sprite.rect.y))