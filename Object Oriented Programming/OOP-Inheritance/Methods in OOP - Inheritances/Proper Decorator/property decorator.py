# PROGRAM TO USE PROPERTY DECORATOR IN THE PYTHON SCRIPT

class Employee:
    company = 'Times of India'
    salary = 5500
    salarybonus = 800
    # totalSalary = 6300  # we will built a property to make this changes automatic


    @property                              # this method is also called as getters-method
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)