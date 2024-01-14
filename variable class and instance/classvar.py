"""these are the variable outside the constructor, function and inside the class
    these can be access through class reference"""


class classvar:
    c=40
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def display(self):
        print(self.a,self.b,self.c)

d= classvar(12,15)
d.c=90
d.display()
