import pygame

from Classes.Boosters.Booster import Booster
from globals import *


class PowerBooster(Booster):
    def __init__(self, block, group):
        Booster.__init__(self, block, group)

        # time of working
        self.timeout = 10

        # attached balls
        self.balls = None

        # draw
        self.image = pygame.image.load('./image/powerBooster.png').convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, sc):
        if not self.isShow or self.activateTime:
            return

        sc.blit(self.image, self.rect)

    def attach(self, balls):
        # change balls
        for ball in balls:
            ball.power = 3
            ball.speed['y'] *= 1.5
            ball.speed['x'] *= 1.5
            ball.color = RED

        # attach ball
        self.balls = balls

    def destroy(self):
        if self.balls:
            for ball in self.balls:
                # change ball back
                ball.power = 1
                ball.speed['x'] /= 1.5
                ball.speed['y'] /= 1.5
                ball.color = BALL_COLOR

            self.balls = None

        self.kill()
