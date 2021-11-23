# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
PROBLEM STATEMENT : Write a program to display a/b where a and b are integers.
If b=0, display infinte by handling the ZeroDivisionError.
'''
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

try:
    print(a/b)
except:
    print('Infinite.')
