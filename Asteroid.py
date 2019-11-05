import pygame
from pygame.locals import *
from FallingObject import FallingObject

class Asteroid(pygame.sprite.Sprite):    
    def __init__(self, image, size, screen):
        FallingObject.__init__(self, image, size, screen)
        
    def falling(self, distance, screen, size):
        FallingObject.fallmove(self, distance, screen, size)
        
    def reset(self, screen, size):
        FallingObject.reset(self, screen, size)