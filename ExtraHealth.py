import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp

#ExtraHealth powerup pickup (self explanatory)
class ExtraHealth(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "assets/extra_health.png", width, height, speed, screen, info_x)
        
    def function(self, hp):
        #Cannot pick up if already at max hp
        if hp == 6:
            print("Max HP: 6")
            return hp
        
        #Add 1 hp to player rocket
        else:
            print("+1 HP! HP left: ", hp + 1)
            return hp + 1