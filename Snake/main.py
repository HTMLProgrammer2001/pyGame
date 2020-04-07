import pygame
from pygame.locals import *
from random import randint

from globals import *
from Classes.Board import Board
from Classes.Snake import Snake
from Classes.Apple import Apple

pygame.init()

#variables
sc = pygame.display.set_mode((W, H))
snake = Snake()
board = Board(snake)
clock = pygame.time.Clock()


pygame.display.set_caption('Snake')

pygame.time.set_timer(EVENT_APPLE_ADD, 5000)


while 1:
	board.update()
	board.draw(sc)

	pygame.display.update()

	events = pygame.event.get()
	for event in events:
		if(event.type == QUIT):
			exit()

		if(event.type == KEYDOWN):
			if(event.key == K_DOWN):
				snake.changeDir(0, 1)

			if(event.key == K_UP):
				snake.changeDir(0, -1)

			if(event.key == K_LEFT):
				snake.changeDir(-1, 0)

			if(event.key == K_RIGHT):
				snake.changeDir(1, 0)

		if(event.type == EVENT_APPLE_ADD):
			board.addApple(Apple(randint(0, W), randint(0, H)))

	clock.tick(FPS)
