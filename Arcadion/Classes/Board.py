import pygame

from globals import *

# my components
from Classes.Player import Player
from Classes.Ball import Ball
from Classes.Level import Level


class Board:
    def __init__(self, level=1):
        # init level
        self.level = Level(level)
        self.curLevel = level

        # status variables
        self.isFail = False
        self.isStop = False
        self.isWin = False

        # init game elements
        self.player = Player(W // 2 - PLAYER_WIDTH // 2)
        self.ball = Ball(self.player.rect.center)

        self.boardSurf = pygame.Surface(SCREEN)

    def update(self):
        if self.isFail or self.isStop or self.isWin:
            return

        self.level.update()

        self.player.update()

        # collide with player
        if self.ball.checkCollisionWith(self.player.rect):
            self.ball.changeDir(y=True)
            self.ball.changeSpeedY()

            if self.player.dir == self.ball.dir['x']:
                self.ball.changeSpeedX()
            elif self.player.dir != 0:
                self.ball.changeSpeedX(False)

        # collide with blocks
        collideSprite = self.level.checkCollisionWith(self.ball)
        if collideSprite:
            # ball change speed and direction
            self.ball.changeDir(y=True)
            self.ball.changeSpeedY()

            collideSprite.damage()

        self.ball.update()

        # user loose
        if self.ball.rect.bottom > H:
            self.isFail = True

        # level passed
        sprites = self.level.group.sprites()

        if not sprites or not list(filter(lambda sprite: sprite.canDamage, sprites)):
            self.nextLevel()

    def draw(self, sc):
        if self.isFail or self.isStop or self.isWin:
            if self.isFail:
                self.drawText(sc, 'You loose'.upper(), fill=True)
            elif self.isWin:
                self.drawText(sc, 'You win'.upper())
            else:
                self.drawText(sc, 'Paused'.upper(), fill=True)

            return

        # fill board
        self.boardSurf.fill(BOARD_COLOR)

        # draw game elements
        self.player.draw(self.boardSurf)
        self.ball.draw(self.boardSurf)

        # draw level
        self.level.draw(self.boardSurf)

        sc.blit(self.boardSurf, (0, 0))

    @staticmethod
    def drawText(sc, text, fill=False):
        font = pygame.font.SysFont('Arial', 36)
        font.set_bold(True)
        fontSurf = font.render(text, 1, TEXT_COLOR, BLACK)
        fontRect = fontSurf.get_rect(center=(W//2, H//2))

        if fill:
            sc.fill(BLACK)

        sc.blit(fontSurf, fontRect)

    def changeStatus(self):
        if not self.isFail:
            self.isStop = not self.isStop

        else:
            self.__init__()

    def nextLevel(self):
        # go to the next level
        self.curLevel += 1
        self.level = Level(self.curLevel)

        if not self.level.levelExist:
            self.win()

        # init game elements
        self.player = Player(W // 2 - PLAYER_WIDTH // 2)
        self.ball = Ball(self.player.rect.center)

    def initBall(self):
        self.ball.move()

    def win(self):
        self.isWin = True
