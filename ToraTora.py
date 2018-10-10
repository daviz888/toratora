import pygame


from pygame.sprite import Group

from Game import *
from Game.Controllers import *
from Game.Models import *
from Game.Views import *
from Game.Shared import gameSettings

class ToraTora:
    def __init__(self):
        self.__lives = 1
        self.__scores = 0

        self.__level = Level(self)
        self.__level.load(0)
    
        self.__player = Player()
        self.__allSprites = Group()

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(gameSettings.GAME_TITLE)

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(gameSettings.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)

        self.__views = (
            PlayingView(self),
            GameOverView(self),
            MenuView(self),
            ScoreBoardView(self)
        )
        
        self.__currentView = 1
        self.allSprites = Group()
        self.allSprites.add(self.__player)

    def start(self):
        while True:
            self.__clock.tick(gameSettings.FPS)

            self.screen.fill(gameSettings.BLACK)

            currentView = self.__views[self.__currentView]
            currentView.handleEvents(pygame.event.get())
            currentView.render()

            pygame.display.update()

    
    def changeView(self):
        pass

    def getScore(self):
        pass

    
    def increaseLives(self):
        pass


    def reset(self):
        pass

    
if __name__== "__main__":
    ToraTora.start()
