import pygame
from pygame.locals import *
from FallingObject import FallingObject

class Asteroid(FallingObject):    
    def __init__(self, minmax, screen):
        FallingObject.__init__(self, '01murocrep512.jpg', minmax, screen)
 
    def collided(self, rocket_rect):
        if self.rect.colliderect(rocket_rect):
            return True
        return FallingObject.collided(self, rocket_rect)