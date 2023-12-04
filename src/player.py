from ast import main
import time
from image_dict import IMAGEDICT
from point import Point 

class Player:
    def __init__(self, point, HEIGHT):
        self.IMAGE_RUNNIG1 = IMAGEDICT['run1'] # 走り画像1
        self.IMAGE_RUNNIG2 = IMAGEDICT['run2'] # 走り画像2
        self.image = self.IMAGE_RUNNIG1 # 初期画像
        self.current_image = self.image # 現在の画像
        self.default_left_top_point = Point(*point.get_xy()) # point # プレイヤーが地面に着地しているときの座標
        self.default_right_bottom_point = Point(point.x + self.image.get_width(), point.y + self.image.get_height())
        self.position = Point(*point.get_xy()) # プレイヤーの位置
        self.Y_VELOCITY = 0 # y方向の速度
        self.on_ground = True # 地面にいるかどうか
        self.GRAVITY = 0.5  # 重力
        self.INITIAL_VELOCITY = -(HEIGHT / 40) # ジャンプの初速
    

    # ジャンプ処理
    def init_jump(self):
        # 速さを更新
        self.Y_VELOCITY = self.INITIAL_VELOCITY
        # 地面にいない状態にする
        self.on_ground = False
        # Spaceキーが押されたj状態を記録
        self.space_pressed = True

    # ジャンプしている間の画像の更新
    def jump(self):
        # 重力を加える
        self.Y_VELOCITY += self.GRAVITY
        # 位置を更新

        self.left_top_point.y += self.Y_VELOCITY
        self.right_bottom_point.x = self.left_top_point.x + self.image.get_width()
        self.right_bottom_point.y = self.left_top_point.y + self.image.get_height()

        # 地面に着地したか判定
        if self.left_top_point.y > self.default_left_top_point.y:
            # フラグを切り替える
            self.on_ground = True
            # 地面に着地したときの位置に矯正
            self.left_top_point.y = self.default_left_top_point.y
            # 速度を0にしてプレイヤーが動かないようにする
            self.Y_VELOCITY = 0

    # 画像を描画
    def switch_image(self, is_game_over):
        # 画像の変更

        # ゲームオーバーのとき
        if is_game_over:
            self.image = IMAGEDICT['error']
        
        # ゲーム中で着地しているとき
        elif self.on_ground:
            self.current_image = self.IMAGE_RUNNIG1
            # 時間が等間隔で馬の画像を切り替え、走っているように見せる
            if True:
                time_now = time.time()
                if int(time_now) % 2 == 0:
                    self.image = self.IMAGE_RUNNIG1
                else:
                    self.image = self.IMAGE_RUNNIG2
        # ジャンプしている時
        else:
            self.image = self.IMAGE_RUNNIG2
    
    # ゲームオーバー時の画像に切り替え
    def game_over(self):
            self.image = IMAGEDICT['stop']

