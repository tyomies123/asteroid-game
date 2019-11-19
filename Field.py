import pygame
import time

from random import *
from pygame.locals import *
from Asteroid import Asteroid
from Star import Star

class FieldObjectFactory():
    def create_FallingObject(self, typ, object_minmax, object_speed, screen):
        targetclass = typ.capitalize()
        
        if targetclass == "Star":
            return Star(object_minmax, object_speed, screen)
        
        if targetclass == "Asteroid":
            return Asteroid(object_minmax, object_speed, screen)
    
class Field():
    def __init__(self, object_num, screen):
        self.objects = []
        self.screen = screen
        
        factory = FieldObjectFactory()
        
        asteroid_count = 0
        
        for n in range(0, object_num):
            choice = randint(0, 1)
            
            if choice == 0:    #Asteroid + star
                if asteroid_count < 4:
                    self.objects.append(factory.create_FallingObject("Asteroid", [25, 100], randrange(15, 31, 5), screen))
                    self.objects.append(factory.create_FallingObject("Star", [25, 75], randrange(30, 51, 5), screen))
                    asteroid_count = asteroid_count + 1
                    
                else:
                    self.objects.append(factory.create_FallingObject("Star", [25, 75], randrange(20, 51, 5), screen))
                
            elif choice == 1:  #Star
                self.objects.append(factory.create_FallingObject("Star", [25, 75], randrange(20, 51, 5), screen))

        self.field_plain = pygame.sprite.RenderPlain(self.objects)
        
    def render(self):
        for object in self.objects:
            object.fallmove()
            
        self.field_plain.draw(self.screen)
    
    def collision_check(self, rocket):
        for object in self.objects:
            if object.collided(rocket):
                object.reset()
                
