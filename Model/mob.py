
import os
import pygame
import random
from pygame.sprite import Sprite
from Shared.gameSettings import GameSettings

class Mob(Sprite):

    def __init__(self):
        super().__init__()
        self.__filename = str(random.randrange(0, 5)) + '.png'
        self.image = pygame.image.load(os.path.join(GameSettings.ASSETS_PATH, self.__filename)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 /2)
        self.__hitspoints = 50 - self.radius

        self.rect.x = random.randrange(GameSettings.SCREEN_SIZE[0])
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top >= GameSettings.SCREEN_SIZE[1] + 10 or self.rect.left < -10 or self.rect.right >= GameSettings.SCREEN_SIZE[0]:
            self.rect.x = random.randrange(GameSettings.SCREEN_SIZE[0])
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

    def getHitPoints(self):
        return self.__hitspoints
