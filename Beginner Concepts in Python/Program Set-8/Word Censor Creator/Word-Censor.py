# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
PROBLEM STATEMENT: A file 'Word.txt' contains few words which are inappropriate, so you need 
to replace these words with &%&%&#& censor cases by updating the same file. 
'''

words = ['donkey','monkey','Get-Out','cartoon']

with open('Words.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "%@%#&@^#*@&")
    with open('Words.txt','w') as f:
        f.write(content)

print('The required words have been swapped with censored characters.')