import pygame

from globals import *

class Rect:
	def __init__(self, rect):
		x, y, w, h =  rect

		self.rect = rect

		self.image = pygame.Surface((w, h))
		self.rect = pygame.Rect((x, y, w, h))
		self.select = ''

	def contains(self, coords):
		return self.rect.contains(pygame.Rect(coords, (1, 1)))

	def draw(self, sc):
		self.image.fill(BG)

		sc.blit(self.image, self.rect)
			
		if(self.select):
			font = pygame.font.SysFont('Arial', 48)
			fontSurf = font.render(self.select, 1, BORDER)

			sc.blit(fontSurf, (self.rect.centerx, self.rect.centery - 25))

		pygame.draw.rect(sc, BORDER, self.rect, 1)

	def setPlayer(self, player):
		if(self.select):
			return

		self.select = player
