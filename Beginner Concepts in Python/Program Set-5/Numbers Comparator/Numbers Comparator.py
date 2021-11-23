# PROGRAM TO FIND THE GREATEST AMONG THE FOUR NUMBERS ENTERED BY A USER

# user input function:
n1 = int(input("Please Enter the first Unique Number : "))
n2 = int(input("Please Enter the Second Unique Number : "))
n3 = int(input("Please Enter the Third Unique Number : "))
n4 = int(input("Please Enter the Fourth Unique Number : "))

# if-else comparision of the four numbers:
if n1>n2 :
    s1 = n1          
else:
    s1 = n2

if n3>n4 :
    s2 = n3
else:
    s2 = n3

if s1>s2 :          # Now comparing the greatest among the s1 and s2
    print( str(s1) + " is the greatest number")
else:
    print( str(s2) + " is the greatest number")

