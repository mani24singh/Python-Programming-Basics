# Program to solve the following problem statement
'''
Problem Statement: Write a class train which has methods to book a ticket, get status(no. of seats) and get 
fare information of trains running under indian railways.
'''


class Train:
  
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f'The name of the train is : {self.name}')
        print(f'The total seats available in the train are : {self.seats}')

    def fareInfo(self):
        print(f'The total fare of the ticket is INR: {self.fare}')

    def bookTicket(self):
        if(self.seats>0):
            print(f'Your ticket has been booked and your seat number is : {self.seats}')
            self.seats = self.seats - 1
        else:
            print('Sorry this train is full, Kindly try in tatkal.')

    def cancelTicket(self, seatNo):
        pass


raj = Train('Rajdhani Express : 12430', 2500, 300)
raj.getStatus()
raj.bookTicket()
raj.fareInfo()

print('###########################################################')

shat = Train('Shatabdi : 12019', 1500, 150)
shat.getStatus()
shat.bookTicket()
shat.bookTicket()
shat.fareInfo()
