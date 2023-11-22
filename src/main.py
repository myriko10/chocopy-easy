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
from hurdle import Hurdle

# これらはグローバル変数だと思う
WIDTH = 700 # 画面の幅ピクセル
HEIGHT = 500 # 画面の高さピクセル 
FPS = 30 # flame per second 1秒あたり30回画面を更新する 
FPSCLOCK = pygame.time.Clock() # フレームレート制御

# 表示される画面　引数((横幅pixel, 縦幅pixel))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HORSE') # 画面のタイトルかな？

# ハードルのシーケンス
hurdles = [Hurdle('red',1,WIDTH)]

# ゲームの内容
def run_game():
    # フォントの設定
    BASICFONT25 = pygame.font.Font('freesansbold.ttf', 25)
    # 初期画面の表示
    while True:
        font = BASICFONT25
        # 表示するテキスト
        text = font.render("Press Any Key to Start", True, (255, 255, 255))

        # 画面の中央の位置を取得。get_rect()はpygame独自のメソッドなので覚えなくてよい。
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        # 画面の中央にテキストを描画。blit()はpygame独自のメソッドなので覚えなくてよい。
        screen.blit(text, text_rect)

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
        if len(hurdles) == 0: # 画面にハードルがないときの生成条件
            if random.random() < 0.05:
                create_hurdle()

        if hurdles:
            if hurdles[-1].left_top_point.x < WIDTH / 3: # 一番新しいハードルが画面の1/3を超えたら
                if random.random() < 0.05:
                    create_hurdle()

        # ハードルを全部動かして描画　くずめくん
            # 画面外に出たハードルをシーケンスから削除
        if hurdles:
            for i in range(len(hurdles)):
                hurdles[i].move()
                screen.blit(hurdles[i].image,hurdles[i].left_top_point.get_xy())
            if hurdles[0].left_top_point.x < 0:
                del hurdles[0]
                

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

# くずめくん用新規関数定義スペース
def create_hurdle():
    num_create = random.randint(1,3)
    appear = random.randint(1,100)
    if appear < 40:
        pic = 'red'
    elif appear < 70:
        pic = 'yellow'
    elif appear < 90:
        pic = 'white'
    else: pic = 'mole'
    for i in range(num_create):
        hurdles.append(Hurdle(pic,1,(WIDTH + (32 * (i-1)))))

# ひょうくん用新規関数定義スペース

# まるやまくん用新規関数定義スペース

# フレームを更新する。つまりコマ送りのコマを一つ進める。
     
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