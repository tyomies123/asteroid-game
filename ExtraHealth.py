import pygame
import time

from random import *
from pygame.locals import *
from PowerUp import PowerUp

class ExtraHealth(PowerUp):
    def __init__(self, width, height, speed, screen):
        PowerUp.__init__(self, "extra_health.png", width, height, speed, screen)
        
    def function(self, hp):
        #Max hp
        if hp == 6:
            print("Max HP: 6")
            time.sleep(0.33)
            return hp
        #+1 hp
        else:
            print("+1 HP! HP left: ", hp + 1)
            time.sleep(0.33)
            return hp + 1