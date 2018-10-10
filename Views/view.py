from Game.Shared.gameSettings import gameSettings
import pygame
class View:

    def __init__(self, game):
        self.__game = game
        self.__texts = []

    def render(self):
        pass

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, string, x=0, y=0, color=gameSettings.WHITE, background=gameSettings.BLACK, size=18):
        font = pygame.font.Font(gameSettings.FONT_NAME, size)
        self.__texts.append([font.render(string, True, color, background, (x,y))])
