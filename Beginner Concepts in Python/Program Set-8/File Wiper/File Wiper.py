# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
##########################################################################################
PROBLEM STATEMENT: Create a program to display the content of a text file and then wipe out
the content of the text file using python.
##########################################################################################
'''
with open('123file.txt') as f:
    read = f.read()
    print(read)

with open('123file.txt', 'w') as f:
    f.write("")
    print('\n And Now the content of the file has been erased.')
    