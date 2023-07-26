class RevealAccess(object):
    """A data descriptor that sets and returns values
    normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name="変数"):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("取得:", self.name)
        return self.val

    def __set__(self, obj, val):
        print("更新:", self.name)
        self.val = val

    def __delete__(self, obj):
        print("削除:", self.name)


class MyClass(object):
    x = RevealAccess(10, '変数"x"')
    y = 5


if __name__ == "__main__":
    m = MyClass()
    m.x
    m.x = 20
    m.x
    del m.x
