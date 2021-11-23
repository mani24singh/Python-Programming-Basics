# THIS PROGRAM IS A MODULE FILE TO BE USED IN OTHER FILE ()

def greet(name):
    print(f"Good Evening, {name}.")

#print(__name__)

if __name__ == '__main__':
    n = input('Enter a name. \n')
    greet(n)