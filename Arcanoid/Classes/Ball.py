import pygame
from random import random

from globals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = BALL_SIZE
        self.power = 1
        self.color = BALL_COLOR

        # move
        self.isInit = False

        # ball direction
        self.dir = {
            'x': -1,
            'y': -1
        }

        self.speed = {
            'x': BALL_INITIAL_SPEED,
            'y': BALL_INITIAL_SPEED
        }

        # draw
        self.surface = pygame.Surface((self.size * 2, self.size * 2))
        self.rect = self.surface.get_rect(
            bottom=pos[1] - 5,
            centerx=pos[0]
        )

    def update(self):
        if not self.isInit:
            return

        # move ball
        self.rect.move_ip(self.dir['x'] * self.speed['x'], self.dir['y'] * self.speed['y'])

        # check collision
        if self.rect.left < 0 or self.rect.right > W:
            self.dir['x'] *= -1

        if self.rect.top < 0 or self.rect.bottom > H:
            self.dir['y'] *= -1

    def draw(self, sc):
        # clear
        self.surface.fill(BOARD_COLOR)
        pygame.draw.circle(self.surface, self.color, (self.size, self.size), self.size)

        # draw on screen
        sc.blit(self.surface, self.rect)

    def checkCollisionWith(self, rect):
        return self.rect.colliderect(rect)

    def changeDir(self, x=False, y=False):
        # change direction of ball
        if x:
            self.dir['x'] *= -1

        if y:
            self.dir['y'] *= -1

    def changeSpeedX(self, faster=True):
        if faster:
            self.speed['x'] *= 1.2

            if self.speed['x'] > BALL_MAX_SPEED:
                self.speed['x'] = BALL_MAX_SPEED
        else:
            self.speed['x'] /= 1.2

            if self.speed['x'] < BALL_MIN_SPEED:
                self.speed['x'] = BALL_MIN_SPEED

    def changeSpeedY(self, faster=True):
        if faster:
            self.speed['y'] += .1

            if self.speed['y'] > BALL_MAX_SPEED:
                self.speed['y'] = BALL_MAX_SPEED

        else:
            self.speed['y'] -= .1

            if self.speed['y'] < BALL_MIN_SPEED:
                self.speed['y'] = BALL_MIN_SPEED

    def move(self):
        self.isInit = True
