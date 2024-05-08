class Vehicle:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

class Car(Vehicle):
    def __init__(self, nr_wheels, **kw):
        self.nr_wheels = nr_wheels
        super().__init__(**kw)

class Boat(Vehicle):
    def __init__(self, used_for_fishing, **kw):
        self.used_for_fishing = used_for_fishing
        super().__init__(**kw)

#Simple inheritance
class Van(Car):
    pass

#Multiple inheritance
class Amphicar(Car, Boat):
    def __init__(self, **kw):
        super().__init__(**kw)

van = Van(size="big", nr_wheels=4)
print(van)

amphicar = Amphicar(size="medium", nr_wheels=0, used_for_fishing=False)
print(amphicar)

class Father:
    def who_is(self):
        print(self.__class__.__name__)

class Son(Father):
    def who_is(self):
        super().who_is()

jake = Son()
print("Father, Son, or jake? ", end="")
jake.who_is()