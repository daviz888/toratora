import pygame
from Views.view import View
from Model.explosion import Explosion
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

        # Check for mob and player collision.
        playerhits = pygame.sprite.spritecollide(game.getPlayer(), game.mobs, True, pygame.sprite.collide_circle)
        if playerhits:
            for hit in playerhits:
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
        # score = "Score: {:,}".format(int(round(game.getScore(), -1)))
        # self.addText(score, GameSettings.SCREEN_SIZE[0] - (len(score) + 100), 20)
        # # self.addText(score, 200, 20)
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
