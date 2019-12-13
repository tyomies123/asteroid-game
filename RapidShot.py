import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

class RapidShot(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "rapid_shot.png", width, height, speed, screen, info_x)
        
    def function(self, powerup_projectiles):
        
        for i in range(5):
            powerup_projectiles.append("RapidProjectile")
            
        while len(powerup_projectiles) > 10:
            powerup_projectiles.remove("RapidProjectile")
            
        return powerup_projectiles