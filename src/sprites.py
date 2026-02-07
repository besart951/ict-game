"""
Alle Spiel-Objekte (Player, Gegner, Plattformen) in einer Datei.
"""
import pygame
import random
from src import settings, assets

class Player(pygame.sprite.Sprite):
    def __init__(self, audio_service):
        super().__init__()
        self.audio_service = audio_service
        
        self.images = {
            "idle": assets.load_image(assets.get_character_path("idle"), settings.CHARACTER_SIZE),
            "jump": assets.load_image(assets.get_character_path("jump"), settings.CHARACTER_SIZE),
            "walk_a": assets.load_image(assets.get_character_path("walk_a"), settings.CHARACTER_SIZE),
            "walk_b": assets.load_image(assets.get_character_path("walk_b"), settings.CHARACTER_SIZE)
        }
        
        self.image = self.images["idle"]
        self.rect = pygame.Rect(0, 0, 32, 44) 
        
        self.pos = pygame.Vector2(100, 400)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        self.facing_right = True
        self.anim_timer = 0.0

    def update(self, platforms):
        self._handle_input()
        self._apply_physics(platforms)
        self._animate()

    def _handle_input(self):
        keys = pygame.key.get_pressed()
        self.accel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.accel_x = -settings.PLAYER_SPEED
            self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.accel_x = settings.PLAYER_SPEED
            self.facing_right = True
            
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel.y = settings.PLAYER_JUMP_FORCE
            self.on_ground = False
            self.audio_service.play_jump()

    def _apply_physics(self, platforms):
        self.vel.x = self.accel_x
        self.pos.x += self.vel.x
        self.rect.x = int(self.pos.x)
        
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if self.vel.x > 0: self.rect.right = plat.rect.left
                elif self.vel.x < 0: self.rect.left = plat.rect.right
                self.pos.x = self.rect.x

        self.vel.y += settings.GRAVITY
        self.pos.y += self.vel.y
        self.rect.y = int(self.pos.y)
        
        self.on_ground = False
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if self.vel.y > 0:
                    self.rect.bottom = plat.rect.top
                    self.vel.y = 0
                    self.on_ground = True
                elif self.vel.y < 0:
                    self.rect.top = plat.rect.bottom
                    self.vel.y = 0
                self.pos.y = self.rect.y

    def _animate(self):
        self.anim_timer += 0.15
        if not self.on_ground:
            img = self.images["jump"]
        elif abs(self.vel.x) > 0:
            frame = int(self.anim_timer) % 2
            img = self.images["walk_a"] if frame == 0 else self.images["walk_b"]
        else:
            img = self.images["idle"]
            
        if not self.facing_right:
            img = pygame.transform.flip(img, True, False)
        self.image = img

class Enemy(pygame.sprite.Sprite):
    """
    Ein Gegner (Barnacle), der animiert ist und besiegt werden kann.
    """
    def __init__(self, x, y, distance=100):
        super().__init__()
        # Bilder laden
        self.images = {
            "attack_a": assets.load_image(assets.get_enemy_path("barnacle_attack_a"), (40, 40)),
            "attack_b": assets.load_image(assets.get_enemy_path("barnacle_attack_b"), (40, 40)),
            "dead": assets.load_image(assets.get_enemy_path("barnacle_attack_rest"), (40, 40))
        }
        
        self.image = self.images["attack_a"]
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.start_x = x
        self.distance = distance
        self.speed = 2
        self.direction = 1
        
        # Status
        self.is_dead = False
        self.dead_timer = 0
        self.anim_timer = 0

    def update(self, platforms):
        if self.is_dead:
            # Wenn besiegt: Kurz liegen bleiben, dann verschwinden
            self.image = self.images["dead"]
            self.dead_timer += 1
            if self.dead_timer > 30: # 0.5 Sekunden warten
                self.kill()
            return

        # Bewegung
        self.rect.x += self.speed * self.direction
        if abs(self.rect.x - self.start_x) >= self.distance:
            self.direction *= -1
        
        # Animation
        self.anim_timer += 0.1
        frame = int(self.anim_timer) % 2
        self.image = self.images["attack_a"] if frame == 0 else self.images["attack_b"]
        
        # Spiegeln je nach Richtung
        if self.direction > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def defeat(self):
        """Wird aufgerufen, wenn der Spieler auf den Kopf springt."""
        self.is_dead = True
        self.speed = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, tile_name="terrain_grass_block_top"):
        super().__init__()
        tile = assets.load_image(assets.get_tile_path(tile_name), (settings.TILE_SIZE, settings.TILE_SIZE))
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        for ix in range(0, w, settings.TILE_SIZE):
            for iy in range(0, h, settings.TILE_SIZE):
                self.image.blit(tile, (ix, iy))
        self.rect = self.image.get_rect(topleft=(x, y))

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = assets.load_image(assets.get_tile_path("sign_exit"), (40, 40))
        self.rect = self.image.get_rect(topleft=(x, y))

class Decoration(pygame.sprite.Sprite):
    def __init__(self, x, y, name, size=(80, 40)):
        super().__init__()
        self.image = assets.load_image(assets.get_tile_path(name), size)
        self.rect = self.image.get_rect(topleft=(x, y))
