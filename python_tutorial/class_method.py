# class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter , which represents the class itself.

# Instance methods = Best for operations on instances of the class(object)
# Static method  = Best for utility functions that do not need access to the class data
# Class methods = Best for class-leval data or require access to the class itself
class Student:
    count =0
    total_cgpa=0

    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        Student.count +=1
        Student.total_cgpa +=cgpa

    # Instance method
    def get_info(self):
         return f"{self.name} : {self.cgpa}"


    # Class Method
    @classmethod
    def get_average_cgpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_cgpa / cls.count}"

s1=Student("Raj" ,8)
s2=Student("Rahul" ,10)
s3=Student("Ramu" ,9)
print(Student.count)
print(Student.get_average_cgpa())



