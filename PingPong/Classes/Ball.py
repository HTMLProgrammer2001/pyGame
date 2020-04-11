from globals import *

from pygame import draw, Rect
import random

class Ball:
	def __init__(self, x, y, speed = 3):
		self.color = BALL_COLOR

		self.isMove = True
		self.speed = speed

		self.size = 10
		self.rect = Rect((x, y, self.size, self.size))

		self.dx = 1 if random.random() < 0.5 else -1
		self.dy = 1 if random.random() < 0.5 else -1

	def update(self):
		self.rect.move_ip(self.speed * self.dx, self.speed * self.dy)

		if(self.rect.y < 0):
			self.rect.y = 0
			self.dy = 1

		if(self.rect.y + self.size > H):
			self.rect.y = H - self.size
			self.dy = -1

		self.speed += 0.001

	def stop(self):
		self.isMove = False

	def move(self):
		self.isMove = True

	def changeDir(self, dx = None, dy = None):
		self.dx = dx if dx is not None else self.dx
		self.dy = dy if dy is not None else self.dy

	def draw(self, sc):
		draw.circle(sc, self.color, self.rect.center, self.size)
