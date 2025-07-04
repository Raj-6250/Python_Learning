# Inheritance = Allow a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Class(Parent)

class Animal :
    def __init__(self,name,food):
        self.name=name
        self.food=food

    def eat(self):
        print(f"{self.name} eats {self.food}")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Herbivore(Animal):
    pass
class Omnivore(Animal):
    pass
class Carnivore(Animal):
    pass

cow1=Herbivore("Cow","grass")
dog1=Omnivore("Dog","flesh and grass")
lion=Carnivore("Lion","meat")

cow1.eat()
dog1.eat()
lion.eat()
cow1.sleep()
dog1.sleep()
lion.sleep()