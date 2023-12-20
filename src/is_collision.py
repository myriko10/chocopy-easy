""" プレイヤーとハードルの矩形の衝突を判定する。

player_left_top_point, player_right_bottom_point: プレイヤーの左上と右下の座標
hurdle_left_top_point, hurdle_right_bottom_point: ハードルの左上と右下の座標
プレイヤーの矩形にはマージンが適用されている。
矩形が重なる場合にはTrue衝突あり、そうでない場合にはFalse衝突なしを返す。 
"""
# ヒットボックスを小さくするためのマージン
MARGIN_FOR_PLAYER = 15

# プレイヤーとハードルの矩形が重なっているかどうかを判定する
def is_collision(player_left_top_point, player_right_bottom_point, 
    hurdle_left_top_point, hurdle_right_bottom_point):
    """衝突判定をする

    Args:
        player_left_top_point (Point): プレイヤー画像の左上座標
        player_right_bottom_point (Point): プレイヤーが象の右下座標
        hurdle_left_top_point (Point): ハードル画像の左上座標
        hurdle_right_bottom_point (Point): ハードル画像の右下座標

    Returns:
        bool: 衝突したらTrue
    """
    # プレイヤーの矩形の左上座標と右下座標、marginあり
    player_left, player_top = [p + MARGIN_FOR_PLAYER for p in player_left_top_point.get_xy()]
    player_right, player_bottom = [p - MARGIN_FOR_PLAYER for p in player_right_bottom_point.get_xy()]

    # ハードルの矩形の左上座標と右下座標
    hurdle_left, hurdle_top = hurdle_left_top_point.get_xy()
    hurdle_right, hurdle_bottom = hurdle_right_bottom_point.get_xy()

    # 矩形の交差判定
    if player_left < hurdle_right and hurdle_left < player_right and \
        player_bottom > hurdle_top and player_top < hurdle_bottom:
        return True  # 衝突が発生
    else:
        return False  # 衝突が発生していない
    