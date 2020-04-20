import pygame
from os.path import join, isfile
from random import choice

from globals import *
from Classes.LevelBlock import LevelBlock

# boosters
from Classes.Boosters.Long import LongBooster


class Level:
    def __init__(self, level):
        self.level = level
        self.levelExist = False

        self.group = pygame.sprite.Group()
        self.boosterGroup = pygame.sprite.Group()

        blocks = self.loadBlocks(level)
        self.levelBlocks = self.convertToBlocks(blocks)

        # create boosters
        self.boosters = []
        self.initBoosters(level)

    def initBoosters(self, count=0):
        if not self.levelBlocks:
            return

        for i in range(0, count):
            block = choice(self.levelBlocks)

            while not block.canDamage:
                block = choice(self.levelBlocks)

            self.boosters.append(LongBooster(block, self.boosterGroup))

    def draw(self, sc):
        self.group.draw(sc)
        self.boosterGroup.draw(sc)

    def update(self):
        self.boosterGroup.update()

    def loadBlocks(self, level):
        fileName = join(LEVELS_DIR, str(level) + '.txt')
        self.levelExist = isfile(fileName)

        result = []

        if isfile(fileName):
            for line in open(fileName, 'r'):
                result.append([int(elem) for elem in line.strip()])

        return result

    def convertToBlocks(self, blocks):
        levelBlocks = []

        for y in range(0, len(blocks)):
            for x in range(0, len(blocks[y])):
                if blocks[y][x]:
                    levelBlocks.append(
                        LevelBlock(x * (BLOCK_WIDTH + BLOCK_GAP) + BLOCK_GAP,
                                   y * (BLOCK_HEIGHT + BLOCK_GAP) + BLOCK_GAP, blocks[y][x], self.group,
                                   not blocks[y][x] == 6)
                    )

        return levelBlocks

    def checkCollisionWith(self, sprite):
        return pygame.sprite.spritecollideany(sprite, self.group)
