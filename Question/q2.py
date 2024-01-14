"""create a list class having the functionality:
    insert at end
    insert at begin

    del end

    del begin

    dispaly"""

class List:

    def __init__(self):
        self.ls=[]

    def insertatend(self,value):
        self.ls.append(value)
    def insertatbegin(self,value):
        self.ls.insert(0,value)

    def delend(self):
        self.ls.pop()

    def delbegin(self):
        if len(self.ls)!=0:
            self.ls.remove(self.ls[0])

    def disp(self):
        print(*self.ls)

obj=List()
obj.insertatend(12)
obj.insertatbegin(14)
obj.insertatbegin(13)
obj.disp()
obj.delbegin()
obj.delend()
obj.disp()