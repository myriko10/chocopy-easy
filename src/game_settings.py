import pygame
import point

WIDTH = 700 # 画面の幅ピクセル
HEIGHT = 450 # 画面の高さピクセル 
FPS = 30 # flame per second 1秒あたり30回画面を更新する 
FPSCLOCK = pygame.time.Clock() # フレームレート制御
PLAYER_DEFAULT_POINT = point.Point(WIDTH*4/70, HEIGHT*3/7)