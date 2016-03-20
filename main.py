import pygame
from rabbit import Rabbit
from game import Game

size = (width,height) = (480,320)

pygame.init()
screen = pygame.display.set_mode(size)

cur_screen = Game(width,height)

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

quit = False
while quit != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    screen.fill(black)

    cur_screen.update()
    cur_screen.draw(screen)

    pygame.display.flip()
