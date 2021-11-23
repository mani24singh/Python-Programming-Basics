# PROGRAM TO HANDLE THE CUSTOMISED EXCEPTION USING RAISE KEYWORD
 
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError('This is not a suitable value.')

a = input('Please enter a number : ')
inc = increment(a)

print(inc)