import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

class RapidShot(PowerUp):
    def __init__(self, width, height, speed, screen, info_x):
        PowerUp.__init__(self, "rapid_shot.png", width, height, speed, screen, info_x)
        
    def function(self):
        return_list = []
        for i in range(5):
            return_list.append("RapidProjectile")
            
        return return_list