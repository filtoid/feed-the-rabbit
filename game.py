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
        self.start_time = 0

    def start(self):
        self.timer = 60
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

    def update(self, key_handler):
        #Update rabbits
        for rabbit in self.rabbits:
            rabbit.update()

        cur_time = datetime.datetime.now()
        diff = (cur_time-self.start_time).seconds
        self.timer = 60 - diff

        if self.timer < 0:
            return 'menu'
        return None
