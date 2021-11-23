# # PROGRAM BASED ON LOGIC OF USING SUPER-CLASS METHOD

class Person:
    country ='India'
    def takeBreath(self):
        print('I am breathing....')

class Employee(Person):
    company = 'Honda'

    def getSalary(self):
        print(f'Salart is {self.salary}')
    
    def takeBreath(self):
        super().takeBreath()
        print('I am an Employee so I am Luckily Breathing..')

class Programmer(Employee):
    company = 'Fiverr'

    def getSalary(self):
        print(f'No salary to programmers')

    def takeBreath(self):
        super().takeBreath()
        print('I am a Programmer so i am breathing++')

p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()