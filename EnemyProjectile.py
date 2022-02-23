import pygame

from pygame.locals import *
from ProjectileObject import ProjectileObject

#Projectiles used by enemy UFOs, can harm player rocket
class EnemyProjectile(ProjectileObject):
    def __init__(self, width, height, speed, screen, owner_x, owner_y):
        ProjectileObject.__init__(self, width, height, "assets/laser_red.png", speed, screen, owner_x, owner_y)

    #Positioning EnemyProjectile
    def start(self):
        self.image = pygame.transform.scale(self.proj_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.proj_plain = pygame.sprite.RenderPlain(self)
        
        self.rect.midbottom = self.owner_x
        self.rect.y = self.owner_y
    
    #Signal if hit rocket
    def rocket_collided(self, rocket):
        if self.rect.colliderect(rocket.rect):
            rocket.hit()
            return True
        return ProjectileObject.rocket_collided(self, rocket)
        
    def render(self):
        self.rect.move_ip(0, self.speed)
        self.proj_plain.draw(self.screen)