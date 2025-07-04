#  @property = Decorator used to define a method as a property (it can be accessed like an attribute )
#              Benefit : Add additional logic when read, write or delete attributes
#              Gives you getter, setter, deleter method

class Rectangle:
    def __init__(self,length,width):
        self._length=length
        self._width=width
    @property
    def length(self):
        return f"{self._length : .1f}cm"

    @property
    def width(self):
        return f"{self._width : .1f}cm"

    @length.setter
    def length(self,new_length):
        if new_length >0:
            self._length =new_length
        else:
            print("length must be greater than zero")

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width=new_width
        else:
            print("width must be greater than zero")

    @length.deleter
    def length(self):
        del self._length
        print("length has been deleted")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

p1 = Rectangle(3,2)
# print(p1._width,p1._length) here we are accessing private member of class

p1.length=0
p1.width=10
print(p1.length)
print(p1.width)
del p1.length #length attribute has been deleted
del p1.width  #width attribute has been deleted









