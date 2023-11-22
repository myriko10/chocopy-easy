import pygame
from image_dict import IMAGEDICT
from point import Point 

# mainに記載しているグローバル変数をまとめて別のファイルに記述するのもありかなと思う
# ↓これはとりあえず
# WIDTH = 700
# HEIGHT = 500
PLAYER_HEIGHT = IMAGEDICT['run1'].get_height()

class Hurdle:
    speed = 10
    
    def __init__(self,image_key,scale,point_x,player_default_top):
        self.image = IMAGEDICT[image_key]
        self.width = self.image.get_width() * scale   # self.width = 32
        self.height = self.image.get_height() * scale # self.height = 45
        self.left_top_point = Point(point_x,(player_default_top - 50 + PLAYER_HEIGHT - self.height))
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self):
        self.left_top_point.x -= self.speed