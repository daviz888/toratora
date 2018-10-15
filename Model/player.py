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
        self.__powerups = []
        self.__guns = 1
        self.__shield = 0
        self.__squad = 0

    def power_up(self, power):

        if power == 0:
            if self.__guns < 4:
                self.__guns += 1
        elif power == 1:
            self.__shield = 100
        elif power == 2: #star
            pass
        elif power == 3: #bolt
            pass
        elif power == 4: #points
            pass
        elif power == 5:
            pass
        # self.__powerups.append(power)

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

        if self.__guns == 1:
            self.bullets.append(Bullet(self.rect.centerx, self.rect.top))
        elif self.__guns == 2:
            self.bullets.append(Bullet(self.rect.left, self.rect.centery))
            self.bullets.append(Bullet(self.rect.right, self.rect.centery))
        elif self.__guns >= 3:
            self.bullets.append(Bullet(self.rect.centerx, self.rect.top))
        #     # self.bullets.append(Bullet(self.rect.left, self.rect.centery))
        #     # self.bullets.append(Bullet(self.rect.right, self.rect.centery))
        #     x = int(self.rect.width / 1)
        #     for i in range(self.__guns -1 ):
        #         self.bullets.append(Bullet(self.rect.left + (i * x), self.rect.centery))
        #         print(self.rect.left + (i * x))
        #
        # elif self.__guns == 4:
            x = int(self.rect.width / (self.__guns - 1))
            for i in range(self.__guns):
                self.bullets.append(Bullet(self.rect.left + (i * x), self.rect.centery))
                print(self.rect.left + (i * x))
        self.bullets[0].sfx.play()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (GameSettings.SCREEN_SIZE[0]/2, GameSettings.SCREEN_SIZE[1] + 200)



