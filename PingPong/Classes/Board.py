from globals import *
from Classes.Player import Player
from Classes.Ball import Ball

import pygame
from pygame.locals import *

class Board:
	def __init__(self):
		self.ball = Ball(W//2, H//2)

		self.player1 = Player(5, H//2 - 40)
		self.player2 = Player(W - 8, H//2 - 40)

		self.isMove = True

	def update(self):

		if(not self.isMove):
			return

		self.ball.update()
		self.player1.update()
		self.player2.update()

		ballCoords = self.ball.getCoords()
		playerCoords1 = self.player1.getCoords()
		playerCoords2 = self.player2.getCoords()

		#ball out of board
		if(ballCoords['TOP_LEFT']['x'] < 0 or ballCoords['TOP_RIGHT']['x'] > W):
			self.stop()


		#hits in players
		if(ballCoords['TOP_LEFT']['x'] <= playerCoords1['TOP_RIGHT']['x'] and
			playerCoords1['BOTTOM_LEFT']['y'] > ballCoords['TOP_LEFT']['y'] > playerCoords1['TOP_LEFT']['y']):
				self.ball.changeDir(dx = 1)

		if(ballCoords['TOP_RIGHT']['x'] >= playerCoords2['TOP_LEFT']['x'] and
			playerCoords2['BOTTOM_LEFT']['y'] > ballCoords['TOP_LEFT']['y'] > playerCoords2['TOP_LEFT']['y']):
				self.ball.changeDir(dx = -1)

	def draw(self, sc):
		sc.fill((255, 255, 255))

		self.update()

		self.ball.draw(sc)
		self.player1.draw(sc)
		self.player2.draw(sc)

	def stop(self):
		self.isMove = False

	def start(self):
		self.isMove = True

	def restart(self):
		self.ball = Ball(W//2, H//2)

		self.player1 = Player(5, H//2 - 40)
		self.player2 = Player(W - 8, H//2 - 40)

		self.isMove = True