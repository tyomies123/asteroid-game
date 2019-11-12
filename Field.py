import pygame
from random import *
from pygame.locals import *
from Asteroid import Asteroid
from Stars import Stars

class FieldObjectFactory():
    def create_object(self, typ, object_minmax, screen):
        targetclass = typ.capitalize()
        
        if targetclass == "Stars":
            return Stars(object_minmax, screen)
        
        if targetclass == "Asteroid":
            return Asteroid(object_minmax, screen)
    
class Field():
    def __init__(self, object_num, screen):
        self.objects = []
        self.object_instances = []
        factory = FieldObjectFactory()
        
        for n in range(0, object_num):
            choice = randint(0, 1)
            
            if choice == 0:
                if self.object_instances.count("Asteroid") < 4:
                    self.objects.append(factory.create_object("Asteroid", [25, 100], screen))
                    self.object_instances.append("Asteroid")
                else:
                    self.objects.append(factory.create_object("Stars", [20, 70], screen))
                    self.object_instances.append("Star")

            elif choice == 1:
                self.objects.append(factory.create_object("Stars", [20, 70], screen))
                self.object_instances.append("Star")
  
        self.field_plain = pygame.sprite.RenderPlain(self.objects)
        
    def render(self, screen):
        for index in self.objects:
            speed = randrange(10, 25, 5)
            index.fallmove(speed, screen)
            
        self.field_plain.draw(screen)
    
    def collided(self, rocket_rect):
        for object in self.objects:
            if object.collided(rocket_rect):
                return True