import pygame
from pygame.locals import *

from globals import *

#my components
from Classes.Player import Player
from Classes.Ball import Ball

class Board:
	def __init__(self):
		#init game elements
		self.player = Player(W//2 - PLAYER_WIDTH//2)
		self.ball = Ball(W//2, H//2)

		self.boardSurf = pygame.Surface(SCREEN)

	def update(self):
		self.player.update()
		self.ball.update()

	def draw(self, sc):
		#fill board
		self.boardSurf.fill(BOARD_COLOR)

		#draw game elements
		self.player.draw(self.boardSurf)
		self.ball.draw(self.boardSurf)

		sc.blit(self.boardSurf, (0, 0))