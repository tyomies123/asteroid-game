import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from BombProjectile import BombProjectile

class BombShot(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "bomb_shot.png", width, height, speed, screen, info_x)
        
    def function(self, powerup_projectiles):
        
        for i in range(5):
            powerup_projectiles.append("BombProjectile")
            
        while len(powerup_projectiles) > 10:
            powerup_projectiles.remove("BombProjectile")
            
        return powerup_projectiles