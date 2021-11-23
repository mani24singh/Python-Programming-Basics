# PROGRAM TO CHECK WHETHER A CERTAIN POST IS TALKING ABOUT ENTERED KEYWORD 

# creating a post with certain keywords:
post = input('Please copy-paste the post-description :\n')

# user input function:
word = input('Please Enter the required keyword to verify from post :\n')

# testing and returning the result of verification:
if (word.upper() in post) or (word.lower() in post):
    print('Matched!! The entered keyword has been existing in the given post.')
else:
    print('Sorry!! The entered word is not available in the post.')