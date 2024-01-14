""" ? Question ::create a stack class that implement push, pop, isempty ,peek oprsn"""

class stack:

    def __init__(self):
        self.s=[]
    def push(self,element):
        self.s.append(element)

    def pop(self):
        if len(self.s)!=0:

            self.s.remove(self.s[-1])

    def isempty(self):
        if len(self.s)==0:
            print(True)
            return True
        print(False)
        return False
    def peek(self):
        if len(self.s)!=0:
            print(self.s[-1])

    def disp(self):
        print(* self.s)

z=stack()
z.pop()
z.push(1)
z.push(2)
z.push(3)
z.pop()
z.disp()
# z.isempty()
z.peek()