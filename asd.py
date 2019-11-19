import pygame
import sys
import time

from pygame.locals import *
from random import *

from Rocket import Rocket
from Asteroid import Asteroid
from Star import Star
from RocketProjectile import RocketProjectile
from Field import Field


#View settings
screen_x = 700
screen_y = 700

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()

#Rocket settings
rocket_width = 40
rocket_height = 70
rocket_life = 3
rocket_spawn_x = screen.get_width() / 2 - rocket_width / 2
rocket_spawn_y = screen.get_height() - rocket_height
rocket_hp = 3

#Rocket projectile
##projectile_width = 3
##projectile_height = 70
##projectile_speed = 30

#NPC settings
background_image = 'background.png'
object_num = 10


pygame.init()


#Creating objects
rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height, rocket_life, screen)  #creating the rocket
world = Field(object_num, screen)

#Background
background = pygame.transform.scale(pygame.image.load(background_image), (screen_x, screen_y)).convert()

#Main loop
clock = pygame.time.Clock()
ticks = 20
finish = False
shoot = False
projectile_list = []



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
        rocket.movement(-10)      #Move left
  
    elif command[K_RIGHT]:
        rocket.movement(10)       #Move right
        
    if command[K_UP]:
        shoot = True
        projectile_list.append(rocket.shoot())    #Create projectile
          
    #Render frame
    world.render()
    if shoot:
        for projectile in projectile_list:
            rocket.projectile_render(projectile)
    rocket.render()

    #Update display
    pygame.display.update()
    
    #Collision check
    world.collision_check(rocket)
    
    #Game speed
    clock.tick(ticks)
