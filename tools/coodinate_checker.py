import tkinter as tk
from PIL import Image, ImageTk

# 画像を読み込む
input_image = Image.open('../horse_goes_home/pic/'
                         'title'
                         '.png')  # 画像のファイル名を適切に変更してください
img_width, img_height = input_image.size

# 新しいウィンドウを作成
window = tk.Tk()
window.title("Image Viewer")

# 画像を表示
image_tk = ImageTk.PhotoImage(input_image)
label = tk.Label(window, image=image_tk)
label.pack()

# マウス座標を表示するラベル
coord_label = tk.Label(window, text="X: 0, Y: 0")
coord_label.pack()

# マウスの座標を取得する関数
def update_coordinates(event):
    x, y = event.x, event.y
    coord_label.config(text=f"X: {x}, Y: {y}")

# マウスイベントを追跡
label.bind("<Motion>", update_coordinates)

# ウィンドウを表示
window.mainloop()