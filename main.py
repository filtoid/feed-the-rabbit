import pygame
from rabbit import Rabbit

size = (width,height) = (480,320)

pygame.init()
screen = pygame.display.set_mode(size)

rabbits = [
        Rabbit(45,190,200,110),
        Rabbit(130,240,250,160),
        Rabbit(205,190,200,110),
        Rabbit(290,240,250,160),
        Rabbit(365,190,200,110)
    ]

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

quit = False
while quit != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    screen.fill(black)

    #Draw background
    pygame.draw.rect(screen, green, (0,100,480,220))
    pygame.draw.ellipse(screen, black, [50, 150, 50, 20])
    pygame.draw.ellipse(screen, black, [130, 200, 65, 25])
    pygame.draw.ellipse(screen, black, [210, 150, 50, 20])
    pygame.draw.ellipse(screen, black, [290, 200, 65, 25])
    pygame.draw.ellipse(screen, black, [370, 150, 50, 20])

    #Update rabbits
    for rabbit in rabbits:
        rabbit.update()

    # Draw rabbits
    for rabbit in rabbits:
        rabbit.draw(screen)

    #Panels to hide the rabbits underground
    pygame.draw.rect(screen, green, (50,170,50,height-170))
    pygame.draw.rect(screen, green, (130,222,50,height-170))
    pygame.draw.rect(screen, green, (210,170,50,height-170))
    pygame.draw.rect(screen, green, (290,222,50,height-170))
    pygame.draw.rect(screen, green, (370,170,50,height-170))

    pygame.display.flip()
