import pygame

from pygame.locals import *
from ProjectileObject import ProjectileObject

class BombProjectile(ProjectileObject):
    def __init__(self, width, height, speed, screen, owner_x, owner_y):
        ProjectileObject.__init__(self, width, height, "assets/bomb.png", speed, screen, owner_x, owner_y)
