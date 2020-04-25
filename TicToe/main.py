import pygame
import sys
from pygame.locals import *

from Classes.Games.OnlineGame import OnlineGame
from Classes.Games.OfflineGame import OfflineGame
from Classes.Games.OnlineFriendGame import OnlineWithFriend
from Classes.Menu import Menu
from globals import *


pygame.init()

# var
menuItems = ['Offline', 'Online with random player', 'Online with friend', 'Exit']
sc = pygame.display.set_mode((W, H))
menu = Menu(menuItems)
isRun = False
game = None

pygame.display.set_caption('TicToe')


while 1:
    if not isRun:
        menu.draw(sc)
    else:
        game.draw(sc)

    events = pygame.event.get()

    pygame.display.update()

    if game:
        game.update(events)

    for event in events:
        if event.type == QUIT:
            pygame.quit()

            # close socket
            if game:
                game.quit()

            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            # if we not play now then we click on the menu
            if not isRun:
                # get menu item that we click or None
                menuItem = menu.checkClick(event.pos)

                # offline game selected
                if menuItem == menuItems[0]:
                    game = OfflineGame()
                    isRun = True
                # online game selected
                elif menuItem == menuItems[1]:
                    game = OnlineGame()
                    game.search()
                    isRun = True
                # online with friend selected
                elif menuItem == menuItems[2]:
                    game = OnlineWithFriend()
                    isRun = True
                # quit selected
                elif menuItem == menuItems[3]:
                    pygame.quit()
                    sys.exit()
            # we play now
            else:
                game.clickBoard(event.pos)

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if game.winner or game.isDraw:
                    isRun = False
                    game.quit()
                else:
                    game.toggleStatus()
