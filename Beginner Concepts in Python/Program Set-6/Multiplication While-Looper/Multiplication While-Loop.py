# PROGRAM TO PRINT A MULTIPLICATION TABLE USING WHILE LOOP

# asking a number from user using an integer input function
num = int(input('please enter a number : '))

# a while loop for printing the multiplication table
i = 1
while i<11:
    print(f'{num}X{i}={num*i}')
    i = i+1
    
print('the required table has been printed.')
