import pygame

from Classes.Games.OnlineGame import OnlineGame
from pygame_input import TextInput
from globals import *


class OnlineWithFriend(OnlineGame):
    def __init__(self):
        OnlineGame.__init__(self)

        # input for id
        self.text = TextInput(font_family='Arial', font_size=24, text_color=TEXT_COLOR)

        # button rect
        self.butRect = None

        self.userID = None

        self.sio.emit('friend_start')

    def draw(self, sc):
        if not self.gameID:
            sc.fill(BG)

            # draw id
            font = pygame.font.SysFont('Arial', 18)
            idSurf = font.render('Your id: ' + str(self.sio.sid), 1, TEXT_COLOR)
            idRect = idSurf.get_rect(center=(W // 2, H // 2 - 60))

            sc.blit(idSurf, idRect)

            # draw message
            msgSurf = font.render('Enter id', 1, TEXT_COLOR)
            msgRect = msgSurf.get_rect(center=(W//2, H//2 - 30))

            sc.blit(msgSurf, msgRect)

            # draw input
            textSurf = self.text.get_surface()
            sc.blit(textSurf, textSurf.get_rect(center=(W//2, H//2)))

            # draw button
            butSurf = font.render('Find', 1, TEXT_COLOR)
            butRect = butSurf.get_rect(center=(W//2, H//2 + 30))

            sc.blit(butSurf, butRect)

            self.butRect = butRect
        else:
            OnlineGame.draw(self, sc)

    def update(self, events):
        self.text.update(events)

    def clickBoard(self, coords):
        if not self.gameID:
            if self.butRect.collidepoint(coords):
                self.sio.emit('friend_find', self.text.get_text())
        else:
            OnlineGame.clickBoard(self, coords)
