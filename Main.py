import pygame
import sys
import time

from pygame.locals import *
from random import *

from Rocket import Rocket
from Field import Field
from InfoField import InfoField

from PiercingProjectile import PiercingProjectile


#View settings
screen_x = 900
screen_y = 700
info_x = 200

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()
 
#Player rocket settings 
rocket_width = 28
rocket_height = 84
rocket_speed = 10
rocket_spawn_x = (screen.get_width() - info_x) / 2 - rocket_width / 2
rocket_spawn_y = screen.get_height() - rocket_height
rocket_hp = 3

#Other settings
background_image = 'assets/background.png'
object_num = 10

#Initialize pygame
pygame.init()

#Creating objects
rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height, rocket_speed, rocket_hp, screen, info_x)
world = Field(object_num, screen, info_x)
info = InfoField(screen, screen_x, info_x, rocket, world)

#Background
background = pygame.transform.scale(pygame.image.load(background_image), (screen_x, screen_y)).convert()



###MAIN LOOP STARTS HERE###

#some variables
clock = pygame.time.Clock()
ticks = 20
finish = False
projectile_list = []

while not finish:
    
    #Checking for key commands and events
    move_command = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        
        #Exit
        if event.type == QUIT:
            finish = True
            sys.exit()

        if event.type == KEYDOWN:
            
            #Player rocket shoots projectile with Up and Space keys
            if event.key == K_UP or event.key == K_SPACE:
                projectile_list.append(rocket.shoot())

            #Game quits with Esc key
            if event.key == K_ESCAPE:
                finish = True
                time.sleep(1)
                pygame.display.quit()
                pygame.quit()
                
    #Player rocket moves left with Left key
    if move_command[K_LEFT]:
        rocket.move_left()
    
    #Player rocket moves right with Right key
    if move_command[K_RIGHT]:
        rocket.move_right()
    
    #Player rocket stays in place
    elif not move_command[K_LEFT] and not move_command[K_RIGHT]:
        rocket.stationary()
        
    screen.blit(background, (0, 0))    
             
    #Rendering the frame
    world.check_rocket_position(rocket)
    
    world.render()
    info.render()

    #Rendering projectiles
    for projectile in projectile_list[:]:
        projectile.render()
        
        #Projectile collision checks
        if world.projectile_collision_check(projectile):
            if type(projectile) != PiercingProjectile:
                #Only remove if projectile cannot pierce multiple objects
                projectile_list.remove(projectile)
            continue
            
        if projectile.rect.y < 0 - projectile.height:
            #Remove projectile when out of bounds
            projectile_list.remove(projectile)
            
    rocket.render()

    #Update display
    pygame.display.update()
    
    #Other Collision checks
    world.rocket_collision_check(rocket)
    world.powerup_collision_check(rocket)
     
    #Game speed control
    clock.tick(ticks)
