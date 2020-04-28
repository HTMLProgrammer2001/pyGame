import pygame
from random import randint

# my components
from Classes.Figures.Figure import Figure
from globals import *


class Board:
    def __init__(self, level=1):
        # status variables
        self.isFail = False
        self.isStop = False

        # player score
        self.score = 0

        # active figure
        self.activeFigure = Figure(randint(BLOCK_SIZE, W - BLOCK_SIZE))

        # init game elements
        self.boardSurf = pygame.Surface(SCREEN)

    def update(self):
        if self.isFail or self.isStop:
            return

        self.activeFigure.update()

    def draw(self, sc):
        if self.isFail or self.isStop:
            if self.isFail:
                self.drawText(sc, 'You loose'.upper(), fill=True)
            else:
                self.drawText(sc, 'Paused'.upper(), fill=True)

            return

        # fill board
        self.boardSurf.fill(BOARD_COLOR)
        sc.blit(self.boardSurf, (0, 0))

        self.activeFigure.draw(sc)

    @staticmethod
    def drawText(sc, text, fill=False):
        font = pygame.font.SysFont('Arial', 36)
        font.set_bold(True)
        fontSurf = font.render(text, 1, TEXT_COLOR, BLACK)
        fontRect = fontSurf.get_rect(center=(W//2, H//2))

        if fill:
            sc.fill(BLACK)

        sc.blit(fontSurf, fontRect)

    def changeStatus(self):
        if not self.isFail:
            self.isStop = not self.isStop

        else:
            self.__init__()
