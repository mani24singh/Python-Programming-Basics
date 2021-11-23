# PROGRAM TO SHOWCASE SETTERS METHOD IN PYTHON

class Employee:
    company = 'Times of India'
    salary = 5500
    salarybonus = 800
    # totalSalary = 6300  # we will built a property to make this changes automatic


    @property                              # this method is also called as getters-method
    def totalSalary(self):
        return self.salary + self.salarybonus


    @totalSalary.setter       
    def totalSalary(self, val):
        self.salarybonus = val - self.salary     # setting changes to salary bonus depending on value of totalsalary
        

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800        # here, we initiate changes to bonus through totalSalary
print(e.salary)
print(e.salarybonus)