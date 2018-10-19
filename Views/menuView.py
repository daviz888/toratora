import pygame
from Views.view import View
from Shared import *


class MenuView(View):

    def __init__(self, game):
        super(MenuView, self).__init__(game)
        self.addText("TORA TORA", GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 4,
                     GameSettings.WHITE, None, 48)

        self.addText("(c) Copyright 2018 daffy_duck", GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] - 20,
                     GameSettings.WHITE, None, 20)

    def render(self):
        super(MenuView, self).render()
        self.addButton("Play")

    def handleEvents(self, events):
        super(MenuView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_p:
                    pygame.mouse.set_visible(0)
                    self.getGame().change_view(GameSettings.VIEW_PLAY)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass




