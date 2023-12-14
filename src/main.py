"""ゲームを実行する

mainモジュール。これを実行するとゲームが開始する。
"""
# Pythonのシステムを操作できるモジュール。ゲームを終了するために必要
import sys
# 時間を扱うモジュール
import time
# 乱数生成のモジュール。ハードル生成のために必要
import random
# ゲーム開発のためのモジュール
import pygame
# キーイベント判定のために必要
from pygame.locals import QUIT, K_SPACE
# プレイヤーのクラス
from player import Player
# 障害物のクラス
from hurdle import Hurdle
# スコアのクラス
from score import Score
# 衝突を検知する関数
from is_collision import is_collision
# 使用する画像のデータ。辞書型なのでdict
from image_dict import IMAGE_DICT
# ゲームの設定
from game_settings import *
# テキストの設定
from text import *


# 表示される画面　引数((横幅pixel, 縦幅pixel))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HORSE")  # 画面のタイトルかな？
is_game_over = False  # ゲームオーバーならTrue


def run_game():
    """ゲームのメインの処理

    Returns:
        tuple(Player, list): player, hurdlesを次に実行されるgame_over()に渡すために返す
    """
    global is_game_over
    hurdles = []  # ハードルのリストの初期化

    # 時間変数の初期化とセット
    start_time = time.time()  # ゲーム開始時の時刻を取得

    # Playerをインスタンス化
    # Playerの初期位置の座標を指定
    player = Player(PLAYER_DEFAULT_POINT)

    # スコアクラスを宣言
    score = Score()

    # ハードル生成用の定数
    jumping_frame = -(player.JUMP_HEIGHT) / player.GRAVITY * 2
    frame_counter = 0
    state = 1
    step_on_frame = IMAGE_DICT['red'].get_height() / Hurdle.speed  # 着地の時に踏んでしまう可能性のあるフレーム数の計算
    COLLISION_MARGIN = IMAGE_DICT['red'].get_width() * 3  # 難易度調整用マージン(係数2と3で大分体感が変わる)
    collision_area = (player.image.get_width() + step_on_frame + COLLISION_MARGIN) / Hurdle.speed
    creatable_frame = jumping_frame - collision_area

    # ゲームスタート
    while True:
        # 背景の描画
        draw_background()

        # スペースキーが押された
        if pressed(K_SPACE) and player.on_ground:
            # ジャンプのための初期化
            player.init_jump()

        # プレイヤーの座標を更新
        player.jump()

        # プレイヤーの画像を切り替え
        player.switch_image()

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

        # スコアを更新して表示
        score.score_update(start_time)
        score.display_score(screen)

        # screen.blit(im.IMAGE_DICT['stop'], horse_cordi)

        # 画面の更新
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

        # 閉じるボタンを押したら終了
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

    return player, hurdles


def draw_background():
    """背景を描画する

    画面の上下で領域を2分割するように、色付きの矩形を二つ表示する。
    空と草原を表現している。まるでアイルランドの景色のようだ。
    """
    # 矩形の表示：空(水色)　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (160, 255, 255), (0, 0, WIDTH, HEIGHT * 3 / 5))
    # 矩形の表示：草原(緑色)　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (120, 255, 0), (0, HEIGHT * 3 / 5, WIDTH, HEIGHT))


def title():
    """タイトル画面を表示する

    main関数で最初に実行される。
    """
    # キーが押されるまでタイトル画面を表示する
    while True:
        # 画面の中央に開始方法のテキスト、下の方に操作説明のテキストを描画
        screen.blit(text_title, text_title_point)
        screen.blit(text_game_rule, text_game_rule_point)
        screen.blit(text_instructions, text_instructions_point)

        # 画面を更新
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

        # イベント(マウスの移動やクリック、キー入力など)を検知
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        # キーの指定なしで、何かキーが押されたかを取得する
        if pressed(None):
            break


def create_hurdle(hurdles):
    """ ハードルを生成する関数

    乱数からハードルをランダムな間隔で生成する

    Args:
        hurdles: 画面に表示するハードルを保持するリスト

    Retruns:
        boolean: ハードルが生成されたかどうかを返す
    """
    if random.random() < 0.05:
        num_create = 1  # ハードルを連続していくつ出すか
        appear = random.randint(1, 100)  # どのハードルを生成するかの判断に使う変数
        if appear < 40:
            pic = 'red'
        elif appear < 70:
            pic = 'yellow'
        elif appear < 90:
            pic = 'white'
        else:
            pic = 'mole'

        for i in range(num_create):
            hurdles.append(Hurdle(pic, 1))
        return True
    return False


def pressed(key):
    """ キーが押されたか判断する関数

    引数に指定したキーが押されていたらTrueを返す

    Args:
        key: 押されたか判断したいキー

    Returns:
        boolen: 引数で指定したキーが押されたかを返す
    """
    # このフレームで押されたすべてのキーのリストを取得
    keys = pygame.key.get_pressed()
    if key is None:
        if True in keys:
            return True
    else:
        return keys[key]  # スペースキーが押されたか判定
    return None


def game_over(player, hurdles):
    """ゲームオーバー時の処理

    Args:
        player (Player): プレイヤーオブジェクト
        hurdles (list): 現在画面に存在するハードルのリスト
    ゲームオーバーの時、テキストを表示し、
    ゲームオーバー時のスコアやプレイヤー位置、ハードル位置をそのまま表示し続ける。
    なにかキーが押されたらループを抜けて終了する。
    """
    # グローバルな変数（ゲームオーバーかどうかのフラグ）を用いることを宣言
    global is_game_over
    # なにかキーが押されたらループを抜ける
    while not pressed(None):
        # blit(表示するテキスト, 座標(テキストの中心位置が配置される)) 。
        draw_background()
        screen.blit(IMAGE_DICT['error'], player.left_top_point.get_xy())
        for h in hurdles:
            screen.blit(h.image, h.left_top_point.get_xy())

        # 画面の中央にテキストを描画。
        # ゲームオーバーの文字の表示
        screen.blit(text_game_over, text_game_over_point)
        screen.blit(text_press_key, text_press_key_point)

        # 閉じるボタンを押したら終了
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        # 画面を更新
        # pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

    is_game_over = False


def terminate():
    """ウィンドウを閉じてゲームを終了する

    画面右上の×ボタンが押されたらウィンドウを閉じる。
    """
    pygame.quit()
    sys.exit()


def main():
    """最初に実行される関数

    ウィンドウが閉じられるまで終わらない。
    """
    while True:
        # タイトル画面を表示する
        title()
        # ゲームをスタートする
        player, hurdles = run_game()
        # ゲームオーバーの処理を行う
        game_over(player, hurdles)


# モジュールの属性__name__は「python hoge.py」のようにコマンドで自分が実行されたら"__main__"を保持する。
# 自分が実行されたときという条件なので、このファイルを実行するとこのif文が実行される。
if __name__ == '__main__':
    main()
