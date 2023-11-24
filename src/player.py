import time

import pygame
from image_dict import IMAGEDICT
from point import Point 

class Player:
    def __init__(self, image_key, x, y):
        self.image = IMAGEDICT[image_key] # 初期画像
        self.image_running1 = IMAGEDICT['run1'] # 走り画像1
        self.image_running2 = IMAGEDICT['run2'] # 走り画像2
        self.current_image = self.image # 現在の画像
        # プレイヤー画像の左上の座標
        self.left_top_point = Point(x, y)
        self.y_velocity = 0 # y方向の速度
        self.size = 50 # 大きさ
        self.on_ground = True # 地面にいるかどうか
        self.gravity = 0.5  # 重力
        self.jump_height = -15 # ジャンプの高さ
        self.start_time = time.time() # インスタンス化時の時間
        self.jump_delay = 1 # ゲーム開始後ジャンプまでの無効時間
        # プレイヤー画像の大きさ
        self.width = self.current_image.get_width()
        self.height = self.current_image.get_height()
        # プレイヤー画像の右下の座標
        self.right_bottom_point = Point(self.left_top_point.x + self.width, 
                                        self.left_top_point.y + self.height)

    # ジャンプ処理
    def jump(self):
        # ジャンプ
        self.y_velocity += self.jump_height
        # 地面にいない状態にする
        self.on_ground = False
        # Spaceキーが押されたj状態を記録
        self.space_pressed = True

    # ジャンプしている間の画像の更新
    def update(self, height_limit):
        # 重力を加える
        self.y_velocity += self.gravity
        # 位置を更新
        self.left_top_point.y += self.y_velocity

        # 地面にいるかどうか判定
        if self.left_top_point.y >= height_limit - self.size:
            self.left_top_point.y = height_limit - self.size
            self.on_ground = True
            self.y_velocity = 0

        # 画像の変更
        if self.on_ground:
            self.current_image = self.image_running1
            
        # ジャンプしている時
        else:
            self.current_image = self.image_running2

    # 画像を描画
    def draw(self, screen):
        screen.blit(self.current_image, (self.left_top_point.x, self.left_top_point.y))
