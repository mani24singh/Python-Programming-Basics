# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT: A list contains the multiplication table of 7. Write a program to convert it to
a vertical string of same number.
'''

l = [str(i*7) for i in range(1,11)]
print(l)

verticalTable = "\n".join(l)
print(verticalTable)