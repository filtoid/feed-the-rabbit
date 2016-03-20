# An object which floats near the bunny we either lost a score from or gained
# a score from. This helps to convey that we scored or were penalised
import pygame
import random

class ScoreHint(object):
    def __init__(self, x, y, negative, value):
        self.isNegative = negative
        self.x = x
        self.y = y
        self.value = value
        self.counter = 20

    def update(self):
        self.counter -= 1
        if self.counter < 0:
            return False

        self.y -= 1
        self.x += random.randint(-1,1)
        return True

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text = ''
        if self.isNegative:
            text = font.render("{}".format(self.value), 1, (255, 10, 10))
        else:
            text = font.render("+{}".format(self.value), 1, (10,10,255))
        textpos = text.get_rect()
        textpos.x = self.x
        textpos.y = self.y
        screen.blit(text, textpos)
