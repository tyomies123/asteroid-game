import pygame

from pygame.locals import *
from random import *

#Object that moves from top of screen to bottom
class FallingObject(pygame.sprite.Sprite):
    def __init__(self, object_image, minmax, speed, screen, info_x):
        pygame.sprite.Sprite.__init__(self)
        self.minmax = minmax
        self.speed = speed
        self.screen = screen
        self.info_x = info_x
        
        self.object_image = object_image
        
        self.reset()

    #Move object downwards, when out of bounds reset position and randomize speed    
    def fallmove(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > self.screen.get_height():
            self.reset()
            self.speed = randrange(20, 50, 5)
    
    #Reset position to top of screen
    def reset(self):
        self.size = randrange(self.minmax[0], self.minmax[1], 1)
        
        self.image = pygame.transform.scale(pygame.image.load(self.object_image), (self.size, self.size))
        self.rect = self.image.get_rect()

        self.rect.x = randint(0, self.screen.get_width() - self.info_x - self.size * 2)
        self.rect.y = 0 - self.size
        
        #Hitbox
        self.rect.height = self.size - self.size * 0.25
        
        self.object_plain = pygame.sprite.RenderPlain(self)

    #Signal if collided with rocket (default: False)    
    def rocket_collided(self, rocket):
        return False
    
    #Signal if hit by projectile (default: False)
    def projectile_collided(self, projectile):
        return False
    
    def render(self):
        self.fallmove()
        self.object_plain.draw(self.screen)
