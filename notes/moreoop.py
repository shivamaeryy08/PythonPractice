# to use inheritance add class Name(CLASSTOINHERITFROM) then add super().__init__() means the super class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def roar(self):
        print("roaring")


class Dog(Animal):
    def __init__(self):
        super().__init__()  # So Dog inherits from ANimal superclass, dog is suibclass

    def roar(self):
        super().roar()  # means do everything super class does here
        print("doggo is roaring its own way")

    def woof(self):
        print("Woof")


doggo = Dog()
doggo.woof()
doggo.roar()
