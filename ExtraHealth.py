import pygame

from random import *
from pygame.locals import *
from PowerUp import PowerUp

class ExtraHealth(PowerUp):
    def __init__(self, size, speed, screen):
        PowerUp.__init__(self, "extra_health.png", size, speed, screen)
        
    def collided(self, rocket):
        if self.rect.colliderect(rocket.rect):
            rocket.powerup_pickup("ExtraHealth")
            return True