# PROGRAM TO BUILT A ITERATIVE-FACTORIAL FUNCTION

# user-input fucntion
p = int(input('Please Enter a number to get the factorial: '))

# defining a function for factorial with argument (as n)
def factorial_iter(n):
    product = 1      
    for i in range(1,n):    
        product = product * (i+1)
    return product    

print(factorial_iter(p))

