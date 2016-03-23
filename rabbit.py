import pygame
import random
import math

class Rabbit(object):
    def __init__(self, x, y, upper, lower, screen_width, screen_height):
        width = math.floor(screen_width/6)
        height = math.floor(screen_height/6)
        self.img = pygame.image.load("rabbit1.png")
        self.img = pygame.transform.scale(self.img, (width, height))

        carrot_width = math.floor(screen_width/14)
        carrot_height = math.floor(screen_height/14)
        self.carrot_offset_y = math.floor(screen_height/16)
        self.carrot_offset_x = math.floor(screen_width/96)
        self.carrot = pygame.image.load("carrot_small.png")
        self.carrot = pygame.transform.scale(self.carrot, (carrot_width,carrot_height))

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.status = 'down'
        self.wait = 0
        self.upper = upper
        self.lower = lower
        self.penalty_timer = 10
        self.speed = math.floor(screen_height/80)

    def draw(self, screen):
        screen.blit(self.img, self.rect)

        if self.status=='carrot':
            carrot_rect = self.rect.copy()
            carrot_rect.x -= self.carrot_offset_x
            carrot_rect.y += self.carrot_offset_y
            screen.blit(self.carrot, carrot_rect)

    def update(self, debug):
        if self.status!='carrot' and self.wait > 0:
            # if debug == True:
            #     print(self.wait)
            self.wait -= 1
            return

        # Don't just let the score go down in bounds for incorrect
        if self.penalty_timer > 0:
            self.penalty_timer -= 1
            if self.penalty_timer < 1:
                self.penalty_timer = 0

        if self.status == 'down' or self.status == 'carrot':
            self.rect.y += self.speed
        elif self.status=='up':
            self.rect.y -= self.speed
        else:
            print("ERROR: Unknown status ({})".format(self.status))

        if(self.rect.y > self.upper):
            # if debug == True:
            #     print("Now here {} {} {}".format(self.status, self.rect.y, self.upper))
            self.rect.y = self.upper
            self.wait = random.randint(20, 70)
            self.status = 'up'
        elif(self.rect.y < self.lower):
            self.rect.y = self.lower
            self.wait = random.randint(10, 70)
            self.status = 'down'

    def feed_carrot(self):
        if self.status == 'carrot':
            return None

        diff = self.upper - self.lower
        if self.rect.y < (self.lower + (diff/4)):
            self.status='carrot'
            return True

        if self.rect.y > (self.upper - (diff/4)):
            # Subtract from score because we are way off
            if self.penalty_timer < 1:
                self.penalty_timer = 10
                return False
            return None

        return None
