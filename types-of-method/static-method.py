class A:

    def dis(self):
        print(self)

    @classmethod
    def cm(c):
        print(c)

    """static method does not take any parameters
    
    """

    @staticmethod
    def sm():
        print("static method")


obj1=A()
obj2=A()

obj1.dis()
obj2.dis()

obj1.cm()
obj2.cm()
A.cm()

obj1.sm()
obj2.sm()
