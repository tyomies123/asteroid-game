import pygame
from pygame.locals import *
from random import randint

class FallingObject(pygame.sprite.Sprite):
    def __init__(self, obj_image, size, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(obj_image), (size, size))
        self.rect = self.image.get_rect()
        
        #Set spawn coordinates
        self.reset(screen, size)
        
    def fallmove(self, distance, screen, size):
        self.rect.move_ip(0, distance)
        if self.rect.y > screen.get_height():
            self.reset(screen, size)

    def reset(self, screen, size, minmax):
        self.rect.x = randint(0, screen.get_width() - size)
        self.rect.y = 0
        self.rect.topleft = (self.rect.x, self.rect.y)
        
        