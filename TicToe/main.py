import pygame
import sys
from pygame.locals import *

from Classes.Games.OnlineGame import OnlineGame
from globals import *

pygame.init()

# var
sc = pygame.display.set_mode((W, H))
game = OnlineGame()

game.search()


while 1:
    game.draw(sc)

    pygame.display.update()

    events = pygame.event.get()

    for event in events:
        if event.type == QUIT:
            pygame.quit()

            # close socket
            if game:
                game.quit()

            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            game.clickBoard(event.pos)

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if game.winner:
                    game = OnlineGame()

                    game.search()
                else:
                    game.toggleStatus()
