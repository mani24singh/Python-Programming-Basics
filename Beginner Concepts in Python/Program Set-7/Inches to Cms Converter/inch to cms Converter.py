# PROGRAM TO CONVERT A VALUE FROM INCHES TO CENTIMETERS

num = int(input('Enter a number to convert it from inchs to cms : '))

def conv(n):
    inch = n*2.54
    return inch

result = conv(num)
print(f'The conversion result is {result} cms.')