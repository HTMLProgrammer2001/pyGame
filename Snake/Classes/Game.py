import pygame
from pygame.locals import *
from random import randint

from Classes.Level import Level
from Classes.Snake import Snake
from Classes.Apple import Apple
from globals import *

class Game:
	def __init__(self, level = 1):
		#game elements
		self.snake = Snake()
		self.level = Level(level)
		self.setApple()

		#player loose
		self.isFail = False

		#pause
		self.isPause = False

	def changePause(self):
		self.isPause = not self.isPause

	def setApple(self):
		self.apple = Apple(randint(APPLE_SIZE, W - APPLE_SIZE), randint(APPLE_SIZE, H - APPLE_SIZE))

	def loose(self):
		self.isFail = True

	def restart(self):
		#clear variables
		self.isFail = False
		self.isPause = False

		#first level
		self.level = Level(1)

		#restart game elements
		self.snake = Snake()
		self.setApple()

	def changeStatus(self):
		if(self.isFail):
			self.restart()
		else:
			self.changePause()



	def update(self):
		if(not self.isFail and not self.isPause):
			self.snake.update()

			#check if snake collidarate with apple
			if(self.snake.rect.colliderect(self.apple.rect)):
				self.setApple()
				self.snake.addBody()

			self.isFail = self.snake.checkCollision() or bool(pygame.sprite.spritecollideany(self.snake, self.level.group))


	def draw(self, sc):
		if(not self.isFail and not self.isPause):
			self.snake.draw(sc)

			if(self.apple):
				self.apple.draw(sc)

			self.level.draw(sc)


		elif(self.isFail):
			self.drawMessage(sc, 'You loose')


		else:
			self.drawMessage(sc, 'Pause')


	def drawMessage(self, sc, msg):
		font = pygame.font.SysFont('Arial', 36);
		font_surf = font.render(msg, 1, (TEXT_COLOR))
		font_rect = font_surf.get_rect(center = (W//2, H//2))

		sc.blit(font_surf, font_rect)
		pygame.display.update()
