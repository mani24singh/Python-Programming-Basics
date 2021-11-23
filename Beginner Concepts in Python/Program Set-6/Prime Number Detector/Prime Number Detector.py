# PROGRAM TO FIND OUT WHETHER THE GIVEN NUMBER IS A PRIME NUMBER OR NOT

# asking user for a number as an input
num = int(input('Please enter a number to check whether it is a prime number : \n'))

prime = True     # keeping prime number value as true by default 

for i  in range(2,num):   # creating a for-loop with if-conditions for detecting a prime number
    if (num%i == 0):
        prime = False
        break

if prime:
    print('The given number is a prime number.')      
else:
    print('The given number is not a prime number.')
