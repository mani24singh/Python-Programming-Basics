# GAME: PLAYING (SNAKE, WATER, GUN)-GAME AGAINST COMPUTER USING PYTHON

# random module : library package to generate random result 
import random       


# Defining a function to get all possible outputs
def gameresult(comp, user):      

    # if choices are same, declare result as a tie!!
    if comp == user:        
        return None
    
    # checking possible result if computer choose snake
    elif comp == 'snake':
        if user == 'g':
            return True
        elif user == 'w':
            return False

    # checking possible result if computer choose gun
    elif comp == 'gun':
        if user == 'w':
            return True
        elif user == 's':
            return False

    # checking possible result if computer choose water
    elif comp == 'water':
        if user == 's':
            return True
        elif user == 'g':
            return False


# displaying computer's turn 
print("Computer's Turn : Computer is choosing from snake, water and gun....... Done!!")

# Assigning random values(integers) to choice-parameters. viz: (1=water,2=snake,3=gun)
randnum = random.randint(1,3)           
if randnum == 1: 
    comp = 'water'
elif randnum == 2:
    comp = 'snake'
elif randnum == 3:
    comp = 'gun'
  

# asking user for input
user = input("Your Turn : Please select from Snake(s) , Water(w) or Gun(g)..? \n")

# assign parameters to user input
if user == 'g':
    u = 'gun'
elif user == 'w':
    u = 'water'
elif user == 's':
    u = 'snake'


# generate result from above user-defined function
result = gameresult(comp,user)


# printing the selected (computer and user) choices using f-string
print(f'The computer choosed {comp}.')
print(f'You choosed {u}.')


# print the required game-result 
if result == None:
    print("Result : Oops!! It's a tie.")
elif result == True:
    print("Result : You win...Congratulations!!")
else: 
    print("Result : You lose...Better luck, Next time!!")
