import pygame

from random import *
from pygame.locals import *

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, powerup_image, size, speed, screen):
        self.size = size
        self.speed = speed
        self.screen = screen
        
        self.image_file = powerup_image
        self.powerup_image = pygame.image.load(self.image_file)
        
        self.start()
    
    def fallmove(self):
        self.rect.move_ip(0, self.speed)
        
    def start(self):
        self.image = pygame.transform.scale(self.powerup_image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.powerup_plain = pygame.sprite.RenderPlain(self)
        
        self.rect.x = randint(0, self.screen.get_width() - self.size)
        self.rect.y = 0 - self.size
