import pygame
from pygame.locals import *
from random import randint

from Car import Car
from Player import Player

pygame.init()

pygame.mixer.music.load('./Faded.mp3')
pygame.mixer.music.play()

#const
FPS = 50
W = 500
H = 150

CARS_SURF = []

#vars
sc = pygame.display.set_mode((W, H))

carsSprite = pygame.sprite.Group()

playerSprite = pygame.sprite.Group()

font = pygame.font.SysFont('Arial', 36)
fontSurf = font.render('You lose. Try again', 1, (0, 0, 0))
fontRect = fontSurf.get_rect(center=(W//2, H//2))

isFail = False

for i in range(1, 4):
	CARS_SURF.append(pygame.transform.rotate(pygame.image.load('./images/car' + str(i) + '.png').convert_alpha(), -90))

player = Player(pygame.transform.rotate(CARS_SURF[0], 180), playerSprite)

pygame.time.set_timer(pygame.USEREVENT, 1000)

while 1:
	sc.fill((175, 175, 175))

	if(not isFail):
		carsSprite.draw(sc)
		carsSprite.update()

		playerSprite.draw(sc)
	else:
		sc.blit(fontSurf, fontRect)

	events = pygame.event.get()

	for event in events:
		if(event.type == KEYDOWN):
			if(event.key == K_DOWN):
				player.moveDown()

			if(event.key == K_UP):
				player.moveUp()

			if(event.key == K_ESCAPE and isFail):
				isFail = False	
				carsSprite.empty()

		if(event.type == USEREVENT):
			enemySurf = CARS_SURF[randint(0, 2)]
			Car(enemySurf, 10 + randint(0, 2) * 50, carsSprite, randint(3, 5))

		if(event.type == QUIT):
			exit()

	if(pygame.sprite.spritecollideany(player, carsSprite)):
		isFail = True

	pygame.display.update()

	pygame.time.delay(round(1000/FPS))