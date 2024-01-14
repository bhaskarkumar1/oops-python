class Test:
    def display(self):
        print("Google")


class Test1(Test):
    def display(self):
        super().display()
        print("Firefox")
t=Test1()
t.display()


# the deafult constructor is
# def __inti__(self):
#     pass