import pygame

from random import *
from pygame.locals import *

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, powerup_image, width, height, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.screen = screen
        
        self.image_file = powerup_image
        self.powerup_image = pygame.image.load(self.image_file)
        
        self.start()
    
    def fallmove(self):
        self.rect.move_ip(0, self.speed)
        
    def start(self):
        self.image = pygame.transform.scale(self.powerup_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        
        self.rect.x = randint(0, self.screen.get_width() - self.width)
        self.rect.y = 0 - self.height
    
    def collided(self, rocket):
        if self.rect.colliderect(rocket.rect):
            return True