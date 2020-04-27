import pygame
from globals import *


class LevelBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, health, group, canDamage=True):
        pygame.sprite.Sprite.__init__(self)
        # surface
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))

        self.rect = self.image.get_rect(topleft=(x, y))

        # add to blocks group
        self.add(group)

        # amount of health
        self.health = health
        self.canDamage = canDamage

        self.image.fill(BLOCK_COLORS[self.health])

    def draw(self, sc):
        self.image.fill(BLOCK_COLORS[self.health])
        sc.blit(self.image, self.rect)

    def damage(self, power=1):
        if not self.canDamage:
            return

        self.health -= power

        # block destroyed
        if self.health <= 0:
            self.destroy()
        else:
            # fill new color
            self.image.fill(BLOCK_COLORS[self.health])

    def destroy(self):
        if hasattr(self, 'booster'):
            self.booster.show()

        self.kill()
