import pygame

from pygame.locals import *
from random import *
from FallingObject import FallingObject

#Objects falling from top of screen, harmless "background" objects
class Star(FallingObject):    
    def __init__(self, minmax, speed, screen, info_x):
        FallingObject.__init__(self, self.pick_sprite(), minmax, speed, screen, info_x)
    
    #Randomize star sprite
    def pick_sprite(self):
        self.asteroid_list = ['assets/star1.png', 'assets/star2.png', 'assets/star3.png', 
                              'assets/star4.png', 'assets/star5.png']
        self.index = randint(0, len(self.asteroid_list) - 1)
        
        return self.asteroid_list[self.index]