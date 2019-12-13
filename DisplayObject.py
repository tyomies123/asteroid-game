import pygame
from pygame.locals import *

class DisplayObject(pygame.sprite.Sprite):
    def __init__(self, width, height, sprite_image, pos_x, pos_y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.sprite_image = sprite_image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        
        self.image = pygame.transform.scale(pygame.image.load(sprite_image), (self.width, self.height))
    
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
        self.sprite_plain = pygame.sprite.RenderPlain(self)
        
    def render(self):
        self.sprite_plain.draw(self.screen)