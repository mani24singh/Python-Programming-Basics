# PROGRAM TO PRINT THE FOLLOWING STAR-PATTERN USING FOR-LOOP IN PYTHON
'''
SIMPLE-NUMBER PATTERN DISPLAYING NUMBER OF ROWS:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n = int(input('Enter the number of rows: '))

for row in range(1,n+1):
    for column in range(1,row+1):
        print(column, end=' ')
    print()

