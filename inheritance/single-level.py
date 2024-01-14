# in single level only two classes is there one is parent class and one child class
#
# the child classs inherit the property from the only one parent class

class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print("area", self.a * self.b)


class square(rectangle):
    def __init__(self, a):
        super().__init__(a, a)


s = square(4)
s.area()

s2=rectangle(4,12)
s2.area()
