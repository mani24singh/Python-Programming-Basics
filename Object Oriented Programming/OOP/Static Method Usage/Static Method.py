# Program to solve the following problem statement
'''
Problem Statement: Write a program with a class name Calculator capable of finding 
square, sqaureroot and cube of a number and also add a static method to greet the user.
'''


class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f'The square of the number {self.number} is : {self.number **2}')

    def cube(self):
        print(f'The cube of the number {self.number} is : {self.number **3}')

    def squareRoot(self):
        print(f'The squareroot of the number {self.number} is : {self.number **0.5}')

    @staticmethod
    def greet():
        print('******* Hello, welcome to My-Calculator.**********')



a = Calculator(9)
a.greet()
a.square()
a.cube()
a.squareRoot()

