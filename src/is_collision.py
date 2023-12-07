# ヒットボックスを小さくするためのマージン        
MARGIN_FOR_PLAYER = (15,15) 

# chatGPTの出力結果をうのみにしているので確認する必要がある11/09 by まるやま
def is_collision(player_left_top_point, player_right_bottom_point, 
    hurdle_left_top_point, hurdle_right_bottom_point):
    
    # プレイヤーの矩形の左上座標と右下座標、marginあり
    player_left = tuple(p + b for p,b in zip(player_left_top_point.get_xy(), MARGIN_FOR_PLAYER))
    player_top = tuple(p + b for p,b in zip(player_left_top_point.get_xy(), MARGIN_FOR_PLAYER))
    player_right = tuple(p - b for p,b in zip(player_right_bottom_point.get_xy(), MARGIN_FOR_PLAYER))
    player_bottom = tuple(p - b for p,b in zip(player_right_bottom_point.get_xy(), MARGIN_FOR_PLAYER))
    
    # ハードルの矩形の左上座標と右下座標
    hurdle_left, hurdle_top = hurdle_left_top_point.get_xy()
    hurdle_right, hurdle_bottom = hurdle_right_bottom_point.get_xy()

    # 矩形の交差判定
    # バックスラッシュを使うか()で囲むことで長い条件文は改行できる
    if player_left[0] < hurdle_right and hurdle_left < player_right[0] and \
        player_bottom[1] > hurdle_top:
        return True  # 衝突が発生
    else:
        return False  # 衝突が発生していない