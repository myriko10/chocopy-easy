
# chatGPTの出力結果をうのみにしているので確認する必要がある11/09 by まるやま
def Is_collision(player_left_top_point, player_right_bottom_point, 
    hurdle_left_top_point, hurdle_right_bottom_point):
    # プレイヤーの矩形の左上座標と右下座標
    player_left, player_top = player_left_top_point.get_xy()
    player_right, player_bottom = player_right_bottom_point.get_xy()

    # ハードルの矩形の左上座標と右下座標
    hurdle_left, hurdle_top = hurdle_left_top_point.get_xy()
    hurdle_right, hurdle_bottom = hurdle_right_bottom_point.get_xy()

    # ヒットボックスを小さくするためのマージン    

    MARGIN_FOR_PLAYER = 15 

    # player_left ,player_top に margin を足す    
    player_left = player_left + MARGIN_FOR_PLAYER 
    player_top = player_top + MARGIN_FOR_PLAYER 

    # player_right 、player_bottomから margin を引く
    player_right = player_right - MARGIN_FOR_PLAYER 
    player_bottom = player_bottom - MARGIN_FOR_PLAYER 

    # 矩形の交差判定
    # バックスラッシュを使うか()で囲むことで長い条件文は改行できる
    if player_left < hurdle_right and hurdle_left < player_right and \
        player_bottom > hurdle_top:
        return True  # 衝突が発生
    else:
        return False  # 衝突が発生していない