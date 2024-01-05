"""ゲームを実行する

mainモジュール。これを実行するとゲームが開始する。
"""
# Pythonのシステムを操作できるライブラリ。ゲームを終了するために使用する。
import sys
# 時間を扱うライブラリ
import time
# 乱数生成のライブラリ。ハードル生成のために使用する。
import random
# ゲーム開発のためのライブラリ
import pygame
# キーイベント判定のために使用する。
from pygame.locals import QUIT, K_SPACE
# プレイヤーのクラス

# 障害物のクラス

# スコアのクラス

# 衝突を検知する関数

# 使用する画像のデータ。辞書型。
from image_dict import IMAGE_DICT
# ゲームの設定
from game_settings import (WIDTH,HEIGHT,FPS,FPSCLOCK,PLAYER_DEFAULT_POINT)
# テキストのクラス
from text import Text
# Pygameの初期化
pygame.init()
# ゲーム画面
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 画面のタイトル
pygame.display.set_caption("HORSE")
# テキストクラスをインスタンス化
text = Text()
def run_game():
    """ゲームのメインの処理

    Returns:
        tuple(Player, list): player, hurdlesを次に実行されるgame_over()に渡すために返す
    """

    # ゲームオーバーのフラグをセット、False:ゲームオーバーでない。
    is_game_over = False

    # ゲームスタート
    while True:
        # 背景の描画
        draw_background()
        # イベント(マウスの移動やクリック、キー入力など)を検知
        # スペースキーが押された
        proceed_event_with_key(K_SPACE)
        #if proceed_event_with_key(K_SPACE) and player.on_ground:

        # ハードルの生成
        # frame_counter += 1
        # state, frame_counter = transition_hurdles_state(hurdles, state, frame_counter, creatable_frame, collision_area)

        # ゲームオーバーならrun_game関数を終了する
        if is_game_over:
            break

        # 画面の更新
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

    # ゲームオーバー関数に渡すため返す
    # return player, hurdles

def draw_background():
    """背景を描画する

    画面の上下で領域を2分割するように、色付きの矩形を二つ表示する。
    空と草原を表現している。まるでアイルランドの景色のようだ。
    """
    # 矩形の表示：空(水色)　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (160, 255, 255), (0, 0, WIDTH, HEIGHT * 3 / 5))
    # 矩形の表示：草原(緑色)　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (120, 255, 0), (0, HEIGHT * 3 / 5, WIDTH, HEIGHT))

def proceed_event_with_key(key):
    """ 引数に渡されたキーが押されたか判断する関数
    
    どのキーでも押されたことを検知したいときはNoneを渡す
    None以外はキーを表す数字(K_SPACEなど)が渡される想定
    引数に指定したキーが押されていたらTrueを返す
    Args:
        key: 押されたか判断したいキー(Noneかint)

    Returns:
        boolen: 引数で指定したキーが押されたかを返す
    """
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if key is None:
                # スペースで画面遷移しないようにする。
                # ジャンプのつもりで押して間に合わずゲームオーバーになったときすぐにタイトルに戻ってしまうことがあるため。
                if event.key == K_SPACE:
                    return False
            # if event.key == key:
            return True
    return False

def terminate():
    """ウィンドウを閉じてゲームを終了する

    画面右上の×ボタンが押されたらウィンドウを閉じる。
    """
    pygame.quit()
    sys.exit()

def create_state_constants(player):
    """ハードル生成の状態遷移のための定数を生成して返す。
    プレイヤーが、ハードルの小さい群の先頭にぎりぎりぶつかる前に飛べば、ゲームオーバーにならないようにする。

    Args:
        player (_type_): Playerインスタンス

    Returns:
        float?: 生成可能時間を表すフレーム数
        float?: 滞空時間が過ぎた後に衝突してしまう時間を表すフレーム数?
    """
    # 着地の時に踏んでしまう可能性のあるフレーム数の計算
    STEP_ON_FRAME = IMAGE_DICT['red'].get_height() / Hurdle.speed
    # 難易度調整用マージン(係数2と3で大分体感が変わる)
    COLLISION_MARGIN = IMAGE_DICT['red'].get_width() * 3
    # プレイヤーの滞空時間が過ぎた後に衝突してしまう時間を表すフレーム数?
    collision_area = (player.image.get_width() + STEP_ON_FRAME + COLLISION_MARGIN) / Hurdle.speed
    # プレイヤーがジャンプしている間に経過する時間を表すフレーム数
    jumping_frame = -(player.JUMP_HEIGHT) / player.GRAVITY * 2
    # ハードルを生成してもよい時間を表すフレーム数
    creatable_frame = jumping_frame - collision_area
    # 生成した定数を返す。
    return creatable_frame, collision_area

