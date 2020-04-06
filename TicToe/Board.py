import pygame

from Rect import Rect
from globals import *

class Board:
	def __init__(self):
		self.board_surf = pygame.Surface((W - 10, H - 10))
		self.board_rect = self.board_surf.get_rect(center = (W//2, H//2))

		self.board_surf.fill(BG)

		self.rects = []
		self.initRects()

	def initRects(self):
		for i in range(0, 9):
			self.rects.append(Rect(((i//3)*100, (i%3)*100, 100, 100)))

	def draw(self, sc):
		sc.blit(self.board_surf, self.board_rect)

		for i in range(0, 9):
			self.rects[i].draw(sc)

	def click(self, coords, player):
		for i in range(0, 9):
			if(self.rects[i].contains(coords)):
				self.rects[i].setPlayer(player)

	def checkWin(self):
		lines = [
   			 [0, 1, 2],
    		 [3, 4, 5],
    		 [6, 7, 8],
    		 [0, 3, 6],
    		 [1, 4, 7],
    		 [2, 5, 8],
    		 [0, 4, 8],
    		 [2, 4, 6]
  		];	

		for a, b, c in lines:
			
			if(self.rects[a].select and
  				self.rects[a].select == self.rects[b].select and 
  				self.rects[a].select == self.rects[c].select):
  				return True

		return False
