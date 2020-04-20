import pygame

from globals import *


class Player:
    def __init__(self, x=0):
        # size
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

        # pos Y
        y = H - PLAYER_HEIGHT - 5

        # draw
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect(
            center=(x, y)
        )

        # user movement direction, default it stay at place
        self.dir = 0

        self.speed = PLAYER_SPEED

    def update(self):
        # move player
        self.rect.move_ip(self.dir * self.speed, 0)

        # check overflow
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > W:
            self.rect.right = W

    def draw(self, sc):
        # fill
        self.surface.fill(PLAYER_COLOR)

        # draw on screen
        sc.blit(self.surface, self.rect)

    def changeDir(self, newDir):
        self.dir = newDir
