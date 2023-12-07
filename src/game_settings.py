import pygame
import point

# ゲームの設定
# 画面のサイズ
# 画面の幅ピクセル
WIDTH = 700 
# 画面の高さピクセル
HEIGHT = 450

# flame per second 1秒あたり30回画面を更新する 
FPS = 30 

# フレームレート制御
FPSCLOCK = pygame.time.Clock() 

# デフォルトのプレイヤーの位置
PLAYER_DEFAULT_POINT = point.Point(WIDTH*4/70, HEIGHT*3/7)