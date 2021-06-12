def add(*args):
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(1,2,3)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nisan", model="GT-R")
print(my_car.model)
