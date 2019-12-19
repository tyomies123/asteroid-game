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
from WideShot import WideShot
from RapidShot import RapidShot

#Enemy objects
from Ufo import Ufo
from EnemyProjectile import EnemyProjectile

from Explosion import Explosion
from Dice import Dice


class FieldObjectFactory():
    def create_FallingObject(self, typ, minmax, speed, screen, info_x):
        
        if typ == "Star":
            return Star(minmax, speed, screen, info_x)
        
        if typ == "Asteroid":
            return Asteroid(minmax, speed, screen, info_x)
    
    
    def create_PowerUp(self, typ, width, height, speed, screen, info_x):
        
        if typ == "ExtraHealth":
            return ExtraHealth(width, height, speed, screen, info_x)
        
        if typ == "PiercingShot":
            return PiercingShot(width, height, speed, screen, info_x)
        
        if typ == "WideShot":
            return WideShot(width, height, speed, screen, info_x)
        
        if typ == "RapidShot":
            return RapidShot(width, height, speed, screen, info_x)
    
    
    def create_Enemy(self, typ, start_x, start_y, size, speed, hp, screen, info_x):
        
        if typ == "Ufo":
            return Ufo(start_x, start_y, size, speed, hp, screen, info_x)


class Field():
    def __init__(self, object_num, screen, info_x):
        self.objects = []
        self.powerups = []
        self.enemies = []
        self.enemy_projectiles = []
        self.explosions = []
        
        self.screen = screen
        self.info_x = info_x
        self.factory = FieldObjectFactory()
        
        #Other variables
        self.score = 0
        self.counter = 20
        self.ufo_threshold = 20
        self.ufo_destroyed_score = 0
        self.n = 1
                
        asteroid_count = 0
        
        for n in range(0, object_num):
            
            #Spawn asteroid + star
            if asteroid_count < 4:
                self.objects.append(self.factory.create_FallingObject("Asteroid", [25, 100], randrange(15, 30, 5),
                                                                      self.screen, self.info_x))

                self.objects.append(self.factory.create_FallingObject("Star", [5, 15], randrange(20, 50, 5),
                                                                      self.screen, self.info_x))
                asteroid_count = asteroid_count + 1
            
            #Spawn star
            else:
                self.objects.append(self.factory.create_FallingObject("Star", [5, 15], randrange(20, 50, 5),
                                                                      self.screen, self.info_x))
                
##        self.enemies.append(self.factory.create_Enemy("Ufo", randrange(0, self.screen.get_width(), 10),
##                                                              0, 56, 10, 3, self.screen, self.info_x))
        
    
    def render(self):
        #Render asteroids and stars
        for object in self.objects:
            object.render()
        
        
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

        if len(self.explosions) > 0:
            
            for explosion in self.explosions:
                explosion.render_cycle()
                
                if explosion.over:
                    self.explosions.remove(explosion)
            
            print(self.explosions)
    
    
    #Rocket collisions
    def rocket_collision_check(self, rocket):
        for object in self.objects:
            if object.rocket_collided(rocket):
                object.reset()

                
        for enemy_projectile in self.enemy_projectiles:
            if enemy_projectile.rocket_collided(rocket):
                self.explosions.append(Explosion(rocket.width * 2, rocket.rect.x, rocket.rect.y, self.screen, enemy_projectile))
                self.enemy_projectiles.remove(enemy_projectile)
    
    
    #Projectile collisions and powerup spawn
    def projectile_collision_check(self, projectile):
        
        #Projectile collided with asteroid
        for object in self.objects:
            if object.projectile_collided(projectile):
                self.explosions.append(Explosion(object.size, object.rect.x, object.rect.y, self.screen, projectile))
                object.reset()
                
                self.score_checker()
                
                powerup_chance = Dice()
                dice_roll = powerup_chance.roll()
                
                #Spawn ExtraHealth
                if dice_roll <= 10:
                    self.powerups.append(self.factory.create_PowerUp("ExtraHealth", 30, 30, 10, self.screen, self.info_x))
                
                #Spawn PiercingShot
                elif dice_roll > 10 and dice_roll <= 20:
                    self.powerups.append(self.factory.create_PowerUp("PiercingShot", 24, 40, 10, self.screen, self.info_x))
                    
                #Spawn WideShot
                elif dice_roll > 20 and dice_roll <= 30:
                    self.powerups.append(self.factory.create_PowerUp("WideShot", 45, 32, 10, self.screen, self.info_x))
                    
                #Spawn RapidShot
                elif dice_roll > 30 and dice_roll <= 40:
                    self.powerups.append(self.factory.create_PowerUp("RapidShot", 30, 45, 10, self.screen, self.info_x))
                    
                return True
        
        #Projectile collided with enemy  
        for enemy in self.enemies[:]:
            if enemy.projectile_collided(projectile):
                enemy_hp = enemy.hit()
                self.explosions.append(Explosion(enemy.size, enemy.rect.x, enemy.rect.y, self.screen, projectile))

                
                if enemy_hp <= 0:
                    time.sleep(0.10)
                    self.enemies.remove(enemy)
                    
                    for enemy_projectile in self.enemy_projectiles[:]:
                        self.enemy_projectiles.remove(enemy_projectile)
                    
                    if self.score > self.ufo_threshold:
                        self.ufo_destroyed_score = self.score - self.ufo_threshold - self.ufo_destroyed_score
                    self.score_checker()
                                                        
                return True
    
    
    #Powerup collision
    def powerup_collision_check(self, rocket):
        for powerup in self.powerups[:]:
            if powerup.collided(rocket):
                rocket.powerup_pickup(powerup)
                self.powerups.remove(powerup)
                
                self.score_checker()
            
            #Enemy projectile can destroy powerup
            for enemy_projectile in self.enemy_projectiles[:]:
                if powerup.collided(enemy_projectile):
                    self.enemy_projectiles.remove(enemy_projectile)
                    if powerup not in self.powerups:
                        pass
                    else:
                        self.powerups.remove(powerup)


    
    
    
    
    #Check if enemy can shoot projectile
    def enemy_shoot(self, dice_roll):
        if dice_roll <= 5:
            for enemy in self.enemies:
                self.enemy_projectiles.append(enemy.shoot())
                
        
        #Enemy always targets powerups
        for powerup in self.powerups:
            for enemy in self.enemies:
                if enemy.rect.center[0] >= powerup.rect.left and enemy.rect.center[0] <= powerup.rect.right:
                    if dice_roll <= 50:
                        self.enemy_projectiles.append(enemy.shoot())

                    
    
    #Tell ufo where to look
    def check_rocket_position(self, rocket):
        for enemy in self.enemies:
            
            #Look left
            if enemy.rect.x >= rocket.rect.x + (self.screen.get_width() - self.info_x) / 3 - rocket.width * 2:
                enemy.look_left()
   
            #Look right
            elif enemy.rect.x <= rocket.rect.x - (self.screen.get_width() - self.info_x) / 3 + rocket.width * 2:
                enemy.look_right()

            #Look down (default sprite)
            else:
                enemy.look_down()
    
    
    def score_checker(self):
        self.score = self.score + 1
        print("Score: ", self.score)
        
        if self.score >= self.ufo_threshold * self.n + self.ufo_destroyed_score:
            if len(self.enemies) > 0:
                pass
            else:
                self.n = self.n + 1
                self.enemies.append(self.factory.create_Enemy("Ufo", randrange(0, self.screen.get_width(), 10),
                                                              0, 56, 10, 3, self.screen, self.info_x))

            
        
##End