import pygame
from pygame.locals import *
from os import listdir
from os.path import join, isfile
from random import randint

from globals import *
from Classes.LevelBlock import LevelBlock

class Level:
	def __init__(self, level):
		self.level = level

		self.group = pygame.sprite.Group()

		blocks = self.loadBlocks(level)
		self.levelBlocks = self.convertToBlocks(blocks)

	def draw(self, sc):
		self.group.draw(sc)


	def loadBlocks(self, level):
		fileName = join(LEVELS_DIR, str(level) + '.txt')
		self.levelExist = isfile(fileName)

		result = []

		if(isfile(fileName)):
			for line in open(fileName, 'r'):
				result.append([int(elem) for elem in line.strip()])

		return result

	def convertToBlocks(self, blocks):
		levelBlocks = []

		for y in range(0, len(blocks) - 1):
			for x in range(0, len(blocks) - 1):
				if(blocks[y][x]):
					levelBlocks.append(LevelBlock(x * BLOCK_SIZE, y * BLOCK_SIZE, self.group))

		return levelBlocks

	def checkCollisionWith(self, sprite):
		return bool(pygame.sprite.spritecollideany(sprite, self.group))