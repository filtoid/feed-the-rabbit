import pygame
from rabbit import Rabbit
from game import Game
from menu import Menu
from keyhandler import KeyHandler

SCREEN_WIDTH = 480 * 2
SCREEN_HEIGHT = 320 * 2
size = (SCREEN_WIDTH,SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feed The Rabbit')

key_handler = KeyHandler()
MENU = Menu(SCREEN_WIDTH,SCREEN_HEIGHT)
GAME = Game(SCREEN_WIDTH,SCREEN_HEIGHT)

cur_screen = MENU

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

quit = False
while quit != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    #Update key handler
    key_handler.handle_keys(pygame.key.get_pressed())

    screen.fill(black)

    ret = cur_screen.update(key_handler)
    if ret=='game':
        cur_screen = GAME
        GAME.penalise_error = MENU.hardcore_mode
        GAME.start()
    elif ret =='menu':
        score = GAME.score
        if score > MENU.high_score:
            MENU.high_score = score
        cur_screen = MENU
        MENU.reset()

    cur_screen.draw(screen)

    pygame.display.flip()
