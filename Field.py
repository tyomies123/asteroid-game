import pygame
import time

from random import *
from pygame.locals import *

from Asteroid import Asteroid
from Star import Star

from ExtraHealth import ExtraHealth
from PiercingShot import PiercingShot

from Dice import Dice

class FieldObjectFactory():
    def create_FallingObject(self, typ, object_minmax, object_speed, screen):
        
        if typ == "Star":
            return Star(object_minmax, object_speed, screen)
        
        if typ == "Asteroid":
            return Asteroid(object_minmax, object_speed, screen)
        
    def create_PowerUp(self, typ, powerup_size, powerup_speed, screen):
        
        if typ == "ExtraHealth":
            return ExtraHealth(powerup_size, powerup_speed, screen)
        
##        if typ == "PiercingShot":
##            return PiercingShot(powerup_size, powerup_speed, screen)
    
class Field():
    def __init__(self, object_num, screen):
        self.objects = []
        self.powerups = []
        self.screen = screen
        
        self.factory = FieldObjectFactory()
        
        asteroid_count = 0
        
        for n in range(0, object_num):
            
            #Spawn Asteroid + Star
            if asteroid_count < 4:
                self.objects.append(self.factory.create_FallingObject("Asteroid", [25, 100], randrange(15, 31, 5), self.screen))
                self.objects.append(self.factory.create_FallingObject("Star", [25, 75], randrange(30, 51, 5), self.screen))
                asteroid_count = asteroid_count + 1
            
            #Spawn Star
            else:
                self.objects.append(self.factory.create_FallingObject("Star", [25, 75], randrange(20, 51, 5), self.screen))
        
        self.objects_plain = pygame.sprite.RenderPlain(self.objects)
        
        
    def render(self):
        for object in self.objects:
            object.fallmove()
        
        if len(self.powerups) > 0:
            for powerup in self.powerups:
                powerup.fallmove()
            powerups_plain = pygame.sprite.RenderPlain(self.powerups)
            powerups_plain.draw(self.screen)

            
        self.objects_plain.draw(self.screen)
    
    def rocket_collision_check(self, rocket):
        for object in self.objects:
            if object.rocket_collided(rocket):
                object.reset()
                
    def projectile_collision_check(self, projectile):
        for object in self.objects:
            if object.projectile_collided(projectile):
                object.reset()
                chance = Dice()
                dice_roll = chance.roll()
                
                #Spawn ExtraHealth
                if dice_roll <= 10:
                    self.powerups.append(self.factory.create_PowerUp("ExtraHealth", 25, 15, self.screen))
                
                #Spawn PiercingShot
##                elif dice_roll > 10 and dice_roll <= 20:
##                    self.powerups.append(self.factory.create_PowerUp("PiercingShot", 50, 15, self.screen))
                    
                return True
    
    def powerup_collision_check(self, rocket):
        for powerup in self.powerups:
            if powerup.collided(rocket):
                rocket.powerup_pickup(powerup)
                self.powerups.remove(powerup)
        
##End