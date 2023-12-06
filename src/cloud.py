import pygame
from image_dict import IMAGEDICT
from point import Point 

class Cloud:
    speed = 3

    def __init__(self,image_key,scale):
        # 雲の画像
        self.image = IMAGEDICT[image_key]
        # 雲の生成位置
        self.left_top_point = Point(700,100)
        # 雲の幅
        self.width = self.image.get_width() * scale
        # 雲の高さ
        self.height = self.image.get_height() * scale
        # 雲の右下の座標
        self.right_bottom_point = Point(self.left_top_point.x + self.width, self.left_top_point.y + self.height)
        # 雲のサイズ
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self):
        self.left_top_point.x -= self.speed
        self.right_bottom_point.x = self.left_top_point.x + self.width