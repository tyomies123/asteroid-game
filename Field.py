import pygame
import time

from random import *
from pygame.locals import *

#Other objects
from Asteroid import Asteroid
from Star import Star

#Powerups
from ExtraHealth import ExtraHealth
from PiercingShot import PiercingShot

#Enemy objects
from FlyingSaucer import FlyingSaucer
from EnemyProjectile import EnemyProjectile

from Dice import Dice

class FieldObjectFactory():
    def create_FallingObject(self, typ, object_minmax, object_speed, screen):
        
        if typ == "Star":
            return Star(object_minmax, object_speed, screen)
        
        if typ == "Asteroid":
            return Asteroid(object_minmax, object_speed, screen)
        
    def create_PowerUp(self, typ, powerup_size, powerup_speed, screen):
        
        if typ == "ExtraHealth":
            return ExtraHealth(powerup_size, powerup_speed, screen)
        
##        if typ == "PiercingShot":
##            return PiercingShot(powerup_size, powerup_speed, screen)
        
    def create_Enemy(self, typ, start_x, start_y, width, height, speed, hp, screen):
        
        if typ == "FlyingSaucer":
            return FlyingSaucer(start_x, start_y, width, height, speed, hp, screen)
    
class Field():
    def __init__(self, object_num, screen):
        self.objects = []
        self.powerups = []
        self.enemies = []
        self.enemy_projectiles = []
        
        self.screen = screen
        
        self.factory = FieldObjectFactory()
        
        asteroid_count = 0
        
        for n in range(0, object_num):
            
            #Spawn asteroid + star
            if asteroid_count < 4:
                self.objects.append(self.factory.create_FallingObject("Asteroid", [25, 100], randrange(15, 31, 5), self.screen))
                self.objects.append(self.factory.create_FallingObject("Star", [25, 75], randrange(30, 51, 5), self.screen))
                asteroid_count = asteroid_count + 1
            
            #Spawn star
            else:
                self.objects.append(self.factory.create_FallingObject("Star", [25, 75], randrange(20, 51, 5), self.screen))
        
        #Spawn enemy
        self.enemies.append(self.factory.create_Enemy("FlyingSaucer", randrange(0, screen.get_width(), 10), 0, 56, 56, 10, 3, self.screen))
        
        self.objects_plain = pygame.sprite.RenderPlain(self.objects)
        
        
    def render(self):
        #Render asteroids and stars
        for object in self.objects:
            object.fallmove()
            
        self.objects_plain.draw(self.screen)
        
        #Render powerups
        if len(self.powerups) > 0:
            for powerup in self.powerups:
                powerup.fallmove()
                
                if powerup.rect.y > self.screen.get_height():
                    self.powerups.remove(powerup)
                
            powerups_plain = pygame.sprite.RenderPlain(self.powerups)
            powerups_plain.draw(self.screen)
        
        #Render enemies
        if len(self.enemies) > 0:
            for enemy in self.enemies:
                enemy.render()
                
        #Render enemy projectiles
        enemy_shoot_chance = Dice()
        dice_roll = enemy_shoot_chance.roll()
        self.enemy_shoot(dice_roll)
                
        if len(self.enemy_projectiles) > 0:
            for enemy_projectile in self.enemy_projectiles:
                enemy_projectile.render()
                
                if enemy_projectile.rect.y > self.screen.get_height():
                    self.enemy_projectiles.remove(enemy_projectile)
    
    #Rocket collisions
    def rocket_collision_check(self, rocket):
        for object in self.objects:
            if object.rocket_collided(rocket):
                object.reset()
                
        for enemy_projectile in self.enemy_projectiles:
            if enemy_projectile.rocket_collided(rocket):
                self.enemy_projectiles.remove(enemy_projectile)
    
    #Projectile collisions and powerup spawn
    def projectile_collision_check(self, projectile):
        
        #Projectile collided with asteroid
        for object in self.objects:
            if object.projectile_collided(projectile):
                object.reset()
                powerup_chance = Dice()
                dice_roll = powerup_chance.roll()
                
                #Spawn ExtraHealth
                if dice_roll <= 10:
                    self.powerups.append(self.factory.create_PowerUp("ExtraHealth", 25, 10, self.screen))
                
                #Spawn PiercingShot
##                elif dice_roll > 10 and dice_roll <= 20:
##                    self.powerups.append(self.factory.create_PowerUp("PiercingShot", 50, 10, self.screen))
                    
                return True
        
        #Projectile collided with enemy  
        for enemy in self.enemies[:]:
            if enemy.projectile_collided(projectile):
                enemy_hp = enemy.hit()
                time.sleep(0.33)
                
                if enemy_hp <= 0:
                    self.enemies.remove(enemy)
                
                return True
    
    #Powerup collision
    def powerup_collision_check(self, rocket):
        for powerup in self.powerups:
            if powerup.collided(rocket):
                rocket.powerup_pickup(powerup)
                self.powerups.remove(powerup)
            
            #Enemy projectile can destroy powerup
            for enemy_projectile in self.enemy_projectiles:
                if powerup.collided(enemy_projectile):
                    self.powerups.remove(powerup)
                    self.enemy_projectiles.remove(enemy_projectile)
    
    #Check if enemy can shoot projectile
    def enemy_shoot(self, dice_roll):
        if dice_roll <= 5:
            for enemy in self.enemies:
                self.enemy_projectiles.append(enemy.shoot())
        
        #Enemy always targets powerups
        for powerup in self.powerups:
            for enemy in self.enemies:
                if enemy.rect.center[0] >= powerup.rect.left and enemy.rect.center[0] <= powerup.rect.right:
                    self.enemy_projectiles.append(enemy.shoot())
        
##End