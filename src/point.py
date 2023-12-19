"""座標を保持するPointクラス

x、y座標を保持する。
"""
class Point:
    """座標を管理する
    
    x、y座標を保持する。
    """

    # プレーヤーの座標を定義する
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 座標を文字列で返す
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 座標をタプルで返す
    def get_xy(self):
        """x,y座標をタプルで返す

        Returns:
            tuple: x,yの順
        """
        return (self.x, self.y)
     