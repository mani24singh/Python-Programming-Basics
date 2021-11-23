# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT: Write a class Complex to represent complex numbers, along with overload
operators + and * which adds and multiplies them.
'''

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return complex(self.real + c.real , self.imaginary + c.imaginary)

# multiplication of complex numbers: (a+bi)(c+di)= (ac-bd)+(ad-bc)i
    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary     
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)         # addition
print(c1 * c2)         # multiplication

c3 = Complex(1, -4)
c4 = Complex(331, -37)
print(c3 + c4)
print(c3 * c4)

