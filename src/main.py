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
import sys # ゲームを終了するのに使う

# これらはグローバル変数だと思う
WIDTH = 700 # 画面の幅ピクセル
HEIGHT = 500 # 画面の高さピクセル 
FPS = 30 # flame per second 1秒あたり30回画面を更新する 
FPSCLOCK = pygame.time.Clock() # クロック

# 表示される画面　引数((横幅pixel, 縦幅pixel))
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # 
pygame.display.set_caption('HORSE') # 画面のタイトルかな？

# ゲームの内容
def run_game():
    title()
    
    # Playerをインスタンス化　ひょうくん

    # 時間変数の初期化とセット まるやま

    score = 0 # スコア

    # ゲームスタート
    while True:
        # 背景の描画
        draw_backgroud()

        # プレイヤーの描画　ひょうくん
        # キーイベントはキューになっているらしい。たぶん。読んだら消してね　from まるやま

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
        FPSCLOCK.tick_busy_loop(FPS)
        refreshFrame()

        # 閉じるボタンを押したら終了
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        
# 背景の描画
def draw_backgroud():
    # 矩形の表示：空　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (160,255,255), (0,0,WIDTH,HEIGHT*3/5))
    # 矩形の表示：草原　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (120,255,0), (0,HEIGHT*3/5,WIDTH,HEIGHT))  

# なかむらくん用新規関数定義スペース
def title():
# フォントの設定
    BASICFONT25 = pygame.font.Font('freesansbold.ttf', 25)
    BASICFONT20 = pygame.font.Font('freesansbold.ttf', 20)
    BASICFONT19 = pygame.font.Font('freesansbold.ttf', 19)
    # 初期画面の表示
    while True:
        font_title = BASICFONT25
        font_regular = BASICFONT20
        font_small = BASICFONT19
        # 表示するテキスト
        title = font_title.render("Press Any Key to Start", True, (255, 255, 255))
        game_rule = font_regular.render("--- GAME RULE ---", True, (255, 255, 255))
        control_description = font_regular.render("Press the space key to jump and avoid obstacles.", True, (255, 255, 255))

        # 画面の位置を取得。get_rect()はpygame独自のメソッドなので覚えなくてよい。
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        game_rule_rect = game_rule.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        control_rect = control_description.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        # 画面の中央にテキストを描画。blit()はpygame独自のメソッドなので覚えなくてよい。
        screen.blit(title, title_rect)
        screen.blit(game_rule, game_rule_rect)
        screen.blit(control_description, control_rect)

        # 画面を更新
        pygame.display.flip()

        # イベント(マウスの移動やクリック、キー入力など)を検知
        for event in pygame.event.get():
            # イベントがキー入力だったら(=何かしらキーが押されたら)forループを抜ける
            if event.type == pygame.KEYDOWN:
                break
            # 閉じるボタンを押したら終了
            elif event.type == QUIT:
                terminate()
        else:
            continue

        # whileループを抜け、初期画面を閉じる
        break
# くずめくん用新規関数定義スペース

# ひょうくん用新規関数定義スペース

# まるやまくん用新規関数定義スペース
# フレームを更新する。つまりコマ送りのコマを一つ進める。
def refreshFrame():
	pygame.event.get() 
	pygame.display.update()
	FPSCLOCK.tick(FPS)
     
def terminate():
    pygame.quit()
    sys.exit()

# 最初に実行される関数
def main():
    # Pygameの初期化
    pygame.init() 
 
    # ゲームがスタートする
    run_game()

    # ゲームを終了する
    terminate()

# モジュールの属性__name__は「python hoge.py」のようにコマンドで自分が実行されたら"__main__"を保持する。
# 自分が実行されたときという条件なので、このファイルを実行するとこのif文だけが実行される。
if __name__ == "__main__":
    main()

