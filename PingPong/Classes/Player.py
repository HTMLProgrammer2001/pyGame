from globals import *

from pygame import draw, Rect

class Player:
	def __init__(self, x, y, speed = 5):
		self.x = x
		self.y = y

		self.color = PLAYER_COLOR

		self.speed = 5
		self.dir = 0

		self.score = 0

		self.size = {
			'width': 3,
			'height': 80
		}

		self.rect = Rect((x, y, self.size['width'], self.size['height']))


	def update(self):
		self.rect.move_ip(0, self.speed * self.dir)

		if(self.rect.y < 0):
			self.rect.y = 0

		if(self.rect.y > H - self.size['height']):
			self.rect.y = H - self.size['height']

	def stop(self):
		self.dir = 0

	def changeDir(self, up = False):
		if(up):
			self.dir = -1
		else:
			self.dir = 1

	def goal(self):
		self.score += 1

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def draw(self, sc):
		draw.rect(sc, self.color, self.rect)
