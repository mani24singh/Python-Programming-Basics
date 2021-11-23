# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT: Create a class Employee and add salary and increment properties to it.
Write a method salaryAfterIncrement method with a @property decorator with a setter which
changes the value of increment based on the salary.
'''

class Employee:
    company = 'Facebook'
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary      # salaryAfterIncrement = Salary * increment

e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)

e.salaryAfterIncrement = 3000
print(e.increment)

