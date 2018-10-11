import pygame

from pygame.sprite import Sprite

from Shared import *


class Bullet(Sprite):

    def __init__(self, x=0, y=0, direction=0):
        super().__init__()

        self.image = pygame.image.load(GameSettings.SPRITE_BULLET).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        self.__direction = direction

    def update(self):
        self.rect.x += self.__direction
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()
