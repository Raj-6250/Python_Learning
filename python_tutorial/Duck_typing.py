# "Duck typing" : Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                "if it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Dog is Barking")

class Cat(Animal):

    def speak(self):
        print("This is a cat")

class Car:
    alive = False
    def speak(self):
        print("This is a car")
animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)