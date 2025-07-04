#multilevel_inheritance
class class1:
    def A(self):
        print("class1")
class class2(class1):
    def B(self):
        print("class2")
class class3(class2):
    pass

t=class3()
t.A()
t.B()