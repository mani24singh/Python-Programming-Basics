# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
Problem statement : Create a class C2d-vector and use it to create another class 
representing a C3d-vector.
'''

class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(3, 4)
v3d = C3dVec(1, 5, 8)
print(v2d)
print(v3d)