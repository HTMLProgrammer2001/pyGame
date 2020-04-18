import pygame
from globals import *

class LevelBlock(pygame.sprite.Sprite):
	def __init__(self, x, y, health, group):
		print(1)

		pygame.sprite.Sprite.__init__(self)
		#surface
		self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
		self.image.fill(BLOCK_COLOR)

		self.rect = self.image.get_rect(topleft=(x, y))

		#add to blocks group
		self.add(group)

		#amount of health
		self.health = health

	def draw(self, sc):
		self.image.fill(BLOCK_COLOR)

		sc.blit(self.image, self.rect)