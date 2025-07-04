# Exception = An event that interrupts the flow of a program (ZeroDivisionError, TypeError, ValueError)
#             1.) try  2.)except  3.)finally

# Exception         	Description
# ZeroDivisionError  	Raised when a number is divided by zero.
# TypeError         	Raised when an operation is performed on an incompatible type.
# ValueError	        Raised when a function gets an argument of the right type but invalid value.
# IndexError	        Raised when trying to access an index that does not exist.
# KeyError	            Raised when a dictionary key is not found.
# FileNotFoundError	    Raised when trying to open a non-existent file.
# ImportError	        Raised when an import statement fails.
# AttributeError    	Raised when an invalid attribute is accessed.
# NameError         	Raised when a variable is not defined.
# IndentationError	    Raised when incorrect indentation is used.

try:
    number = int(input("Enter a number : "))
    print(1/number)
except ZeroDivisionError:
    print("you can't divide by zero ! ")
except ValueError:
    print("Enter only number plz!")
except Exception as e:
    print("Something went wrong")

try:
    int("abc")
except Exception as e:
    print(e)

finally:
    print("this is finally bolck")
