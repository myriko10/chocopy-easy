"""ゲームの基本設定
- 700x450ピクセルの画面を設定しています。
- 1秒あたり30フレームで画面が更新されます。
- FPSCLOCKは、pygameのtime.Clock()を用いてフレームレートを制御するため、ゲームのアニメーションの速度が一定に保たれます。
- PLAYER_DEFAULT_POINTは、プレイヤーのデフォルトの位置で、画面の幅の4/70、高さの3/7に設定されている。
"""
# ゲーム開発のためのモジュール
import pygame
# プレイヤーのデフォルト位置のために使用
import point

# 画面のサイズ
# 画面の幅ピクセル
WIDTH = 700
# 画面の高さピクセル
HEIGHT = 450
# flame per second 1秒あたり30回画面を更新する
FPS = 30
# フレームレート制御
FPSCLOCK = pygame.time.Clock()
# デフォルトのプレイヤー位置(地上を走るとき)。画像の左上の座標。
PLAYER_DEFAULT_POINT = point.Point()
# point.Point(WIDTH * 4/70, HEIGHT * 3/7)
