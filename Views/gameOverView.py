import pygame
from Views.view import View
from Views.button import Button
from Controllers.userscore import UserScore
from Shared.gameSettings import GameSettings


class GameOverView(View):

    def __init__(self, game):
        super(GameOverView, self).__init__(game)
        self.__player_name = ""
        self.__back_btn = Button(self.getGame().screen, (70, 50), "<<Back", 130)
        self.show_cursor(True)

    def render(self):

        self.clearText()
        self.addText("GAME OVER", GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 8,
                     GameSettings.WHITE, None, 40)
        self.addText("Player Name: ",
                     GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 8 + 100,
                     GameSettings.WHITE,
                     GameSettings.BLACK, 30)
        self.addText(self.__player_name,
                     GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 8 + 150,
                     GameSettings.WHITE,
                     GameSettings.BLACK, 30)
        self.__back_btn.draw_button()
        super(GameOverView, self).render()

    def handleEvents(self, events):
        super(GameOverView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    UserScore().add_score(self.__player_name, game.getScore())
                    game.reset()
                    self.getGame().change_view(GameSettings.VIEW_MENU)
                if event.key == pygame.K_BACKSPACE:
                    if len(self.__player_name) >= 1:
                        self.__player_name = self.__player_name[:len(self.__player_name) - 1]
                elif event.key >= 65 and event.key <= 122:
                    self.__player_name += chr(event.key)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_back_clicked(mouse_pos=pygame.mouse.get_pos()):
                    self.getGame().change_view(GameSettings.VIEW_MENU)

    def btn_back_clicked(self, mouse_pos):
        return self.__back_btn.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])


