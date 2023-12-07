# ゲームを作りやすくするモジュール
import pygame
# ゲームウィンドウの横幅、縦幅を取得
from game_settings import WIDTH, HEIGHT

# フォントの代入　pygame.init()の後でないと定義できない
BASICFONT20 = pygame.font.Font('freesansbold.ttf', 20)
BASICFONT25 = pygame.font.Font('freesansbold.ttf', 25)
BASICFONT50 = pygame.font.Font('freesansbold.ttf', 50)
# タイトル画面用のテキスト
text_title = BASICFONT25.render("Press Any Key to Start", True, (255, 255, 255))
# 画面中央の位置を取得、タイトル表示位置
text_title_center_point = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
# ゲームルールのテキスト
text_game_rule = BASICFONT20.render("--- GAME RULE ---", True, (255, 255, 255))
# 画面中央の少し下の位置を取得、ゲームルール表示位置
text_game_rule_center_point = text_game_rule.get_rect(center=(WIDTH // 2, HEIGHT - 60))
# ルール説明のテキスト
text_instructions = BASICFONT20.render("Press the space key to jump and avoid obstacles.", True, (255, 255, 255))
# 画面の下の位置を取得、タイトル画面のルール表示位置
text_instructions_center_point = text_instructions.get_rect(center=(WIDTH // 2, HEIGHT - 30))
# ゲームオーバー表示用のテキスト
text_game_over = BASICFONT50.render("Game Over", True, (75, 40, 20))
# 画面中央の位置を取得、ゲームオーバー表示位置
text_game_over_center_point = text_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
# リトライ用のテキスト
text_press_key = BASICFONT25.render("Press Any Key To Retry", True, (75, 40, 20))
# 画面中央の少し下の位置を取得、ゲームオーバー時のキー入力案内の表示位置
text_press_key_center_point = text_press_key.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
