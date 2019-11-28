import pygame
import time

from pygame.locals import *
from random import *
from EnemyProjectile import EnemyProjectile

class Ufo(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, width, height, speed, hp, screen):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.hp = hp
        self.screen = screen
        
        enemy_list = ['ufo_green_new.png', 'ufo_pink_new.png', 'ufo_orange_new.png']
        
        self.image = pygame.transform.scale(pygame.image.load(enemy_list[randint(0, len(enemy_list) - 1)]), (self.width, self.height))
        
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.enemy_plain = pygame.sprite.RenderPlain(self)
        
        self.going_right = True

    def movement(self):
        #Turn around at edges
        if self.rect.collidepoint(self.screen.get_width(), 0):
            self.going_right = False 
        if self.rect.collidepoint(0, 0):
            self.going_right = True
            
        if self.going_right:
            self.rect.move_ip(self.speed, 0)    
        if not self.going_right:
            self.rect.move_ip(0 - self.speed, 0)
    
    def shoot(self):
        return EnemyProjectile(5, 50, 20, self.screen, self.rect.midbottom[0], self.rect.center[1])
    
    def projectile_collided(self, projectile):
        if self.rect.colliderect(projectile.rect):
            return True
        else:
            return False
        
    def hit(self):
        self.hp = self.hp - 1
        return self.hp
    
    def render(self):
        self.movement()
        self.enemy_plain.draw(self.screen)
        
        
##End