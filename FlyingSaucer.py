import pygame
import time

from pygame.locals import *
from random import *

class FlyingSaucer(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, width, height, speed, hp, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.hp = hp
        self.screen = screen
        
        self.image = pygame.transform.scale(pygame.image.load('ufo.png'), (self.width, self.height))
        
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.enemy_plain = pygame.sprite.RenderPlain(self)
        
        self.going_right = True

    def movement(self):
        #Turn around
        if self.rect.collidepoint(self.screen.get_width(), 0):
            self.going_right = False 
        if self.rect.collidepoint(0, 0):
            self.going_right = True
            
        if self.going_right:
            self.rect.move_ip(self.speed, 0)    
        if not self.going_right:
            self.rect.move_ip(0 - self.speed, 0)
    
    def hit(self):
        self.hp = self.hp - 1
        
        if self.hp <= 0:
            pass
    
    def shoot(self):
        pass
    
    def render(self):
        self.movement()
        
        self.enemy_plain.draw(self.screen)
        
        
##End