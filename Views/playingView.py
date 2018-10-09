import pygame
from Game.Views.view import View
from Game.Shared import *

class PlayingView(View):

    def __init__(self, game):
        super(PlayingView, self).__init__(game)

    def render(self):
        super().render()

        game = self.getGame()
        