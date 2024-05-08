class Animal:
    def nr_legs(self):
        print("unspecified")

class Human(Animal):
    def nr_legs(self):
        print("Humans have 2 legs")

class Dog(Animal):
    def nr_legs(self):
        print("Dogs have 4 legs")
    
def count_legs(obj):
    obj.nr_legs()

count_legs(Animal())
count_legs(Human())
count_legs(Dog())