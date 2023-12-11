import time
from image_dict import IMAGEDICT
from point import Point

class Player:
    def __init__(self, point, HEIGHT):
        # playerの初期画像を設定
        self.image = IMAGEDICT['run1']

        # playerのデフォルト位置（着地している位置）を設定
        self.DEFAULT_LEFT_TOP_POINT = Point(*point.get_xy())  

        # playerの初期位置を着地している位置に設定 
        self.left_top_point = Point(*point.get_xy())

        # playerのy方向の速度
        self.y_velocity = 0 

        # playerの初期状態を「着地している」に設定
        self.on_ground = True

        # 重力の定数
        self.GRAVITY = 0.5

        # ジャンプの高さ(負の値にすることで上に移動する)
        self.JUMP_HEIGHT = -(HEIGHT / 40)
        
        # 右下の座標を設定
        self.right_bottom_point = Point(
            self.left_top_point.x + self.image.get_width(), 
            self.left_top_point.y + self.image.get_height()
        ) # 右下の座標

    # ジャンプ処理する
    def init_jump(self):

        # y方向速度を更新
        self.y_velocity = self.JUMP_HEIGHT

        # 地面にいない状態にする
        self.on_ground = False

        # Spaceキーが押された状態を記録
        self.space_pressed = True

    # ジャンプしている間の画像を更新する
    def jump(self):

        # ｙ方向の速度に重力を加える
        self.y_velocity += self.GRAVITY

        # player位置を更新
        self.left_top_point.y += self.y_velocity
        self.right_bottom_point.x = self.left_top_point.x + self.image.get_width()
        self.right_bottom_point.y = self.left_top_point.y + self.image.get_height()

        # 地面に着地したか判定
        if self.left_top_point.y > self.DEFAULT_LEFT_TOP_POINT.y:

            # 着地フラッグの状態を切り替える
            self.on_ground = True

            # 地面に着地したときの位置に矯正
            self.left_top_point.y = self.DEFAULT_LEFT_TOP_POINT.y

            # ｙ方向の速度を0にして、ジャンプ処理を終了
            self.y_velocity = 0

    # 画像を切り替えて表示する
    def switch_image(self, is_game_over):

        # 画像の変更
        # ゲームオーバーのとき
        if is_game_over:
            self.image = IMAGEDICT['error']
        
        # ゲーム中で着地しているとき
        elif self.on_ground:
            self.image = IMAGEDICT['run1']
            
            # 時間が等間隔で馬の画像を切り替え、走っているように見せる
            if True:
                # 現在の時間をミリ秒で取得
                time_now = time.time() * 1000
                # 500ミリ秒ごとに画像を切り替える
                if int(time_now) % 500 < 250:
                    self.image = IMAGEDICT['run1']
                else:
                    self.image = IMAGEDICT['run2']

        # ジャンプしている時
        else:
            self.image = IMAGEDICT['run2']

