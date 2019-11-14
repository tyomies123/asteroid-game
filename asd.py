import pygame
import sys
import time
from pygame.locals import *
from random import *

from Asteroid import Asteroid
from Star import Star
from Field import Field


class Rocket(pygame.sprite.Sprite):  
    def __init__(self, start_x, start_y, width, height, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(rocket_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.base = pygame.Rect(start_x, start_y - height, width, height)
        self.rocket_plain = pygame.sprite.RenderPlain(self)
        
        self.screen = screen
    
    def movement(self, distance, width):
        self.rect.move_ip(distance, 0)
        
        #Prevent the rocket from going offscreen
        if self.rect.x < 0:
            self.rect.move_ip(10, 0)
            
        elif self.rect.x > self.screen.get_width() - width:
            self.rect.move_ip(-10, 0)
    
    def render(self):
        self.rocket_plain.draw(self.screen)


#View settings
screen_x = 700
screen_y = 700

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()

#Rocket settings
rocket_width = 40
rocket_height = 70
rocket_spawn_x = screen_x / 2 - rocket_width / 2
rocket_spawn_y = screen_y - rocket_height
rocket_image = 'cohete_on_wf.png'
rocket_hp = 3

#NPC settings
asteroid_image = '01murocrep512.jpg'
background_image = 'chikyuu_16_edge.png'
object_num = 10


pygame.init()


#Creating objects
rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height, screen)  #creating the rocket
world = Field(object_num, screen)

#Background
background = pygame.transform.scale(pygame.image.load(background_image), (screen_x, screen_y)).convert()

clock = pygame.time.Clock()

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
        rocket.movement(-10, rocket_width)   #Move left
  
    elif command[K_RIGHT]:
        rocket.movement(10, rocket_width)    #Move right
          
    #Render frame
    world.render()
    rocket.render()

    #Update display
    pygame.display.update()
    
    #Collisions
    if world.collided(rocket.rect):
        
        #Game over
        time.sleep(1)
        rocket_hp = rocket_hp - 1
        print("Collided! HP: ", rocket_hp)
        
        if rocket_hp == 0:
            finish = True
            print("Game Over!")
            time.sleep(2)
            sys.exit()
        
            
    #Game speed
    clock.tick(20)
