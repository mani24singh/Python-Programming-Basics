# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT: Write a program to input name, marks, and phone number of a 
student and format it using the format function like below:

"The name of the student is Mani, his marks are 85 and phone number is 8887776661"
'''

name = input('Enter your name : ')
marks = input('Enter your marks : ')
phone = input('Enter your phone-number : ')

template = "The name of the student is {}, his marks are {} and phone number is {}"

output = template.format(name, marks, phone)

print(output)