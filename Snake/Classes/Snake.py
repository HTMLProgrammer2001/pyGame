import pygame
from pygame.locals import *

from globals import *

class Snake(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0):
		pygame.sprite.Sprite.__init__(self)

		self.head = {
			'x': x,
			'y': y
		}
		self.size = 15
		self.rect = pygame.Rect(self.head['x'], self.head['y'], self.size, self.size)

		self.body = [self.head]

		self.delta = {
			'x': 1,
			'y': 0
		}

		#set initial body size
		self.addBody()
		self.addBody()

	def checkCollision(self):
		for elem in self.body[1::]:
			elemRect = pygame.Rect(elem['x'], elem['y'], self.size, self.size)

			if(self.rect.colliderect(elemRect)):
				return True

		return False

	def update(self):
		newHead = {
			'x': self.head['x'] + self.delta['x']*self.size,
			'y': self.head['y'] + self.delta['y']*self.size
		}

		newHead['x'] = newHead['x'] % W
		newHead['y'] = newHead['y'] % H


		self.head = newHead
		self.rect = pygame.Rect(newHead['x'], newHead['y'], self.size, self.size)

		self.body = [newHead] + self.body[:-1:]

	def draw(self, sc):
		for elem in self.body:
			#draw rect
			pygame.draw.rect(sc, SNAKE_COLOR, pygame.Rect(elem['x'], elem['y'], self.size, self.size))
			#draw stroke of rect
			pygame.draw.rect(sc, BORDER_COLOR, pygame.Rect(elem['x'], elem['y'], self.size, self.size), 1)

	def addBody(self):
		last = self.body[-1::][0]

		if(len(self.body) == 1):
			#if we have only body
			last = self.body[-1::][0]

			newBody = {
				'x': last['x'] - self.size,
				'y': last['y']
			}
		else:
			last = self.body[-2::]

			newBody = {
				'x': last[1]['x'] + last[1]['x'] - last[0]['x'],
				'y': last[1]['y'] + last[1]['y'] - last[0]['y']
			}

		self.body.append(newBody)

	def changeDir(self, x, y):
		self.delta = {
			'x': self.delta['x'] if self.delta['x'] == -x else x,
			'y': self.delta['y'] if self.delta['y'] == -y else y
		}