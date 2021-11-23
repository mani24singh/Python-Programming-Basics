# GAME : THE PERFECT GUESS GAME TO GUESS THE CORRECT NUMBER IN MINIMUM TRIES

# using random module for generation of random numbers
import random
randNumber = random.randint(1, 100)

print('The Perfect Number Guess Game.')
print('Tip : Make a Guess of a Number Between 1 to 100. ')

userGuess = None
guesses = 0

while (userGuess != randNumber):
    userGuess = int(input('Enter your guess here : '))
    guesses += 1
    if userGuess == randNumber:
        print('Congrats!!!...You guessed it right..!!')
    else:
        if userGuess > randNumber:
            print('You guessed it wrong!!....Guess a smaller Number.')
        else:
            print('You guessed it wrong!!....Guess a larger Number.')

print(f'You guessed the number in {guesses} guesses.')

# creating and updating a text file for highest score breaker
with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if (guesses < hiscore):
    print('Congratulations...You have broken the new high score!!')
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses))
