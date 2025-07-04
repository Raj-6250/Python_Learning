# Magic Methods = Dunder Method (double underscore) __init__, __str__, __eq__, __gt__
#                 They are automatically called by many of the Python's built-in operations.
#                 They allow developers to define or customize the behaviour of object

class Student:
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa

    def __str__(self):
        return f"{self.name} : {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa
    def __add__(self, other):
        return self.gpa+other.gpa
    def __contains__(self, item):
        return item in self.name


s1=Student("Raj" ,7.0)
s2=Student("Shreem",8)
print(s1,s2)
print(s1==s2)
print(s1<s2)
print(s1 + s2)
print("Raj" in s1)
