import pygame
from pygame.locals import *

from globals import *

class Apple:
	def __init__(self, x, y):
		self.pos = {
			'x': x,
			'y': y
		}

		self.size = APPLE_SIZE

		self.rect = pygame.Rect(self.pos['x'], self.pos['y'], self.size, self.size)

	def draw(self, sc):
		pygame.draw.rect(sc, APPLE_COLOR, self.rect)