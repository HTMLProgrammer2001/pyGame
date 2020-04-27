import pygame

from Classes.Boosters.Booster import Booster
from globals import *


class PowerBooster(Booster):
    def __init__(self, block, group):
        Booster.__init__(self, block, group)

        # time of working
        self.timeout = 10

        # attached ball
        self.ball = None

        # draw
        self.image = pygame.image.load('./image/powerBooster.png').convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, sc):
        if not self.isShow or self.activateTime:
            return

        sc.blit(self.image, self.rect)

    def attach(self, ball):
        # change ball
        ball.power = 3
        ball.speed['y'] *= 1.5
        ball.speed['x'] *= 1.5
        ball.color = RED

        # attach ball
        self.ball = ball

    def destroy(self):
        if self.ball:
            # change ball back
            self.ball.power = 1
            self.ball.speed['x'] /= 1.5
            self.ball.speed['y'] /= 1.5
            self.ball.color = BALL_COLOR

            self.ball = None

        self.kill()
