# PROGRAM TO CHECK THE ENTERED TEXT IS A SPAM 

# user input function:
text = input("Please entered the given text :\n")

# if elif else statement to check the spam conditions as true/false:
if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("click this" in text):
    spam = True
elif ("subscribe now" in text):
    spam = True
else: 
    spam = False

if (spam):
    print('The entered text is a spam')
else:
    print('This text is not a spam')