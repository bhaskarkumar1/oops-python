# the all n-1 classes will have the same parent
# only parent is there  and other is child


class person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def disp(self):
        print(self.name,self.age,self.city)


class student(person):
    def __init__(self,name, age,city,school, std):
        super().__init__(name,age,city)
        self.school=school
        self.std=std

    def disp(self):
        super().disp()
        print(self.school,self.std)


class employee(person):
    def __init__(self,name,age,city,company,salary):
        super().__init__(name,age,city)
        self.company=company
        self.salary=salary

    def disp(self):
        super().disp()
        print(self.company,self.salary)


obj1=employee("Bhaskar", 23,"hyd","ibm",50000)
obj1.disp()

obj2=student("Bhaskar Kumar", 23.00,"hyd","ibm","b.tech")
obj2.disp()