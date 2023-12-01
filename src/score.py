import pygame
import time

BASICFONT20 = pygame.font.Font('freesansbold.ttf', 20)
WIDTH = 700

class Score:
    def __init__(self):
        self.score = 0

    # スコア計算
    def score_calc(self, start_time):
        self.score = int(time.time() - start_time) * 100 
    
    # スコア表示更新
    def score_update(self, is_game_over, start_time):
        global score # スコア保持用の変数
        # ゲームが続く限りスコアを更新
        if is_game_over == False:
            self.score_calc(start_time)
         
    # スコアを描画
    def score_display(self, screen):
        # スコア表示用のテキストを代入。
        text_score = BASICFONT20.render("score : " + str(self.score).zfill(8), True, (0, 0, 0))
        # スコア表示用の画像位置を取得(テキストの中心座標)
        text_score_center_point = text_score.get_rect(center = (WIDTH-100, 20))
        
        screen.blit(text_score, text_score_center_point)