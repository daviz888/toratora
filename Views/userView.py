import pygame
from Views.view import View
from Views.button import Button
from Controllers.userscore import UserScore
from Shared.gameSettings import GameSettings

class UserView(View):

    def __init__(self, game):
        super(UserView, self).__init__(game)
        self.__back_btn = Button(self.getGame().screen, (70, 50), "<<Back", 130)

    def render(self):
        user_score = UserScore()
        self.clearText()
        self.addText("User High Score", GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 8,
                     GameSettings.WHITE, None, 40)
        x = GameSettings.SCREEN_SIZE[0] / 2 - 100
        y = GameSettings.SCREEN_SIZE[1] / 6 + 50

        if len(user_score.get_users()) >= 1:
            for user in user_score.get_users():
                self.addText(user[0], x, y, GameSettings.WHITE, None, 30)
                self.addText(str(user[1]), x + 100, y, GameSettings.WHITE, None, 30)
                y += 30
        else:
            self.addText("User score list is empty.", x, y, GameSettings.YELLOW, None, 30)

        y += 80

        self.__back_btn.draw_button()

        super(UserView, self).render()

    def handleEvents(self, events):
        super(UserView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_back_clicked(mouse_pos=pygame.mouse.get_pos()):
                    self.getGame().change_view(GameSettings.VIEW_MENU)

    def btn_back_clicked(self, mouse_pos):
        return self.__back_btn.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])

