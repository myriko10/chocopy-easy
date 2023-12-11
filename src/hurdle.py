import pygame
from image_dict import IMAGEDICT
from point import Point 

class Hurdle:
    SPEED = 8

    def __init__(self,image_key,scale):
        # ハードルの画像
        self.image = IMAGEDICT[image_key]
        # 生成位置
        self.left_top_point = Point(700,290)
        # 画像の幅
        self.width = self.image.get_width() * scale
        # 画像の高さ
        self.height = self.image.get_height() * scale
        # 画像の右下の座標
        self.right_bottom_point = Point(self.left_top_point.x + self.width, self.left_top_point.y + self.height)
        # ハードルのサイズを修正
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    # ハードルを右から左に動かく関数
    def move(self):
        # xの座標をSPEED分減らす
        self.left_top_point.x -= self.SPEED
        self.right_bottom_point.x = self.left_top_point.x + self.width
