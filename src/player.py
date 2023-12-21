"""プレイヤーのキャラクターを表すクラスを含むモジュール
"""
import time
from image_dict import IMAGE_DICT
from point import Point
from game_settings import HEIGHT

class Player:
    """プレイヤーのキャラクターを表すクラス
    """
    def __init__(self, point):
        """プレイヤーを初期化

        Args:
            point (Point): プレイヤーの初期位置。画像の左上の座標。
        """
        # playerの初期画像を設定
        self.image = IMAGE_DICT['run1']

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
        self.JUMP_HEIGHT = -(HEIGHT / 38)

        # 衝突判定のための画像右下の座標を設定
        self.right_bottom_point = Point(
            self.left_top_point.x + self.image.get_width(),
            self.left_top_point.y + self.image.get_height()
        )

    def init_jump(self):
        """ジャンプのための初期化
        
        """
        # y方向速度を更新
        self.y_velocity = self.JUMP_HEIGHT

        # 地面にいない状態にする
        self.on_ground = False

    def jump(self):
        """ジャンプしている間の処理
        
        毎フレームで実行され、徐々に速度を変化させる
        """
        # 地面にいたらjump処理をしない
        if self.on_ground:
            return

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

    def switch_image(self):
        """画像を切り替えて表示する

        プレイヤーが着地しているとき等間隔の時間で馬の画像を切り替え、走っているように見せる
        """
        if self.on_ground:
            # 現在の時間をミリ秒で取得
            time_now = time.time() * 1000
            # 500ミリ秒ごとに画像を切り替える
            if int(time_now) % 500 < 250:
                self.image = IMAGE_DICT['run1']
            else:
                self.image = IMAGE_DICT['run2']
        # ジャンプしている時の画像を指定
        else:
            self.image = IMAGE_DICT['run2']

    def update(self):
        """プレイヤーのパラメータの変更をする
        
        ジャンプによる位置の更新と、地上にいるとき走るアニメを表示する
        """
        self.jump()
        self.switch_image()
