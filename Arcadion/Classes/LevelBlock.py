import pygame
from globals import *

class LevelBlock(pygame.sprite.Sprite):
	def __init__(self, x, y, health, group):
		pygame.sprite.Sprite.__init__(self)
		#surface
		self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))

		self.rect = self.image.get_rect(topleft=(x, y))

		#add to blocks group
		self.add(group)

		#amount of health
		self.health = health

		self.image.fill(BLOCK_COLORS[self.health])

	def draw(self, sc):
		self.image.fill(BLOCK_COLORS[self.health])
		sc.blit(self.image, self.rect)

	def damage(self, power = 1):
		self.health -= power

		#block destroyed
		if(self.health <= 0):
			self.kill()
		else:
			#fill new color
			self.image.fill(BLOCK_COLORS[self.health])	