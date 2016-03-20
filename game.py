from rabbit import Rabbit
import pygame
import datetime

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

class Game(object):
    def __init__(self,width,height):
        self.rabbits = [
            Rabbit(45,190,200,110),
            Rabbit(130,240,250,160),
            Rabbit(205,190,200,110),
            Rabbit(290,240,250,160),
            Rabbit(365,190,200,110)
        ]
        self.width = width
        self.height = height
        self.score = 0
        self.timer = 0
        self.GAME_LENGTH = 60
        self.start_time = 0

    def start(self):
        self.timer = self.GAME_LENGTH
        self.start_time = datetime.datetime.now()

    def draw(self, screen):
        #Draw background
        pygame.draw.rect(screen, green, (0,100,480,220))
        pygame.draw.ellipse(screen, black, [50, 150, 50, 20])
        pygame.draw.ellipse(screen, black, [130, 200, 65, 25])
        pygame.draw.ellipse(screen, black, [210, 150, 50, 20])
        pygame.draw.ellipse(screen, black, [290, 200, 65, 25])
        pygame.draw.ellipse(screen, black, [370, 150, 50, 20])

        # Draw rabbits
        for rabbit in self.rabbits:
            rabbit.draw(screen)

        #Panels to hide the rabbits underground
        pygame.draw.rect(screen, green, (50,170,50,self.height-170))
        pygame.draw.rect(screen, green, (130,222,50,self.height-170))
        pygame.draw.rect(screen, green, (210,170,50,self.height-170))
        pygame.draw.rect(screen, green, (290,222,50,self.height-170))
        pygame.draw.rect(screen, green, (370,170,50,self.height-170))

        font = pygame.font.Font(None, 36)
        text = font.render("Time: {}".format(self.timer), 1, (255, 255, 0))
        textpos = text.get_rect()
        screen.blit(text, textpos)

        text = font.render("Score: {}".format(self.score), 1, (255, 255, 0))
        textpos = text.get_rect()
        textpos.x += 350
        screen.blit(text, textpos)

    def update(self, key_handler):
        #Update rabbits
        done_debug = False
        for rabbit in self.rabbits:
            # if done_debug==False:
            #     done_debug = True
            #     rabbit.update(True)
            rabbit.update(False)

        if key_handler.get_key_down('left'):
            if self.rabbits[0].feed_carrot():
                self.score += 1

        if key_handler.get_key_down('up'):
            if self.rabbits[1].feed_carrot():
                self.score += 1

        if key_handler.get_key_down('down'):
            if self.rabbits[2].feed_carrot():
                self.score += 1

        if key_handler.get_key_down('right'):
            if self.rabbits[3].feed_carrot():
                self.score += 1

        if key_handler.get_key_down('space'):
            if self.rabbits[4].feed_carrot():
                self.score += 1

        cur_time = datetime.datetime.now()
        diff = (cur_time-self.start_time).seconds
        self.timer = self.GAME_LENGTH - diff

        if self.timer < 0:
            return 'menu'
        return None
