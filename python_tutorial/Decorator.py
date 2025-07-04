# Decorator = A function that extends the behaviour of another function without modifying the base function
#             Pass the base function as an argument to the decorator

def decorate(func):
    def wrapper():
        print("before the base function called ")
        func()
        print("after the base function called")
    return wrapper
@decorate
def base():
    print("hello dear")

base()