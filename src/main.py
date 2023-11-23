# ゲームを作りやすくするモジュール
import pygame

# なんかのために必要
from pygame.locals import *

# 乱数生成
import random

# IMAGEDICTを引っ張ってくるためにfrom 拡張子ファイル名 import 引っ張ってきたい名前
from image_dict import IMAGEDICT

# 衝突検知
from check_collision import check_collision
from player import Player

# 座標のクラス
from point import Point

# ゲームを終了するのに使う
import sys

# 障害物のクラス
from hurdle import Hurdle

# 時間を扱う
import time

# フォントの設定 なかむらくん


# これらはグローバル変数だと思う
WIDTH = 700  # 画面の幅ピクセル
HEIGHT = 450  # 画面の高さピクセル
FPS = 30  # flame per second 1秒あたり30回画面を更新する
FPSCLOCK = pygame.time.Clock()  # フレームレート制御
# インスタンスを画面の高さの4／7に設定
PLAYER_DEFAULT_TOP = HEIGHT * 4 / 7

# 表示される画面　引数((横幅pixel, 縦幅pixel))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HORSE")  # 画面のタイトルかな？

# ハードルのシーケンス
hurdles = []


# ゲームの内容
def run_game():
    title()

    # Playerをインスタンス化　ひょうくん
    # Playerの初期画像、ｘｙ座標を設定
    player = Player("run1", 40, 250)  # 画像のキー、x座標、y座標

    # 時間変数の初期化とセット どもんくん
    start_time = time.time()  # ゲーム開始時の時刻を取得
    score = 0  # スコア
    is_game_over = False  # ゲームオーバーならTrue

    # ゲームスタート
    while True:
        # 背景の描画
        draw_backgroud()

        # キーが押されたらジャンプの処理 ひょうくん
        # 現在の時刻を取得
        current_time = time.time()
        # for eventで書くと上手くいかない泣　中村
        # キー入力を取得
        keys = pygame.key.get_pressed()
        # 無効時間を過ぎており、ゲームオーバーでないならジャンプ
        if not is_game_over and (current_time - player.start_time > player.jump_delay):
            # 押されたキーの状態を判定
            if keys[pygame.K_SPACE] and player.on_ground:
                player.jump()
        # ゲームオーバーの時、ゲームオーバー用の画像をセット
        else:
            pass

        # プレイヤーの座標を更新
        player.update(PLAYER_DEFAULT_TOP)
        # プレイヤーの描画　ひょうくん
        player.draw(screen)

        # ハードルを生成するかしないか　くずめくん
        # 乱数でなんとかしてほしい
        # ハードルを生成するならシーケンスに追加
        if random.randint(1, 100) == 1:
            appear = random.randint(1, 100)
            if appear < 40:
                pic = "red"
            elif appear < 70:
                pic = "yellow"
            elif appear < 90:
                pic = "white"
            else:
                pic = "mole"
            hurdles.append(Hurdle(pic, 1))

        # ハードルを全部動かして描画　くずめくん
        if not is_game_over and hurdles:
            for i in range(len(hurdles)):
                hurdles[i].move()
            if hurdles[0].left_top_point.x < 0:
                # 画面外に出たハードルをシーケンスから削除
                del hurdles[0]

            # 衝突判定　まるやま
            # 生存しているハードル全てに対して
            for h in hurdles:
                # プレイヤーの右端の座標をハードルが右に超えていたら
                if h.left_top_point.x <= player.position.x + player.image.get_width():
                    # プレイヤーとハードルの左上と右下の座標をそれぞれ求めて変数に格納
                    player_left_top_point = player.position
                    player_right_bottom_point = Point(
                        player.position.x + player.image.get_width(),
                        player.position.y + player.image.get_height(),
                    )
                    hurdle_left_top_point = h.left_top_point
                    hurdle_right_bottom_point = Point(
                        h.left_top_point.x + h.image.get_width(),
                        h.left_top_point.y + h.image.get_height(),
                    )
                    # 衝突検知：戻り値はTrueかFalse
                    is_game_over = check_collision(
                        player_left_top_point,
                        player_right_bottom_point,
                        hurdle_left_top_point,
                        hurdle_right_bottom_point,
                    )

        # ハードルを描画
        for h in hurdles:
            screen.blit(h.image, h.left_top_point.get_xy())

        # ゲームオーバーなら文字を表示
        if is_game_over:
            game_over()

        # スコアを表示　どもんくん
        score = int(
            current_time - start_time
        )  # 現在の時刻からスタート時の時刻を引くことでプレイ時間を算出。プレイ時間をスコアとする
        score_display(score)
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
    pygame.draw.rect(screen, (160, 255, 255), (0, 0, WIDTH, HEIGHT * 3 / 5))
    # 矩形の表示：草原　引数(画面, RGBカラー, 矩形領域を座標指定)
    pygame.draw.rect(screen, (120, 255, 0), (0, HEIGHT * 3 / 5, WIDTH, HEIGHT))


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

