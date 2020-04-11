import pygame
from pygame.locals import *

class Car(pygame.sprite.Sprite):
	def __init__(self, surf, y, group, speed):
		pygame.sprite.Sprite.__init__(self)

		self.x = 550
		self.y = y
		self.image = surf

		self.rect = surf.get_rect(topleft=(550, y))

		self.add(group)

		self.speed = speed

	def update(self):
		self.x -= self.speed
		self.rect.move_ip(-self.speed, 0)

		if(self.x < -50):
			self.kill()