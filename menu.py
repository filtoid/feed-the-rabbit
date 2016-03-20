from game import Game
import pygame

class Menu(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.high_score = 0

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render("Feed the Rabbit", 1, (255, 10, 10))
        textpos = text.get_rect()
        textpos.x = (self.width/2) - (textpos.width/2)
        textpos.centery = self.height/4
        screen.blit(text, textpos)

        text = font.render("Touch Any Carrot To Start", 1, (255, 10, 10))
        textpos = text.get_rect()
        textpos.x = (self.width/2) - (textpos.width/2)
        textpos.centery = self.height/2
        screen.blit(text, textpos)

        text = font.render("Current High Score: {}".format(self.high_score), 1, (255, 10, 10))
        textpos = text.get_rect()
        textpos.x = (self.width/2) - (textpos.width/2)
        textpos.centery = self.height * 3/4
        screen.blit(text, textpos)



    def update(self, key_handler):
        if key_handler.get_key_down('up') or key_handler.get_key_down('down')\
            or key_handler.get_key_down('left') or key_handler.get_key_down('right'):
            return 'game'

        return None
