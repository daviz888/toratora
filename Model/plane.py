
import os
import pygame
import random
from pygame.sprite import Sprite
from Shared.gameSettings import GameSettings
from Model.bullet import Bullet


class Plane(Sprite):

    def __init__(self, allsprites, enemy_bullets):
        super().__init__()
        # self.__filename = str(random.randrange(0, 5)) + '.png'
        self.allsprites = allsprites
        self.enemy_bullets = enemy_bullets
        self.__filename = "1.png"
        self.image = pygame.image.load(os.path.join(GameSettings.ASSETS_PATH, self.__filename)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 /2)
        self.__hitspoints = 50 - self.radius
        self.rect.x = GameSettings.SCREEN_SIZE[0]
        self.rect.y = GameSettings.SCREEN_SIZE[1]
        self.speedx = 3
        self.speedy = 3
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1000
        self.shooting = False

    def update(self):

        self.rect.y += self.speedy

        if self.rect.y >= GameSettings.SCREEN_SIZE[1] / 2:
            self.rect.x += self.speedx
            self.speedy = 0
            self.shoot()

        if self.rect.right >= GameSettings.SCREEN_SIZE[0] and (self.rect.y >= GameSettings.SCREEN_SIZE[1] / 2):
            self.speedy = -3
            self.rect.x = GameSettings.SCREEN_SIZE[0] - self.rect.width
            self.rect.y += self.speedy
            self.shoot()

        if self.rect.top <= self.rect.height and self.shooting:
            self.speedy = 0
            self.rect.x -= self.speedx
            self.rect.y = self.rect.height
            self.shoot()

        if self.rect.left <= 0 and self.shooting:
            self.speedy = 3
            self.rect.x = 0
            self.shoot()

    def getHitPoints(self):
        return self.__hitspoints

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.shooting = True
            self.last_update = now
            bullets = Bullet(self.rect.centerx, self.rect.bottom, 10)
            bullets.sfx.play()
            self.allsprites.add(bullets)
            self.enemy_bullets.add(bullets)

