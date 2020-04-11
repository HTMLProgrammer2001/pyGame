import pygame

class Audio:
	def __init__(self):
		self.winSound = pygame.mixer.Sound('./music/win.ogg')
		self.bitSound = pygame.mixer.Sound('./music/bit.ogg')

	def win(self):
		self.winSound.play()

	def bit(self):
		self.bitSound.play()