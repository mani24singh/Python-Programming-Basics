# PROGRAM TO CHECK IF THE AGE ENTERED BY THE USER IS LEGAL FOR VOTING (Age greater than or equal to 18)

# Input function for the user
age = int(input("Please Enter your Age :\n"))

# Using Conditional Expression 
if (age>=18):
    print("Hello, your age is legal for voting.")
else:
    print("Sorry, your age is not approved as legal age for voting.")
    
print("Thankyou")