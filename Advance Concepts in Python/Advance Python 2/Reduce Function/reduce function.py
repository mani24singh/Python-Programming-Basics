# PROGRAM TO SHOWCASE THE USE OF REDUCE FUNCTION IN PYTHON

from functools import reduce

sum = lambda a,b : a+b

l = [1,2,3,4]

val = reduce(sum, l)
print(val)

