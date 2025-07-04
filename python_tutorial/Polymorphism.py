# Polymorphism = Greek word that means to "have many forms or faces"
#         Poly = Many
#       Morphe = Form
# Method_Overloading # Operator_Loading #

##  Two way to achieve polymorphism
  # 1.) Inheritance = An object could be treated of the same type as a parent class
  # 2.) "Duck Typing" = Objects must have necessary attributes/methods

from abc import ABC,abstractmethod

class Shape:
    @abstractmethod

    def area(self):
        pass

class  Rectangle(Shape):
    def __init__(self,length,width):
        self.length =length
        self.width =width

    def area(self):
        return self.length * self.width
class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side *self.side
shapes=[Square(5), Rectangle(3,5)]
for shape in shapes:
    print(shape.area())
# square =Square(5)
# print(square.area())
