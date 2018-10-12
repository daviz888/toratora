import os
import pygame

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
    # GAME_PATH = os.path.join("Assets")
    ASSETS_PATH = os.path.join("Assets")

    # define player life bars indicator.
    LIFE_BAR_LENGTH = 100
    LIFE_BAR_HEIGHT = 10
    
    # default fontname.
    FONT_NAME = pygame.font.match_font('arial')

    # sprites
    SPRITE_PLAYER = os.path.join(ASSETS_PATH, "plane.png")
    SPRITE_BULLET = os.path.join(ASSETS_PATH, "shot.png")
    SPRITE_LASER = os.path.join(ASSETS_PATH, "laserRed16.png")
    SPRITE_PLAYER_EXPLODE = os.path.join(ASSETS_PATH, "explosionframes.png")
    SPRITE_MOB_EXPLODE = os.path.join(ASSETS_PATH, 'explosion.png')

    SFX_LASER = os.path.join(ASSETS_PATH, "sfx_laser2.ogg")
    SFX_EXPLOSION = os.path.join(ASSETS_PATH, "rumble1.ogg")

    EXPLOSION_SCALE = (64, 64)
    PLAYER_LIVES = 3