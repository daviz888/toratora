import os
import pygame

class GameSettings:

    SCREEN_SIZE = [800, 600]
    FPS = 50
    POWER_UP_TIME = 5000
    GAME_TITLE = "TORA TORA"
    SALT = 'daffy'

    # define colors.
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 255, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (211, 211, 211)
    DARK_GRAY = (169, 169, 169)
    YELLOW = (255, 255, 0)

    # define asset folders paths.
    # GAME_PATH = os.path.join("Assets")
    ASSETS_PATH = os.path.join("Assets")
    USER_DATA = os.path.join("Data", "userscore.dat")

    # define player life bars indicator.
    LIFE_BAR_LENGTH = 100
    LIFE_BAR_HEIGHT = 10
    
    # default fontname.
    FONT_NAME = pygame.font.match_font('arial')

    # sprites
    SPRITE_BG = os.path.join(ASSETS_PATH,"background.png")
    SPRITE_PLAYER = os.path.join(ASSETS_PATH, "player1.png")
    SPRITE_BULLET = os.path.join(ASSETS_PATH, "shot1.png")
    SPRITE_LASER = os.path.join(ASSETS_PATH, "laserRed16.png")
    SPRITE_PLAYER_EXPLODE = os.path.join(ASSETS_PATH, "explosionframes.png")
    SPRITE_MOB_EXPLODE = os.path.join(ASSETS_PATH, "explosion.png")
    SPRITE_POWER = os.path.join(ASSETS_PATH, "powerup.png")
    SFX_LASER = os.path.join(ASSETS_PATH, "sfx_laser2.ogg")
    SFX_EXPLOSION = os.path.join(ASSETS_PATH, "rumble1.ogg")
    SFX_POWER = os.path.join(ASSETS_PATH, "sfx_shieldUp.ogg")

    # power up types.
    POWER_TYPE = {
        0: "bullet",
        1: "shield",
        2: "star",
        3: "bolt",
        4: "points",
        5: "repair"
    }

    EXPLOSION_SCALE = (64, 64)
    PLAYER_LIVES = 1

    ENEMY_INTERVAL = 6000
    ENEMY_BULLET_HIT_POINTS = 10

    VIEW_MENU = 0
    VIEW_PLAY = 1
    VIEW_GAME_OVER = 2
    VIEW_HIGH_SCORE = 3
    VIEW_SETTINGS = 4
