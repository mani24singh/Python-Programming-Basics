# PROGRAM TO USE OPERATOR-OVERLOADING IN PYTHON

class Number:
    def __init__(self, num):
        self.num = num 

    def __add__(self, num2):                     # operator overloading for addition
        print('Lets add the number.')
        return self.num + num2.num


    def __mul__(self, num2):                     # operator overloading for multiplication
        print('Lets multiply the number.')
        return self.num * num2.num


n1 = Number(14)       # number is not an integer instead it is an object of an class Number
n2 = Number(8)

sum = n1 + n2
print(sum)

mul = n1 * n2
print(mul)
