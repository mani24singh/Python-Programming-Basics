# PROGRAM TO DISPLAY ONLY THE UNIQUE NUMBERS ENTERED BY THE USER

# user input fucntion to get numbers from the user
num1 = int(input("Please enter the 1st number : \n"))
num2 = int(input("Please enter the 2nd number : \n"))
num3 = int(input("Please enter the 3rd number : \n"))
num4 = int(input("Please enter the 4th number : \n"))
num5 = int(input("Please enter the 5th number : \n"))
num6 = int(input("Please enter the 6th number : \n"))
num7 = int(input("Please enter the 7th number : \n"))
num8 = int(input("Please enter the 8th number : \n"))

set = {num1,num2,num3,num4,num5,num6,num7,num8} # add the user entered numbers to the set

print("The unique numbers entered by you are :\n", set)  # print the unique set