import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

#PiercingShot powerup pickup (projectiles pierce multiple objects)
class PiercingShot(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "assets/piercing_shot.png", width, height, speed, screen, info_x)
        
    def function(self, powerup_projectiles):
        
        #Add 5 ammo
        for i in range(5):
            powerup_projectiles.append("PiercingProjectile")

        #Remove additional ammo if over max
        while len(powerup_projectiles) > 10:
            powerup_projectiles.remove("PiercingProjectile")
            
        return powerup_projectiles