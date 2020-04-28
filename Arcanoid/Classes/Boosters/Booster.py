import pygame
from time import time

from globals import *


class Booster(pygame.sprite.Sprite):
    def __init__(self, block, group):
        pygame.sprite.Sprite.__init__(self)

        # set this booster to block
        block.booster = self

        # is block destroyed
        self.isShow = False

        # time of working
        self.timeout = 10
        self.activateTime = None

        self.pos = block.rect.center
        self.speed = BOOSTER_SPEED

        # add this booster to group
        self.add(group)

    def show(self):
        self.isShow = True

        print('Show')

    def activate(self):
        if self.activateTime:
            return

        self.activateTime = time()

    def isActive(self):
        return self.activateTime + self.timeout >= time()

    def update(self):
        # is not destroy block
        if not self.isShow or self.activateTime:
            return

        # move
        self.rect.move_ip(0, self.speed)

        # over playground
        if self.rect.bottom > H:
            self.kill()
