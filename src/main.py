# ゲームを作りやすくするモジュール
import pygame
# Pygameの初期化
pygame.init()
# キーイベント判定のために必要
from pygame.locals import QUIT, K_SPACE
# ハードル生成のための乱数生成
import random
# IMAGEDICTを引っ張ってくるためにfrom 拡張子ファイル名 import 引っ張ってきたい名前
from image_dict import IMAGEDICT
# 衝突検知
from is_collision import is_collision
# 時間を扱う
import time
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
# ゲームの設定
from game_settings import *
# テキストのインポート pygame.initされないと実行できない
from text import *
# 表示される画面　引数((横幅pixel, 縦幅pixel))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HORSE")  # 画面のタイトルかな？
is_game_over = False # ゲームオーバーならTrue

# ゲームの内容
def run_game():
    global is_game_over
    hurdles = [] # ハードルのリストの初期化

    # 時間変数の初期化とセット
    start_time = time.time() # ゲーム開始時の時刻を取得

    # Playerをインスタンス化
    # Playerの初期位置の座標を指定
    # Pointオブジェクトを更新すると
    player = Player(PLAYER_DEFAULT_POINT, HEIGHT)

    # スコアクラスを宣言
    score = Score()

    # ハードル生成用の定数
    jumping_frame = -(player.JUMP_HEIGHT) / player.GRAVITY * 2
    frame_counter = 0
    state = 1
    step_on_frame = IMAGEDICT['red'].get_height() / Hurdle.speed # 着地の時に踏んでしまう可能性のあるフレーム数の計算
    COLLISION_MARGIN = IMAGEDICT['red'].get_width() * 3 # 難易度調整用マージン(係数2と3で大分体感が変わる)
    collision_area = (player.image.get_width() + step_on_frame + COLLISION_MARGIN) / Hurdle.speed
    creatable_frame = jumping_frame - collision_area
    
    # ゲームスタート
    while True:
        # 背景の描画
        draw_background()
        # 無効時間を過ぎており、ゲームオーバーでないならジャンプ
        if not is_game_over:
            # 押されたキーの状態を判定
            if pressed(K_SPACE) and player.on_ground:
                player.init_jump()
        
        # プレイヤーの座標を更新
        player.jump()
        
        # プレイヤーの画像を切り替え
        player.switch_image(is_game_over)

        # ハードルの生成条件
        frame_counter += 1
        if state == 1:
            if create_hurdle(hurdles):
                state = 2
                frame_counter = 0
        elif state == 2:
            create_hurdle(hurdles)
            if frame_counter >= creatable_frame:
                state = 3
                frame_counter = 0
        else:
            if frame_counter >= collision_area:
                state = 1
                frame_counter = 0            

        # ハードルの表示位置を更新
        if not is_game_over and hurdles:
            # 生存しているハードル全てに対して衝突判定
            for h in hurdles.copy():
                h.move()
                if h.left_top_point.x < 0:
                    # 画面外に出たハードルをシーケンスから削除
                    hurdles.remove(h)

                # プレイヤーの右端のx座標をハードルが左に超えていたら
                if h.left_top_point.x <= player.left_top_point.x + player.image.get_width():
                    # 衝突検知：戻り値は衝突していたらTrue、していなかったらFalse
                    is_game_over = is_collision(player.left_top_point, player.right_bottom_point,
                                    h.left_top_point, h.right_bottom_point)
                    
        # ハードルを描画
        for h in hurdles: 
            screen.blit(h.image, h.left_top_point.get_xy())
            
        # ゲームオーバーなら文字を表示
        if is_game_over:
            break

        # プレイヤーの画像を描画
        screen.blit(player.image, player.left_top_point.get_xy())
        
        # スコアを表示
        score.score_update(is_game_over, start_time)
        score.display_score(screen)
        
        # screen.blit(im.IMAGEDICT['stop'], horse_cordi)

        # 画面の更新
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

        # 閉じるボタンを押したら終了
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
    return player,hurdles

# 背景を描画する
def draw_background():
    # 矩形の表示：空(水色)　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (160, 255, 255), (0, 0, WIDTH, HEIGHT * 3 / 5))
    # 矩形の表示：草原(緑色)　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (120, 255, 0), (0, HEIGHT * 3 / 5, WIDTH, HEIGHT))

# タイトル画面を表示する
def title():
    # キーが押されるまでタイトル画面を表示する
    while True:
        # 画面の中央に開始方法のテキスト、下の方に操作説明のテキストを描画
        screen.blit(text_title, text_title_center_point)
        screen.blit(text_game_rule, text_game_rule_center_point)
        screen.blit(text_instructions, text_instructions_center_point)

        # 画面を更新
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

        # イベント(マウスの移動やクリック、キー入力など)を検知
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        
        # 
        if pressed(None):
            break

# ハードルを生成する関数
def create_hurdle(hurdles):
    if random.random() < 0.05:
        num_create = 1 #random.randint(1,3) # ハードルを連続していくつ出すか
        appear = random.randint(1,100) # どのハードルを生成するかの判断に使う変数
        if appear < 40:
            pic = 'red'
        elif appear < 70:
            pic = 'yellow'
        elif appear < 90:
            pic = 'white'
        else: pic = 'mole'
        for i in range(num_create): 
            hurdles.append(Hurdle(pic,1))
        return True
    else:
        return False

# 引数に指定したキーが押されていたらTrueを返す
def pressed(key):
    keys = pygame.key.get_pressed()
    if key == None:
        if True in keys:
            return True
    else:
        return keys[key] # K_SPACE
    return None

# ゲームオーバーの処理
def game_over(player,hurdles):
    # グローバルな変数（ゲームオーバーかどうかのフラグ）を用いることを宣言
    global is_game_over
    # キーが押されたらループを抜ける
    while not pressed(None):
        # blit(表示するテキスト, 座標(テキストの中心位置が配置される)) 。
        draw_background()
        screen.blit(IMAGEDICT['error'], player.left_top_point.get_xy())
        for h in hurdles:
            screen.blit(h.image, h.left_top_point.get_xy())
            
        # 画面の中央にテキストを描画。
        # ゲームオーバーの文字の表示
        screen.blit(text_game_over, text_game_over_center_point)
        screen.blit(text_press_key, text_press_key_center_point)
        
         # 閉じるボタンを押したら終了
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
        # 画面を更新
        # pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)
    
    is_game_over = False    

# ゲームを終了する
def terminate():
    pygame.quit()
    sys.exit()

# 最初に実行される関数
def main():
    while True:
        # タイトル画面の表示
        title()
        # ゲームがスタートする
        player, hurdles = run_game()
        # ゲームオーバーの処理
        game_over(player, hurdles)

# モジュールの属性__name__は「python hoge.py」のようにコマンドで自分が実行されたら"__main__"を保持する。
# 自分が実行されたときという条件なので、このファイルを実行するとこのif文が実行される。
if __name__ == '__main__':
    main()