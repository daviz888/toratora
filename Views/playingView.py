import pygame
import random
from Views.view import View
from Model.explosion import Explosion
from Model.powerups import Powerup
from Shared.gameSettings import GameSettings


class PlayingView(View):
    """ Playing view class """
    def __init__(self, game):
        super(PlayingView, self).__init__(game)
        self.__background = pygame.image.load(GameSettings.SPRITE_BG).convert()
        self.__background = pygame.transform.scale(self.__background, GameSettings.SCREEN_SIZE)
        self.__background_rect = self.__background.get_rect()
        self.__last_update = pygame.time.get_ticks()

    def render(self):
        super(PlayingView, self).render()
        self.__game = self.getGame()
        self.__game.screen.blit(self.__background, self.__background_rect)
        self.__game.allSprites.update()

        # spawn enemy squad.
        current = pygame.time.get_ticks()
        if current - self.__last_update > GameSettings.ENEMY_INTERVAL:
            self.__last_update = current
            self.__game.create_squad(self.__game.get_enemy_direction())

        if len(self.__game.enemy_squad) <= 0:
            self.__game.create_squad(self.__game.get_enemy_direction())

        # if len(self.__game.mobs) <= 0:
            # self.__game.spawnMobs(6)

        self.check_player_bullet_collision(self.__game.enemy_squad)
        self.check_player_bullet_collision(self.__game.mobs)
        self.check_player_power_collision(self.__game.powerups)
        self.check_player_collision(self.__game.enemy_bullets)
        self.check_player_collision(self.__game.enemy_squad)
        self.check_player_collision(self.__game.mobs)

        if self.__game.getLives() == 0:
            # self.__game.game_over = True
            pygame.mouse.set_visible(True)
            self.getGame().change_view(GameSettings.VIEW_GAME_OVER)

        self.clearText()
        self.getGame().getScoreboard().render()
        self.__game.allSprites.draw(self.__game.screen)
        pygame.display.flip()

    def handleEvents(self, events):
        super(PlayingView, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_SPACE:
                    self.getGame().getPlayer().shoot()

                    for bullet in self.getGame().getPlayer().bullets:
                        self.getGame().playerBullets.add(bullet)
                        self.getGame().allSprites.add(bullet)

    def check_player_collision(self, other):
        """ Player and enemies collisions(enemy ship, bullets & mobs)"""
        player_hits = pygame.sprite.spritecollide(self.__game.getPlayer(),
                                                  other, True,
                                                  pygame.sprite.collide_circle)
        if player_hits:
            for hit in player_hits:
                self.__game.reduceShield(hit.radius)
                self.__game.power_down()
                explosion = Explosion(GameSettings.SPRITE_MOB_EXPLODE, GameSettings.EXPLOSION_SCALE, hit.rect.center)
                explosion.sfx.play()
                self.__game.allSprites.add(explosion)

                if self.__game.getShield() <= 0:
                    self.__game.reduceLives()
                    self.__game.increaseShield(100)
                    explosion.sfx.play()
                    self.__game.getPlayer().hide()
                    self.__game.allSprites.add(explosion)

    def check_player_bullet_collision(self, other):
        """check for mob and players bullets collision."""
        bullet_hits = pygame.sprite.groupcollide(other, self.__game.playerBullets, True, True)
        if bullet_hits:
            for hit in bullet_hits:
                self.__game.increaseScore(hit.getHitPoints())
                explosion = Explosion(GameSettings.SPRITE_MOB_EXPLODE, GameSettings.EXPLOSION_SCALE,
                                      hit.rect.center)
                explosion.sfx.play()
                self.__game.allSprites.add(explosion)
                # Randomize the chances of getting a power up.
                if random.random() > 0.8:
                    power = Powerup(hit.rect.center)
                    self.__game.powerups.add(power)
                    self.__game.allSprites.add(power)

    def check_player_power_collision(self, other):
        """ Check if player and power ups collision. """
        power_hits = pygame.sprite.spritecollide(self.__game.getPlayer(), other, True)
        if power_hits:
            for hits in power_hits:
                self.__game.add_power(hits.power_type)
                hits.sfx.play()
