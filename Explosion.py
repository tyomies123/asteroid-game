import pygame
from pygame.locals import *

from PiercingProjectile import PiercingProjectile
from WideProjectile import WideProjectile
from RapidProjectile import RapidProjectile
from EnemyProjectile import EnemyProjectile

class Explosion(pygame.sprite.Sprite):
    def __init__(self, size, start_x, start_y, screen, projectile):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.start_x = start_x
        self.start_y = start_y
        self.screen = screen
        self.projectile = projectile
        
        self.n = 0
        self.over = False
        
        self.sprites = []
        
##        self.sprites = ['boom1_green.png', 'boom2_green.png', 'boom3_green.png', 'boom4_green.png', 'boom5_green.png']

##        self.image = pygame.transform.scale(pygame.image.load(self.sprites[self.n]), (self.size, self.size))
##        
##        self.rect = self.image.get_rect()
##        self.rect.x = self.start_x
##        self.rect.y = self.start_y
        
##        self.explosion_plain = pygame.sprite.RenderPlain(self)
    
    def check_projectile_type(self):
        if type(self.projectile) is PiercingProjectile:
            self.sprites = ['boom1_blue.png', 'boom2_blue.png', 'boom3_blue.png', 'boom4_blue.png', 'boom5_blue.png']
            
        elif type(self.projectile) is WideProjectile:
            self.sprites = ['boom1_yellow.png', 'boom2_yellow.png', 'boom3_yellow.png', 'boom4_yellow.png', 'boom5_yellow.png']
        
        elif type(self.projectile) is RapidProjectile:
            self.sprites = ['boom1_purple.png', 'boom2_purple.png', 'boom3_purple.png', 'boom4_purple.png', 'boom5_purple.png']
        
        elif type(self.projectile) is EnemyProjectile:
            self.sprites = ['boom1_red.png', 'boom2_red.png', 'boom3_red.png', 'boom4_red.png', 'boom5_red.png']
        
        else:
            self.sprites = ['boom1_green.png', 'boom2_green.png', 'boom3_green.png', 'boom4_green.png', 'boom5_green.png']
            
            
    def render_cycle(self):
        self.check_projectile_type()
        
        if self.n < len(self.sprites):
            self.image = pygame.transform.scale(pygame.image.load(self.sprites[self.n]), (self.size, self.size))
            self.rect = self.image.get_rect()
            self.rect.x = self.start_x
            self.rect.y = self.start_y
            self.explosion_plain = pygame.sprite.RenderPlain(self)
            self.explosion_plain.draw(self.screen)
            
            self.n = self.n + 1
        else:
            self.over = True