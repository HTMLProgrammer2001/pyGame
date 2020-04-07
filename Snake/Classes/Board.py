import pygame
from pygame.locals import *

from globals import *

class Board:
	def __init__(self, snake):
		self.board_surf = pygame.Surface((W, H))
		self.board_rect = self.board_surf.get_rect(center = (W//2, H//2))

		self.snake = snake
		self.apples = []

	def draw(self, sc):
		self.board_surf.fill(BG)

		self.snake.draw(self.board_surf)

		for apple in self.apples:
			apple.draw(self.board_surf)

		sc.blit(self.board_surf, self.board_rect)

	def update(self):
		self.snake.update()

	def addApple(self, apple):
		self.apples.append(apple)