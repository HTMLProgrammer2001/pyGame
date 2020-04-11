import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self, surf, group):
		pygame.sprite.Sprite.__init__(self)

		self.x = 0
		self.y = 10
		self.image = surf

		self.rect = surf.get_rect(topleft=(0, 10))

		self.add(group)

	def update(self):
		pass

	def moveUp(self):

		if(self.y >= 50):
			self.y -= 50
			self.rect.move_ip(0, -50)

	def moveDown(self):

		if(self.y <= 100):
			self.y += 50
			self.rect.move_ip(0, 50)