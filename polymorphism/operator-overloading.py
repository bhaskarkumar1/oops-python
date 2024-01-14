class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        return self.a+ o.a


obj1=A(9)
obj2=A(1)

print(obj1+obj2)
