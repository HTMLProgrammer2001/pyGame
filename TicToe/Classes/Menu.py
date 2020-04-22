import pygame

from globals import *


class Menu:
    def __init__(self, items):
        self.itemsRect = {}

        for index, item in enumerate(items):
            x = W//2 - len(item) * 4
            y = (H//2 - len(items) * 15 + index * 30)
            self.itemsRect[item] = pygame.Rect(x, y, len(item) * 10, 30)

    def draw(self, sc):
        sc.fill(BG)

        for item in self.itemsRect:
            self.drawText(sc, item, self.itemsRect[item])

    def checkClick(self, pos):
        for item in self.itemsRect:
            if self.itemsRect[item].collidepoint(*pos):
                return item

    @staticmethod
    def drawText(sc, text, rect):
        font = pygame.font.SysFont('Arial', 24)
        fontSurf = font.render(text, 1, TEXT_COLOR)

        sc.blit(fontSurf, rect)
