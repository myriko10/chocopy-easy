"""スコアを管理するクラス

class: Score
    func __init__ : スコアを初期化
    func score_update : スコアの値を更新する

"""
# プレイ時間を計算するために使用
import time

class Score:
    """スコアを表すクラス
    
    """
    def __init__(self):
        """ スコアを初期化する
        
        valueにスコアの値を持つ
        """
        self.value = 0

    def update_score(self, start_time):
        """ スコアを更新する

        ゲーム開始時の時刻を引数として受け取り
        現在の時刻との差分からスコアを計算、更新する
        param: 
            start_time: ゲーム開始時の時刻
        """
        self.value = int(time.time() - start_time) * 100  # スコア計算
        