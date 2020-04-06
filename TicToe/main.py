import pygame
from pygame.locals import *

from Rect import Rect
from Board import Board
from globals import *

pygame.init()

#var
player = 'X'
sc = pygame.display.set_mode((W, H))
board = Board()
isStop = False

def showWinner():
	global isStop

	isStop = True

	sc.fill(BG)

	font = pygame.font.SysFont('Arial', 48)
	fontSurf = font.render('Player {} win'.format(player), 1, BORDER)
	fontRect = fontSurf.get_rect(center=(W//2, H//2))

	sc.blit(fontSurf, fontRect)

while 1:
	if(not isStop):
		sc.fill(BG)
		board.draw(sc)
		pygame.draw.rect(sc, BORDER, (0, 0, W, H), 10)

	pygame.display.update()

	events = pygame.event.get()

	for event in events:
		if(event.type == QUIT):
			exit()

		if(event.type == MOUSEBUTTONDOWN):
			if(isStop):
				continue

			board.click(event.pos, player)

			if(board.checkWin()):
				showWinner()

			player = 'X' if player == 'O' else 'O'

		if(event.type == KEYDOWN):
			if(event.key == K_ESCAPE):
				if(isStop):
					board = Board()
					isStop = False
