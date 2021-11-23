# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
Problem: write a python program to rename a file to "renamed_by_python.txt".
Solution: Here we copy the content of the oldfile to new file and then delete the oldfile 
using os module remove function.
'''

import os   # os module contains a function to remove a file

oldname = "sample.txt"
newname = "renamed_by_python.txt"

with open(oldname, encoding='utf-8') as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)