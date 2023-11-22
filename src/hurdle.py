<<<<<<< HEAD
import pygame
from image_dict import IMAGEDICT
from point import Point 

# mainに記載しているグローバル変数をまとめて別のファイルに記述するのもありかなと思う
# ↓これはとりあえず
# WIDTH = 700
# HEIGHT = 500
PLAYER_HEIGHT = IMAGEDICT['stop'].get_height() # 馬の高さ：160 幅：140

class Hurdle:
    speed = 10

    def __init__(self,image_key,scale,point_x):
        self.image = IMAGEDICT[image_key]
        self.width = self.image.get_width() * scale   # self.width = 32
        self.height = self.image.get_height() * scale # self.height = 45
        self.left_top_point = Point(point_x,(290 + PLAYER_HEIGHT - self.height)) # playerのy座標は仮定
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self):
=======
import pygame
from image_dict import IMAGEDICT
from point import Point 

class Hurdle:
    speed = 5

    def __init__(self,image_key,scale):
        self.image = IMAGEDICT[image_key]
        self.left_top_point = Point(700,300)
        self.width = self.image.get_width() * scale
        self.height = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self):
>>>>>>> 6d4694de65065b5a30f823db154f781b3e9fa2dc
        self.left_top_point.x -= self.speed