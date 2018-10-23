import pygame
from Views.view import View
from Controllers.userscore import UserScore
from Shared.gameSettings import GameSettings

class UserView(View):

    def __init__(self, game):
        super(UserView, self).__init__(game)

        self.clearText()
        self.addText("User High Score", GameSettings.SCREEN_SIZE[0] / 2,
                     GameSettings.SCREEN_SIZE[1] / 6,
                     GameSettings.WHITE, None, 40)

    def render(self):
        user_score = UserScore()
        x = GameSettings.SCREEN_SIZE[0] / 2
        y = GameSettings / 6 + 50

        for user in user_score.get_users():
            self.addText(user[0], x,y)
            self.addText(user[1], x + 200, y + 50)

        super(UserView, self).render()

    def handleEvents(self, events):
        super(UserView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                pass
