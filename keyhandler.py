import pygame

class KeyHandler(object):
    def __init__(self):
        # List of whether handled or not
        self.keys = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }
        self.handled = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }

    def handle_keys(self, pressed):
        if pressed[pygame.K_LEFT]:
            self.keys['left'] = True
        else:
            self.keys['left'] = False
            self.handled['left'] = False

        if pressed[pygame.K_RIGHT]:
            self.keys['right'] = True
        else:
            self.keys['right'] = False
            self.handled['right'] = False

        if pressed[pygame.K_UP]:
            self.keys['up'] = True
        else:
            self.keys['up'] = False
            self.handled['up'] = False

        if pressed[pygame.K_DOWN]:
            self.keys['down'] = True
        else:
            self.keys['down'] = False
            self.handled['down'] = False

        if pressed[pygame.K_SPACE]:
            self.keys['space'] = True
        else:
            self.keys['space'] = False
            self.handled['space'] = False


    def get_key_down(self, key):
        #Let us know if key is down and unhandled
        if key=='left' and self.keys['left'] == True and self.handled['left'] == False:
            return True
        if key=='right' and self.keys['right'] == True and self.handled['right'] == False:
            return True
        if key=='up' and self.keys['up'] == True and self.handled['up'] == False:
            return True
        if key=='down' and self.keys['down'] == True and self.handled['down'] == False:
            return True
        if key=='space' and self.keys['space'] == True and self.handled['space'] == False:
            return True

        return False
