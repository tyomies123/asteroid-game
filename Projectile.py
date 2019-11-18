import pygame
from pygame.locals import *

from AttackObject import AttackObject


class Projectile(AttackObject):
    def __init__(self, width, height, proj_image, speed, owner, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.owner = owner
        self.screen = screen
        
        self.image_file = proj_image
        self.proj_image = pygame.image.load(self.image_file)
        
    def movement(self):
        self.rect.move_ip(0, 0 - self.speed)
        if self.rect.y < self.screen.get_height():
            self.image.remove
            
    def start(self):
        self.image = pygame.transform.scale(self.proj_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.owner.midtop - self.width
        self.rect.y = self.screen.get_height() - self.owner.y - self.height
    
    
    def hit(self, asteroid):
        if self.rect.colliderect(asteroid.rect):
##            rocket.hit()
            return True
        return False

        