import pygame


from pygame.sprite import Group

from Controllers import *
from Model import *
from Views import *
from Shared import *


class ToraTora:

    def __init__(self):
        self.__lives = GameSettings.PLAYER_LIVES
        self.__score = 0

        self.__level = Level(self)
        self.__shield = 100
        self.__level.load(0)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GameSettings.GAME_TITLE)

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        self.screen_rect = self.screen.get_rect()

        pygame.mouse.set_visible(0)

        self.__player = Player()

        # self.__allSprites = Group()
        self.__views = (
            PlayingView(self),
            GameOverView(self),
            MenuView(self),
            ScoreBoardView(self)
        )
        
        self.__currentView = 0
        self.__scoreboard = ScoreBoardView(self)

        self.playerBullets = Group()
        self.mobs = Group()
        self.powerups = Group()
        self.allSprites = Group()
        self.allSprites.add(self.__player)
        self.spawnMobs(10)


    def start(self):

        while True:
            self.__clock.tick(GameSettings.FPS)

            self.screen.fill(GameSettings.BLACK)

            currentView = self.__views[self.__currentView]
            currentView.handleEvents(pygame.event.get())
            currentView.render()

            pygame.display.update()

    def getPlayer(self):
        return self.__player

    def spawnMobs(self, total):

        for n in range(total):
            m = Mob()
            self.allSprites.add(m)
            self.mobs.add(m)

    def changeView(self):
        pass

    def getLives(self):
        return self.__lives

    def increaseLives(self):
        self.__lives += 1

    def reduceLives(self):
        if self.__lives >= 1:
            self.__lives -= 1

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getShield(self):
        return self.__shield

    def increaseShield(self, amount):

        if (self.__shield + amount) >= 100:
            self.__shield = 100
        else:
            self.__shield += amount

    def reduceShield(self, amount):

        if (self.__shield - amount) <= 0:
            self.__shield = 0
        else:
            self.__shield -= amount

    def getScoreboard(self):
        return self.__scoreboard

    def powerup(self, power):
        pass

    def reset(self):
        pass

    
if __name__ == "__main__":
    ToraTora().start()
