import pygame

from Boundary import Boundary
from DisplayObject import DisplayObject

#Creating numbers to display player ammo, hp and enemy hp
class NumberFactory():
    def __init__(self):
        self.numbers = {'0':'assets/zero.png', '1':'assets/one.png', '2' :'assets/two.png', '3':'assets/three.png', 
                        '4':'assets/four.png', '5':'assets/five.png', '6':'assets/six.png', '7':'assets/seven.png', 
                        '8':'assets/eight.png', '9':'assets/nine.png'}
        
    def number_picker(self, number):
        for n in self.numbers:
            if number in self.numbers.keys():
                return self.numbers.get(number)
    
#Useful gameplay info on right side of screen    
class InfoField():
    def __init__(self, screen, screen_x, info_x, rocket, world):
        self.screen = screen
        self.info_x = info_x
        self.rocket = rocket
        self.world = world
        
        self.factory = NumberFactory()
        self.basic_unit = 25
        
        #Setup boundary
        self.info_width = screen_x - self.info_x
        self.boundary = Boundary(self.info_width, 0, 3, screen.get_height(), screen)
        
        

    #Display player rocket hp sprite
    def hp_display_setup(self):
        heart_size = 60
        
        #Display hp heart differently when full
        if self.rocket.hp > 5:
            heart_image = 'assets/max_health.png'
        else:
            heart_image = 'assets/extra_health.png'
        
        heart_x = self.screen.get_width() - self.info_x / 2 - heart_size / 2
        heart_y = self.screen.get_height() / 2 - heart_size / 2
        
        return_list = []
        
        return_list.append(DisplayObject(heart_size, heart_size, heart_image, heart_x , heart_y, self.screen))
        return_list.append(self.hp_number_display(heart_x, heart_y))
        
        return return_list
    
    #Display player rocket hp amount
    def hp_number_display(self, parent_x, parent_y):
        
        #Select number sprite corresponding to player rocket hp
        if self.rocket.hp < 6:
            hp = str(self.rocket.hp)
            number_image = self.factory.number_picker(hp)
        else:
            number_image = 'assets/six_max.png'
        
        number_width = 20
        number_height = 28
        number_x = parent_x + number_width
        number_y = parent_y + number_height / 2 + 5
        
        return DisplayObject(number_width, number_height, number_image, number_x, number_y, self.screen)
    
    
    
    #Display current powerup
    def powerup_display_setup(self):        
        if self.rocket.piercingshot:
            powerup_width = 48
            powerup_height = 80
            powerup_image = 'assets/piercing_shot.png'
        elif self.rocket.wideshot:
            powerup_width = 90
            powerup_height = 64
            powerup_image = 'assets/wide_shot.png'
        elif self.rocket.rapidshot:
            powerup_width = 60
            powerup_height = 90
            powerup_image = 'assets/rapid_shot.png'
        elif self.rocket.bombshot:
            powerup_width = 84
            powerup_height = 84
            powerup_image = 'assets/bomb_shot.png'
        else:
            powerup_width = 56
            powerup_height = 56
            powerup_image = 'assets/default_shot.png'
            
        powerup_x = self.screen.get_width() - self.info_x / 2 - powerup_width / 2
        powerup_y = self.screen.get_height() - self.screen.get_height() / 3 - powerup_height / 2
        
        return_list = []
        
        return_list.append(DisplayObject(powerup_width, powerup_height, powerup_image, powerup_x, powerup_y, self.screen))
        return_list.append(self.powerup_number_display(powerup_x + powerup_width / 2, powerup_y + powerup_height / 2))
        
        return return_list
    
    #Display current powerup ammo
    def powerup_number_display(self, parent_x, parent_y):
        powerup_num = str(len(self.rocket.powerup_projectiles))

        if len(self.rocket.powerup_projectiles) < 10:

            #If out of powerup ammo, revert to default rocket weapon
            if len(self.rocket.powerup_projectiles) <= 0:
                number_width = 28
                number_height = 20
                number_image = 'assets/infinite.png'
            
            #Select number sprite corresponding to powerup ammo
            else:
                number_width = 20
                number_height = 28
                number_image = self.factory.number_picker(powerup_num)

        #Display powerup ammo differently when max
        else:
            number_width = 45
            number_height = 28
            number_image = 'assets/ten_max.png'
        
        number_x = parent_x - number_width / 2
        number_y = parent_y + number_height + self.basic_unit
        
        return DisplayObject(number_width, number_height, number_image, number_x, number_y, self.screen)
    
    
    
    #Display current enemy UFO
    def ufo_display_setup(self):
        ufo_size = 60
        for ufo in self.world.enemies:
            ufo_image = ufo.chosen_image
        ufo_x = self.screen.get_width() - self.info_x / 2 - ufo_size / 2
        ufo_y = self.screen.get_height() - self.screen.get_height() * 2/3 - ufo_size / 2 - self.basic_unit
        
        return_list = []
        
        return_list.append(DisplayObject(ufo_size, ufo_size, ufo_image, ufo_x, ufo_y, self.screen))
        return_list.append(self.ufo_number_display(ufo_x + ufo_size / 2, ufo_y + ufo_size / 2))
        
        return return_list
    
    #Display current enemy UFO hp
    def ufo_number_display(self, parent_x, parent_y):
        for ufo in self.world.enemies:
            ufo_hp = str(ufo.hp)
        
        number_width = 20
        number_height = 28

        #Select number sprite corresponding to UFO hp
        number_image = self.factory.number_picker(ufo_hp)
        number_x = parent_x - number_width / 2
        number_y = parent_y + number_height + self.basic_unit / 2
        
        return DisplayObject(number_width, number_height, number_image, number_x, number_y, self.screen)
    
    
    #Display score label
    def score_display_setup(self):
        score_width = 120
        score_height = 28
        score_image = 'assets/score.png'
        score_x = self.screen.get_width() - self.info_x / 2 - score_width / 2
        score_y = self.basic_unit
        
        return_list = []
        
        return_list.append(DisplayObject(score_width, score_height, score_image, score_x, score_y, self.screen))
        return_list = return_list + self.score_number_display(score_x + score_width, score_y + score_height / 2)
        
        return return_list
    
    #Display current score
    def score_number_display(self, parent_x, parent_y):
        score = self.world.score
        
        number_width = 20
        number_height = 28
        number_x = parent_x - number_width
        number_y = parent_y + number_height
        
        gap = 5
        return_list = []

        #Select number sprites corresponding to current score
        #Score between 0 and 9
        if len(str(score)) == 1:
            return_list.append(DisplayObject(number_width, number_height,
                                             self.factory.number_picker(str(score)), number_x, number_y, self.screen))
        
        #Score between 10 and 99
        if len(str(score)) == 2:
            return_list.append(DisplayObject(number_width, number_height,
                                             self.factory.number_picker(str(score)[0]), number_x - number_width - gap,
                                             number_y, self.screen))
            return_list.append(DisplayObject(number_width, number_height,
                                             self.factory.number_picker(str(score)[len(str(score)) - 1]), number_x,
                                             number_y, self.screen))

        #Score between 100 and 999
        if len(str(score)) == 3:
            return_list.append(DisplayObject(number_width, number_height,
                                             self.factory.number_picker(str(score)[0]), number_x - number_width * 2 - gap * 2,
                                             number_y, self.screen))
            return_list.append(DisplayObject(number_width, number_height,
                                             self.factory.number_picker(str(score)[1]), number_x - number_width - gap,
                                             number_y, self.screen))
            return_list.append(DisplayObject(number_width, number_height,
                                             self.factory.number_picker(str(score)[len(str(score)) - 1]), number_x,
                                             number_y, self.screen))

        return return_list



    #Rendering everything
    def render(self):
        self.boundary.render()
        
        hp_display = self.hp_display_setup()
        for object in hp_display:
            object.render()
            
        powerup_display = self.powerup_display_setup()
        for object in powerup_display:
            object.render()
        
        if len(self.world.enemies) > 0:
            ufo_display = self.ufo_display_setup()
            for object in ufo_display:
                object.render()
                
        score_display = self.score_display_setup()
        for object in score_display:
            object.render()
        