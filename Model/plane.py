
import os
import pygame
import random
from pygame.sprite import Sprite
from Shared.gameSettings import GameSettings
from Model.bullet import Bullet


class Plane(Sprite):

    def __init__(self, allsprites, enemy_bullets, direction):
        super().__init__()
        # self.__filename = str(random.randrange(0, 5)) + '.png'
        self.allsprites = allsprites
        self.enemy_bullets = enemy_bullets
        self.__filename = "1.png"
        self.__direction = direction
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
        if self.__direction == 0:
            self.square_formation()
        elif self.__direction == 1:
            self.square_reverse_formation()
        elif self.__direction == 2:
            self.x_formation()
        elif self.__direction == 3:
            self.x_formation_reverse()

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

    def square_formation(self):
        """ square formation-> down->right->up->left"""
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

    def square_reverse_formation(self):
        """ square formation-> down->right->up->left"""
        self.rect.y += self.speedy
        # track down the ship direction
        down = False
        if self.rect.y >= GameSettings.SCREEN_SIZE[1] / 2:
            self.rect.x -= self.speedx
            self.speedy = 0
            self.shoot()
            down = False
        if self.rect.left <= 0 and self.shooting:
            self.speedy = -3
            self.rect.x = 0
            self.shoot()
        if self.rect.top <= self.rect.height and self.shooting:
            self.speedy = 0
            self.rect.x += self.speedx
            self.rect.y = self.rect.height
            self.shoot()
            down = True
        if self.rect.right >= GameSettings.SCREEN_SIZE[0] and down:
            self.rect.x = GameSettings.SCREEN_SIZE[0] - self.rect.width
            self.speedy = 3
            self.rect.y += self.speedy
            self.shoot()

    def x_formation(self):
        """ x formation-"""
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.shoot()

        if self.rect.top <= GameSettings.SCREEN_SIZE[1] and self.rect.right > GameSettings.SCREEN_SIZE[0]:
            self.rect.x = 0
            self.speedy = 3
            self.rect.x = 3

        if self.rect.bottom >= GameSettings.SCREEN_SIZE[1]:
            self.rect.x = 0
            self.speedy = -3
            self.speedx = 3

    def x_formation_reverse(self):
        """ x formation-"""
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.shoot()

        if self.rect.top >= GameSettings.SCREEN_SIZE[1] and self.rect.right <= 0:
            self.rect.y = GameSettings.SCREEN_SIZE[1] - self.rect.height
            self.speedy = -3
            self.speedx = -3

        if self.rect.bottom <= GameSettings.SCREEN_SIZE[1]:
            # self.rect.x = GameSettings.SCREEN_SIZE[0] - self.rect.width
            self.speedy = 3
            self.speedx = -3


