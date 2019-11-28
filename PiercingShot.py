import pygame

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

class PiercingShot(PowerUp):
    def __init__(self, size, speed, screen):
        PowerUp.__init__(self, "piercing_shot.png", size, speed, screen)
        
    def function(self):
        pass