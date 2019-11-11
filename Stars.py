import pygame
from pygame.locals import *
from FallingObject import FallingObject

class Stars(FallingObject):    
    def __init__(self, minmax, screen):
        FallingObject.__init__(self, 'Blue Star.png', minmax, screen)
