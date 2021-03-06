import pygame

from pygame.sprite import Sprite

from Shared import *
from Model.bullet import Bullet

class Player(Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(GameSettings.SPRITE_PLAYER).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 / 2)
        # pygame.draw.circle(self.image, pygame.Color(0, 255, 0, 100), self.rect.center, self.radius)
        self.imageSize = self.image.get_size()
        self.rect.centerx = GameSettings.SCREEN_SIZE[0] / 2
        self.rect.bottom = GameSettings.SCREEN_SIZE[1]
        self.bullets = []
        self.speedx = 0
        self.hidden = False
        self.hide_time = pygame.time.get_ticks()
        self.__weapon = 1
        self.__shield = 0
        self.__squad = 0

    def weapon_up(self, bullet=1):
        if (self.__weapon + bullet) < 5:
                self.__weapon += bullet
        else:
            self.__weapon = bullet

    def weapon_down(self):
        self.__weapon = 1

    def update(self):
        # hide/unhide the player.
        if self.hidden and pygame.time.get_ticks() - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = GameSettings.SCREEN_SIZE[0] / 2
            self.rect.bottom = GameSettings.SCREEN_SIZE[1]

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.rect.top -= 5
        if keystate[pygame.K_DOWN]:
            self.rect.top += 5
        self.rect.x += self.speedx
        if self.rect.right > GameSettings.SCREEN_SIZE[0]:
            self.rect.right = GameSettings.SCREEN_SIZE[0]
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= GameSettings.SCREEN_SIZE[1]:
            self.rect.bottom = GameSettings.SCREEN_SIZE[1]

    def shoot(self):
        self.bullets.clear()

        if self.__weapon == 1:
            self.bullets.append(Bullet(self.rect.centerx, self.rect.top, -10))
        elif self.__weapon == 2:
            self.bullets.append(Bullet(self.rect.left, self.rect.centery, -10))
            self.bullets.append(Bullet(self.rect.right, self.rect.centery, -10))
        elif self.__weapon >= 3:
            self.bullets.append(Bullet(self.rect.centerx, self.rect.top, -10))
            x = int(self.rect.width / (self.__weapon - 1))
            for i in range(self.__weapon):
                self.bullets.append(Bullet(self.rect.left + (i * x), self.rect.centery, -10))
        self.bullets[0].sfx.play()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (GameSettings.SCREEN_SIZE[0]/2, GameSettings.SCREEN_SIZE[1] + 200)




