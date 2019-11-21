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
        
    def create_PowerUp(self, typ, powerup_size, powerup_speed, screen):
        targetclass = typ.capitalize()
        
        if targetclass == "Extra Health":
            return ExtraHealth(powerup_size, powerup_speed, screen)
    
class Field():
    def __init__(self, object_num, screen):
        self.objects = []
        self.powerups = []
        self.screen = screen
        
        factory = FieldObjectFactory()
        
        asteroid_count = 0
##        wait = 0
        
        for n in range(0, object_num):
            
            #Spawn Asteroid + Star
            if asteroid_count < 4:
                self.objects.append(factory.create_FallingObject("Asteroid", [25, 100], randrange(15, 31, 5), screen))
                self.objects.append(factory.create_FallingObject("Star", [25, 75], randrange(30, 51, 5), screen))
                asteroid_count = asteroid_count + 1
            
            #Spawn Star
            else:
                self.objects.append(factory.create_FallingObject("Star", [25, 75], randrange(20, 51, 5), screen))
        
##        chance = randint(1, 25)
##            
##            #Spawn Extra Health
##            if chance <= 5:
##                self.powerups.append(factory.create_PowerUp("Extra Health", 50, 25, screen))
##                while wait < 200:
##                    wait = wait + 1
##            
##            wait = 0

        self.field_plain = pygame.sprite.RenderPlain(self.objects)
        
        
        
    def render(self):
        for object in self.objects:
            object.fallmove()
            
        self.field_plain.draw(self.screen)
    
    def rocket_collision_check(self, rocket):
        for object in self.objects:
            if object.rocket_collided(rocket):
                object.reset()
                
    def projectile_collision_check(self, projectile):
        for object in self.objects:
            if object.projectile_collided(projectile):
                object.reset()
                return True