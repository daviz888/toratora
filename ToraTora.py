
import pygame
import random
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

        self.__player = Player()

        # self.__allSprites = Group()
        self.__views = (
            MenuView(self),
            PlayingView(self),
            GameOverView(self),
            UserView(self),
        )
        
        self.__currentView = GameSettings.VIEW_MENU
        self.__scoreboard = ScoreBoardView(self)

        self.playerBullets = Group()
        self.mobs = Group()
        self.powerups = Group()
        self.enemy_bullets = Group()
        self.enemy_squad = Group()
        self.allSprites = Group()
        self.allSprites.add(self.__player)
        self.spawnMobs(8)
        self.create_squad()
        self.game_over = False

    def start(self):

        while not self.game_over:
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

    def change_view(self, view):
        self.__currentView = view

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

        if self.__shield - amount <= 0:
            self.__shield = 0
        else:
            self.__shield -= amount

    def getScoreboard(self):
        return self.__scoreboard

    def add_power(self, power):
        if power == 0:
            self.__player.weapon_up()
        elif power == 1:
            self.__shield = 100
        elif power == 2:  # star add life
            self.increaseLives()
        elif power == 3:  # bolt
            self.__player.weapon_up(5)
        elif power == 4:  # points
            points = random.randrange(1000, 5000)
            self.increaseScore(points)
        elif power == 5:
            self.increaseShield(20)
        # self.__powerups.append(po wer)

    def power_down(self):
        self.__player.weapon_down()

    def create_squad(self):
        for n in range(5):
            ship = Plane(self.allSprites, self.enemy_bullets)
            ship_width = ship.rect.width
            ship.x = ship_width
            ship.rect.x = ship.x
            ship.rect.y = ship.rect.height + 2 * ship.rect.height * (n * -1)
            self.allSprites.add(ship)
            self.enemy_squad.add(ship)

    def reset(self):
        pass

    
if __name__ == "__main__":
    ToraTora().start()
