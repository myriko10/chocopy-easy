import pygame
from image_dict import IMAGEDICT
from point import Point 

class Hurdle:
    speed = 20

    def __init__(self,image_key,scale):
        self.image = IMAGEDICT[image_key]
        self.left_top_point = Point(700,400)
        self.width = self.image.get_width() * scale
        self.height = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self):
        self.left_top_point.x -= self.speed