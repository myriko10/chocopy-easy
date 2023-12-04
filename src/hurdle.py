import pygame
from image_dict import IMAGEDICT
from point import Point 

class Hurdle:
    speed = 8

    def __init__(self,image_key,scale):
        # ハードルの画像
        self.image = IMAGEDICT[image_key]
        # 生成位置
        self.left_top_point = Point(700,300)
        # 画像の幅
        self.width = self.image.get_width() * scale
        # 画像の高さ
        self.height = self.image.get_height() * scale
        # 画像の右下の座標
        self.right_bottom_point = Point(self.left_top_point.x + self.width, self.left_top_point.y + self.height)
        # ハードルのサイズを修正
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def move(self):
        # xの座標をspeed分減らす
        self.left_top_point.x -= self.speed
        self.right_bottom_point.x = self.left_top_point.x + self.width
