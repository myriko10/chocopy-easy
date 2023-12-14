"""スコアを管理するクラス

class: Score
    func __init__ : スコアを初期化
    func score_update : スコアを更新する
    func display_score : スコアをゲーム画面に表示する

"""

import time
from text import BASICFONT20
from game_settings import WIDTH


class Score:
    """ スコアクラス

    スコアを初期化、更新、表示する

    """

    def __init__(self):
        """ スコアを初期化する
        
        """
        self.score = 0

    def score_update(self, start_time):
        """ スコアを更新する

        ゲーム開始時の時刻を引数として受け取り
        現在の時刻との差分からスコアを計算、更新する

        :param start_time: ゲーム開始時の時刻
        """
        self.score = int(time.time() - start_time) * 100  # スコア計算

    def display_score(self, screen):
        """ スコアを表示する

        スコアをゲーム画面上に表示する際の
        テキストと位置を決定し、引数で受け取った
        ゲーム画面にスコアを表示する

        :param screen: ゲーム画面の変数
        """
        # スコア表示用のテキストを代入。
        text_score = BASICFONT20.render("score : " + str(self.score).zfill(8), True, (0, 0, 0))
        # スコア表示用の画像位置を取得(テキストの中心座標)
        text_score_center_point = text_score.get_rect(center=(WIDTH - 100, 20))

        screen.blit(text_score, text_score_center_point)
