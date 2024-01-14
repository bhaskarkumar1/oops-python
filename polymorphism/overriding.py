

class rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        print(self.l*self.w)


class sqr(rect):

    def __init__(self,a,l,w):
        super().__init__(l,w)
        self.a=a

    def area(self):
        print(self.a*self.a)

obj=sqr(1,2,3)
obj.area()