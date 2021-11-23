# PROGRAM BASED ON LOGIC OF USING SINGLE-INHERITANCE

class Employee:
    company = 'Google'
   
    def showDetails(self):
        print('This is an employee.') 

class Programmer(Employee):
    language = 'Python'
    # company = 'Youtube'    # if we use this line, then the company attribute is overwritten to Youtube

    def getLanguage(self):
        print('This is an programmer.')

e = Employee()
e.showDetails()    
p = Programmer()
p.showDetails()
p.getLanguage()
print(p.company)
    