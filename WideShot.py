import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp
from PiercingProjectile import PiercingProjectile

class WideShot(PowerUp):
    def __init__(self, width, height, speed, screen):
        PowerUp.__init__(self, "wide_shot.png", width, height, speed, screen)
    
    def function(self):
        return_list = []
        for i in range(5):
            return_list.append("WideProjectile")
            
        time.sleep(0.33)
        print("Wide shots left: ", len(return_list))
        
        return return_list