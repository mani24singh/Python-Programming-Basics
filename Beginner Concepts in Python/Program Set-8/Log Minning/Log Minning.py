# PROGRAM TO SOLVE THE FOLLOWING PROBLEM
'''
PROBLEM STATEMENT: write a program to mine a log file and find whether it contains the 
'python' word. Also, the program should be able to give the line number where the python 
word is present in the given log text file.
'''
content = True
i = 1 

with open('logfile.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i+=1