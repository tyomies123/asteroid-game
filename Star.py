import pygame

from pygame.locals import *
from FallingObject import FallingObject

class Star(FallingObject):    
    def __init__(self, minmax, speed, screen):
        FallingObject.__init__(self, 'Blue Star.png', minmax, speed, screen)
