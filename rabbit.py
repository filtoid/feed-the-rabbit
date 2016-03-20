import pygame

class Rabbit():
    def __init__(self, x, y):
        self.img = pygame.image.load("rabbit1.png")
        self.img = pygame.transform.scale(self.img, (60, 60))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.status = 'down'

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def update(self):
        if self.status == 'down':
            self.rect.y += 1
        elif self.status=='up':
            self.rect.y -= 1

        if(self.rect.y>200):
            self.status = 'up'
        elif(self.rect.y < 110):
            self.status = 'down'
