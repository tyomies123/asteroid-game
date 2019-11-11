import pygame
import sys
import time
from pygame.locals import *
from random import randint

from Asteroid import Asteroid
from Stars import Stars
from Field import Field


class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(rocket_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.base = pygame.Rect(start_x, start_y - height, width, height)
        self.rocket_plain = pygame.sprite.RenderPlain(self)
    
    def movement(self, distance, screen, width):
        self.rect.move_ip(distance, 0)
        
        #Prevent the rocket to disappear off screen
        if self.rect.x < 0:
            self.rect.move_ip(10, 0)
            
        elif self.rect.x > screen.get_width() - width:
            self.rect.move_ip(-10, 0)
                  
##    def shoot(self):
##        pass
    
    def render(self, screen):
        self.rocket_plain.draw(screen)




class Doom():
    def __init__(self, asteroid_num, screen, asteroid_minmax):
        self.asteroids = []
        
        for index in range(0, asteroid_num):
            self.asteroids.append(Asteroid(asteroid_image, asteroid_minmax, screen))
     
        self.asteroid_plain = pygame.sprite.RenderPlain(self.asteroids)
        
    def collided(self, rocket_rect):
        list = self.asteroids
        return Asteroid.collision(list, rocket_rect)
        
    def render(self, asteroid_speed, screen):
        for index in self.asteroids:
            index.falling(asteroid_speed, screen)
            
        self.asteroid_plain.draw(screen)
        
    

#View settings
screen_x = 700
screen_y = 700

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()

#Rocket properties
rocket_width = 40
rocket_height = 70
rocket_spawn_x = screen_x / 2 - rocket_width / 2
rocket_spawn_y = screen_y - rocket_height
rocket_image = 'cohete_on_wf.png'

#Asteroid properties
asteroid_num = 4
asteroid_speed = 10
##asteroid_minmax = [25, 100]
##asteroid_size = randint(asteroid_minmax[0], asteroid_minmax[1])     #width = height
asteroid_image = '01murocrep512.jpg'

#Stars properties
stars_num = 10
stars_speed = 15
##stars_minmax = [20, 70]
##stars_size = randint(stars_minmax[0], stars_minmax[1])         #width = height

background_image = 'chikyuu_16_edge.png'
                                 

pygame.init()


rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height)  #creating the rocket
world = Field(14, screen)
##doom = Doom(asteroid_num, screen, asteroid_minmax)

clock = pygame.time.Clock()

#Background
background = pygame.transform.scale(pygame.image.load(background_image), (screen_x, screen_y)).convert()

finish = False

while not finish:
    
    #Exit
    for event in pygame.event.get():
        if event.type == QUIT:
            finish = True
            sys.exit()

    screen.blit(background, (0, 0))
    
    #Commands     
    command = pygame.key.get_pressed()
        
    if command[K_LEFT]:
        rocket.movement(-10, screen, rocket_width)   #Move left
  
    elif command[K_RIGHT]:
        rocket.movement(10, screen, rocket_width)    #Move right
        
    
    #Render frame
    rocket.render(screen)
    world.render(stars_speed, screen)
##    doom.render(asteroid_speed, screen)

    
    #Update display
    pygame.display.update()
    
    #Collisions
    if world.collided(rocket.rect):
        finish = True
        print("collided")
        time.sleep(2)
        sys.exit()
        

    #Game speed
    clock.tick(25)