def create_hurdle(hurdles):
    """ ハードルを生成する関数

    乱数からハードルをランダムな間隔で生成する

    Args:
        hurdles: 画面に表示するハードルを保持するリスト

    Retruns:
        boolean: ハードルが生成されたかどうかを返す
    """
    # 確率でハードルを生成する
    if random.random() < 0.05:
        # 生成する場合
        # どのハードルを生成するか乱数の範囲で決定する
        appear = random.randint(1, 100)
        if appear < 40:
            pic = 'red'
        elif appear < 70:
            pic = 'yellow'
        elif appear < 90:
            pic = 'white'
        else:
            pic = 'mole'
        hurdles.append(Hurdle(pic, 1))
        # ハードルが生成されたのでTrueを返す
        return True
    # ハードルが生成されない場合Falseを返す
    return False

def transition_hurdles_state(hurdles, state, frame_counter, creatable_frame, collision_area):
    """ハードル生成用のステートマシンをあらわす

    状態stateは1->2->3->...と遷移する。初期状態は1
    frame_counterは関数の呼び出し元で毎フレームでカウントアップされるものとする
    stateは関数の呼び出し元で
    Args:
        hurdles (_type_): 生成されたハードルのリスト
        state (_type_): ハードル生成を制御するための状態
        frame_counter (_type_): フレームをリセットしてから現在までの経過時間を表すフレーム数
        creatable_frame (_type_): 生成可能状態の時間を表すフレーム数
        collision_area (_type_): 衝突してしまう時間を表すフレーム数

    Returns:
        int: state 状態を呼び出し元に反映させるため返す
        int: frame_counter カウンタを呼び出し元に反映させるため返す
    """
    # 生成可能(未生成)状態
    if state == 1:
        # ハードルが生成されたら状態2に遷移する
        if create_hurdle(hurdles):
            state = 2
            frame_counter = 0
    # 生成可能(1つ以上生成済み)状態
    elif state == 2:
        create_hurdle(hurdles)
        # frame_counterは関数の外側で
        if frame_counter >= creatable_frame:
            state = 3
            frame_counter = 0
    # 生成禁止状態
    elif state == 3:
        if frame_counter >= collision_area:
            state = 1
            frame_counter = 0
    return state, frame_counter

def display_title():
    """タイトル画面を表示する

    main関数で最初に実行される。
    """
    # キーが押されるまでタイトル画面を表示する
    while True:
        # 画面の中央に開始方法のテキスト、下の方に操作説明のテキストを描画
        screen.fill((0, 0, 0))
        screen.blit(text.text_title, text.text_title_point)
        screen.blit(text.text_game_rule, text.text_game_rule_point)
        screen.blit(text.text_instructions, text.text_instructions_point)

        # 画面を更新
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

        # イベント(マウスの移動やクリック、キー入力など)を検知
        # キーの指定なしで、何かキーが押されたかを取得する
        if proceed_event_with_key(None):
            break

def display_game_over(player, hurdles):
    """ゲームオーバー時の処理

    Args:
        player (Player): プレイヤーオブジェクト
        hurdles (list): 現在画面に存在するハードルのリスト
    ゲームオーバーの時、テキストを表示し、
    ゲームオーバー時のスコアやプレイヤー位置、ハードル位置をそのまま表示し続ける。
    なにかキーが押されたらループを抜けて終了する。
    """
    # イベント(マウスの移動やクリック、キー入力など)を検知
    # なにかキーが押されたらループを抜ける
    while not proceed_event_with_key(None):
        # 背景を表示
        draw_background()
        # ゲームオーバー用のプレイヤー画像を表示
        screen.blit(IMAGE_DICT['error'], player.left_top_point.get_xy())
        # スコアを表示
        screen.blit(text.text_score, text.text_score_center_point)
        # ハードルを表示
        for h in hurdles:
            screen.blit(h.image, h.left_top_point.get_xy())

        # 画面の中央にテキストを描画。
        # ゲームオーバーの文字の表示
        screen.blit(text.text_game_over, text.text_game_over_point)
        screen.blit(text.text_press_key, text.text_press_key_point)

        # 画面を更新
        # pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick_busy_loop(FPS)

def main():
    """実行する関数

    ウィンドウが閉じられるまで終わらない。
    """
    while True:
        # タイトル画面を表示する
        display_title()
        # ゲームをスタートする
        # player, hurdles = 
        run_game()
        # ゲームオーバーの処理を行う
        # display_game_over(player, hurdles)

# 「python hoge.py」のようにコマンドで自分が実行されたらモジュールの属性__name__は"__main__"を保持する。
# 自分が実行されたときだけこのif文が実行される。
if __name__ == '__main__':
    main()
