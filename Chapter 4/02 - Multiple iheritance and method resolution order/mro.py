class CommonBase:
    pass


class Base1(CommonBase):
    pass


class Base2(CommonBase):
    def method(self):
        print("Base2.method()が呼ばれた")


class MyClass(Base1, Base2):
    pass


if __name__ == "__main__":
    print("MyClassのMRO:", MyClass.__mro__)
