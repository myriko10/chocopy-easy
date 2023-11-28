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
# Playerクラス
from player import Player
# 座標のクラス
from point import Point
# ゲームを終了するのに使う
import sys 
# 障害物のクラス
from hurdle import Hurdle
# 時間を扱う
import time

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

    # ゲームスタート
    while True:
        # 背景の描画
        draw_backgroud()

        # キーが押されたらジャンプの処理 ひょうくん
        current_time = time.time()
        keys = pygame.key.get_pressed()
        # 無効時間を過ぎており、ゲームオーバーでないならジャンプ
        if not is_game_over:
            # 押されたキーの状態を判定
            if  keys[pygame.K_SPACE] and player.on_ground:
                player.init_jump()
        
        # プレイヤーの座標を更新
        player.jump()
        
        # プレイヤーの画像を切り替え
        player.switch_image()
        
        # 画像を描画
        screen.blit(player.current_image, (player.left_top_point.x, player.left_top_point.y))

        # ゲームオーバーの時、ゲームオーバー用の画像をセット
        if is_game_over:
            player.game_over() # 中身ヲX_Xの画像ニ変エレバ良イ
        
        # プレイヤーの画像を描画
        screen.blit(player.current_image, player.position.get_xy())

        # ハードルを生成するかしないか　くずめくん
            # 乱数でなんとかしてほしい
            # ハードルを生成するならシーケンスに追加
        if random.randint(1,100) == 1:
            appear = random.randint(1,100)
            if appear < 40:
                pic = 'red'
            elif appear < 70:
                pic = 'yellow'
            elif appear < 90:
                pic = 'white'
            else: pic = 'mole'
            hurdles.append(Hurdle(pic,1))

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

                # プレイヤーの右端のx座標をハードルが左に超えていたら
                if h.left_top_point.x <= player.left_top_point.x + player.current_image.get_width():
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
        score_display(is_game_over, start_time)
        
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

# ひょうくん用新規関数定義スペース

# まるやまくん用新規関数定義スペース     
# テキストの設定はこれで一回で済ませておく。
def make_texts():
    # グローバル変数として使うという宣言
    global BASICFONT20, BASICFONT25, BASICFONT50,text_title,text_game_rule,text_instructions, text_game_over,text_press_key,\
        text_title_center_point, text_game_rule_center_point,text_instructions_center_point, text_game_over_center_point, text_press_key_center_point,\
        text_score, text_score_center_point
    # フォントの代入　pygame.init()の後でないと定義できない
    BASICFONT20 = pygame.font.Font('freesansbold.ttf', 20)
    BASICFONT25 = pygame.font.Font('freesansbold.ttf', 25)
    BASICFONT50 = pygame.font.Font('freesansbold.ttf', 50)

    # タイトル画面用のテキストを代入。
    text_title = BASICFONT25.render("Press Any Key to Start", True, (255, 255, 255))
    text_game_rule = BASICFONT20.render("--- GAME RULE ---", True, (255, 255, 255))
    text_instructions = BASICFONT20.render("Press the space key to jump and avoid obstacles.", True, (255, 255, 255))
    # 画面の中央の位置を取得。
    text_title_center_point = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    # 画面の中央の少し下の位置を取得。
    text_game_rule_center_point = text_game_rule.get_rect(center=(WIDTH // 2, HEIGHT - 60))
    text_instructions_center_point = text_instructions.get_rect(center=(WIDTH // 2, HEIGHT - 30))

    # ゲームオーバー表示用のテキストを代入。
    text_game_over = BASICFONT50.render("Game Over", True, (75, 40, 20))
    text_press_key = BASICFONT25.render("Press Any Key To Retry", True, (75, 40, 20))
    # 画面の中央の位置を取得。
    text_game_over_center_point = text_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    # 画面の中央の少し下の位置を取得。
    text_press_key_center_point = text_press_key.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

# ゲームオーバー表示
def game_over():
    # blit(表示するテキスト, 座標(テキストの中心位置が配置される)) 。
    # 画面の中央にテキストを描画。
    screen.blit(text_game_over, text_game_over_center_point)
    screen.blit(text_press_key, text_press_key_center_point)
    
# どもんくん用新規関数定義スペース
# スコア計算
def score_calc(start_time):
        score = int(time.time() - start_time) * 100 
        return score
        
# スコア表示
def score_display(is_game_over, start_time):
    global score # スコア保持用の変数

    # ゲームが続く限りスコアを更新
    if is_game_over == False:
        score = score_calc(start_time)
    # スコア表示用のテキストを代入。
    text_score = BASICFONT20.render("score : " + str(score).zfill(8), True, (0, 0, 0))
    # スコア表示用の画像位置を取得(テキストの中心座標)
    text_score_center_point = text_score.get_rect(center = (WIDTH-100, 20))

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

