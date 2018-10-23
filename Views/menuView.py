import pygame
from Views.view import View
from Views.button import Button
from Shared import *


class MenuView(View):

    def __init__(self, game):
        super(MenuView, self).__init__(game)
        self.addText("TORA TORA",
                     GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 6,
                     GameSettings.WHITE, None, 64)

        self.play_button = Button(self.getGame().screen, (400, 230), "Play")
        self.user_button = Button(self.getGame().screen, (400, 300), "Top Users")

        self.addText("Click Play button or press 'P' key to begin",
                     GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 2 + 50,
                     GameSettings.YELLOW, None, 22)

        self.addText("Use arrow keys to Move and space bar to Fire",
                     GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 2 + 75,
                     GameSettings.YELLOW, None, 22)

        self.addText("(c) Copyright 2018 daffy_duck", GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] - 30,
                     GameSettings.WHITE, None, 20)

    def render(self):
        super(MenuView, self).render()
        # self.addButton("Play")
        self.play_button.draw_button()
        self.user_button.draw_button()

    def handleEvents(self, events):
        super(MenuView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_p:
                    self.show_cursor(False)
                    self.getGame().change_view(GameSettings.VIEW_PLAY)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_play_clicked(mouse_pos=pygame.mouse.get_pos()):
                    self.show_cursor(False)
                    self.getGame().change_view(GameSettings.VIEW_PLAY)

                elif self.btn_user_clicked(mouse_pos=pygame.mouse.get_pos()):
                    self.getGame().change_view(GameSettings.VIEW_HIGH_SCORE)

    @staticmethod
    def show_cursor(flag=True):
        pygame.mouse.set_visible(flag)

    def btn_play_clicked(self, mouse_pos):
        return self.play_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])

    def btn_user_clicked(self, mouse_pos):
        return self.user_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])