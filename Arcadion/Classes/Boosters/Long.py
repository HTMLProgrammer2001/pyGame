import pygame

from Classes.Boosters.Booster import Booster


class LongBooster(Booster):
    def __init__(self, block, group):
        Booster.__init__(self, block, group)

        # time of working
        self.timeout = 10

        # attached player
        self.player = None

        # draw
        self.image = pygame.image.load('./image/longBooster.png').convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, sc):
        if not self.isShow or self.activateTime:
            return

        sc.blit(self.image, self.rect)

    def attach(self, player):
        # change draw attributes
        player.surface = pygame.Surface((player.surface.get_width()*2, player.surface.get_height()))
        player.rect = player.surface.get_rect(center=player.rect.center)

        # attach player
        self.player = player

    def destroy(self):
        if self.player:
            # short player
            self.player.surface = pygame.Surface((self.player.surface.get_width()/2,
                                                  self.player.surface.get_height()))
            self.player.rect = self.player.surface.get_rect(center=self.player.rect.center)

            self.player = None

        self.kill()
