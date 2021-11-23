# PROGRAM TO PRINT NUMBERS FROM USER USING A WHILE LOOP

## input function to get starting number of loop from the user
s = int(input('Please enter the starting number :\n'))

## input function to get the loop ending number
e = int(input('Please enter the ending number :\n'))

## Using while loop for printing the numbers required
while s<=e:
    print(s)
    s = s + 1

## printing a message to indicate the looper is completed
print('The required looping is completed.')