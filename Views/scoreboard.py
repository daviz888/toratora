import pygame

from Views.view import View
from Shared.gameSettings import GameSettings


class ScoreBoardView(View):
    def __init__(self, game):
        super(ScoreBoardView, self).__init__(game)

    def render(self):
        super(ScoreBoardView, self).render()

        self.prep_score(self.getGame().getScore())
        self.prep_player()
        if self.getGame().getLives() >= 1:
            self.prep_shield_bar()

    def prep_score(self, score):
        str_score = "Score {:,}".format(int(round(score, -1)))
        x = self.getGame().screen_rect.right - 50
        y = 20
        self.addText(str_score, x, y, GameSettings.WHITE, GameSettings.BLACK, 30)

    def prep_shield_bar(self):
        bar_fill = (self.getGame().getShield() / 100) * GameSettings.LIFE_BAR_LENGTH
        bar_outline = pygame.Rect(5, 30, GameSettings.LIFE_BAR_LENGTH, GameSettings.LIFE_BAR_HEIGHT)
        fill_rect = pygame.Rect(5, 30, bar_fill, GameSettings.LIFE_BAR_HEIGHT)
        pygame.draw.rect(self.getGame().screen, GameSettings.GREEN, fill_rect)
        pygame.draw.rect(self.getGame().screen, GameSettings.WHITE, bar_outline, 2)

    def prep_player(self):
        scale = (30, 32)
        player_image = self.getGame().getPlayer().image
        player_image = pygame.transform.scale(player_image, scale)
        for p in range(self.getGame().getLives()):
            coordinates = (5 + p * scale[0], 5)
            self.getGame().screen.blit(player_image, coordinates)

