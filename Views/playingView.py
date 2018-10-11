import pygame
from Views.view import View
from Shared import *

class PlayingView(View):

    def __init__(self, game):
        super(PlayingView, self).__init__(game)
        self.__game = self.getGame()
        self.__player = self.__game.getPlayer()

    def render(self):
        super(PlayingView, self).render()

        # game = self.getGame()
        self.__game.allSprites.update()
        self.__game.allSprites.draw(self.__game.screen)
        pygame.display.flip()

    def handleEvents(self, events):
        super(PlayingView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_SPACE:
                    self.__player.shoot()
                    for bullet in self.__player.bullets:
                        self.__game.playerBullets.add(bullet)
                        self.__game.allSprites.add(bullet)
