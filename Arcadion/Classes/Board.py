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
		self.curLevel = level

		#status variables
		self.isFail = False
		self.isStop = False

		#init game elements
		self.player = Player(W//2 - PLAYER_WIDTH//2)
		self.ball = Ball(W//2, H//2)

		self.boardSurf = pygame.Surface(SCREEN)

	def update(self):
		if(self.isFail or self.isStop):
			return

		self.player.update()

		#collide with player
		if(self.ball.checkCollisionWith(self.player.rect)):
			self.ball.changeDir(y = True)

		#collide with blocks
		collideSprite = self.level.checkCollisionWith(self.ball)
		if(collideSprite):
			self.ball.changeDir(y = True)
			collideSprite.damage()

		self.ball.update()

		#user loose
		if(self.ball.rect.bottom > H):
			self.isFail = True

		#level passed
		if(not self.level.group.sprites()):
			self.nextLevel()

	def draw(self, sc):
		if(self.isFail or self.isStop):
			return

		#fill board
		self.boardSurf.fill(BOARD_COLOR)

		#draw game elements
		self.player.draw(self.boardSurf)
		self.ball.draw(self.boardSurf)

		#draw level
		self.level.draw(self.boardSurf)

		sc.blit(self.boardSurf, (0, 0))

	def changeStatus(self):
		if(not self.isFail):
			self.isStop = not self.isStop

		else:
			self.__init__()

	def nextLevel(self):
		#go to the next level
		self.curLevel += 1
		self.level = Level(self.curLevel)