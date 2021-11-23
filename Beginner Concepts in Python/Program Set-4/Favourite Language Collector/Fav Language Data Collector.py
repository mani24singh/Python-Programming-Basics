# PROGRAM TO ASK STUDENTS THEIR FAVORITE LANGUAGE AND STORE IT IN AN EMPTY DICTIONARY WITH THEIR NAMES AS THE KEYS
 # An empty dictionary
fav_language = {}
 
  # User-input function
s1 = input("Please Enter Your favorite Programming Language Karan : ")
s2 = input("Please Enter Your favorite Programming Language Abhay : ")
s3 = input("Please Enter Your favorite Programming Language Roshni : ")
s4 = input("Please Enter Your favorite Programming Language Amit : ")
s5 = input("Please Enter Your favorite Programming Language Trupti : ")
s6 = input("Please Enter Your favorite Programming Language Shikha : ")

# Adding the given inputs in the dictionary as values to the keys of students names 
fav_language['Karan'] = s1
fav_language['Abhay'] = s2
fav_language['Amit'] = s4
fav_language['Roshni'] = s3
fav_language['Trupti'] = s5
fav_language['Shikha'] = s6

print(fav_language)

