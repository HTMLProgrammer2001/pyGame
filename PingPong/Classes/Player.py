from globals import *

from pygame import draw

class Player:
	def __init__(self, x, y, speed = 5):
		self.x = x
		self.y = y

		self.color = PLAYER_COLOR

		self.speed = 5
		self.dir = 0

		self.size = {
			'width': 3,
			'height': 80
		}

	def getCoords(self):
		return {
			'TOP_LEFT': {
				'x': self.x,
				'y': self.y
			},
			'TOP_RIGHT': {
				'x': self.x + self.size['width'],
				'y': self.y
			},
			'BOTTOM_LEFT': {
				'x': self.x,
				'y': self.y + self.size['height']
			},
			'BOTTOM_RIGHT': {
				'x': self.x + self.size['width'],
				'y': self.y + self.size['height']
			}
		}


	def update(self):
		self.y += self.speed * self.dir

		if(self.y < 0):
			self.y = 0

		if(self.y > H - self.size['height']):
			self.y = H - self.size['height']

	def stop(self):
		self.dir = 0

	def changeDir(self, up = False):
		if(up):
			self.dir = -1
		else:
			self.dir = 1

	def draw(self, sc):
		draw.rect(sc, self.color, (
			self.x, self.y, self.size['width'], self.size['height']))
