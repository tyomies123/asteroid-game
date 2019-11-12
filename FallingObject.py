import pygame
from pygame.locals import *
from random import randint

class FallingObject(pygame.sprite.Sprite):
    def __init__(self, object_image, minmax, screen):
        pygame.sprite.Sprite.__init__(self)
        self.minmax = minmax
        self.imageFile = object_image
        self.object_image = pygame.image.load(self.imageFile)
        self.reset(screen)
        
    def fallmove(self, speed, screen):
        self.distance = speed
        self.rect.move_ip(0, self.distance)
        if self.rect.y > screen.get_height():
            self.reset(screen)

    def reset(self, screen):
        size = randint(self.minmax[0], self.minmax[1])
        
        self.image = pygame.transform.scale(self.object_image, (size, size))
        self.rect = self.image.get_rect()

        self.rect.x = randint(0, screen.get_width() - size)
        self.rect.y = 0 - size
        self.rect.topleft = (self.rect.x, self.rect.y)
        
    def collided(self, rocket_rect):
        return False