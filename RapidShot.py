import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

#RapidShot powerup pickup (increased projectile speed)
class RapidShot(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "assets/rapid_shot.png", width, height, speed, screen, info_x)
        
    def function(self, powerup_projectiles):
        
        #Add 5 ammo
        for i in range(5):
            powerup_projectiles.append("RapidProjectile")
        
        #Remove additional ammo if over max
        while len(powerup_projectiles) > 10:
            powerup_projectiles.remove("RapidProjectile")
            
        return powerup_projectiles