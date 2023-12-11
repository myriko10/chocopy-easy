# ヒットボックスを小さくするためのマージン        
MARGIN_FOR_PLAYER = 15 

# プレイヤーとハードルの矩形が重なっているかどうかを判定する
def is_collision(player_left_top_point, player_right_bottom_point, 
    hurdle_left_top_point, hurdle_right_bottom_point):
    
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