import pygame

size = (width,height) = (480,320)

pygame.init()
screen = pygame.display.set_mode(size)

rabbit = pygame.image.load("rabbit1.png")
rabbit = pygame.transform.scale(rabbit, (60, 60))
rabbit_rect = rabbit.get_rect()
rabbit_rect.x = 45
rabbit_rect.y = 110

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

    # Draw rabbits
    screen.blit(rabbit, rabbit_rect)


    rabbit_rect.y += 1

    #Panels to hide the rabbits underground
    pygame.draw.rect(screen, green, (50,170,50,height-170))

    pygame.display.flip()
