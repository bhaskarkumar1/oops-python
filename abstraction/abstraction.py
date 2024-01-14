# hiding the complex details and providing only the necessary details to the user
from abc import abstractmethod


class shape:

    @abstractmethod
    def area(self,l,b,h=1):
        pass


class rect(shape):

    def area(self,w,l,h=1):
        print(w*l)


c=rect()
c.area(1,2)
