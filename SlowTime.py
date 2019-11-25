import pygame

from random import *
from pygame.locals import *
from PowerUp import PowerUp

class SlowTime(PowerUp):
    def __init__(self, size, speed, screen):
        PowerUp.__init__(self, "slow_time.png", size, speed, screen)
        
    def collided(self, rocket):
        if self.rect.colliderect(rocket.rect):
            rocket.powerup_pickup("SlowTime")
            return True