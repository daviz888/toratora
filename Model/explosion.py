import os
import pygame

from pygame.sprite import Sprite

from Shared.gameSettings import GameSettings


class Explosion(Sprite):

    def __init__(self, sprite, scale, center):
        super().__init__()

        self.sheet = pygame.image.load(sprite).convert()
        self.sheet.set_colorkey(GameSettings.BLACK)
        self.scale = scale
        self.sheetSize = self.sheet.get_size()
        self.sprite_frames = []
        self.prep_sheet()
        self.image = self.sprite_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 50
        self.last_update = pygame.time.get_ticks()
        self.sfx = pygame.mixer.Sound(GameSettings.SFX_EXPLOSION)

    def prep_sheet(self):

        self.sprite_frames.clear()
        for x in range(int(self.sheetSize[1] / self.scale[1])):
            for y in range(int(self.sheetSize[0] / self.scale[0])):
                self.sprite_frames.append(self.sheet.subsurface(
                    (y * self.scale[0], 0, self.scale[0], self.scale[1])
                ))

    def update(self):
        current = pygame.time.get_ticks()
        if current - self.last_update > self.frame_rate:
            self.last_update = current
            self.frame += 1
            if self.frame == len(self.sprite_frames):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.sprite_frames[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
