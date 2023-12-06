from coodinate_checker import image_path
from PIL import Image

input_path = image_path
# input_path = './img/'+''+'.png'
output_path = './newimg/'+'horse_run2'+'.png'

# clopする領域の座標指定
left = 10
top = 15
right = 135
bottom = 155

def crop_and_save_image(input_path, output_path, left, top, right, bottom):
    """
    指定された座標で画像を切り取り、指定されたパスに保存する関数。

    Parameters:
    - input_path: 元画像のファイルパス
    - output_path: 切り取った画像を保存するファイルパス
    - left, top, right, bottom: 切り取る範囲の座標

    Example:
    crop_and_save_image('input.jpg', 'output.jpg', 100, 100, 300, 300)
    """
    # 画像を開く
    img = Image.open(input_path)

    # 指定された座標で画像を切り取る
    cropped_img = img.crop((left, top, right, bottom))

    # 切り取られた画像を保存する
    cropped_img.save(output_path)

print('-------CROP----------')
print('input path:'+input_path)
print('new image size')
print('width='+str(right-left)+' height='+str(bottom-top))
print('output path:'+output_path)
if input('execute? y/n: ').lower() == 'y':
    crop_and_save_image(input_path, output_path, left, top, right, bottom)
    print('保存しました')
