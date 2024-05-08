class Bike:
    def __init__(self, brand, color, year, price):
        print("PYTHON: class instance inicialized.")
        self.brand = brand
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return f"new object {self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

    def __del__(self):
        print("PYTHON: class instance deleted")

    def run(self):
        print(f"{self.brand} {self.color} running...")

    def stop(self):
        print(f"{self.brand} {self.color} stopped.")

bike1 = Bike("condor", "red", 2002, 200)
bike2 = Bike("monaco", "grey", 2004, 400)
bike3 = Bike("pro-x", "yellow", 2004, 450)

print(bike1)
Bike.run(bike1)
Bike.stop(bike1)
del bike1

print(bike2)
bike2.run()
bike2.stop()

print(bike3)
bike3.run()
bike3.stop()