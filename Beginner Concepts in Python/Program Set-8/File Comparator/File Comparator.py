# PROGRAM TO SOLVE THE PROBLEM STATED BELOW
'''
Problem statement: Program to find out whether a file is identical and 
matches the content of another file.
'''

file1 = 'myfile.txt'
file2 = 'copy.txt'

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print('The files are identical.')
else:
    print('The files are not identical.')