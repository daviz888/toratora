import pygame
import random
from Views.view import View
from Model.explosion import Explosion
from Model.powerups import Powerup
from Shared.gameSettings import GameSettings

class PlayingView(View):

    def __init__(self, game):
        super(PlayingView, self).__init__(game)

    def render(self):
        super(PlayingView, self).render()

        game = self.getGame()
        game.allSprites.update()

        # check for mob and bullets collision.
        mobhits = pygame.sprite.groupcollide(game.mobs, game.playerBullets, True, True)
        if mobhits:
            for hit in mobhits:
                game.increaseScore(hit.getHitPoints())
                explosion = Explosion(GameSettings.SPRITE_MOB_EXPLODE, GameSettings.EXPLOSION_SCALE, hit.rect.center)
                explosion.sfx.play()
                game.allSprites.add(explosion)

                # Randomize the chances of getting a power up.
                if random.random() > 0.8:
                    power = Powerup(hit.rect.center)
                    game.powerups.add(power)
                    game.allSprites.add(power)

            game.spawnMobs(1)

        # Check if player and power ups collision.
        power_hits = pygame.sprite.spritecollide(game.getPlayer(), game.powerups, True)
        if power_hits:
            for hits in power_hits:
                game.addPower(hits.power_type)
                hits.sfx.play()

        # Check for mob and player collision.
        player_hits = pygame.sprite.spritecollide(game.getPlayer(), game.mobs, True, pygame.sprite.collide_circle)
        if player_hits:
            for hit in player_hits:
                game.reduceShield(hit.radius)
                explosion = Explosion(GameSettings.SPRITE_MOB_EXPLODE, GameSettings.EXPLOSION_SCALE, hit.rect.center)
                explosion.sfx.play()
                game.allSprites.add(explosion)

                if game.getShield() <= 0:
                    game.reduceLives()
                    game.increaseShield(100)
                    explosion = Explosion(GameSettings.SPRITE_PLAYER_EXPLODE, GameSettings.EXPLOSION_SCALE, game.getPlayer().rect.center)
                    explosion.sfx.play()
                    game.getPlayer().hide()
                    game.allSprites.add(explosion)

            game.spawnMobs(2)

        self.clearText()
        self.getGame().getScoreboard().render()
        game.allSprites.draw(game.screen)
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
