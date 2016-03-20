from game import Game

class Menu(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def draw(self, screen):
        pass

    def update(self, key_handler):
        if key_handler.get_key_down('up'):
            return 'game'

        return None
