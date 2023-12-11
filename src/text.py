"""テキストの設定を含むモジュール

main.pyにインポートして使う。グローバル変数が主である。
pygame.init()の後にimportする。
"""
# ゲームを作りやすくするモジュール
import pygame
# ゲームウィンドウの横幅、縦幅を取得
from game_settings import WIDTH, HEIGHT

# フォントの代入　pygame.init()の後でないと定義できない
BASICFONT20 = pygame.font.Font('freesansbold.ttf', 20)
BASICFONT25 = pygame.font.Font('freesansbold.ttf', 25)
BASICFONT50 = pygame.font.Font('freesansbold.ttf', 50)
# タイトルのテキスト。
text_title = BASICFONT25.render(
    "Press Any Key to Start", True, (255, 255, 255))
# text_titleがゲーム画面中央にくるような座標を取得。タイトル表示位置。
text_title_point = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
# ゲームルールのテキスト。
text_game_rule = BASICFONT20.render("--- GAME RULE ---", True, (255, 255, 255))
# text_game_ruleがゲーム画面中央の少し下にくるような位置を取得、ゲームルール表示位置。
text_game_rule_point = text_game_rule.get_rect(
    center=(WIDTH // 2, HEIGHT - 60))
# ルール説明のテキスト。
text_instructions = BASICFONT20.render(
    "Press the space key to jump and avoid obstacles.", True, (255, 255, 255))
# text_instructionsがゲーム画面の下部にくるような位置を取得、タイトル画面のルール表示位置。
text_instructions_point = text_instructions.get_rect(
    center=(WIDTH // 2, HEIGHT - 30))
# ゲームオーバー表示用のテキスト。
text_game_over = BASICFONT50.render("Game Over", True, (75, 40, 20))
# ゲーム画面中央の位置を取得、ゲームオーバー表示位置。
text_game_over_point = text_game_over.get_rect(
    center=(WIDTH // 2, HEIGHT // 2))
# リトライ用のテキスト。
text_press_key = BASICFONT25.render(
    "Press Any Key To Retry", True, (75, 40, 20))
# text_press_keyがゲーム画面中央の少し下にくるような位置を取得、ゲームオーバー時のキー入力案内の表示位置。
text_press_key_point = text_press_key.get_rect(
    center=(WIDTH // 2, HEIGHT // 2 + 30))
