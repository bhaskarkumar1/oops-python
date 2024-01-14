""" create a class that contain name age phonenumber address as a data member and
 display as a member function"""


class Person:
    def __init__(self, name, age, phno, address):
        self.name = name
        self.age = age
        self.phno = phno
        self.address = address

    def display(self):
        print(self.name, self.age, self.phno, self.address)


p = Person("Bhaskar", 23, 9060000, "HYD")
p.display()
