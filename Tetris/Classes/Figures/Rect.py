import pygame
from random import randint

from Classes.Figures.Figure import Figure
from globals import *


class RectFigure(Figure):
    def __init__(self):
        self.variants = [
            [
                ['1', '1', '1'],
                ['1', '1', '1'],
                ['1', '1', '1']
            ],
        ]

        self.cur = 0
        self.blocks = self.variants[self.cur]

        Figure.__init__(self, randint(0, W//BLOCK_SIZE - 4)*BLOCK_SIZE)

    def rotate(self):
        self.cur = (self.cur + 1) % len(self.variants)
        self.blocks = self.variants[self.cur]

        self.initBlocks()
