class Point:
    x: int
    y: int

    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(0, 0):
            print("原点")
        case Point(0, y):
            print(f"Y={y}")
        case Point(x, 0):
            print(f"X={x}")
        case Point():
            print("それ以外のどこか")
        case _:
            print("点ではありません")

if __name__ == "__main__":
    where_is(Point(1, 20))
    where_is(Point(20, 0))
    where_is(Point(0, 20))
