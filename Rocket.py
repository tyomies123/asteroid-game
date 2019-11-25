import pygame
import sys
import time

from pygame.locals import *
from RocketProjectile import RocketProjectile
from FallingObject import FallingObject

class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height, hp, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('cohete_on_wf.png'), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.width = width
        self.height = height
        self.hp = hp
        
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
        if powerup == "ExtraHealth":
            if self.hp == 6:
                print("Max HP: 6")
                time.sleep(0.33)
            else:
                self.hp = self.hp + 1
                print("+1 HP! HP left: ", self.hp)
                time.sleep(0.33)
            
            
    def render(self):
        self.rocket_plain.draw(self.screen)
    

        
##End