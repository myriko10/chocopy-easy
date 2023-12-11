class Point:
    # プレーヤーの座標を定義する
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 座標を文字列で返す
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # 座標をタプルで返す
    def get_xy(self):
        return (self.x, self.y)