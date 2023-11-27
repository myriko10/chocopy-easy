import time
from image_dict import IMAGEDICT
from point import Point 

class Player:
    def __init__(self, image_key, x, y):
        self.image = IMAGEDICT[image_key] # 初期画像
        self.image_running1 = IMAGEDICT['run1'] # 走り画像1
        self.image_running2 = IMAGEDICT['run2'] # 走り画像2
        self.current_image = self.image # 現在の画像
        self.position = Point(x, y) # 位置
        self.y_velocity = 0 # y方向の速度
        self.on_ground = True # 地面にいるかどうか
        self.gravity = 0.5  # 重力
        self.jump_height = -15 # ジャンプの高さ
        self.start_time = time.time() # インスタンス化時の時間
        self.jump_delay = 1 # ゲーム開始後ジャンプまでの無効時間

    # ジャンプ処理
    def jump(self):
        # ジャンプ
        self.y_velocity += self.jump_height
        # 地面にいない状態にする
        self.on_ground = False
        # Spaceキーが押されたj状態を記録
        self.space_pressed = True

    # ジャンプしている間の画像の更新
    def update_position(self, height_limit):
        # 重力を加える
        self.y_velocity += self.gravity
        # 位置を更新
        self.position.y += self.y_velocity

        # 地面に着地したか判定
        if self.position.y >= height_limit:
            # フラグを切り替える
            self.on_ground = True
            # 
            self.position.y = height_limit
            # 
            self.y_velocity = 0

    # 画像を描画
    def draw(self, screen):
        # 画像の変更
        if self.on_ground:
            self.current_image = self.image_running1
        # ジャンプしている時
        else:
            self.current_image = self.image_running2
        screen.blit(self.current_image, (self.position.x, self.position.y))
