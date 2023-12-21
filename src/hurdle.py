""" hurdle

    ハードルのモジュール
"""
# import pygame
from image_dict import IMAGE_DICT
from point import Point
from game_settings import WIDTH, HEIGHT

class Hurdle:
    """ ハードルクラス

    単体のハードルの定義するクラス
    """
    # ハードルが移動する速度
    speed = 8

    # ハードルインスタンスの初期化
    def __init__(self, image_key, scale):
        self.image = IMAGE_DICT[image_key]  # ハードルの画像
        self.left_top_point = Point(WIDTH, HEIGHT*3/7 + IMAGE_DICT['run1'].get_height() - self.image.get_height())  # 生成位置
        self.width = self.image.get_width() * scale  # 画像の幅
        self.height = self.image.get_height() * scale  # 画像の高さ
        self.right_bottom_point = Point(
            self.left_top_point.x + self.width, self.left_top_point.y + self.height)  # 画像の右下の座標
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))  # ハードルの描画サイズを修正

    def move(self):
        """ ハードルを動かす関数

        自分自身の座標を右から左に移動する
        """
        # ハードルのxの座標をspeed分減らす
        self.left_top_point.x -= self.speed
        self.right_bottom_point.x = self.left_top_point.x + self.width
