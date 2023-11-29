import pygame
import time
from main import WIDTH, HEIGHT

# pygame を初期化
# pygame.init()

# フォントの代入　pygame.init()の後でないと定義できない
BASICFONT20 = pygame.font.Font('freesansbold.ttf', 20)
BASICFONT25 = pygame.font.Font('freesansbold.ttf', 25)
BASICFONT50 = pygame.font.Font('freesansbold.ttf', 50)

# タイトル画面用のテキスト
text_title = BASICFONT25.render("Press Any Key to Start", True, (255, 255, 255))
# 画面中央の位置を取得
text_title_center_point = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# ゲームルールのテキスト
text_game_rule = BASICFONT20.render("--- GAME RULE ---", True, (255, 255, 255))
# 画面中央の少し下の位置を取得
text_game_rule_center_point = text_game_rule.get_rect(center=(WIDTH // 2, HEIGHT - 60))

# ルール説明のテキスト
text_instructions = BASICFONT20.render("Press the space key to jump and avoid obstacles.", True, (255, 255, 255))
# 画面の下の位置を取得
text_instructions_center_point = text_instructions.get_rect(center=(WIDTH // 2, HEIGHT - 30))

# ゲームオーバー表示用のテキスト
text_game_over = BASICFONT50.render("Game Over", True, (75, 40, 20))
# 画面中央の位置を取得
text_game_over_center_point = text_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# リトライ用のテキスト
text_press_key = BASICFONT25.render("Press Any Key To Retry", True, (75, 40, 20))
# 画面中央の少し下の位置を取得
text_press_key_center_point = text_press_key.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

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