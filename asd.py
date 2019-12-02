import pygame
import sys
import time

from pygame.locals import *
from random import *

from Rocket import Rocket
from Field import Field

from PiercingProjectile import PiercingProjectile


#View settings
screen_x = 700
screen_y = 700

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()

#Rocket settings
rocket_width = 28
rocket_height = 84
rocket_speed = 10
rocket_spawn_x = screen.get_width() / 2 - rocket_width / 2
rocket_spawn_y = screen.get_height() - rocket_height
rocket_hp = 3

#NPC settings
background_image = 'background.png'
object_num = 10


pygame.init()


#Creating objects
rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height, rocket_speed, rocket_hp, screen)
world = Field(object_num, screen)

#Background
background = pygame.transform.scale(pygame.image.load(background_image), (screen_x, screen_y)).convert()

#Main loop and variables
clock = pygame.time.Clock()
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
        
        #Create projectile
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                projectile_list.append(rocket.shoot())
                
    
    if move_command[K_LEFT]:
        rocket.move_left()
  
    if move_command[K_RIGHT]:
        rocket.move_right()
    
    elif not move_command[K_LEFT] and not move_command[K_RIGHT]:
        rocket.stationary()
        
    screen.blit(background, (0, 0))    
             
    #Rendering the frame
    world.check_rocket_position(rocket)
    
    world.render()

    for projectile in projectile_list[:]:
        projectile.render()
        
        if world.projectile_collision_check(projectile):
            if type(projectile) is not PiercingProjectile:
                projectile_list.remove(projectile)
            continue
            
        if projectile.rect.y < 0:
            projectile_list.remove(projectile)
            
    rocket.render()

    #Update display
    pygame.display.update()
    
    #Collision checks
    world.rocket_collision_check(rocket)
    world.powerup_collision_check(rocket)
    
    #Game speed
    clock.tick(20)

##End