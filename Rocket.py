import pygame
import sys
import time

from pygame.locals import *
from RocketProjectile import RocketProjectile
from FallingObject import FallingObject

from ExtraHealth import ExtraHealth
from PiercingShot import PiercingShot

class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height, speed, hp, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.hp = hp
        
        self.image = pygame.transform.scale(pygame.image.load('rocket.png'), (self.width, self.height))
        
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.rocket_plain = pygame.sprite.RenderPlain(self)
        
        self.screen = screen
    
    def move_left(self):
        self.image = pygame.transform.scale(pygame.image.load('rocket_move_left.png'), (self.width, self.height))
        
        self.rect.move_ip(0 - self.speed, 0)
        
        #Prevent the rocket from going offscreen
        if self.rect.x < 0:
            self.rect.move_ip(self.speed, 0)
            
        self.rocket_plain = pygame.sprite.RenderPlain(self)

        
    def move_right(self):
        self.image = pygame.transform.scale(pygame.image.load('rocket_move_right.png'), (self.width, self.height))
        
        self.rect.move_ip(self.speed, 0)
        
        #Prevent the rocket from going offscreen
        if self.rect.x > self.screen.get_width() - self.width:
            self.rect.move_ip(0 - self.speed, 0)
            
        self.rocket_plain = pygame.sprite.RenderPlain(self)
        
    def stationary(self):
        self.image = pygame.transform.scale(pygame.image.load('rocket.png'), (self.width, self.height))
        
        self.rocket_plain = pygame.sprite.RenderPlain(self)

        
    def hit(self):
        self.hp = self.hp - 1
        print("Hit! HP left: ", self.hp)
        time.sleep(1)
        
        if self.hp <= 0:
            print("Game Over!")
            time.sleep(2)
            sys.exit()
            
    def shoot(self):
        return RocketProjectile(3, 70, 30, self.screen, self.rect.midtop, self.height)
    
    def powerup_pickup(self, powerup):
        #Check which powerup type was picked up
        
        if type(powerup) is ExtraHealth:
            self.hp = powerup.function(self.hp)

##        if type(powerup) is PiercingShot:
##            powerup.function()
            
            
    def render(self):
        self.rocket_plain.draw(self.screen)
    

        
##End