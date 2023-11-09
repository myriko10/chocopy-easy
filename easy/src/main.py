import pygame
# なんかのために必要
from pygame.locals import *
import random
import math
# IMAGEDICTを引っ張ってくるためにimport ファイル名(.pyの前の部分) as 略称
import image_dict as im

# これらはグローバル変数だと思う
WIDTH = 700
HEIGHT = 500
FPS = 30

# 表示される画面　引数((横幅pixel, 縦幅pixel), わからない, わからない)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32) # 

def main():
    # Pygameの初期化
    pygame.init() 
    # 座標指定の方法？？？　
    # 画像の中心が指定した座標にくるのか、左上が来るのか？？？
    # 馬を表示する座標
    horse_cordi = (60,300) 

    # 11/02 14:30なんかウィンドウは出るけど応答なしとなる → python強制終了
    while True:
        # 矩形の表示：空　引数(画面, RGBカラー, 矩形領域を座標指定)
        pygame.draw.rect(screen, (160,255,255), (0,0,WIDTH,HEIGHT*3/5))
        # 矩形の表示：草原　引数(画面, RGBカラー, 矩形領域を座標指定)
        pygame.draw.rect(screen, (120,255,0), (0,HEIGHT*3/5,WIDTH,HEIGHT))       
        
        # 馬の表示
        screen.blit(im.IMAGEDICT['stop'], horse_cordi)

        # 画面の更新
        pygame.display.update()  

# ファイルが実行されたときに指定した関数を実行する
if __name__ == "__main__":
    main()