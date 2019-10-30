import pygame
import sys
from pygame.locals import *
from random import randint



class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(rocket_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.base = pygame.Rect(start_x, start_y - height, width, height)
    
    def move(self, command):
        if command == [K_LEFT]:
            self.rect.move(-4, 0)
        elif command == [K_RIGHT]:
            self.rect.move(4, 0)
            
    def shoot(self):
        pass
    
    def status(self):
        #rocket health, weapon, score etc
        pass

class World():
    def __init__(self):
        pass
    
    def move(self):
        pass
               
    def powerup(self):
        pass
    
    def hp(self):
        pass
    
    def update(self, screen):
        pass


class Asteroid():
    def __init__(self):
        pass
    
    def size(self, size):
        pass
    
    def move(self):
        pass
    
    def collided(self, rocket_rect):
        pass
    
    def destroyed(self):
        pass
    
    def reset(self):
        pass
    
    def update(self, screen):
        pass




#Settings
screen_x = 700
screen_y = 700
rocket_width = 40
rocket_height = 70
rocket_spawn_x = screen_x / 2 - rocket_width / 2
rocket_spawn_y = screen_y - rocket_height
rocket_image = 'cohete_on_wf.png'
background_image = 'Space001.png'

pygame.init()

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()


rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height)  #creating the rocket
rocket_plain = pygame.sprite.RenderPlain(rocket)



clock = pygame.time.Clock()
command = pygame.key.get_pressed()

#Background
background = pygame.transform.scale(pygame.image.load(
            background_image), (screen_x, screen_y)).convert()

finish = False

while not finish:
    
    #Exit
    for event in pygame.event.get():
        if event.type == QUIT:
            finish = True
            sys.exit()
    
    #Commands
    if command[K_LEFT] or command[K_RIGHT]:
        Rocket.move(command)           #Move left or right
        
    if command[K_SPACE]:
        Rocket.shoot()                 #Shoot
        
    if command[K_x]:
        World.powerup()                #Use power-up
    
    #Render frame
    screen.blit(background, (0, 0))
    rocket_plain.draw(screen)
    
    #Update display
    pygame.display.update()

    #Game speed
    clock.tick(20)
