import pygame

from pygame.locals import *
from ProjectileObject import ProjectileObject

class EnemyProjectile(ProjectileObject):
    def __init__(self, width, height, speed, screen, owner_x, owner_y):
        ProjectileObject.__init__(self, width, height, "laser_red.png", speed, screen, owner_x, owner_y)

    def start(self):
        self.image = pygame.transform.scale(self.proj_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.proj_plain = pygame.sprite.RenderPlain(self)
        
        self.rect.x = self.owner_x - (self.width / 2)
        self.rect.y = self.owner_y
        
    def rocket_collided(self, rocket):
        if self.rect.colliderect(rocket.rect):
            rocket.hit()
            return True
        return ProjectileObject.rocket_collided(self, rocket)
        
    def render(self):
        self.rect.move_ip(0, self.speed)
        self.proj_plain.draw(self.screen)