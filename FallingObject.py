import pygame

from pygame.locals import *
from random import *

class FallingObject(pygame.sprite.Sprite):
    def __init__(self, object_image, minmax, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.minmax = minmax
        self.speed = speed
        self.screen = screen
        
        self.object_image = object_image
        self.size = 0
        
        self.reset()

        
    def fallmove(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > self.screen.get_height():
            self.reset()
            self.speed = randrange(20, 51, 5)

    def reset(self):
        self.size = randrange(self.minmax[0], self.minmax[1], 1)
        
        self.image = pygame.transform.scale(pygame.image.load(self.object_image), (self.size, self.size))
        self.rect = self.image.get_rect()

        self.rect.x = randint(0, self.screen.get_width() - self.size * 2)
        self.rect.y = 0 - self.size
        
        #Hitbox
        self.rect.inflate_ip(0 - self.size * 0.15, 0 - self.size * 0.25)
        
        self.object_plain = pygame.sprite.RenderPlain(self)
        
    def rocket_collided(self, rocket):
        return False
    
    def projectile_collided(self, projectile):
        return False
    
    def render(self):
        self.fallmove()
        self.object_plain.draw(self.screen)
