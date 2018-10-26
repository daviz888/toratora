
import pygame

from Views.button import Button
from Shared.gameSettings import GameSettings


class View:

    def __init__(self, game):
        self.__game = game
        self.__texts = []
        # self.__backround = pygame.image.load(GameSettings.SPRITE_BG).convert()
        # self.__backround = pygame.transform.scale(self.__backround, GameSettings.SCREEN_SIZE)
        # self.__backround_rect = self.__backround.get_rect()

    def render(self):
        # self.__game.screen.blit(self.__backround, self.__backround_rect)
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, string, x=0, y=0, color=GameSettings.WHITE, background=GameSettings.BLACK, size=17):
        # font = pygame.font.SysFont(GameSettings.FONT_NAME, size)
        default_font = pygame.font.match_font('arial')
        font = pygame.font.SysFont(default_font, size)
        text_image = font.render(string, True, color, background)
        text_rect = text_image.get_rect()
        text_rect.midtop = (x, y)
        self.__texts.append([text_image, text_rect])
        # self.__texts.append([font.render(string, True, color, background), (x, y)])

    def addButton(self, text):
        # width, height = 200, 50
        # screen_rect = self.__game.screen.get_rect()
        # self.button_rect = pygame.Rect(0, 0, width, height)
        # self.button_rect.center = screen_rect.center
        #
        # font = pygame.font.Font(None, 48)
        # self.text_image = font.render(text, True, GameSettings.WHITE, None)
        # self.text_image_rect = self.text_image.get_rect()
        # self.text_image_rect.center = self.button_rect.center
        #
        # self.__game.screen.fill(GameSettings.RED, self.button_rect)
        # self.__game.screen.blit(self.text_image, self.text_image_rect)
        self._play_button = Button(self.__game.screen, text)

    @staticmethod
    def show_cursor(flag=True):
        pygame.mouse.set_visible(flag)



