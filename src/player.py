import time

import pygame
from image_dict import IMAGEDICT
from point import Point 

class Player:
    def __init__(self, point):
        self.image_running1 = IMAGEDICT['run1'] # 走り画像1
        self.image_running2 = IMAGEDICT['run2'] # 走り画像2
        self.image = self.image_running1 # 初期画像
        self.current_image = self.image # 現在の画像
        self.default_left_top_point = Point(*point.get_xy()) # point # プレイヤーが地面に着地しているときの座標
        self.position = Point(*point.get_xy()) # プレイヤーの位置
        self.y_velocity = 0 # y方向の速度
        self.on_ground = True # 地面にいるかどうか
        self.GRAVITY = 0.5  # 重力
        self.INITIAL_VELOCITY = -15 # ジャンプの初速

    # ジャンプ処理
    def init_jump(self):
        # 速さを更新
        self.y_velocity = self.INITIAL_VELOCITY
        # 地面にいない状態にする
        self.on_ground = False
        # Spaceキーが押されたj状態を記録
        self.space_pressed = True

    # ジャンプしている間の画像の更新
    def jump(self):
        # 重力を加える
        self.y_velocity += self.GRAVITY
        # 位置を更新
        self.position.y += self.y_velocity

        # 地面に着地したか判定
        if self.position.y > self.default_left_top_point.y:
            # フラグを切り替える
            self.on_ground = True
            # 地面に着地したときの位置に矯正
            self.position.y = self.default_left_top_point.y
            # 速度を0にしてプレイヤーが動かないようにする
            self.y_velocity = 0

    # 画像を描画
    def switch_image(self):
        # 画像の変更
        if self.on_ground:
            self.current_image = self.image_running1
            # 時間が等間隔で馬の画像を切り替え、走っているように見せる
            if True:
                pass
        # ジャンプしている時
        else:
            self.current_image = self.image_running2
            
        
