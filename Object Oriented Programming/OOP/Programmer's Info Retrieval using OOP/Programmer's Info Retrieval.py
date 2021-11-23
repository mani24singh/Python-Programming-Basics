# Program to solve the following problem statement
'''
Problem Statement: Write a program with class name as (Programmer) for storing information 
of a few programmers working at microsoft.
'''


class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f'The Name of the {self.company} programmer is {self.name} and the product is {self.product}')


mani = Programmer("Mani", 'Skype')
ruchi = Programmer("Ruchi", 'Github')
mani.getInfo()
ruchi.getInfo()

