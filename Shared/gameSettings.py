import os

class GameSettings:

    SCREEN_SIZE = [800, 600]
    FPS = 50
    POWER_UP_TIME = 5000
    GAME_TITLE = "TORA TORA"

    # define colors.
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    # define asset folders paths.
    GAME_PATH = os.path.dirname(__file__)
    GAME_ASSETS_PATH = os.path.join(GAME_PATH, 'Assets')

    # define player life bars indicator.
    LIFE_BAR_LENGTH = 100
    LIVE_BAR_HEIGHT = 10
    
    # default fontname.
    FONT_NAME = 'Arial'

    # sprites
    SPRITE_PLAYER = os.path.join("Assets", "plane.png")
    SPRITE_BULLET = os.path.join(GAME_ASSETS_PATH, "shot.png")