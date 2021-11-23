# PROGRAM TO ELABORATE USE OF LAMBDA FUNCTION IN PYTHON

# def func(a):        ---> this whole function can be written in one line with lambda
#     return a+5

func = lambda x : x+5
square = lambda x : x*x
sum = lambda a,b,c : a+b+c

x = 7

print(func(x))  # prints 12
print(square(x))  # prints 49
print(sum(x,1,2))  # prints 10
