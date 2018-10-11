import pygame


from pygame.sprite import Group

# from toratora import *
from Controllers import *
from Model import *
from Views import *
from Shared import *


class ToraTora:

    def __init__(self):
        self.__lives = 1
        self.__scores = 0

        self.__level = Level(self)
        self.__level.load(0)
    


        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GameSettings.GAME_TITLE)

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)
        self.__player = Player()
        self.__allSprites = Group()
        self.__views = (
            PlayingView(self),
            GameOverView(self),
            MenuView(self),
            ScoreBoardView(self)
        )
        
        self.__currentView = 0
        self.allSprites = Group()
        self.allSprites.add(self.__player)

    def start(self):

        while True:
            self.__clock.tick(GameSettings.FPS)

            self.screen.fill(GameSettings.BLACK)

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

    
if __name__ == "__main__":
    ToraTora().start()
