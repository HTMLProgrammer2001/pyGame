import pygame
from random import choice
from copy import copy

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

    def draw(self, sc):
        self.surf.fill(BOARD_COLOR)
        self.blockGroup.draw(self.surf)

        sc.blit(self.surf, self.rect)

    def initBlocks(self):
        self.blockGroup.empty()

        for y, row in enumerate(self.blocks):
            for x, elem in enumerate(row):
                if elem == '1':
                    pos = (x * BLOCK_SIZE, y * BLOCK_SIZE)

                    Block(pos, self.color, self.blockGroup)

    def move(self, right=True):
        if right:
            self.rect.move_ip(BLOCK_SIZE, 0)
        else:
            self.rect.move_ip(-BLOCK_SIZE, 0)

    def getSprites(self):
        newGroup = pygame.sprite.Group()

        for sprite in self.blockGroup.sprites():
            newSprite = copy(sprite)
            newSprite.rect = newSprite.rect.move(self.rect.left, self.rect.top)
            newGroup.add(newSprite)

        return newGroup
