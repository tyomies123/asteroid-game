import pygame
from random import randint
from pygame.locals import *
from Asteroid import Asteroid
from Stars import Stars

class FieldObjectFactory():
    def create_object(self, typ, screen, object_minmax):
        targetclass = typ.capitalize()
        if targetclass == "Stars":
            return Stars(object_minmax, screen)
        if targetclass == "Asteroid":
            return Asteroid(object_minmax, screen)
    
class Field():
    def __init__(self, object_num, screen):
        self.objects = []
        factory = FieldObjectFactory()
        
        for n in range(0, object_num):
            choice = randint(0, 1)
            if choice == 1:
                self.objects.append(factory.create_object("Stars", screen, [20, 70]))
            else:
                self.objects.append(factory.create_object("Asteroid", screen, [25, 100]))
            
        self.field_plain = pygame.sprite.RenderPlain(self.objects)
        
    def render(self, object_speed, screen):
        for index in self.objects:
            index.fallmove(object_speed, screen)
            
        self.field_plain.draw(screen)
    
    def collided(self, rocket_rect):
        for object in self.objects:
            if object.collided(rocket_rect):
                return True