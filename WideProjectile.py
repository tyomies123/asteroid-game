import pygame

from pygame.locals import *
from ProjectileObject import ProjectileObject

class WideProjectile(ProjectileObject):
    def __init__(self, width, height, speed, screen, owner_x, owner_y):
        ProjectileObject.__init__(self, width, height, "laser_yellow.png", speed, screen, owner_x, owner_y)

        