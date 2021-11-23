# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
PROBLEM STATEMENT: Create a virtual environments, install few packages in the 
first one. How do you create a similar environment in the second one.
'''

'''
# Steps:
1. Install virtual environment in the terminal. => pip install virtualenv
2. create two environments in terminal as env1 and env2. => virtual projectname
3. activate the env1 and install few packages to it like: panda, matplotlib etc.
4. pip freeze the env1 and create the text file for packages installed in first env1. => pip freeze > packs.txt
5. deactivate the first env1.
6. activate the second env2 and add virtual environment from env1 packs.txt file into env2 => pip install -r packs.txt
7. pip freeze to display the packages and then deactivate the env2.
'''
