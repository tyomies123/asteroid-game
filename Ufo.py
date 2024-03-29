import pygame
import time

from pygame.locals import *
from random import *
from EnemyProjectile import EnemyProjectile

#Enemy UFOs that shoot back at the player
class Ufo(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, size, speed, hp, screen, info_x):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.speed = speed
        self.hp = hp
        self.screen = screen
        self.info_x = info_x
        
        self.ufo_default_list = ['assets/ufo_green_default.png', 'assets/ufo_pink_default.png', 'assets/ufo_orange_default.png']
        self.ufo_look_right_list = ['assets/ufo_green_look_right.png', 'assets/ufo_pink_look_right.png', 'assets/ufo_orange_look_right.png']
        self.ufo_look_left_list = ['assets/ufo_green_look_left.png', 'assets/ufo_pink_look_left.png', 'assets/ufo_orange_look_left.png']
        
        #Randomize UFO sprites
        self.index = randint(0, len(self.ufo_default_list) - 1)
        self.chosen_image = self.ufo_default_list[self.index]
        
        self.image = pygame.transform.scale(pygame.image.load(self.chosen_image), (self.size, self.size))
        self.rect = self.image.get_rect()
        
        self.rect.x = start_x
        self.rect.y = start_y
        
        #Hitbox
        self.rect.left = self.size - self.size * 0.25
        self.rect.right = self.size - self.size * 0.25
        self.rect.height = self.size - self.size * 0.25
        
        self.enemy_plain = pygame.sprite.RenderPlain(self)
        
        self.going_right = True

    #UFO movement
    def movement(self):
        #Turn around at edges
        if self.rect.collidepoint(self.screen.get_width() - self.info_x, 0):
            self.going_right = False 
        if self.rect.collidepoint(0, 0):
            self.going_right = True

        #Move sideways at top of screen    
        if self.going_right:
            self.rect.move_ip(self.speed, 0)    
        if not self.going_right:
            self.rect.move_ip(0 - self.speed, 0)
    
    #Shoot UFO projectile
    def shoot(self):
        return EnemyProjectile(3, 70, 20, self.screen, self.rect.midbottom, self.rect.center[1])
    
    #Signal if collided with player rocket projectile
    def projectile_collided(self, projectile):
        if self.rect.colliderect(projectile.rect):
            return True
        else:
            return False

    #Adjust UFO hp when hit    
    def hit(self):
        self.hp = self.hp - 1
        return self.hp
    
    #Change sprite to look left
    def look_left(self):
        self.image = pygame.transform.scale(pygame.image.load(self.ufo_look_left_list[self.index]), (self.size, self.size))

    #Change sprite to look right   
    def look_right(self):
        self.image = pygame.transform.scale(pygame.image.load(self.ufo_look_right_list[self.index]), (self.size, self.size))

    #Change sprite to look downwards    
    def look_down(self):
        self.image = pygame.transform.scale(pygame.image.load(self.ufo_default_list[self.index]), (self.size, self.size))
        
    def render(self):
        self.movement()
        self.enemy_plain.draw(self.screen)
