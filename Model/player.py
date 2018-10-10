import pygame

from pygame.sprite import Sprite

from Game.Shared import *

class Player:
    def __init__(self):
        super().__init__()

        self.__image = pygame.load(gameSettings.SPRITE_PLAYER).convert()
        self.__rect = self.__image.get_rect()
        self.__radius = int(self.__rect.width * .8 / 2)
        # pygame.draw.circle(self.__image, gameSettings.RED, self.__rect.center, self.__radius)
        self.__imageSize = self.__image.get_size()
        self.__rect.centerx = gameSettings.SCREEN_SIZE[0] / 2
        self.__rect.bottom = gameSettings.SCREEN_SIZE[1]


    def getRect(self):
        return self.__rect

    def getImage(self):
        return self.__image

    def getRadius(self):
        return self.__radius

    def getImageSize(self):
        return self.__imageSize

    def powerUp(self):
        pass

    def update(self):
        self.__speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.__speedx = 5
        if keystate[pygame.K_RIGTH]:
            self.__speedx -= 5
        if keystate[pygame.K_UP]:
            self.__rect.top -= 5
        if keystate[pygame.K_DOWN]:
            self.__rect.top += 5
        self.__rect.x = self.__speedx
        if self.__rect.right >= gameSettings.SCREEN_SIZE[0]:
            self.__rect.right = gameSettings.SCREEN_SIZE[0]
        if self.__rect.left <= 0:
            self.__rect.left = 0
        if self.__rect.top <= 0:
            self.__rect.top = 0
        if self.__rect.bottom >= gameSettings.SCREEN_SIZE[1]
            self.__rect.bottom = gameSettings.SCREEN_SIZE[1]



        