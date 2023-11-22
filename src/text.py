import pygame

def make_texts(WIDTH, HEIGHT):
    # pygame を初期化
    pygame.init()

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

    return (BASICFONT20, BASICFONT25, BASICFONT50,
text_title, text_game_rule, text_instructions,
text_game_over, text_press_key, text_title_center_point,
text_game_rule_center_point, text_instructions_center_point,
text_game_over_center_point, text_press_key_center_point)