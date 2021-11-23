# PROGRAM TO HANDLE DIFFERENT EXCEPTIONS

try:
    a = int(input('Enter a number : '))
    c = 1/a
    print(c)

except ValueError as e:
    print('Please add a valid value as input.')

except ZeroDivisionError as e:
    print('Please make sure you are not dividing by 0.')

except:
    print('Your input occured some error.')

print('Thanks for using this code.!!!')