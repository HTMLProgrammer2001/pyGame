import pygame
from pygame.locals import *

from globals import *

class Snake:
	def __init__(self, x = 0, y = 0):
		self.head = {
			'x': x,
			'y': y
		}

		self.size = 15

		self.body = [self.head]

		self.delta = {
			'x': 1,
			'y': 0
		}

		self.addBody()
		self.addBody()
		self.addBody()

	def update(self):
		newHead = {
			'x': self.head['x'] + self.delta['x']*self.size,
			'y': self.head['y'] + self.delta['y']*self.size
		}

		newHead['x'] = newHead['x'] % W
		newHead['y'] = newHead['y'] % H


		self.head = newHead

		self.body = [newHead] + self.body[:-1:]

	def draw(self, sc):
		for elem in self.body:
			pygame.draw.rect(sc, SNAKE_COLOR, pygame.Rect(elem['x'], elem['y'], self.size, self.size))
			pygame.draw.rect(sc, BORDER_COLOR, pygame.Rect(elem['x'], elem['y'], self.size, self.size), 1)

	def addBody(self):
		last = self.body[-1::][0]

		newBody = {
			'x': last['x'] - self.size,
			'y': last['y']
		}

		self.body.append(newBody)

	def changeDir(self, x, y):
		self.delta = {
			'x': x,
			'y': y
		}