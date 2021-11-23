# PROGRAM TO USE OTHER DUNDER/ MAGIC METHODS IN PYTHON

class Number:
    def __init__(self, num):
        self.num = num 

    def __str__(self):           # use to return true value of the object
        return f"Decimal Number: {self.num}"

    def __len__(self):        # use to return the length of object
        return 1

n = Number(9)
print(n)

print(len(n))