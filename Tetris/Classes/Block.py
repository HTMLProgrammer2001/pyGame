import pygame

from globals import *


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, color, group):
        pygame.sprite.Sprite.__init__(self)

        # init draw elements
        self.rect = pygame.Rect(*pos, BLOCK_SIZE, BLOCK_SIZE)
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(self.image, color, self.image.get_rect(topleft=(0, 0)))
        pygame.draw.rect(self.image, BLOCK_BORDER_COLOR, self.image.get_rect(topleft=(0, 0)), BLOCK_BORDER)

        # add to figure group
        self.add(group)

    def draw(self, sc):
        # draw on figure surface
        pygame.draw.rect(sc, self.color, self.rect)
        pygame.draw.rect(sc, BLOCK_BORDER_COLOR, self.rect, BLOCK_BORDER)
