
# chatGPTの出力結果をうのみにしているので確認する必要がある11/09 by まるやま
def check_collision(player_left_top_point, player_right_bottom_point, 
hurdle_left_top_point, hurdle_right_bottom_point):
    # プレイヤーの矩形の左上座標と右下座標
    player_left = player_left_top_point.x
    player_right = player_right_bottom_point.x
    player_top = player_left_top_point.y
    player_bottom = player_right_bottom_point.y

    # 障害物の矩形の左上座標と右下座標
    hurdle_left = hurdle_left_top_point.x
    hurdle_right = hurdle_right_bottom_point.x
    hurdle_top = hurdle_left_top_point.y
    hurdle_bottom = hurdle_right_bottom_point.y

    # 矩形の交差判定
    if player_left < hurdle_right and hurdle_left < player_right and player_top < hurdle_bottom and player_bottom > hurdle_top:
        return True  # 衝突が発生
    else:
        return False  # 衝突が発生していない