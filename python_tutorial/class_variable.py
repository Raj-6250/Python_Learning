# class variable : Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from the class

class Student:

    class_year=2025  # this is a class variable
    num_student=0

     #this is a constructor
    def __init__(self,name,age,course):
        self.identity=name
        self.old=age
        self.course=course
        Student.num_student +=1

# there is no need to call a constructor because it is automatically  call when object of class is created
student1=Student("Raj",18,"cse")
print(student1.identity)
print(student1.old)
print(student1.course)
print(f"total strength : {Student.num_student}" )

#we can access class variable directly by class name dot class variable name (Student.class_year)
print(Student.class_year)



