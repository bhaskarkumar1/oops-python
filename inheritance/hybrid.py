# in hybrid there is combiation of hierarchial and other inherirtance
# basically it is made up of more than one type inheritance

class A:
    def __init__(self,a):
        self.a=a
    def disp(self):
        print(self.a)


class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def disp(self):
        super().disp()
        print(self.b)


class C(B):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c

    def disp(self):
        super().disp()
        print(self.c)


class D(B):
    def __init__(self,a,b,d):
        super().__init__(a,b)
        self.d=d

    def disp(self):
        super().disp()
        print(self.d)


obj1=D(1,2,3)
obj1.disp()

obj2=C(4,5,6)
obj2.disp()