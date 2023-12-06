import tkinter as tk
from PIL import Image, ImageTk

# 画像ファイルのパス
# image_path = '../images/horse_run1.png'
image_path = "../images/horse_run2.png"

if __name__ == '__main__':
    # 画像を開く
    image = Image.open(image_path)

    # Tkinterウィンドウを作成
    root = tk.Tk()
    root.title("マウス座標の表示")

    # 画像を表示するためのキャンバスを作成
    canvas = tk.Canvas(root, width=image.width, height=image.height)
    canvas.pack()

    # 画像をキャンバスに表示
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

    # マウス座標を表示するラベル
    label = tk.Label(root, text="")
    label.pack()

    # マウスの動きを監視する関数
    def update_mouse_position(event):
        x, y = event.x, event.y
        label.config(text=f"座標: ({x}, {y})")

    # マウスの動きをバインド
    canvas.bind("<Motion>", update_mouse_position)

    # Tkinterループを開始
    root.mainloop()