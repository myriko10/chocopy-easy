import pygame
import point

"""
ゲームの基本設定

- 700x450ピクセルの画面を設定しています。
- 1秒あたり30フレームで画面が更新されます。
- FPSCLOCKは、pygameのtime.Clock()を用いてフレームレートを制御するため、ゲームのアニメーションの速度が一定に保たれます。
- PLAYER_DEFAULT_POINTは、プレイヤーのデフォルトの位置で、画面の幅の4/70、高さの3/7に設定されている。

"""

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
 