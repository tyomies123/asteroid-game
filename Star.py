import pygame

from pygame.locals import *
from random import *
from FallingObject import FallingObject

class Star(FallingObject):    
    def __init__(self, minmax, speed, screen):
        FallingObject.__init__(self, self.pick_sprite(), minmax, speed, screen)
    
    def pick_sprite(self):
##        self.asteroid_list = ['star_blue.png', 'star_green.png', 'star_purple.png', 'star_red.png', 'star_yellow.png']
        self.asteroid_list = ['star1.png', 'star2.png', 'star3.png', 'star4.png', 'star5.png']
        self.index = randint(0, len(self.asteroid_list) - 1)
        
        return self.asteroid_list[self.index]