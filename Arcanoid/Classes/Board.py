import pygame

from globals import *

# my components
from Classes.Player import Player
from Classes.Ball import Ball
from Classes.Level import Level

from Classes.Boosters.Long import LongBooster
from Classes.Boosters.Power import PowerBooster
from Classes.Boosters.Balls import BallsBooster


class Board:
    def __init__(self, level=1):
        # init level
        self.level = Level(level)
        self.curLevel = level

        # status variables
        self.isFail = False
        self.isStop = False
        self.isWin = False

        self.boosters = []

        # init game elements
        self.player = Player(W // 2 - PLAYER_WIDTH // 2)
        self.balls = [Ball(self.player.rect.center)]

        self.boardSurf = pygame.Surface(SCREEN)

    def update(self):
        if self.isFail or self.isStop or self.isWin:
            return

        self.level.update()
        self.player.update()

        # collide with player
        self.collidePlayer()

        # collide with blocks
        self.collideBlocks()

        # collide with boosters
        self.collideBoosters()

        for booster in self.boosters:
            if not booster.isActive():
                booster.destroy()
                self.boosters.remove(booster)

        for ball in self.balls:
            ball.update()

        # user loose
        for ball in self.balls:
            if ball.rect.bottom > H:
                self.balls.remove(ball)

        if not len(self.balls):
            self.isFail = True

        # level passed
        sprites = self.level.group.sprites()

        if not sprites or not list(filter(lambda sprite: sprite.canDamage, sprites)):
            self.nextLevel()

    def collidePlayer(self):
        for ball in self.balls:
            if ball.checkCollisionWith(self.player.rect):
                # ball bump into player
                ball.changeDir(y=True)
                ball.changeSpeedY()

                # change angle by x
                if self.player.dir == ball.dir['x']:
                    ball.changeSpeedX()
                elif self.player.dir != 0:
                    ball.changeSpeedX(False)

    def collideBlocks(self):
        for ball in self.balls:
            collideSprite = self.level.checkCollisionWith(ball)
            if collideSprite:
                # ball change speed and direction
                ball.changeDir(y=True)
                ball.changeSpeedY()

                collideSprite.damage(ball.power)

    def collideBoosters(self):
        booster = self.level.checkBoosterCollisionWith(self.player)
        if booster:
            # remove from group
            booster.remove(self.level.boosterGroup)

            # add to active boosters
            self.boosters.append(booster)

            # activate
            booster.activate()

            # long player
            if isinstance(booster, LongBooster):
                booster.attach(self.player)

            # power booster
            if isinstance(booster, PowerBooster):
                booster.attach(self.balls)

            # balls booster
            if isinstance(booster, BallsBooster):
                booster.attach(self.balls, (self.player.rect.centerx, self.player.rect.centery - 30))

                self.initBall()

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

        for ball in self.balls:
            ball.draw(self.boardSurf)

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
        self.balls = [Ball(self.player.rect.center)]

    def initBall(self):
        for ball in self.balls:
            ball.move()

    def win(self):
        self.isWin = True
