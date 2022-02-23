import pygame
from pygame.locals import *

from PiercingProjectile import PiercingProjectile
from WideProjectile import WideProjectile
from RapidProjectile import RapidProjectile
from BombProjectile import BombProjectile
from EnemyProjectile import EnemyProjectile

from PiercingShot import PiercingShot
from WideShot import WideShot
from RapidShot import RapidShot
from BombShot import BombShot
from ExtraHealth import ExtraHealth

from Asteroid import Asteroid

#Explosions from different kinds of collisions
class Explosion(pygame.sprite.Sprite):
    def __init__(self, size, start_x, start_y, screen, object):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.start_x = start_x
        self.start_y = start_y
        self.screen = screen
        self.object = object
        
        self.n = 0
        self.over = False
        
        self.sprites = []
    
    #Create different explosions based on projectiles and objects involved
    def check_object_type(self):
        if type(self.object) is PiercingProjectile or type(self.object) is PiercingShot:
            self.sprites = ['assets/boom1_blue.png', 'assets/boom2_blue.png', 'assets/boom3_blue.png',
                            'assets/boom4_blue.png', 'assets/boom5_blue.png']
            
        elif type(self.object) is WideProjectile or type(self.object) is WideShot:
            self.sprites = ['assets/boom1_yellow.png', 'assets/boom2_yellow.png', 'assets/boom3_yellow.png',
                            'assets/boom4_yellow.png', 'assets/boom5_yellow.png']
        
        elif type(self.object) is RapidProjectile or type(self.object) is RapidShot:
            self.sprites = ['assets/boom1_purple.png', 'assets/boom2_purple.png', 'assets/boom3_purple.png',
                            'assets/boom4_purple.png', 'assets/boom5_purple.png']
            
        elif type(self.object) is BombProjectile or type(self.object) is BombShot:
            self.sprites = ['assets/boom1_orange.png', 'assets/boom2_orange.png', 'assets/boom3_orange.png',
                            'assets/boom4_orange.png', 'assets/boom5_orange.png']
        
        elif type(self.object) is EnemyProjectile or type(self.object) is ExtraHealth:
            self.sprites = ['assets/boom1_red.png', 'assets/boom2_red.png', 'assets/boom3_red.png',
                            'assets/boom4_red.png', 'assets/boom5_red.png']
            
        elif type(self.object) is Asteroid:
            self.sprites = ['assets/boom1_asteroid.png', 'assets/boom2_asteroid.png', 'assets/boom3_asteroid.png',
                            'assets/boom4_asteroid.png', 'assets/boom5_asteroid.png']
        else:
            self.sprites = ['assets/boom1_green.png', 'assets/boom2_green.png', 'assets/boom3_green.png',
                            'assets/boom4_green.png', 'assets/boom5_green.png']
            
    #Cycle through explosion "spritesheet"
    def render_cycle(self):
        self.check_object_type()
        
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