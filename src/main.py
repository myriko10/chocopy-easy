# ゲームを作りやすくするモジュール
import pygame
# QUITために必要
from pygame.locals import *
# 乱数生成
import random
# IMAGEDICTを引っ張ってくるためにfrom 拡張子ファイル名 import 引っ張ってきたい名前
from image_dict import IMAGEDICT
# 衝突検知
from check_collision import check_collision
# 時間を扱う
import time
# Pygameの初期化
pygame.init()
# テキストのインポート
from text import *
# Playerクラス
from player import Player
# 座標のクラス
from point import Point
# ゲームを終了するのに使う
import sys 
# 障害物のクラス
from hurdle import Hurdle
# スコアクラス
from score import Score
    
WIDTH = 700 # 画面の幅ピクセル
HEIGHT = 450 # 画面の高さピクセル 
FPS = 30 # flame per second 1秒あたり30回画面を更新する 
FPSCLOCK = pygame.time.Clock() # フレームレート制御
PLAYER_DEFAULT_POINT = Point(WIDTH*4/70, HEIGHT*3/7)

# 表示される画面　引数((横幅pixel, 縦幅pixel))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HORSE') # 画面のタイトルかな？

# ハードルのシーケンス
hurdles = []

# ゲームの内容
def run_game():
    title()

    # 時間変数の初期化とセット どもんくん
    start_time = time.time() # ゲーム開始時の時刻を取得
    is_game_over = False # ゲームオーバーならTrue

    # Playerをインスタンス化　ひょうくん
    # Playerの初期位置の座標を指定
    '''
    ここでPointオブジェクトをそのまま引数に渡す仕様にすると、参照渡しになる。
    Pointオブジェクトをinit関数内でdefault_left_top_pointとleft_top_point属性の両方に代入すると、
    片方の値を書き替えたらもう一方の値も書き換わってしまう。
    *はリストを展開してx,yの数値(not参照型)ふたつを渡している。
    '''
    # Pointオブジェクトを更新すると
    player = Player(PLAYER_DEFAULT_POINT)

    # スコアクラスを宣言
    score = Score()

    # ハードル生成用の定数
    jumping_frame = -(player.INITIAL_VELOCITY) / player.GRAVITY * 2
    # collision_area = (player.image.get_width() + IMAGEDICT['red'].get_width()) / Hurdle.speed
    frame_counter = 0
    state = 1
    step_on_frame = IMAGEDICT['red'].get_height() / Hurdle.speed # 着地の時に踏んでしまう可能性のあるフレーム数の計算
    COLLISION_MARGIN = IMAGEDICT['red'].get_width() * 3 # 難易度調整用マージン(係数2と3で大分体感が変わる)
    collision_area = (player.image.get_width() + step_on_frame + COLLISION_MARGIN) / Hurdle.speed
    creatable_frame = jumping_frame - collision_area
    
    # ゲームスタート
    while True:
        # 背景の描画
        draw_backgroud()

        keys = pygame.key.get_pressed()
        # 無効時間を過ぎており、ゲームオーバーでないならジャンプ
        if not is_game_over:
            # 押されたキーの状態を判定
            if  keys[pygame.K_SPACE] and player.on_ground:
                player.init_jump()
        
        # プレイヤーの座標を更新
        player.jump()
        
        # プレイヤーの画像を切り替え
        player.switch_image(is_game_over)
        
        # プレイヤーの画像を描画
        screen.blit(player.image, player.left_top_point.get_xy())

        # ハードルを生成するかしないか
        # 画面にハードルがないときの生成条件
        # if len(hurdles) == 0: 
        #     create_hurdle()

        # # 一番新しいハードルが画面の1/3を超えたら
        # if hurdles:
        #     if hurdles[-1].left_top_point.x < WIDTH / 3: 
        #         if random.random() < 0.04:
        #             create_hurdle()

        # 生成条件
        frame_counter += 1
        if state == 1:
            if create_hurdle():
                state = 2
                frame_counter = 0
        elif state == 2:
            create_hurdle()
            if frame_counter >= creatable_frame:
                state = 3
                frame_counter = 0
        else:
            if frame_counter >= collision_area:
                state = 1
                frame_counter = 0            

        # ハードルを全部動かして描画
        if not is_game_over and hurdles:
            # 衝突判定　まるやま
            # 生存しているハードル全てに対して
            for h in hurdles:
                h.move()
                if h.left_top_point.x < 0:
                    # 画面外に出たハードルをシーケンスから削除
                    hurdles.remove(h)

                # プレイヤーの右端のx座標をハードルが左に超えていたら
                if h.left_top_point.x <= player.left_top_point.x + player.image.get_width():
                    # 衝突検知：戻り値は衝突していたらTrue、していなかったらFalse
                    is_game_over = check_collision(player.left_top_point, player.right_bottom_point,
                                    h.left_top_point, h.right_bottom_point)
                    
        # ハードルを描画
        for h in hurdles: 
            screen.blit(h.image,h.left_top_point.get_xy())
            
        # ゲームオーバーなら文字を表示
        if is_game_over:
            game_over()

        # スコアを表示　どもんくん
        score.score_update(is_game_over, start_time)
        score.score_display(screen)
        
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
def title():
    # 初期画面の表示
    while True:
        # blit(表示するテキスト, 座標(テキストの中心位置が配置される)) 
        # 画面の中央に開始方法のテキスト、下の方に操作説明のテキストを描画
        screen.blit(text_title, text_title_center_point)
        screen.blit(text_game_rule, text_game_rule_center_point)
        screen.blit(text_instructions, text_instructions_center_point)

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
def create_hurdle():
    if random.random() < 0.05:
        num_create = 1 #random.randint(1,3) # ハードルを連続していくつ出すか
        appear = random.randint(1,100)
        if appear < 40:
            pic = 'red'
        elif appear < 70:
            pic = 'yellow'
        elif appear < 90:
            pic = 'white'
        else: pic = 'mole'
        for i in range(num_create):
            #point_x = WIDTH + (32 * (i-1)) # 32は花のデフォルト画像サイズ、サイズが変わったときこの値も変わるようにしたい
            hurdles.append(Hurdle(pic,1))
        return True
    else:
        return False

# def judge_create_hurdle():

# ひょうくん用新規関数定義スペース

# まるやまくん用新規関数定義スペース     


# ゲームオーバー表示
def game_over():
    # blit(表示するテキスト, 座標(テキストの中心位置が配置される)) 。
    # 画面の中央にテキストを描画。
    screen.blit(text_game_over, text_game_over_center_point)
    screen.blit(text_press_key, text_press_key_center_point)
    
# どもんくん用新規関数定義スペース

# ゲームを終了する
def terminate():
    pygame.quit()
    sys.exit()

# 最初に実行される関数
def main():
    # ゲームがスタートする
    run_game()
    # ゲームを終了する
    terminate()

# モジュールの属性__name__は「python hoge.py」のようにコマンドで自分が実行されたら"__main__"を保持する。
# 自分が実行されたときという条件なので、このファイルを実行するとこのif文が実行される。
if __name__ == '__main__':
    main()