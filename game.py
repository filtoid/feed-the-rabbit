from rabbit import Rabbit
import pygame

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
        self.timer = 60

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

    def update(self):
        #Update rabbits
        for rabbit in self.rabbits:
            rabbit.update()
