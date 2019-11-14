import pygame
from pygame.locals import *
from random import *
from FallingObject import FallingObject

class Asteroid(FallingObject):    
    def __init__(self, minmax, speed, screen):
        FallingObject.__init__(self, '01murocrep512.jpg', minmax, speed, screen)
    
    def fallmove(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > self.screen.get_height():
            self.reset()
            self.speed = randrange(15, 31, 5)
            
    def collided(self, rocket_rect):
        if self.rect.colliderect(rocket_rect):
            return True
        return FallingObject.collided(self, rocket_rect)
