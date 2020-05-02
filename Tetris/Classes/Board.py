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
        self.nextFigure = self.generateFigure()
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
            self.next()

            row = self.checkRow()
            while row:
                print(row)
                self.destroyRow(row)
                row = self.checkRow(row)

        if self.collideActive():
            self.blocks.add(self.activeFigure.getSprites())
            row = self.checkRow()
            while row:
                print(row)
                self.destroyRow(row)
                row = self.checkRow(row)

            if self.checkLoose():
                self.isFail = True

            self.next()

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

        self.drawScore(sc)

        self.drawNext(sc)

    def drawScore(self, sc):
        font = pygame.font.SysFont('Arial', 24)
        fontSurf = font.render(str(self.score), 1, TEXT_COLOR)
        fontRect = fontSurf.get_rect(topleft=(10, 10))

        sc.blit(fontSurf, fontRect)

    def changeStatus(self):
        if not self.isFail:
            self.isStop = not self.isStop

        else:
            self.__init__()

    def checkLoose(self):
        for sprite in self.blocks.sprites():
            if sprite.rect.top < 0:
                print(sprite.rect.top)
                return True

        return False

    def checkRow(self, start=None):
        start = H//BLOCK_SIZE - 1 if start is None else start

        for y in range(start, 0, -1):
            isFilled = True

            for x in range(0, W//BLOCK_SIZE):
                for sprite in self.blocks.sprites():
                    if sprite.rect.collidepoint(x * BLOCK_SIZE + BLOCK_SIZE//2,
                                                    y * BLOCK_SIZE + BLOCK_SIZE//2):
                        break

                else:
                    isFilled = False

            if isFilled:
                return y

        return False

    def destroyRow(self, row):
        # destroy from blocks
        for x in range(0, W // BLOCK_SIZE):
            for sprite in self.blocks.sprites():
                if sprite.rect.collidepoint(x * BLOCK_SIZE + BLOCK_SIZE // 2,
                                                row * BLOCK_SIZE + BLOCK_SIZE // 2):
                    sprite.remove(self.blocks)

        # fall down blocks
        for sprite in self.blocks.sprites():
            if sprite.rect.bottom < row * BLOCK_SIZE + BLOCK_SIZE//2:
                sprite.rect.move_ip(0, BLOCK_SIZE)

        self.score += 10

    def collideActive(self):
        for sprite in self.activeFigure.getSprites():
            if pygame.sprite.spritecollideany(sprite, self.blocks) is not None or sprite.rect.bottom > H:
                return True

        return False

    def next(self):
        self.activeFigure = self.nextFigure
        self.nextFigure = self.generateFigure()

    def drawNext(self, sc):
        nextSurface = pygame.Surface(self.nextFigure.surf.get_size())
        self.nextFigure.draw(nextSurface, False)
        nextSurface = pygame.transform.scale(nextSurface, (60, 60))
        nextRect = nextSurface.get_rect(topright=(W - 10, 10))

        sc.blit(nextSurface, nextRect)

    @staticmethod
    def drawText(sc, text, fill=False):
        font = pygame.font.SysFont('Arial', 28)
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
