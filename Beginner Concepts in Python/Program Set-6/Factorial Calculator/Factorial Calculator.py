# PROGRAM TO CALCULATE THE FACTORIAL OF A GIVEN NUMBER

num = int(input('Please Enter a Number to get the Factorial : '))    # user-input fucntion

fact = 1          # initial value of the factorial

for i in range(1,num+1):   # for-loop with range
    fact = fact * i

print(f'The factorial of {num} is : {fact}.')