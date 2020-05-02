import pygame
from random import choice
from copy import copy
from math import ceil, floor

from globals import *
from Classes.Block import Block


class Figure:
    def __init__(self, x):
        self.blockGroup = pygame.sprite.Group()

        self.color = choice(BLOCK_COLORS)

        self.surf = pygame.Surface((len(self.blocks[0]) * BLOCK_SIZE, len(self.blocks) * BLOCK_SIZE))

        y = (-(len(self.blocks) + 2)) * BLOCK_SIZE

        self.rect = pygame.Rect((x, y),
                                (len(self.blocks[0]) * BLOCK_SIZE, len(self.blocks) * BLOCK_SIZE))

        self.initBlocks()

    def update(self):
        self.rect.move_ip(0, 3)

    def draw(self, sc, withRect=True):
        self.surf.fill(BOARD_COLOR)
        self.blockGroup.draw(self.surf)

        if withRect:
            sc.blit(self.surf, self.rect)
        else:
            sc.blit(self.surf, pygame.Rect((0, 0), (self.rect.width + 10, self.rect.height + 10)))

    def initBlocks(self):
        self.blockGroup.empty()

        for y, row in enumerate(self.blocks):
            for x, elem in enumerate(row):
                if elem == '1':
                    pos = (x * BLOCK_SIZE, y * BLOCK_SIZE)

                    Block(pos, self.color, self.blockGroup)

    def move(self, right=True):
        if right:
            for sprite in self.getSprites():
                if sprite.rect.right + BLOCK_SIZE > W:
                    return

            self.rect.move_ip(BLOCK_SIZE, 0)
        else:
            for sprite in self.getSprites():
                if sprite.rect.left - BLOCK_SIZE < 0:
                    return

            self.rect.move_ip(-BLOCK_SIZE, 0)

    def down(self):
        self.rect.move_ip(0, BLOCK_SIZE)

    def up(self):
        self.rect.move_ip(0, -BLOCK_SIZE)

    def getSprites(self):
        newGroup = pygame.sprite.Group()

        for sprite in self.blockGroup.sprites():
            newSprite = copy(sprite)
            newSprite.rect = newSprite.rect.move(self.rect.left, self.rect.top)
            newGroup.add(newSprite)

        return newGroup
