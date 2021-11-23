# PROGRAM TO FIND THE SUM OF FIRST N-NATRUAL NUMBERS USING WHILE-LOOP

num = int(input('Enter a number :\n'))   # creating an input function
x = num
if num<0:                                     # the entered number is a negative number print a warning
    print('Please enter a positive number.')
else: 
    sum = 0

while (num>0):                    # while loop to calculate addition of the natural nos.
    sum += num
    num -= 1
    
print('The sum of First',x,'natural number is: ',sum)  
'''
other way to print result using f-string:
# print(f'The sum of first {n} natural-number is :',sum)
'''

# **************************************************************

'''
Note:
Another way to print a sum of n-natural number is using a mathematical formula:
sum = n(n+1)/2
synatx:

n = int(input('Please enter a number: '))
sum = (n*(n+1))/2
print('The sum of numbers is : ', sum )
'''

