# # PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
Problem statement : Create a class pets from a class animals and further create class dog
from pets. Add a method bark to class dog.
'''

class Animals:
    animalType = 'Mammal'

class Pets(Animals):
    color = 'White'

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!!!!")

d = Dog()
d.bark()
print(d.color)
print(d.animalType)