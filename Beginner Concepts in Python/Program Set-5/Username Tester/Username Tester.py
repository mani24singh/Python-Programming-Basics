# PROGRAM TO CHECK WHETHER THE ENTERED USERNAME IS VALID OR NOT
'''
Problem: To test whether the entered username has not more than 10 characters.
'''
 # creating a user input function:
usn = input("Please enter a valid username[not more than 10 characters] : \n")

if len(usn)<=10:
    print('This is a valid username, your username is : ', usn)
else:
    print('The entered username '+ usn + ' is invalid.Please enter a valid username')
