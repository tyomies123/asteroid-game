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
    
    def check_object_type(self):
        if type(self.object) is PiercingProjectile or type(self.object) is PiercingShot:
            self.sprites = ['boom1_blue.png', 'boom2_blue.png', 'boom3_blue.png',
                            'boom4_blue.png', 'boom5_blue.png']
            
        elif type(self.object) is WideProjectile or type(self.object) is WideShot:
            self.sprites = ['boom1_yellow.png', 'boom2_yellow.png', 'boom3_yellow.png',
                            'boom4_yellow.png', 'boom5_yellow.png']
        
        elif type(self.object) is RapidProjectile or type(self.object) is RapidShot:
            self.sprites = ['boom1_purple.png', 'boom2_purple.png', 'boom3_purple.png',
                            'boom4_purple.png', 'boom5_purple.png']
            
        elif type(self.object) is BombProjectile or type(self.object) is BombShot:
            self.sprites = ['boom1_orange.png', 'boom2_orange.png', 'boom3_orange.png',
                            'boom4_orange.png', 'boom5_orange.png']
        
        elif type(self.object) is EnemyProjectile or type(self.object) is ExtraHealth:
            self.sprites = ['boom1_red.png', 'boom2_red.png', 'boom3_red.png',
                            'boom4_red.png', 'boom5_red.png']
            
        elif type(self.object) is Asteroid:
            self.sprites = ['boom1_asteroid.png', 'boom2_asteroid.png', 'boom3_asteroid.png',
                            'boom4_asteroid.png', 'boom5_asteroid.png']
        else:
            self.sprites = ['boom1_green.png', 'boom2_green.png', 'boom3_green.png',
                            'boom4_green.png', 'boom5_green.png']
            
            
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