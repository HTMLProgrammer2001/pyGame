import pygame
from pygame.locals import *
from random import random

from globals import *

class Ball(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		#size 
		self.size = BALL_SIZE

		#ball direction
		self.dir = {
			'x': -1 if random() < 0.5 else 1,
			'y': -1 if random() < 0.5 else 1
		}

		self.speed = BALL_MIN_SPEED

		#draw
		self.surface = pygame.Surface((self.size * 2, self.size * 2))
		self.rect = self.surface.get_rect(
			center=(x, y)
		)

	def update(self):
		#move ball
		self.rect.move_ip(self.dir['x'] * self.speed, self.dir['y'] * self.speed)

		#check collision
		if(self.rect.left < 0 or self.rect.right > W):
			self.dir['x'] *= -1

		if(self.rect.top < 0 or self.rect.bottom > H):
			self.dir['y'] *= -1

	def draw(self, sc):
		#clear
		self.surface.fill(BOARD_COLOR)
		pygame.draw.circle(self.surface, BALL_COLOR, (self.size, self.size), self.size)

		#draw on screen
		sc.blit(self.surface, self.rect)

	def checkCollisionWith(self, rect):
		return self.rect.colliderect(rect)

	def changeDir(self, x = False, y = False):
		#change direction of ball
		if(x):
			self.dir['x'] *= -1

		if(y):
			self.dir['y'] *= -1