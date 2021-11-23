# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT: Write a program to find the maximum of the numbers in a 
list using the reduce function.
'''

from functools import reduce

l = [3, 8, 4, 2, 5]

a = reduce(max,l)

print(a)