import pygame

from Classes.Boosters.Booster import Booster


class LongBooster(Booster):
    def __init__(self, block, group):
        Booster.__init__(self, block, group)

        self.image = pygame.image.load('./image/longBooster.png').convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, sc):
        if not self.isShow:
            return

        sc.blit(self.image, self.rect)
