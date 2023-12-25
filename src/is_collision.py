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

    # 矩形の交差判定->交差していたら衝突:True, していなかったら衝突していない:False
    # return player_left < hurdle_right and hurdle_left < player_right and player_bottom > hurdle_top and player_top < hurdle_bottom