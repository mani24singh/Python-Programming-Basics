# PROGRAM TO SUM TWO NUMBERS USING OBJECT ORIENTED PROGRAMMING

class Number:
    def sum(self):
        return self.a + self.b

num = Number()

num.a = 34
num.b = 56
s = num.sum()

print(s)
