import pygame
from pygame.locals import *

from globals import *

from Classes.Board import Board

# init pygame
pygame.init()

# create window
sc = pygame.display.set_mode(SCREEN)
sc.fill(WHITE)

clock = pygame.time.Clock()

# create board
board = Board()

# set caption
pygame.display.set_caption('Tetris')

# game loop
while 1:
    board.update()
    board.draw(sc)

    # redraw screen
    pygame.display.update()

    # handle events
    events = pygame.event.get()

    for event in events:
        # exit
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                board.activeFigure.move(right=False)

            if event.key == K_RIGHT:
                board.activeFigure.move(right=True)

            if event.key == K_UP:
                board.activeFigure.rotate()

            if event.key == K_ESCAPE:
                board.changeStatus()

    clock.tick(FPS)
