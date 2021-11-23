# PROGRAM TO HANDLE EXCEPTION USING TRY WITH FINALLY CLAUSE

try:
    i = int(input('Enter the number : '))
    c = 1/i
    print(c)
except Exception as e:
    print(e)
    exit()

finally:                     # final clause executes in try and also in exception
    print('We are done.')

print('Thanks for using the program.')    # this statement doesnt execute if program goes for exception