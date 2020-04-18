import pygame
from pygame.locals import *

from globals import *

#my components
from Classes.Player import Player
from Classes.Ball import Ball
from Classes.Level import Level

class Board:
	def __init__(self, level = 1):
		#init level
		self.level = Level(level)

		#isFail
		self.isFail = False

		#init game elements
		self.player = Player(W//2 - PLAYER_WIDTH//2)
		self.ball = Ball(W//2, H//2)

		self.boardSurf = pygame.Surface(SCREEN)

	def update(self):
		if(self.isFail):
			return

		self.player.update()

		#collide with player
		if(self.ball.checkCollisionWith(self.player.rect)):
			self.ball.changeDir(y = True)

		#collide with blocks
		collideSprite = self.level.checkCollisionWith(self.ball)
		if(collideSprite):
			self.ball.changeDir(y = True)
			collideSprite.kill()

		self.ball.update()

		if(self.ball.rect.bottom > H):
			self.isFail = True

	def draw(self, sc):
		if(self.isFail):
			return

		#fill board
		self.boardSurf.fill(BOARD_COLOR)

		#draw game elements
		self.player.draw(self.boardSurf)
		self.ball.draw(self.boardSurf)

		#draw level
		self.level.draw(self.boardSurf)

		sc.blit(self.boardSurf, (0, 0))

	def restart(self):
		pass