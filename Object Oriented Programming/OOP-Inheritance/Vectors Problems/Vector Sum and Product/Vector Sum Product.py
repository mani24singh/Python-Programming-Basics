# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT : Write a class vector representing a vector of n dimension. 
Overload the + and * operator which calculates the sum and the dot product of them. 
'''

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] + vec2.vec[i]
        return sum

v1 = Vector([1, 4, 6])    # we can also take a huge vector here like Vector([1,2,3,5,7,4])
v2 = Vector([1, 6, 9])

print(v1 + v2)     # vector quantity

print(v1 * v2)     # scaler quantity

