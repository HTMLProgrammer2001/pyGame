from globals import *
from Classes.Player import Player
from Classes.Ball import Ball
from Classes.Audio import Audio

import pygame
from pygame.locals import *

class Board:
	def __init__(self):
		self.ball = Ball(W//2, H//2)

		self.player1 = Player(5, H//2 - 40)
		self.player2 = Player(W - 8, H//2 - 40)

		self.isMove = True
		self.winner = None

		self.audio = Audio()

	def update(self):
		if(not self.isMove):
			return

		self.ball.update()
		self.player1.update()
		self.player2.update()

		#ball out of board
		if(self.ball.rect.x < 0 or self.ball.rect.right > W):
			if(self.ball.rect.x < 0):
				self.player2.goal()
			elif(self.ball.rect.right > W):
				self.player1.goal()

			#update state
			self.stop()
			self.ball = Ball(W//2, H//2)
			self.player1.move(5, H//2 - 40)
			self.player2.move(W - 8, H//2 - 40)

			#checkWin
			if(self.player1.score >= 3):
				self.audio.win()
				self.winner = 'Player 1'

			if(self.player2.score >= 3):
				self.audio.win()
				self.winner = 'Player 2'

		#hits in players
		if(self.player1.rect.colliderect(self.ball.rect)):
			self.ball.changeDir(dx = 1)
			self.audio.bit()

		if(self.player2.rect.colliderect(self.ball.rect)):
			self.audio.bit()
			self.ball.changeDir(dx = -1)

	def draw(self, sc):
		if(self.winner):
			sc.fill((255, 255, 255))

			self.drawMessage(sc, '{} win'.format(self.winner))
			return

		if(self.isMove):
			sc.fill((255, 255, 255))

			self.update()

			self.ball.draw(sc)
			self.player1.draw(sc)
			self.player2.draw(sc)

			self.drawScore(sc)	

	def drawScore(self, sc):
		font = pygame.font.SysFont('Arial', 24)
		fontSurf = font.render(str(self.player1.score) + ':' + str(self.player2.score), 1, (0, 0, 0))
		fontRect = fontSurf.get_rect(center = (W//2, 14))

		sc.blit(fontSurf, fontRect)

	def drawMessage(self, sc, msg):
		font = pygame.font.SysFont('Arial', 36)
		fontSurf = font.render(msg, 1, (0, 0, 0))
		fontRect = fontSurf.get_rect(center = (W//2, H//2))

		sc.blit(fontSurf, fontRect)

	def stop(self):
		self.isMove = False

	def start(self):
		self.isMove = True

	def unpause(self):
		if(self.winner):
			self.restart()

		if(self.isMove):
			self.stop()
		else:
			self.start()

	def restart(self):
		self.ball = Ball(W//2, H//2)

		self.player1 = Player(5, H//2 - 40)
		self.player2 = Player(W - 8, H//2 - 40)

		self.isMove = True
		self.winner = None