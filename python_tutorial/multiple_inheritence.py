# multiple inheritance = inherit from more than one parent class child(parent1,parent2)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B)<-B(A)<-A

#multiple inheritance
class Parent1:
    def A(self):
        print("parent1")

class Parent2:
    def B(self):
        print("parent2")
class child1(Parent1,Parent2):
    pass

child=child1()
child.A()
child.B()