# ひょうくん用新規関数定義スペース


# まるやまくん用新規関数定義スペース
# テキストの設定はこれで一回で済ませておく。
def make_texts():
    # グローバル変数として使うという宣言
    global BASICFONT20, BASICFONT25, BASICFONT50, text_title, text_game_rule, text_instructions, text_game_over, text_press_key, text_title_center_point, text_game_rule_center_point, text_instructions_center_point, text_game_over_center_point, text_press_key_center_point, text_score, text_score_center_point
    # フォントの代入　pygame.init()の後でないと定義できない
    BASICFONT20 = pygame.font.Font("freesansbold.ttf", 20)
    BASICFONT25 = pygame.font.Font("freesansbold.ttf", 25)
    BASICFONT50 = pygame.font.Font("freesansbold.ttf", 50)

    # タイトル画面用のテキストを代入。
    text_title = BASICFONT25.render("Press Any Key to Start", True, (255, 255, 255))
    text_game_rule = BASICFONT20.render("--- GAME RULE ---", True, (255, 255, 255))
    text_instructions = BASICFONT20.render(
        "Press the space key to jump and avoid obstacles.", True, (255, 255, 255)
    )
    # 画面の中央の位置を取得。
    text_title_center_point = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    # 画面の中央の少し下の位置を取得。
    text_game_rule_center_point = text_game_rule.get_rect(
        center=(WIDTH // 2, HEIGHT - 60)
    )
    text_instructions_center_point = text_instructions.get_rect(
        center=(WIDTH // 2, HEIGHT - 30)
    )

    # ゲームオーバー表示用のテキストを代入。
    text_game_over = BASICFONT50.render("Game Over", True, (75, 40, 20))
    text_press_key = BASICFONT25.render("Press Any Key To Retry", True, (75, 40, 20))
    # 画面の中央の位置を取得。
    text_game_over_center_point = text_game_over.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )
    # 画面の中央の少し下の位置を取得。
    text_press_key_center_point = text_press_key.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 30)
    )


# ゲームオーバー表示
def game_over():
    # blit(表示するテキスト, 座標(テキストの中心位置が配置される)) 。
    # 画面の中央にテキストを描画。
    screen.blit(text_game_over, text_game_over_center_point)
    screen.blit(text_press_key, text_press_key_center_point)


# どもんくん用新規関数定義スペース
# スコア表示
def score_display(score):
    # スコア表示用のテキストを代入。
    text_score = BASICFONT20.render("score : " + str(score).zfill(8), True, (0, 0, 0))
    # スコア表示用の画像位置を取得(テキストの中心座標)
    text_score_center_point = text_score.get_rect(center=(WIDTH - 100, 20))

    screen.blit(text_score, text_score_center_point)


# ゲームを終了する
def terminate():
    pygame.quit()
    sys.exit()


# 最初に実行される関数
def main():
    # Pygameの初期化
    pygame.init()
    # テキストの設定
    make_texts()
    # ゲームがスタートする
    run_game()
    # ゲームを終了する
    terminate()


# モジュールの属性__name__は「python hoge.py」のようにコマンドで自分が実行されたら"__main__"を保持する。
# 自分が実行されたときという条件なので、このファイルを実行するとこのif文だけが実行される。
if __name__ == "__main__":
    main()
