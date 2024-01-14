# in multiple ineritance at there is child class inheriting the property from more than one parent class
# the order of accessibilty is defined by mro


class A:
    def disp(self):
        print("Class A")
        super().disp()

class B:
    def disp(self):
        print("Class B")

class C(A,B):
    pass



obj=C()
obj.disp()
