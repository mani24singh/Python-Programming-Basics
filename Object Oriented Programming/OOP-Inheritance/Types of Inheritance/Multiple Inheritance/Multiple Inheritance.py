# PROGRAM BASED ON LOGIC OF USING MULTIPLE-INHERITANCE

class Employee:
    company = 'Visa'
    eCode = 120
     
class Freelancer:
    company = 'Fiver'
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
 
class Programmer(Employee, Freelancer):  # the class that is written first gets the priority
    name = 'Mani'

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)




