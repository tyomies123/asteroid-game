import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

class PiercingShot(PowerUp):
    def __init__(self, width, height, speed, screen):
        PowerUp.__init__(self, "piercing_shot.png", width, height, speed, screen)
        
    def function(self):
        return_list = []
        for i in range(5):
            return_list.append("PiercingProjectile")
            
        time.sleep(0.33)
        return return_list