from game import Game
import pygame

class Menu(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.high_score = 0
        self.hardcore_mode = False
        self.cooldown = 0

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

        val = "Off"
        if self.hardcore_mode==True:
            val = "On"
        font = pygame.font.Font(None, 24)
        text = font.render("Hardcore Mode (Press Space to Toggle): {}".format(val), 1, (255, 10, 10))
        textpos = text.get_rect()
        textpos.x = 0
        textpos.centery = self.height - textpos.height
        screen.blit(text, textpos)


    def update(self, key_handler):
        if self.cooldown > 0:
            self.cooldown -= 1
            #Just in case we somehow jump over the value
            if self.cooldown < 0:
                self.cooldown = 0

        if key_handler.get_key_down('up') or key_handler.get_key_down('down')\
            or key_handler.get_key_down('left') or key_handler.get_key_down('right'):
            return 'game'

        if key_handler.get_key_down('space') and self.cooldown==0:
            self.cooldown = 10
            self.hardcore_mode = not self.hardcore_mode

        return None
