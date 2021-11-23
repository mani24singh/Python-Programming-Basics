# PROGRAM TO ASSIGN GRADES TO STUDENTS BASED ON THE MARKS-NUMBER SCHEME
'''
GIVEN : 85-100 -->'A++' , 75-85 -->'A+' , 70-74 -->'A' , 60-69 -->'B+' ,
55-60 -->'B' , 50-54 -->'C+' , 45-49 -->'C' , 40-44 -->'D' , Less than 40 --> 'F' .
'''

# create a user input function 
x = int(input('Please Enter the total percentage marks of the student for grading : '))

# if-elif-else ladder statement to grade depending upon the marks entered
if (x>=85):
    print('You have passed the exam with Distinction and your grade is A++')
elif (x>=75):
    print('You have passed the exam with Distinction and your grade is A+')
elif (x>=70):
    print('You have passed the exam with Distinction and your grade is A')
elif (x>=60):
    print('You have passed the exam with First Class and your grade is B+')
elif (x>=55):
    print('You have passed the exam with Second Class and your grade is B')
elif (x>=50):
    print('You have passed the exam with Second Class and your grade is C+')
elif (x>=45):
    print('You have passed the exam and your grade is C')
elif (x>=40):
    print('You have passed the exam and your grade is D')
elif (x<40):
    print('You have failed in the exam and your grade is F')
else:
    print('Err!!! Please enter a valid percentage mark.')

print('Thankyou. Wish you goodluck')
    