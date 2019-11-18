import pygame
from pygame.locals import *

class AttackObject(pygame.sprite.Sprite):
    def __init__(self, width, height, proj_image, speed, owner, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.owner = owner
        self.screen = screen
        
        self.image_file = proj_image
        self.proj_image = pygame.image.load(self.image_file)
        
        self.start()
    
    def movement(self):
        self.rect.move_ip(0, self.speed)
    
    def start(self):
        pass
    
    def hit(self):
        pass