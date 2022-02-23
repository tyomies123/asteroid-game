import pygame
from pygame.locals import *

class Boundary(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, width, height, screen):
        pygame.sprite.Sprite.__init__(self)
        self.start_x = start_x - width
        self.start_y = start_y
        self.width = width
        self.height = height
        self.screen = screen
        
        self.image = pygame.transform.scale(pygame.image.load('assets/boundary.png'), (self.width, self.height))
        
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.boundary_plain = pygame.sprite.RenderPlain(self)
        
    def render(self):
        self.boundary_plain.draw(self.screen)
