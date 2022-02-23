import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from BombProjectile import BombProjectile

#BombShot powerup pickup (big explosion, multihit)
class BombShot(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "assets/bomb_shot.png", width, height, speed, screen, info_x)
        
    def function(self, powerup_projectiles):

        #Add 5 ammo
        for i in range(5):
            powerup_projectiles.append("BombProjectile")

        #Remove additional ammo if over max
        while len(powerup_projectiles) > 10:
            powerup_projectiles.remove("BombProjectile")
            
        return powerup_projectiles
