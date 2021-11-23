# The-Perfect-Guess-Game 
- Guessing Game based on guessing of random numbers generated using random module in minimum chances.

**GAME RULES :** The game is based on "Guess the Number" strategy. The Python program generates an integer within a given range {here, [1,100]}. The user tries to guess the exact number. If the guess is incorrect, then the computer dsiplays the user that the guess made is either too high or too low. Eventually, the user guesses the correct number, then score equals the number of guesses user made.

**STRATEGY :** The key strategy in this game is to generate a clever guess. If, for example, the user knows the number is between 1 and 100, then a reasonable first guess is 50. This choice evenly splits the range, giving you the maximum amount of information about the next guess. If the computer says the guess is too low, then the user splits the reduced range and guesses 75. If the computer says the guess is too high, then the optimal guess is 25. It can be shown that by splitting the remaining range in half after each guess, it will, at worst, take less amount of guesses to arrive at the correct number and scoring user the high score of getting it in minimum guesses.

**random module :** we are using a module called as Random to generate random number which the user has to guess. 
- To import random module just type **import random** in your IDE.
- To call the random module function, use random.randint() function to generate a random number.


**Instruction :** To run this python script in your system, follow the below steps:
- step 1: Download The-Perfect-Guess-Game.py file in your system.
- step 2: open this script in your IDE eg.(VS-code).
- step 3: select your python interpreter for the program.
- step 4: run the script and input your guessed number in terminal. The script will run untill you guessed the number right.
- step 5: the result will be displayed on the terminal with number of guesses made.
- step 6: Suppose, if you break the highscore then it will be stored in highscore.txt file 
- step 7: run the program again to replay the game.

