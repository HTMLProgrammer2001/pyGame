import pygame
from pygame.locals import *

from globals import *
from Classes.Game import Game

pygame.init()

#variables
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
game = Game()


pygame.display.set_caption('Snake')


while 1:
	events = pygame.event.get()

	sc.fill(BG)

	game.update()
	game.draw(sc)

	pygame.display.update()

	for event in events:
		if(event.type == QUIT):
			exit()

		if(event.type == KEYDOWN):
			if(event.key == K_DOWN):
				game.snake.changeDir(0, 1)

			if(event.key == K_UP):
				game.snake.changeDir(0, -1)

			if(event.key == K_LEFT):
				game.snake.changeDir(-1, 0)

			if(event.key == K_RIGHT):
				game.snake.changeDir(1, 0)

			if(event.key == K_ESCAPE):
				game.changeStatus()
			

	clock.tick(FPS)
