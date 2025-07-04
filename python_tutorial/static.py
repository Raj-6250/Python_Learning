# static methods = A method that belongs to a class rather than any object from that class(instance)
#                  Usually used for general utility functions


# Instance method = Best for operations on instances of the class (objects)
# Static method =  Best for utility function that do not need access to class data
class Parent:
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    @staticmethod
    def get_info(name,age):
        print(f"{name} is {age} year old")


Parent.get_info("Raj",18)