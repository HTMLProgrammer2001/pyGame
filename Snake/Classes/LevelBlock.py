import pygame
from globals import *

class LevelBlock(pygame.sprite.Sprite):
	def __init__(self, x, y, group):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
		self.image.fill(BLOCK_COLOR)

		self.rect = self.image.get_rect(topleft=(x, y))

		self.add(group)