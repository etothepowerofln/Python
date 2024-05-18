class Fibonacci:  # Creating an iterable class
    def __init__(self, max=100):
        self.x, self.y = 0, 1
        self.max = max

    def __iter__(self):  # Object to be iterable
        return self  # The iterable object is itself

    def __next__(self):
        if self.x > self.max:  # Condition to stop iteraton
            raise StopIteration  # To stop iteration, raise StopIteration
        value, self.x, self.y = self.x, self.y, self.x + self.y
        return value


fibonacci = Fibonacci()
for i in fibonacci:
    print(f"{i}", end=" ")
print("- Iterator")


def fibonacci_generator(max=100):  # Creating a generator
    x, y = 0, 1
    while x < max:
        yield x  # Generators use yield instead of return. That's it.
        x, y = y, x + y


for i in fibonacci_generator():
    print(f"{i}", end=" ")
print("- Generator")
