def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("add sprinkler")
        func(*args,**kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You add fudge")
        func(*args,**kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def ice_cream(flavour):
    print(f"here's your {flavour} ice cream")

ice_cream("Vanilla")