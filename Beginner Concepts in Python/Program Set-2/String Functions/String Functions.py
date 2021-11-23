# Basic-Applications of a string functions in Python

avenger = 'the philanthropist tony stark built a super-power suit to create an avenger named Iron-Man'  # create a string

# String-Functions:

# 1.len() : function to get the length of the required string
print(len(avenger))   

# 2.endwith() : function to verify either the given string is ending with specific word/letter (True/False)
print(avenger.endswith('Iron-Man'))  

# 3.count() : function to count number of letter/word appearing in the given string
print(avenger.count('s')) 
print(avenger.count('to'))
print(avenger.count('stark'))

# 4.capitalize() : function to capitalize starting letter of first word in the string 
print(avenger.capitalize())

# 5.find() : function to find an index of the first occurence of particular word/letter in the string
print(avenger.find('tony'))
print(avenger.find('h'))

# 6.replace() : function to get a string by replacing a particular letter/word in the given string with something else
print(avenger.replace('suit','machine'))

