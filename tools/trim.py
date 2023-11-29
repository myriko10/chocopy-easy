from PIL import Image

# 画像を読み込む
input = Image.open('../horse_goes_home/pic/'
                   'title'
                   '.png')  # 画像のファイル名を適切に変更してください

# トリミングの範囲を指定
x1, y1, x2, y2 = 210, 65, 485, 240

# 画像をトリミング
cropped = input.crop((x1, y1, x2, y2))

# トリミングした画像を保存
cropped.save('title_horse_goes_home.png')  # 保存するファイル名を適切に変更してください
