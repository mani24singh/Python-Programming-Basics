# Program to solve the following problem statement
'''
Problem Statement: Create a class with a class attribute (a); create an object from it
and set a directly using objecta a = 0. Does this change the class attribute?...
'''


class Sample:
    a = "Mani"


obj = Sample()
obj.a = "Rahul"

print(Sample.a)
print(obj.a)

'''
Answer: The answer is Nope, the class attribute doesnt change. Instead it adds a 
new instant-attribute for the object along with the class-attribute.

Suppose, if we wish to change the class attribute we can do it by providing the 
following:

sample.a = "Rahul"   then it changes the class attribute by giving output as Rahul 
instead of "Mani".
'''
