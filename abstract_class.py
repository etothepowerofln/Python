from abc import ABC, abstractmethod

class Remote(ABC): #Creating the abstract class
    #Creating abstract methods
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
    
    #Creating abstract property
    @property
    @abstractmethod
    def brand(self):
        pass

    #Non-abstract methods can also be created
    def recharge(self):
        print("Recharging remote.")

class Remote_TV(Remote):
    #The children classes have to implement all the abstract methods
    def turn_on(self):
        print("Turning TV on.")

    def turn_off(self):
        print("Turning TV off.")

    #The children class also have to implement all the abstract properties
    @property
    def brand(self):
        return "LG"

    #Additional methods can be implemented, however
    def change_channel(self):
        print("Changing channel.")

r1 = Remote_TV()
print(f"TV brand: {r1.brand}")
r1.turn_on()
r1.change_channel()
r1.turn_off()
r1.recharge()