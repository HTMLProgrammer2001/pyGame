import pygame

from Classes.Boosters.Booster import Booster
from Classes.Ball import Ball


class BallsBooster(Booster):
    def __init__(self, block, group):
        Booster.__init__(self, block, group)

        # draw
        self.image = pygame.image.load('./image/ballsBooster.png').convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, sc):
        if not self.isShow or self.activateTime:
            return

        sc.blit(self.image, self.rect)

    def attach(self, balls, pos):
        balls.append(Ball(pos))

    def destroy(self):
        self.kill()
