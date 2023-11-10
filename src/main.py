import pygame
# なんかのために必要
from pygame.locals import *
import random
import math
# IMAGEDICTを引っ張ってくるためにfrom 拡張子ファイル名 import 引っ張ってきたい名前
from image_dict import IMAGEDICT
# 衝突検知
from check_collision import check_collision
# 座標のクラス
from point import Point

# これらはグローバル変数だと思う
WIDTH = 700 # 画面の幅ピクセル
HEIGHT = 500 # 画面の高さピクセル 
FPS = 30 # flame per second 1秒あたり30回画面を更新する 

# 表示される画面　引数((横幅pixel, 縦幅pixel), わからない, わからない)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32) # 

# ゲームの内容
def runGame():
    # 初期画面の表示文字　なかむらくん

    # キーを受け取ってゲームスタート　なかむらくん
    
    # Playerをインスタンス化　ひょうくん

    # 時間変数の初期化とセット まるやま

    score = 0 # スコア

    # ゲームスタート
    while True:
        # 背景の描画
        draw_backgroud()

        # プレイヤーの描画　ひょうくん

        # キーが押されたらジャンプの処理 ひょうくん

        # ハードルを生成するかしないか　くずめくん
            # 乱数でなんとかしてほしい
            # ハードルを生成するならシーケンスに追加

        # ハードルを全部動かして描画　くずめくん
            # 画面外に出たハードルをシーケンスから削除

        # 衝突判定　まるやま
        if check_collision(Point(0,0),Point(0,0),Point(0,0),Point(0,0)):
            pass
            # 衝突したらゲームオーバーの文字を表示
            # ボタンが押されたら初期画面へ

        # スコアを表示　まるやま

        # screen.blit(im.IMAGEDICT['stop'], horse_cordi)
    
        # 画面の更新
        pygame.display.update() 
        
# 背景の描画
def draw_backgroud():
    # 矩形の表示：空　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (160,255,255), (0,0,WIDTH,HEIGHT*3/5))
    # 矩形の表示：草原　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (120,255,0), (0,HEIGHT*3/5,WIDTH,HEIGHT))  

# 最初に実行される関数
def main():
    # Pygameの初期化
    pygame.init() 
 
    # ゲームがスタートする
    runGame()

# ファイルが実行されたときに指定した関数を実行する
if __name__ == "__main__":
    main()

