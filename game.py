import pygame
import datetime

from rabbit import Rabbit
from scorehint import ScoreHint

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
        self.score_objects = []
        self.width = width
        self.height = height
        self.score = 0
        self.timer = 0
        self.GAME_LENGTH = 60
        self.start_time = 0
        self.penalise_error = True

    def start(self):
        self.score = 0
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

        for so in self.score_objects:
            so.draw(screen)

    def _feed_carrot(self, index):
        rabbit = self.rabbits[index]
        ret = rabbit.feed_carrot()
        if ret == False and self.penalise_error:
            # Penalise as we are in hardcore_mode
            self.score -= 1
            self.score_objects.append(ScoreHint(rabbit.rect.x, rabbit.rect.y, True, -1))
        elif ret == True:
            # If we are in hardcore_mode then score 2 otherwise 1
            if self.penalise_error:
                self.score_objects.append(ScoreHint(rabbit.rect.x, rabbit.rect.y, False, 2))
                self.score += 2
            else:
                self.score_objects.append(ScoreHint(rabbit.rect.x, rabbit.rect.y, False, 1))
                self.score += 1

    def update(self, key_handler):
        #Update rabbits
        # done_debug = False
        for rabbit in self.rabbits:
            # if done_debug==False:
            #     done_debug = True
            #     rabbit.update(True)
            rabbit.update(False)

        if key_handler.get_key_down('left'):
            self._feed_carrot(0)

        if key_handler.get_key_down('up'):
            self._feed_carrot(1)

        if key_handler.get_key_down('down'):
            self._feed_carrot(2)

        if key_handler.get_key_down('right'):
            self._feed_carrot(3)

        if key_handler.get_key_down('space'):
            self._feed_carrot(4)

        # Don't allow negative scores
        if self.score < 0:
            self.score = 0

        cur_time = datetime.datetime.now()
        diff = (cur_time-self.start_time).seconds
        self.timer = self.GAME_LENGTH - diff

        # Loop through and update the score_objects
        for k,v in enumerate(self.score_objects):
            if v.update()==False:
                v = None
                self.score_objects = self.score_objects[:k] + self.score_objects[k+1:]

        if self.timer < 0:
            return 'menu'
        return None
