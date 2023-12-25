"""テキストの設定を含むモジュール

main.pyにインポートして使う。
pygame.init()を含む。
"""
# ゲームを作りやすくするモジュール
import pygame
# ゲームウィンドウの横幅、縦幅を取得
from game_settings import WIDTH, HEIGHT
# Pygameの初期化
pygame.init()

class Text:
    """テキストに関わる変数を保持するクラス
    
    スコア表示のupdate関数を含む
    """
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
    def __init__(self):
        # スコア用のテキスト。
        self.text_score = self.BASICFONT20.render("score : " + str(0).zfill(8), True, (0, 0, 0))
        # スコア表示用の画像位置を取得(テキストの中心座標)。
        self.text_score_center_point = self.text_score.get_rect(center=(WIDTH - 100, 20))

    def update_score(self, value):
        """スコア表示のテキストを書き換える

        Args:
            score (_type_): 更新するスコアの値
        """
        # スコア表示用のテキストを代入。
        self.text_score = self.BASICFONT20.render("score : " + str(value).zfill(8), True, (0, 0, 0))
        # スコア表示用の画像位置を取得(テキストの中心座標)。
        self.text_score_center_point = self.text_score.get_rect(center=(WIDTH - 100, 20))
        