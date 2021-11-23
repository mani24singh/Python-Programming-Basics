# PROGRAM TO PRINT THE STAR PATTERN AS BELOW USING NESTED FOR-LOOP
'''
* * *
*   *
* * *
'''

for row in range(0,3):   
    for col in range(0,5): 
        if (row==0 and col%2==0) or (row==2 and col%2==0)  or (row==1 and col%4==0):
            print("*",end="")
        else:
            print(end=" ")
    print()

