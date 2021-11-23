# PROGRAM TO SHOWCASE USE OF A CLASS METHOD IN PYTHON

class Employee:
    company = 'Nestle'
    salary = 150000
    location = 'Jaipur'

    '''
# It adds a new instance attribute, instead of changing the class attribute of salary :
    def changeSalay(self, sal):      
        self.salary = sal
'''

# Inorder to change the class attribute of salary we use the following:
    
    # def changeSalary(self, sal):
    #        self.__class__.salary = sal   #----> dunder class method

    @classmethod                     # class method decorator 
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
print(Employee.salary)

e.changeSalary(360000)    # changing the class attribute salary
print(e.salary)     

