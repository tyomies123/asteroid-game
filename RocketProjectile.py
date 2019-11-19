import pygame

from pygame.locals import *
from AttackObject import AttackObject

class RocketProjectile(AttackObject):
    def __init__(self, width, height, speed, screen, owner_x, owner_y):
        AttackObject.__init__(self, width, height, "laser_green.png", speed, screen, owner_x, owner_y)

        