import pygame
import sys
import time

from pygame.locals import *
from RocketProjectile import RocketProjectile
from FallingObject import FallingObject

from ExtraHealth import ExtraHealth
from PiercingShot import PiercingShot

class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height, hp, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.hp = hp
        
        self.image = pygame.transform.scale(pygame.image.load('rocket.png'), (self.width, self.height))
        
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.rocket_plain = pygame.sprite.RenderPlain(self)
        
        self.screen = screen
    
    def movement(self, distance):
        self.rect.move_ip(distance, 0)
        
        #Prevent the rocket from going offscreen
        if self.rect.x < 0:
            self.rect.move_ip(10, 0)
            
        elif self.rect.x > self.screen.get_width() - self.width:
            self.rect.move_ip(-10, 0)
        
    def hit(self):
        self.hp = self.hp - 1
        print("Hit! HP left: ", self.hp)
        time.sleep(1)
        
        if self.hp <= 0:
            print("Game Over!")
            time.sleep(2)
            sys.exit()
            
    def shoot(self):
        return RocketProjectile(5, 50, 30, self.screen, self.rect.midtop[0], self.height)
    
    def powerup_pickup(self, powerup):
        #Check which powerup type was picked up
        
        if type(powerup) is ExtraHealth:
            self.hp = powerup.function(self.hp)

##        if type(powerup) is PiercingShot:
##            powerup.function()
            
            
    def render(self):
        self.rocket_plain.draw(self.screen)
    

        
##End