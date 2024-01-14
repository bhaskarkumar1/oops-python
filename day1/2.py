class Box:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def area(self):
        area=self.a*self.b
        print(area)

b= Box(1,2)
b.area()
