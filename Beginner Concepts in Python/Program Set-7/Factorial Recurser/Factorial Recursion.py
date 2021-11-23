# PROGRAM TO BUILT A RECURSIVE-FACTORIAL FUNCTION 

u = int(input('Enter a number to get the Factorial: '))

def factorial_recur(n):
    if n==0 or n==1:
        return 1
    else:
        r = n * factorial_recur(n-1)
        return r

k = factorial_recur(u)
print(k)
