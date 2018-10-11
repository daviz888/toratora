import pygame
from Views.view import View
from Shared import *

class PlayingView(View):

    def __init__(self, game):
        super(PlayingView, self).__init__(game)

    def render(self):
        super(PlayingView, self).render()

        game = self.getGame()
        game.allSprites.update()
        game.allSprites.draw(game.screen)
        pygame.display.flip()

    def handleEvents(self, events):
        super(PlayingView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()