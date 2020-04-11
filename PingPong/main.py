import pygame
import sys
import time
from pygame.locals import *

from Classes.Board import Board
from globals import *

pygame.init()

#variables
pyTime = pygame.time.Clock()
initializeTime = time.time()

board = Board()

sc = pygame.display.set_mode((W, H))

#functions

def onKeyDown(event):
    #player 1
    if(event.key == K_DOWN):
        board.player1.changeDir(False)
    if(event.key == K_UP):
        board.player1.changeDir(True)

    #player 2
    if(event.key == K_w):
        board.player2.changeDir(True)
    if(event.key == K_s):
        board.player2.changeDir(False)

    if(event.key == K_ESCAPE):
        board.unpause()

def onKeyUp(event):
    if(event.key in [K_DOWN, K_UP]):
        board.player1.stop()

    if(event.key in [K_w, K_s]):
        board.player2.stop()

while(1):
    board.draw(sc)
    pygame.display.update()

    pygame.display.set_caption("You play {} seconds".format(round(time.time() - initializeTime)))
    
    events = pygame.event.get()

    for event in events:
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()

        if(event.type == KEYDOWN):
            onKeyDown(event)

        if(event.type == KEYUP):
            onKeyUp(event)
        
    pyTime.tick(FPS)
