import random
from datetime import date

class Student:
    school = "UNI" #Class variable

    def __init__(self, name, age, nr):
        self.__name = name #Instance variables (different for each object)
        self.__age = age
        self.__nr = nr

    def __str__(self):
        return f"{', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

    #Constructs the class from birth year
    @classmethod
    def from_b_year(cls, name, year, nr):
        return cls(name, date.today().year - year, nr)

    #Checks if matriculation is valid
    @staticmethod
    def is_student(number):
        return random.choice(['yes', 'no'])
    
student1 = Student("Will", 14, 2342)
student2 = Student.from_b_year("Jess", 2012, 1422)

print(student1)
print(student2)

print("Is 5467 a valid matriculation?", Student.is_student(5467))