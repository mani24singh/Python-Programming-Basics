# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT : Write a program to filter a list of numbers which are divisible by 5.
'''

l = [1, 2, 15, 255, 54, 67, 88, 76, 95, 10000, 124, 243, 555, 345]

a = filter(lambda a: a%5==0, l)
print(list(a))