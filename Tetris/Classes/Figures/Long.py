import pygame
from random import choice, randint

from Classes.Figures.Figure import Figure
from globals import *


class LongFigure(Figure):
    def __init__(self):
        self.variants = [
            [
                ['0', '0', '0', '0'],
                ['0', '0', '0', '0'],
                ['0', '0', '0', '0'],
                ['1', '1', '1', '1']
            ],
            [
                ['0', '1', '0', '0'],
                ['0', '1', '0', '0'],
                ['0', '1', '0', '0'],
                ['0', '1', '0', '0']
            ]
        ]

        self.cur = 0
        self.blocks = self.variants[self.cur]

        Figure.__init__(self, randint(0, W//BLOCK_SIZE - 4)*BLOCK_SIZE)

    def rotate(self):
        self.cur = (self.cur + 1) % len(self.variants)
        self.blocks = self.variants[self.cur]

        self.initBlocks()
