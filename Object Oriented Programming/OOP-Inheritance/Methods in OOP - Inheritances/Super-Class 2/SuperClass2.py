# # PROGRAM BASED ON LOGIC OF USING SUPER-CLASS METHOD using (INIT) CONSTRUCTOR

class Person:
    country ='India'
    def __init__(self):
        print('Initializing person....\n')

class Employee(Person):
    company = 'Honda'

    def __init__(self):
        super().__init__()
        print('Initializing Employee....\n')

    def getSalary(self):
        print(f'Salart is {self.salary}')
    
    def takeBreath(self):
        super().takeBreath()
        print('I am an Employee so I am Luckily Breathing..')

class Programmer(Employee):
    company = 'Fiverr'

    def __init__(self):
        super().__init__()
        print('Initializing Programmer....\n')

    def getSalary(self):
        print(f'No salary to programmers')

    def takeBreath(self):
        super().takeBreath()
        print('I am a Programmer so i am breathing++')

pr = Programmer()
