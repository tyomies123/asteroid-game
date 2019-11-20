import pygame
import sys
import time

from pygame.locals import *
from random import *

from Rocket import Rocket
##from Asteroid import Asteroid
##from Star import Star
##from RocketProjectile import RocketProjectile
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
projectile_list = []


while not finish:
    
    #Commands and events
    move_command = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        
        #Exit
        if event.type == QUIT:
            finish = True
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                projectile_list.append(rocket.shoot())    #Create projectile
                
    
    if move_command[K_LEFT]:
        rocket.movement(-10)    #Move left
  
    if move_command[K_RIGHT]:
        rocket.movement(10)     #Move right
    
    screen.blit(background, (0, 0))    
             
    #Render frame
    world.render()
    for projectile in projectile_list:
        projectile.render()
        if world.projectile_collision_check(projectile):
            projectile_list.remove(projectile)
    rocket.render()

    #Update display
    pygame.display.update()
    
    #Collision check
    world.rocket_collision_check(rocket)
    
    #Game speed
    clock.tick(ticks)
