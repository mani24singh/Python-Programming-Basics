# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT

'''
PROBLEM STATEMENT:
The game() function is a program lets a user play a game and returns the score as an 
integer. You need to read a file 'Hiscore.txt' which is either blank or contains the 
previous High-score.You need to write the program to update the Hi-score whenever game()
breaks the Hi-score.
'''
t = int(input('Enter the highest score : '))

def game():
    return t

score = game()
with open('hiscore.txt') as f:
    hiscorestr = f.read()

if hiscorestr == '':
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))

elif int(hiscorestr)< score:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))

print('The Highest Score number has been updated in "hiscore.txt" file.')