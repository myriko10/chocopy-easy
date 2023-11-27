import time
from image_dict import IMAGEDICT
from point import Point 

class Player:
    def __init__(self, x, y):
        self.image_running1 = IMAGEDICT['run1'] # 走り画像1
        self.image_running2 = IMAGEDICT['run2'] # 走り画像2
        self.image = self.image_running1 # 初期画像
        self.current_image = self.image # 現在の画像
        self.default_left_top_point = Point(x,y) # プレイヤーが地面に着地しているときの座標
        self.position = Point(x,y) # プレイヤーの位置
        self.y_velocity = 0 # y方向の速度
        self.on_ground = True # 地面にいるかどうか
        self.gravity = 0.5  # 重力
        self.jump_height = -15 # ジャンプの高さ

    # ジャンプ処理
    def init_jump(self):
        # 速さを更新
        self.y_velocity += self.jump_height
        # 地面にいない状態にする
        self.on_ground = False

    # ジャンプしている間の画像の更新
    def jump(self):
        # 重力を加える
        self.y_velocity += self.gravity
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
    def draw(self, screen):
        # 画像の変更
        if self.on_ground:
            self.current_image = self.image_running1
        # ジャンプしている時
        else:
            self.current_image = self.image_running2
            
        # 画像を描画
        screen.blit(self.current_image, (self.position.x, self.position.y))
