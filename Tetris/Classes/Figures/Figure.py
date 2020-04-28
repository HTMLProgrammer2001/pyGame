import pygame
from random import choice

from globals import *
from Classes.Block import Block


class Figure:
    def __init__(self, x):
        self.blocks = [
            ['1', '1', '1'],
            ['0', '1', '0'],
            ['1', '1', '1']
        ]

        self.blockGroup = pygame.sprite.Group()

        self.surf = pygame.Surface((len(self.blocks[0]) * BLOCK_SIZE, len(self.blocks) * BLOCK_SIZE))
        self.rect = self.surf.get_rect(center=(x, - len(self.blocks) * BLOCK_SIZE * 2))

        self.color = choice(BLOCK_COLORS)

        self.initBlocks()

    def update(self):
        self.rect.move_ip(0, 3)

    def draw(self, sc):
        self.surf.fill(BOARD_COLOR)
        self.blockGroup.draw(self.surf)

        sc.blit(self.surf, self.rect)

    def initBlocks(self):
        for y, row in enumerate(self.blocks):
            for x, elem in enumerate(row):
                if elem:
                    pos = (x * BLOCK_SIZE, y * BLOCK_SIZE)

                    Block(pos, self.color, self.blockGroup)

    def move(self, right=True):
        if right:
            self.rect.move_ip(BLOCK_SIZE, 0)
        else:
            self.rect.move_ip(-BLOCK_SIZE, 0)
