import pygame

from Boundary import Boundary

class InfoField():
    def __init__(self, screen, screen_x, info_x):
        self.screen = screen
        self.info_width = screen_x - info_x
        self.info_x = info_x
        
        #Setup boundary
        self.boundary = Boundary(self.info_width, 0, 3, screen.get_height(), screen)

    def render(self):
        self.boundary.render()