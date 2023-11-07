import pygame
from pygame.locals import *
import random
import math
import image_dict as im

WIDTH = 700
HEIGHT = 500
FPS = 30
# 表示される画面
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32) # 

def main():
    pygame.init() # Pygameの初期化
    horse_cordi = (60,300)

    # 11/02 14:30なんかウィンドウは出るけど応答なしとなる→python強制終了
    while True:
        # 空の色
        pygame.draw.rect(screen, (160,255,255), (0,0,WIDTH,HEIGHT*3/5))
        # 草の色
        pygame.draw.rect(screen, (120,255,0), (0,HEIGHT*3/5,WIDTH,HEIGHT))       
        #set.screen.blit(im.IMAGEDICT['back'],(0,0))

        # 馬の表示
        # 座標指定の方法？？？　
        # 画像の中心が指定した座標にくるのか、左上が来るのか？？？
        screen.blit(im.IMAGEDICT['stop'], horse_cordi)
        pygame.display.update()  

if __name__ == "__main__":
    main()

