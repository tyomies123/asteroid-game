import pygame

from pygame.locals import *
from random import *
from FallingObject import FallingObject

class Asteroid(FallingObject):    
    def __init__(self, minmax, speed, screen, info):
        FallingObject.__init__(self, self.pick_sprite(), minmax, speed, screen, info)
    
    def pick_sprite(self):
        self.asteroid_list = ['asteroid1.png', 'asteroid2.png', 'asteroid3.png', 'asteroid4.png']
        self.index = randint(0, len(self.asteroid_list) - 1)
        
        return self.asteroid_list[self.index]
        
    
    def fallmove(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > self.screen.get_height():
            self.reset()
            self.speed = randrange(15, 31, 5)
            
    def rocket_collided(self, rocket):        
        if self.rect.colliderect(rocket.rect):
            rocket.hit()
            return True
        return FallingObject.rocket_collided(self, rocket)
    
    def projectile_collided(self, projectile):
        if self.rect.colliderect(projectile.rect):
            return True
        return FallingObject.projectile_collided(self, projectile)