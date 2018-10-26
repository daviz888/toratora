"""
button.py
"""
import os

import pygame
from Shared.gameSettings import GameSettings


class Button():
    """Create a Button class object"""

    def __init__(self, screen, screen_center, text, width=200, height=50, text_size=48):
        """Initialize attributes"""
        # self.__screen_xx = screen_center
        self.__screen = screen
        self.__screen_rect = screen.get_rect()
        self.__text = text
        # set the dimension and properties of the button.
        self.__width, self.__height = width, height
        self.__button_color = GameSettings.WHITE
        self.__font = pygame.font.SysFont(GameSettings.FONT_NAME, text_size)

        # build the button's rect object and center itself.
        self.__button_rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.__button_rect.center = screen_center
        # print(self.__screen_rect.center)

        # prep the text of the button.
        self.__prep_text()
        # self.__draw_button()

    def __prep_text(self):
        """render text into image and center the text on the button."""
        self.__text_image = self.__font.render(self.__text, True, GameSettings.WHITE, None)
        self.__text_image_rect = self.__text_image.get_rect()
        self.__text_image_rect.center = self.__button_rect.center

    def draw_button(self):
        """draw the button and the message."""
        self.__screen.fill(GameSettings.GRAY, self.__button_rect)
        self.__screen.blit(self.__text_image, self.__text_image_rect)

    def get_rect(self):
        return self.__button_rect
