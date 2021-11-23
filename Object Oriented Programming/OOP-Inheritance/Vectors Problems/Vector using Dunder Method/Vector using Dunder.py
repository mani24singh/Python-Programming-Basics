# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT : write __str__() method to print the vector as follows:
7icap + 8jcap + 10kcap
Assume vector of dimension 3 for this problem.
'''

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = Vector([7, 8, 10])
v2 = Vector([1, 3, 7])
print(v1)
print(v2)

