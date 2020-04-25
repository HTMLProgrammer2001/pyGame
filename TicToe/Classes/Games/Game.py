import pygame

from globals import *
from Classes.Board import Board


class Game:
    def __init__(self):
        # current player step
        self.curPlayer = 'X'

        self.isPause = False
        self.isDraw = False
        self.winner = None
        self.msg = ''

        self.board = Board()

    def draw(self, sc):
        sc.fill(BG)
        self.board.draw(sc)
        pygame.draw.rect(sc, BORDER_COLOR, (0, 0, W, H), 10)

        if self.msg:
            self.showMessage(sc, self.msg, True)
        elif self.isPause:
            self.showMessage(sc, 'Paused'.upper(), True)
        elif self.isDraw:
            self.showMessage(sc, 'Draw'.upper(), True)
        elif self.winner:
            self.showMessage(sc, 'Winner {}'.format(self.winner), True)

    @staticmethod
    def showMessage(sc, msg, fill=False):
        if fill:
            sc.fill(BG)

        font = pygame.font.SysFont('Arial', 40)
        fontSurf = font.render(msg, 1, TEXT_COLOR)
        fontRect = fontSurf.get_rect(center=(W // 2, H // 2))

        sc.blit(fontSurf, fontRect)

    def pause(self):
        self.isPause = True

    def run(self):
        self.isPause = False

    def toggleStatus(self):
        if self.isPause:
            self.run()
        else:
            self.pause()

    def quit(self):
        pass

    def update(self, *args):
        pass
