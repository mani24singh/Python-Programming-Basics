# Program to solve the following problem statement
'''
Problem Statement: Write a class train which has display the booking chart 
information of trains running under indian railways.
'''


class Train:
    Country = "Indian Railway"

    def __init__(self, name, fare, status, seat, berth, destination, date, time):
        self.name = name
        self.fare = fare
        self.status = status
        self.seat = seat
        self.berth = berth
        self.destination = destination
        self.date = date
        self.time = time

    def trainDetails(self):
        print(f'The name of the train is : {self.name}')
        print(f'The total fare of the ticket is INR: {self.fare}')

    def journeyInfo(self):
        print(f'The status of the ticket is : {self.status}')
        print(f'The allocated seat number in train is : {self.seat}')
        print(f'The provided berth of the seat is : {self.berth}')
        print(f'The destination of the train is : {self.destination}')
        print(f'The departure date of the train is : {self.date}')
        print(f'The departure time of the train : {self.time}')

    @staticmethod
    def greet():
        print('___________Hello Passenger, Indian Railway Welcomes You.____________')


raj = Train('Rajdhani Express : 12430', 2500, 'CNF', 24,
            'side upper', 'Delhi', 20/6/2021, '20:50')
raj.greet()
raj.trainDetails()
raj.journeyInfo()


shat = Train('Shatabdi : 12019', 1500, 'RAC3', 16,
             'Lower', 'Ranchi', 16/7/2021, '06:05')
shat.greet()
shat.trainDetails()
shat.journeyInfo()


mailExp = Train('Mail Express : 11077', 1950, 'CNF',
                8, 'upper', 'Pune', 6/6/2021, '17:20')
mailExp.greet()
mailExp.trainDetails()
mailExp.journeyInfo()

dur = Train('Duronto : 22204', 3500, 'CNF', 21,
            'side-lower', 'Secunderabad', 19/8/2021, '20:15')
dur.greet()
dur.trainDetails()
dur.journeyInfo()
