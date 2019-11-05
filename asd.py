import pygame
import sys
from pygame.locals import *
from random import randint
from Asteroid import Asteroid



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
                  
    def shoot(self):
        pass
    
    def render(self, screen):
        self.rocket_plain.draw(screen)


class World():
    def __init__(self, stars_num, screen):
        self.stars = []
        global stars_size
        
        for i in range(0, stars_num):
            self.stars.append(...)
            stars_size = randint(..., ...)
        
        self.stars_plain = pygame.sprite.RenderPlain(self.stars)
        
    def render(self, stars_speed, screen, stars_size):
        for i in self.stars:
            i
            
        self.stars_plain.draw(screen)


class Doom():
    def __init__(self, asteroid_num, screen):
        self.asteroids = []
        global asteroid_size
        
        for i in range(0, asteroid_num):
            self.asteroids.append(Asteroid(asteroid_image, asteroid_size, screen))
            asteroid_size = randint(25, 100)
        
        self.asteroid_plain = pygame.sprite.RenderPlain(self.asteroids)
        
    def render(self, asteroid_speed, screen, asteroid_size):
        for i in self.asteroids:
            i.falling(asteroid_speed, screen, asteroid_size)
            
        self.asteroid_plain.draw(screen)
    

    



#Settings
screen_x = 700
screen_y = 700

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()

rocket_width = 40
rocket_height = 70
rocket_spawn_x = screen_x / 2 - rocket_width / 2
rocket_spawn_y = screen_y - rocket_height
rocket_image = 'cohete_on_wf.png'

asteroid_num = 4
asteroid_speed = 10
asteroid_size = randint(25, 100)    #width = height
asteroid_image = '01murocrep512.jpg'

##stars_num
##stars_speed
##stars_size
##stars_image

background_image = 'chikyuu_16_edge.png'
                                 

pygame.init()

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()


rocket = Rocket(rocket_spawn_x, rocket_spawn_y, rocket_width, rocket_height)  #creating the rocket
world = World(stars_num, screen)
doom = Doom(asteroid_num, screen)

clock = pygame.time.Clock()

#Background
background = pygame.transform.scale(pygame.image.load(
            background_image), (screen_x, screen_y)).convert()

finish = False

rocket.rocket_plain.draw(screen)

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
    world.render(stars_speed, screen, stars_size)
    doom.render(asteroid_speed, screen, asteroid_size)
    
    #Update display
    pygame.display.update()

    #Game speed
    clock.tick(25)
