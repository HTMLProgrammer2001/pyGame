import pygame
from pygame.locals import *

from globals import *

class Apple:
	def __init__(self, x, y):
		self.pos = {
			'x': x,
			'y': y
		}

		self.size = 10

	def draw(self, sc):
		pygame.draw.rect(sc, APPLE_COLOR, pygame.Rect(self.pos['x'], self.pos['y'], self.size, self.size))