
import pygame
import random

from pygame.sprite import Sprite

from Shared.gameSettings import GameSettings


class Powerup(Sprite):

    def __init__(self, center):
        super().__init__()

        self.sheet = pygame.image.load(GameSettings.SPRITE_POWER).convert_alpha()
        self.sheet = pygame.transform.scale(self.sheet, (180, 30))
        self.sheet.set_colorkey(GameSettings.WHITE)
        self.scale = (30, 30)
        self.sheetSize = self.sheet.get_size()
        self.power_frames = []
        self.prep_sheet()
        self.power_type = random.choice(list(GameSettings.POWER_TYPE))
        print(self.power_type)
        # self.image = self.power_frames[random.randrange(6)]
        self.image = self.power_frames[self.power_type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.sfx = pygame.mixer.Sound(GameSettings.SFX_POWER)
        self.speedy = 1

    def prep_sheet(self):
        self.power_frames.clear()
        for x in range(int(self.sheetSize[1] / self.scale[1])):
            for y in range(int(self.sheetSize[0] / self.scale[0])):
                self.power_frames.append(self.sheet.subsurface(
                    (y * self.scale[0], 0, self.scale[0], self.scale[1])
                ))

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= GameSettings.SCREEN_SIZE[1]:
            self.kill()
