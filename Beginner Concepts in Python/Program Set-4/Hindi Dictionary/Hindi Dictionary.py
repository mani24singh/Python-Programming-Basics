#  PROGRAM TO CREATE A FEW HINDI WORDS DICTIONARY TO GIVE USER ITS MEANING IN ENGLISH

 # creating a dictionary of words
dict = {
     'hathi' : 'Elephant','sher'  : 'Tiger','bandar': 'Monkey','bhaalu': 'Bear',
     'machli': 'Fish','kabutar': 'Pigeon','murgi' : 'Hen','kawa': 'Crow',
     'kutta' : 'Dog', 'billi' : 'Cat', 'gaay': 'Cow', 'bakri': 'Goat'
       }

# print an option list for the user convinence
print("Please select an option from the following to get an english translation :\n", dict.keys())

# Give an input option to the user
user = input("Please Enter a valid option from the above list : ")

# Accessing the dictionary for asked word and giving the english translation to user
print("The meaning of the entered hindi word in english is : ", dict.get(user))