from globals import *

from pygame import draw
import random

class Ball:
	def __init__(self, x, y, speed = 3):
		self.x = x
		self.y = y

		self.color = BALL_COLOR

		self.isMove = True
		self.speed = speed

		self.size = 10

		self.dx = 1 if random.random() < 0.5 else -1
		self.dy = 1 if random.random() < 0.5 else -1

	def getCoords(self):
		return {
			'TOP_LEFT': {
				'x': self.x - self.size,
				'y': self.y - self.size
			},
			'TOP_RIGHT': {
				'x': self.x + self.size,
				'y': self.y - self.size
			},
			'BOTTOM_LEFT': {
				'x': self.x - self.size,
				'y': self.y + self.size
			},
			'BOTTOM_RIGHT': {
				'x': self.x + self.size,
				'y': self.y + self.size
			}
		}

	def update(self):
		self.x += self.speed * self.dx
		self.y += self.speed * self.dy

		if(self.y < 0):
			self.y = 0
			self.dy = 1

		if(self.y + self.size > H):
			self.y = H - self.size
			self.dy = -1

	def stop(self):
		self.isMove = False

	def move(self):
		self.isMove = True

	def changeDir(self, dx = None, dy = None):
		self.dx = dx if dx is not None else self.dx
		self.dy = dy if dy is not None else self.dy

	def draw(self, sc):
		draw.circle(sc, self.color, (self.x, self.y), self.size)
