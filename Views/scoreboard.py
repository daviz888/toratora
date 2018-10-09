import pygame

from Game.Views.view import View
from Game.Shared.gameSettings import GameSettings

class ScoreBoard(View):

    def __init__(self, game):
        super(ScoreBoard, self).__init__(game)
       
    def render(self):
        # self.game().screen.blit(self.)

