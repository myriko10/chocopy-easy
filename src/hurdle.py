""" hurdle

    ハードルのモジュール
"""
# ハードル画像を取得するために使用
from image_dict import IMAGE_DICT
# 座標を表現するために使用
from point import Point
# ゲーム画面の幅と高さに依存する定数を
from game_settings import WIDTH, HEIGHT

class Hurdle:
    """ ハードルクラス

    単体のハードルの定義するクラス
    """
    # ハードルが移動する速度
    speed = 8

    # ハードルインスタンスの初期化
    def __init__(self, image_key, scale):
        # ハードルの画像
        self.image = IMAGE_DICT[image_key]
        # 生成位置
        self.left_top_point = Point(WIDTH, HEIGHT*3/7 + IMAGE_DICT['run1'].get_height() - self.image.get_height())  
        # 画像の幅
        self.width = self.image.get_width() * scale
        # 画像の高さ
        self.height = self.image.get_height() * scale
        # 画像の右下の座標。衝突判定に使用する。
        self.right_bottom_point = Point(
            self.left_top_point.x + self.width, self.left_top_point.y + self.height)
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))  # ハードルの描画サイズを修正

    def move(self):
        """ ハードルを動かす関数

        自分自身の座標を右から左に移動する
        """
        # ハードルのxの座標をspeed分動かす。
        self.left_top_point.x -= self.speed
        self.right_bottom_point.x = self.left_top_point.x + self.width
