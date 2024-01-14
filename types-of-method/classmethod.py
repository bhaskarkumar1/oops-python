class A:
    a=20
    b=30

    @classmethod
    def disp(cls):
        print(cls.a,cls.b)

    @staticmethod
    def disp2():
        print(A.a,A.b)

z=A()
z.disp()
z.disp2()