#object = A bundle of related attributes (variables) and methods (functions)
#         Ex. phone,cup,book
#         You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
# __init__ Method: The __init__ method is used to initialize the object's state when it is created.
# Attributes: In this example, model, year, color, and for_Sale are the attributes of the Car class.
# Object (car1): When you create an instance of the class (car1), you assign values to these attributes.
class Car:
    #constructor
    def __init__(self,model,year,color,for_Sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_Sale=for_Sale
    #method
    def drive(self):
        print(f"you are driving {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

car1 = Car("BMW", 2020, "Red" , False)
car2= Car("fortuner",2024,"white",True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_Sale)
car1.drive()
car1.stop()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_Sale)
car2.drive()
car2.stop( )