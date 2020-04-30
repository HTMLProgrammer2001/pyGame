import pygame
from random import choice

# my components
from Classes.Figures.Long import LongFigure
from Classes.Figures.Rect import RectFigure
from Classes.Figures.TShape import TShapeFigure
from Classes.Figures.Zigzag import ZigzagFigure
from globals import *


class Board:
    def __init__(self):
        # status variables
        self.isFail = False
        self.isStop = False

        # player score
        self.score = 0

        # active figure
        self.activeFigure = self.generateFigure()

        # init board blocks
        self.blocks = pygame.sprite.Group()

        # init game elements
        self.boardSurf = pygame.Surface(SCREEN)

    def update(self):
        if self.isFail or self.isStop:
            return

        self.activeFigure.update()

        if self.activeFigure.rect.bottom >= H:
            self.blocks.add(self.activeFigure.getSprites())
            self.activeFigure = self.generateFigure()

        for sprite in self.activeFigure.getSprites():
            if pygame.sprite.spritecollideany(sprite, self.blocks) is not None:
                self.blocks.add(self.activeFigure.getSprites())
                self.activeFigure = self.generateFigure()
                break

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
        self.blocks.draw(sc)

    @staticmethod
    def drawText(sc, text, fill=False):
        font = pygame.font.SysFont('Arial', 36)
        font.set_bold(True)
        fontSurf = font.render(text, 1, TEXT_COLOR, BLACK)
        fontRect = fontSurf.get_rect(center=(W//2, H//2))

        if fill:
            sc.fill(BLACK)

        sc.blit(fontSurf, fontRect)

    @staticmethod
    def generateFigure():
        figures = [LongFigure, TShapeFigure, ZigzagFigure, RectFigure]

        return choice(figures)()

    def changeStatus(self):
        if not self.isFail:
            self.isStop = not self.isStop

        else:
            self.__init__()
