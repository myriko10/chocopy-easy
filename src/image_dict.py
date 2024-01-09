"""image_dict

使用する画像のデータを辞書型で保持する。
"""
# ゲーム開発のためのモジュール
import pygame

# 画像を保持する辞書。
IMAGE_DICT = {'bird': pygame.image.load('../images/bird.png'),
              'calrun1': pygame.image.load('../images/callot_horse_run1.png'),
              'calrun2': pygame.image.load('../images/callot_horse_run2.png'),
              'cloud': pygame.image.load('../images/cloud.png'),
              'red': pygame.image.load('../images/flower_red.png'),
              'white': pygame.image.load('../images/flower_white.png'),
              'yellow': pygame.image.load('../images/flower_yellow.png'),
              'home': pygame.image.load('../images/home.png'),
              'run1': pygame.image.load('../images/horse_run1.png'),
              'run2': pygame.image.load('../images/horse_run2.png'),
              'smile': pygame.image.load('../images/horse_smile.png'),
              'stop': pygame.image.load('../images/horse_stop.png'),
              'walk1': pygame.image.load('../images/horse_walk1.png'),
              'walk2': pygame.image.load('../images/horse_walk2.png'),
              'mole': pygame.image.load('../images/mole.png'),
              'town': pygame.image.load('../images/town.png'),
              'error': pygame.image.load('../images/horse_error.png'),
              }
