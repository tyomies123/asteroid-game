import pygame
from pygame.locals import *

#Generic projectile template
class ProjectileObject(pygame.sprite.Sprite):
    def __init__(self, width, height, proj_image, speed, screen, owner_x, owner_y):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.screen = screen   
        self.owner_x = owner_x
        self.owner_y = owner_y
        
        self.image_file = proj_image
        self.proj_image = pygame.image.load(self.image_file)
        
        self.start()

    #Move projectile upward    
    def start(self):
        self.image = pygame.transform.scale(self.proj_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.proj_plain = pygame.sprite.RenderPlain(self)
        
        self.rect.midbottom = self.owner_x
        self.rect.y = self.screen.get_height() - self.owner_y

    #Signal if collided with rocket (only relevant in EnemyProjectiles)    
    def rocket_collided(self, rocket):
        return False
    
    def render(self):
        self.rect.move_ip(0, 0 - self.speed)
        self.proj_plain.draw(self.screen)