# PROGRAM TO PRINT A SUM OF N-NATURAL NUMBERS USING RECURSIVE FUNCTION

num = int(input('Enter the number: '))

def sum_recur(n):
    if n<=1:
        return n
    else:
        r = n + sum_recur(n-1)
        return r
if num<0:
    print('Enter a positive number')
else:
    print('The sum is ', sum_recur(num))