class Cat:
    def __init__(self, age):
        self.age = age

    def sound(self):
        print("야옹")

class Dog:
    def __init__(self, age):
        self.age = age

    def sound(self):
        print("멍멍")

Dubo = Cat(3)
Dubo.sound()

Bug = Dog(3)
Bug.sound()