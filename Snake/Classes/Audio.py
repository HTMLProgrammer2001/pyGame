import pygame

class Audio:
	def __init__(self):
		pygame.mixer.music.load('./music/bg.mp3')
		pygame.mixer.music.play(-1)

		self.failSound = pygame.mixer.Sound('music/fail.ogg')
		self.foodSound = pygame.mixer.Sound('music/food.ogg')
		self.passedSound = pygame.mixer.Sound('music/passed.ogg')

	def pause(self):
		pygame.mixer.music.pause()

	def unpause(self):
		pygame.mixer.music.unpause()

	def fail(self):
		self.failSound.play()

	def food(self):
		self.foodSound.play()

	def passed(self):
		self.passedSound.play()