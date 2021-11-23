# PROGRAM TO READ A FILE AND FIND A REQUIRED FROM THE FILE

f = open('poem.txt')
read = f.read()
word = input('Enter the required word to find : ')
if word.upper() and word.lower() in read:
    print('The required word is present.')
else:
    print('The required word is not present.')
f.close()