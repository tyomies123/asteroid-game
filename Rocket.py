import pygame
import sys
import time

from pygame.locals import *
from Projectile import Projectile


class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height, hp, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('cohete_on_wf.png'), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.hp = hp
##        self.base = pygame.Rect(start_x, start_y - height, width, height)
        self.rocket_plain = pygame.sprite.RenderPlain(self)
        
        self.screen = screen
    
    def movement(self, distance, width):
        self.rect.move_ip(distance, 0)
        
        #Prevent the rocket from going offscreen
        if self.rect.x < 0:
            self.rect.move_ip(10, 0)
            
        elif self.rect.x > self.screen.get_width() - width:
            self.rect.move_ip(-10, 0)
        
    def hit(self):
        self.hp = self.hp - 1
        time.sleep(1)
        
        if self.hp <= 0:
            time.sleep(2)
            sys.exit()
            
    def shoot(self):
        pass
            
    def render(self):
        self.rocket_plain.draw(self.screen)
        
    