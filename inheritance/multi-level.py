"""supppose three classes are there A B C ,
now B inheriting the proprty from A and the C inheriting the property from B"""


class A:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def disp(self):
        print("class A",self.a,self.b,end="")


class B(A):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def disp(self):
        super().disp()
        print("class B",self.c,end="")


class C(B):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d

    def disp(self):
        super().disp()
        print("class c",self.d,end="")


obj=C(1,2,3,4)
obj.disp()