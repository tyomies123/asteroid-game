import pygame

from Boundary import Boundary
from ExtraHealth import ExtraHealth
from DisplayObject import DisplayObject

class NumberFactory():
    def __init__(self):
        self.numbers = {'0':'zero.png', '1':'one.png', '2' :'two.png', '3':'three.png', '4':'four.png', '5':'five.png',
                        '6':'six.png', '7':'seven.png', '8':'eight.png', '9':'nine.png', '10':'ten.png'}
        
    def number_picker(self, number):
        for n in self.numbers:
            if number in self.numbers.keys():
                return self.numbers.get(number)
    
    
class InfoField():
    def __init__(self, screen, screen_x, info_x, rocket):
        self.screen = screen
        self.info_x = info_x
        self.rocket = rocket
        
        self.factory = NumberFactory()
        self.basic_unit = 25
        
        #Setup boundary
        self.info_width = screen_x - self.info_x
        self.boundary = Boundary(self.info_width, 0, 3, screen.get_height(), screen)
        
        
    #Hp display
    def hp_display_setup(self):
        heart_size = 60
        
        if self.rocket.hp > 5:
            heart_image = 'max_health.png'
        else:
            heart_image = 'extra_health.png'
        
        heart_x = self.screen.get_width() - self.info_x / 2 - heart_size / 2
        heart_y = self.screen.get_height() / 2 - heart_size / 2
        
        return_list = []
        
        return_list.append(DisplayObject(heart_size, heart_size, heart_image, heart_x , heart_y, self.screen))
        return_list.append(self.hp_number_display(heart_x, heart_y))
        
        return return_list
    
    def hp_number_display(self, parent_x, parent_y):
        hp = str(self.rocket.hp)
        
        number_width = 20
        number_height = 28
        number_image = self.factory.number_picker(hp)
        number_x = parent_x + number_width
        number_y = parent_y + number_height / 2 + 5
        
        return DisplayObject(number_width, number_height, number_image, number_x, number_y, self.screen)
    
    
    
    #Powerup display
    def powerup_display_setup(self):        
        if self.rocket.piercingshot:
            powerup_width = 48
            powerup_height = 80
            powerup_image = 'piercing_shot.png'
        elif self.rocket.wideshot:
            powerup_width = 90
            powerup_height = 64
            powerup_image = 'wide_shot.png'
        elif self.rocket.rapidshot:
            powerup_width = 60
            powerup_height = 90
            powerup_image = 'rapid_shot.png'
        else:
            powerup_image = 'default_shot.png'
            powerup_width = 56
            powerup_height = 56
            
        powerup_x = self.screen.get_width() - self.info_x / 2 - powerup_width / 2
        powerup_y = self.screen.get_height() - self.screen.get_height() / 3 - powerup_height / 2
        
        return_list = []
        
        return_list.append(DisplayObject(powerup_width, powerup_height, powerup_image, powerup_x, powerup_y, self.screen))
        return_list.append(self.powerup_number_display(powerup_x + powerup_width / 2, powerup_y + powerup_height / 2))
        
        return return_list
    
    def powerup_number_display(self, parent_x, parent_y):
        powerup_num = str(len(self.rocket.powerup_projectiles))
        
        if len(self.rocket.powerup_projectiles) < 10:
            number_width = 20
            number_height = 28
        else:
            number_width = 40
            number_height = 28

        number_image = self.factory.number_picker(powerup_num)
        number_x = parent_x - number_width / 2
        number_y = parent_y + number_height + self.basic_unit
        
        return DisplayObject(number_width, number_height, number_image, number_x, number_y, self.screen)
    
    
    
    #Rendering
    def render(self):
        self.boundary.render()
        
        hp_display = self.hp_display_setup()
        for object in hp_display:
            object.render()
            
        powerup_display = self.powerup_display_setup()
        for object in powerup_display:
            object.render()
        
        
##End