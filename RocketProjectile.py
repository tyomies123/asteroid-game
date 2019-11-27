import pygame

from pygame.locals import *
from ProjectileObject import ProjectileObject

class RocketProjectile(ProjectileObject):
    def __init__(self, width, height, speed, screen, owner_x, owner_y):
        ProjectileObject.__init__(self, width, height, "laser_green.png", speed, screen, owner_x, owner_y)

        