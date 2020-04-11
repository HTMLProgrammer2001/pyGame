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

def showMessage(sc, msg):
	sc.fill(BG)

	font = pygame.font.SysFont('Arial', 48)
	fontSurf = font.render(msg, 1, BORDER)
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

			if(board.click(event.pos, player)):
				if(board.checkWin()):
					isStop = True
					showMessage(sc, 'Player {} win'.format(player))
				elif(board.checkDraw()):
					isStop = True
					showMessage(sc, 'Draw')

				player = 'X' if player == 'O' else 'O'

		if(event.type == KEYDOWN):
			if(event.key == K_ESCAPE):
				if(isStop):
					board = Board()
					isStop = False
