import os
import fileinput
import pygame
import random

from Shared.gameSettings import GameSettings

class Level:

    def __init__(self, game):
        self.__game = game
        self.__current_level = 0

    def load(self, level):
        self.__current_level = level

    def loadNextLevel(self):
        pass

