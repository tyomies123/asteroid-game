import pygame

from random import *
from pygame.locals import *
from PowerUp import PowerUp

class ExtraHealth(PowerUp):
    def __init__(self, powerup_image, size, speed, screen):
        PowerUp.__init__(self, "extra_health.png", size, speed, screen)