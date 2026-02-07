"""
Spielfiguren und Level-Objekte.
"""
import pygame
from src import constants

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # Basis-Grafik
        self.base_image = pygame.Surface((40, 60), pygame.SRCALPHA)
        pygame.draw.rect(self.base_image, constants.COLOR_PLAYER, (0, 0, 40, 60), border_radius=5)
        pygame.draw.rect(self.base_image, (0, 0, 0), (8, 12, 6, 6)) # Augen
        pygame.draw.rect(self.base_image, (0, 0, 0), (26, 12, 6, 6))
        
        self.image = self.base_image.copy()
        
        # Physics Hitbox (Konstante Größe, damit man nicht stecken bleibt)
        self.rect = pygame.Rect(0, 0, 36, 58) 
        self.pos = pygame.Vector2(100, 400)
        self.vel = pygame.Vector2(0, 0)
        
        self.on_ground = False
        self.jump_sound = None
        
        # Animation State
        self.walk_frame = 0
        self.stretch_factor = 1.0

    def jump(self) -> None:
        if self.on_ground:
            self.vel.y = constants.PLAYER_JUMP_FORCE
            self.on_ground = False
            self.stretch_factor = 1.3 # Stretch beim Absprung
            if self.jump_sound:
                self.jump_sound.play()

    def update(self, platforms: pygame.sprite.Group) -> None:
        # 1. Horizontale Bewegung
        keys = pygame.key.get_pressed()
        target_vel_x = 0
        if keys[pygame.K_LEFT]: target_vel_x = -constants.PLAYER_SPEED
        if keys[pygame.K_RIGHT]: target_vel_x = constants.PLAYER_SPEED
        
        # Sanftes Beschleunigen/Bremsen (Lerp-like)
        accel = 0.2 if self.on_ground else 0.1
        self.vel.x += (target_vel_x - self.vel.x) * accel

        # 2. Vertikale Bewegung (Schwerkraft)
        self.vel.y += constants.GRAVITY
        if self.vel.y > 15: self.vel.y = 15 # Terminal Velocity

        # 3. X-Kollision
        self.pos.x += self.vel.x
        self.rect.centerx = int(self.pos.x)
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            if self.vel.x > 0:
                self.rect.right = hit.rect.left
                self.pos.x = self.rect.centerx
                self.vel.x = 0
            elif self.vel.x < 0:
                self.rect.left = hit.rect.right
                self.pos.x = self.rect.centerx
                self.vel.x = 0

        # 4. Y-Kollision
        self.pos.y += self.vel.y
        self.rect.bottom = int(self.pos.y)
        self.on_ground = False
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            if self.vel.y > 0:
                self.rect.bottom = hit.rect.top
                self.pos.y = self.rect.bottom
                self.vel.y = 0
                self.on_ground = True
            elif self.vel.y < 0:
                self.rect.top = hit.rect.bottom
                self.pos.y = self.rect.bottom
                self.vel.y = 0

        # 5. Animation (Visual Only)
        self.animate()

        # Welt-Grenzen
        if self.rect.top > constants.SCREEN_HEIGHT + 200:
            self.reset()

    def animate(self) -> None:
        # Stretch Faktor kehrt langsam zur Normalität (1.0) zurück
        self.stretch_factor += (1.0 - self.stretch_factor) * 0.1
        
        # Dynamisches Squash bei Landung oder Stretch bei Fall
        if not self.on_ground:
            # Stretch im Flug basierend auf Y-Geschwindigkeit
            anim_stretch = 1.0 + abs(self.vel.y) * 0.02
            w = int(40 / anim_stretch)
            h = int(60 * anim_stretch)
        else:
            # Squash beim Laufen
            anim_squash = 1.0 + abs(self.vel.x) * 0.02
            w = int(40 * anim_squash)
            h = int(60 / anim_squash)
        
        # Letzten Stretch-Impuls (z.B. vom Sprung) addieren
        w = int(w / self.stretch_factor)
        h = int(h * self.stretch_factor)

        self.image = pygame.transform.scale(self.base_image, (w, h))
        # Das Bild soll immer unten zentriert am Hitbox-Boden kleben
        self.visual_rect = self.image.get_rect(midbottom=self.rect.midbottom)

    def reset(self) -> None:
        self.pos = pygame.Vector2(100, 400)
        self.vel = pygame.Vector2(0, 0)
        self.rect.midbottom = (int(self.pos.x), int(self.pos.y))

    def reset(self) -> None:
        self.pos = pygame.Vector2(100, 400)
        self.vel = pygame.Vector2(0, 0)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(constants.COLOR_PLATFORM)
        # Ein bisschen Textur
        for i in range(0, w, 20):
            pygame.draw.line(self.image, (80, 80, 100), (i, 0), (i, h), 1)
        
        self.rect = self.image.get_rect(topleft=(x, y))

class Goal(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.Surface((60, 80))
        self.image.fill(constants.COLOR_GOAL)
        self.rect = self.image.get_rect(topleft=(x, y))
