# super() = Function used in a child class to call methods from a parent class(SuperClass)
#           Allows you to extend the functionality of the inherited methods

class Base:
    def A(self):
        print("this is base class")
class Derived(Base):
    def B(self):
        print("this is derived class")
        super().A()

d=Derived()
d.B()


