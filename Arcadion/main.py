import pygame
from pygame.locals import *

from globals import *

from Classes.Board import Board

#init pygame
pygame.init()

#create window
sc = pygame.display.set_mode(SCREEN)
sc.fill(WHITE)

clock = pygame.time.Clock()

#create board
board = Board()

#set caption
pygame.display.set_caption('Arcadion')

#game loop
while 1:
	board.update()
	board.draw(sc)

	#redraw screen
	pygame.display.update()

	#handle events
	events = pygame.event.get()

	for event in events:
		#exit
		if(event.type == QUIT):
			exit()

		if(event.type == KEYDOWN):
			if(event.key == K_LEFT):
				#player move left
				board.player.changeDir(-1)

			if(event.key == K_RIGHT):
				#player move left
				board.player.changeDir(1)

		if(event.type == KEYUP):
			board.player.changeDir(0)


	clock.tick(FPS)		