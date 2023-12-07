import time
from text import BASICFONT20
from game_settings import WIDTH

class Score:

    def __init__(self):
        self.score = 0

    # スコア計算
    def calc_score(self, start_time):
        self.score = int(time.time() - start_time) * 100 
    
    # スコア更新
    def score_update(self, is_game_over, start_time):
        # スコア保持用の変数
        global score 
        # ゲームが続く限りスコアを更新
        if is_game_over == False:
            self.calc_score(start_time)
         
    # スコアを表示
    def display_score(self, screen):
        # スコア表示用のテキストを代入。
        text_score = BASICFONT20.render("score : " + str(self.score).zfill(8), True, (0, 0, 0))
        # スコア表示用の画像位置を取得(テキストの中心座標)
        text_score_center_point = text_score.get_rect(center = (WIDTH-100, 20))
        
        screen.blit(text_score, text_score_center_point)