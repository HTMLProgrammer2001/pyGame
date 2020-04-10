import pygame
from pygame.locals import *
from random import randint

from Classes.Level import Level
from Classes.Snake import Snake
from Classes.Apple import Apple
from Classes.Audio import Audio
from globals import *

class Game:
	def __init__(self, curLevel = 1):
		#game elements
		self.snake = Snake()
		self.level = Level(curLevel)
		self.setApple()

		self.curLevel = curLevel
		self.eatedApples = 0

		#player loose
		self.isFail = False

		#pause
		self.isPause = False

		#is win game
		self.isWin = False

		#music controller
		self.audio = Audio()

	def nextLevel(self):
		self.audio.passed()
		self.audio.pause()

		self.eatedApples = 0
		self.curLevel += 1

		self.level = Level(self.curLevel)

		if(not self.level.levelExist):
			self.isWin = True

	def changePause(self):
		self.isPause = not self.isPause

		if(self.isPause):
			self.audio.pause()
		else:
			self.audio.unpause()

	def setApple(self):
		while 1:
			newApple = Apple(randint(APPLE_SIZE, W - APPLE_SIZE), randint(APPLE_SIZE, H - APPLE_SIZE))

			if(not self.level.checkCollisionWith(newApple)):
				break

		self.apple = newApple

	def loose(self):
		self.isFail = True

		self.audio.fail()

	def restart(self):
		#clear variables
		self.isFail = False
		self.isPause = False
		self.isWin = False

		self.eatedApples = 0

		#first level
		self.curLevel = 1
		self.level = Level(self.curLevel)

		#restart game elements
		self.snake = Snake()
		self.setApple()

		#music controller
		self.audio = Audio()

	def changeStatus(self):
		if(self.isFail or self.isWin):
			self.restart()
		else:
			self.changePause()
			self.audio.unpause()

	def eat(self):
		self.audio.food()

		self.eatedApples += 1

		if(self.eatedApples >= 10):
			self.nextLevel()
			self.isPause = True
			self.snake = Snake()
		else:
			self.snake.addBody()

		self.setApple()
		



	def update(self):
		if(not self.isFail and not self.isPause):
			self.snake.update()

			#check if snake collidarate with apple
			if(self.snake.rect.colliderect(self.apple.rect)):
				self.eat()

			if(self.snake.checkCollision() or self.level.checkCollisionWith(self.snake)):
				self.audio.pause()
				self.loose()


	def draw(self, sc):
		if(not self.isFail and not self.isWin):
			self.snake.draw(sc)

			if(self.apple):
				self.apple.draw(sc)

			self.level.draw(sc)

			self.drawScore(sc)


		elif(self.isFail):
			self.drawMessage(sc, 'You loose')

		else:
			self.drawMessage(sc, 'YOU WIN!!!')			


	def drawMessage(self, sc, msg):
		font = pygame.font.SysFont('Arial', 36);
		font_surf = font.render(msg, 1, (TEXT_COLOR))
		font_rect = font_surf.get_rect(center = (W//2, H//2))

		sc.blit(font_surf, font_rect)
		pygame.display.update()

	def drawScore(self, sc):
		font = pygame.font.SysFont('Arial', 20);
		font_surf = font.render(str(self.eatedApples), 1, (TEXT_COLOR))
		font_rect = font_surf.get_rect(topright = (W - 10, 0))

		sc.blit(font_surf, font_rect)
		pygame.display.update()		